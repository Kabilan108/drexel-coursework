# By Kelvin Koser and Michael Welsh.
#-----------------------------------------------------------------------------------------------------------------------

#import modules

import numpy as np
import pandas as pd
from goatools.base import download_go_basic_obo
from goatools.base import download_ncbi_associations
from goatools.anno.genetogo_reader import Gene2GoReader
from goatools import obo_parser
import sqlite3
from sqlite3 import Error

#-----------------------------------------------------------------------------------------------------------------------

#-----------------------------------------------------------------------------------------------------------------------
def main():
    # Define local functions
    def connect_to_db(db_file):
        """
        Connect to an SQlite database, if db file does not exist it will be created
        :param db_file: absolute or relative path of db file
        :return: sqlite3 connection
        """
        sqlite3_conn = None

        try:
            sqlite3_conn = sqlite3.connect(db_file)
            return sqlite3_conn

        except Error as err:
            print(err)

            if sqlite3_conn is not None:
                sqlite3_conn.close()

    def create_anno_table(table_name, csv_file):

        conn = connect_to_db('gene_db')  # replace with database name

        if conn is not None:
            c = conn.cursor()

            # Create table if it does not exist
            c.execute(f"""CREATE TABLE IF NOT EXISTS {table_name} (
                      uniq_id   INTEGER PRIMARY KEY UNIQUE,
                      nt_accession VARCHAR,
                      symbol VARCHAR,
                      GO_ID VARCHAR)""")

            df = pd.read_csv(csv_file)

            df.to_sql(name=table_name, con=conn, if_exists='append', index=False)

            conn.commit()
            conn.close()
        else:
            print('Connection to database failed')

    def create_go_table(table_name, csv_file):

        conn = connect_to_db('gene_db')  # replace with database name

        if conn is not None:
            c = conn.cursor()

            # Create table if it does not exist
            c.execute(f"""CREATE TABLE IF NOT EXISTS {table_name} (
                      GO_ID   VARCHAR KEY UNIQUE,
                      Description    VARCHAR,
                      class VARCHAR)""")

            df = pd.read_csv(csv_file)

            df.to_sql(name=table_name, con=conn, if_exists='append', index=False)
            conn.commit()
            conn.close()
        else:
            print('Connection to database failed')


    # Generate gene2accession liftover file
    gene2accession = pd.read_csv("gene2accession_human_filt.csv")
    n_gene2accesion = gene2accession[['gene_id', 'genomic_nucleotide_accession', 'symbol']] #subset
    n_gene2accesion = n_gene2accesion[n_gene2accesion.genomic_nucleotide_accession != '-'] #remove missing nt_accession


    # Generate gene2go liftover file
    fin_gene2go = download_ncbi_associations() # read in gene2go dataset (full)
    objanno = Gene2GoReader(fin_gene2go, taxids=[9606])  # subset to human
    ns2assc = objanno.get_ns2assc()  # get a dict of gene ID's/ GO ID's

    # Convert dict to dataframe, and melt to long format
    namespaces = []
    gids = []
    goids = []

    for namespace, gid in ns2assc.items():
        namespaces.append(namespace)
        gids.append(pd.DataFrame.from_dict(gid, orient='index'))

    data_wide = pd.concat(gids, keys=namespaces)
    data_wide.columns = np.arange(len(data_wide.columns))
    data_wide_2 = data_wide.reset_index()
    val_cols = data_wide_2.columns[2:len(data_wide_2)]
    data_long = data_wide_2.melt(
        id_vars=['level_0', 'level_1'],
        value_vars=val_cols
    )
    data_long = data_long.rename(columns={"level_0": "Namespace", "level_1": "gene_id", "value": "GO_ID"})
    data_long = data_long.drop(['variable'], axis=1)
    gene_go_lift = data_long.fillna('None')

    # Merge into comprehensive accession2goterm liftover file
    comp_liftover = pd.merge(gene_go_lift, n_gene2accesion, on='gene_id')
    comp_liftover.index.names = ['uniq_id']
    comp_liftover = comp_liftover[['genomic_nucleotide_accession', 'symbol', 'GO_ID']]
    comp_liftover = comp_liftover.rename(columns={'genomic_nucleotide_accession': 'nt_accession'})
    comp_lift_nodupes = comp_liftover.drop_duplicates()
    comp_lift_nodupes.to_csv("gene_annotation_liftover.csv", index=True)


    # Make go2function (gene ontology) liftover file
    obo_fname = download_go_basic_obo()
    fin_gene2go = download_ncbi_associations()  # function to download
    go = obo_parser.GODag("go-basic.obo")

    # extract GO term ID, name, and namespace
    go_list = []
    for go_term in go.values():
        entry = [go_term.id, go_term.name, go_term.namespace]
        go_list.append(entry)

    go_df = pd.DataFrame(go_list)
    go_df.columns = ['GO_ID', 'Descriptor', 'Namespace']
    go_df = go_df.set_index('GO_ID')
    go_df = go_df.drop_duplicates()
    go_df = go_df.rename(columns={'Namespace': 'class', 'Descriptor': 'Description'})
    go_df.to_csv("gene_ontology_liftover.csv", index=True)

    #connect to database
    connect_to_db('gene_db')

    #make annotation table
    create_anno_table("annotation_table", "gene_annotation_liftover.csv")

    #make gene ontology table
    create_go_table('gene_ontology_table', 'gene_ontology_liftover.csv')

#-----------------------------------------------------------------------------------------------------------------------
if __name__ == '__main__':
    main()
# EOF