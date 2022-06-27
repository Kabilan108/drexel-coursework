import GEOparse
import pandas as pd
import numpy as np
import scipy.stats as stats
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
import sys,os; sys.path.append(os.environ['BMESAHMETDIR']); import bmes

def get_gsedata(geo_id, loc):
    '''
    Description: This function takes in a geo id and parses the data. It performs normalization and log2 transformation &
    preprocesses the data for differential gene expression analysis and machine learning

    Input: geo_id [str]: GSE id of the dataset. Ex: "GSE15471"
           loc [int]: the index of the 'characteristics_ch1' metadata that describes the type of tissue (normal or tumor)

    Output: gsedata [DataFrame]: GSE data that is parsed   
    
    '''
    gse = GEOparse.get_GEO(geo=geo_id, destdir=bmes.tempdir())

    #get the expression table with rows representing probes and columns representing samples
    gsedata = gse.pivot_samples('VALUE')
    gsedata.columns.name = None
    gsedata.index.name = 'Gene Symbols'


    #if the data is not log2 values then convert
    if (gsedata > 100).any().any():
        gsedata = np.log2(gsedata + 1)


    #get gpl information
    gpl = list(gse.gpls.values())[0].table

    #get the gsm list and data
    gsm = list(gse.gsms.values())


    #convert the ID and Gene Symbol column into a dictionary
    #this is to convert the probe ID to gene symbols in the gsedata

    #the probe id is the key and the gene symbol is the value
    gene_dict = gpl.set_index(gpl.ID).to_dict()['Gene Symbol']


    for key in gene_dict.keys():
        if pd.isnull(gene_dict[key]):
            gene_dict[key] = key


    #map the gse probe id to the gpl gene symbol
    gsedata.index = gsedata.index.map(gene_dict)


    #get patient characteristics (group assignment)
    groups = [gsm[x].metadata['characteristics_ch1'][loc] for x in range(len(gsm))]

    #change gsedata column names to the group assignment
    gsedata.columns = groups

    #for each patient 
    for x in range(len(gsedata.columns)):

        #if 'normal' is in the patient's group 
        if 'normal' in gsedata.columns[x].lower():

            #then, assign 'normal' 
            gsedata.columns.values[x] = 'normal'
        else:

            #otherwise, assign 'tumor'
            gsedata.columns.values[x] = 'tumor'

    #Z Normalize data 
    gsedata = (gsedata - gsedata.mean()) / gsedata.std()

    return gsedata

def get_sig_genes(gsedata, fc_threshold, pval_threshold):
    '''
    Description: This function performs differential gene expression analysis by taking in the gsedata, fold change threshold,
    and pvalue threshold to determine significant genes
    
    Input: gsedata [DataFrame]: The gse data
           fc_threshold [float]: The fold change threshold. Ex: fc > 5 = fc_threshold
           pval_threshold [float]: The pvalue threshold. Ex: p < 0.05 = pval_threshold

    Output: sig_genes [DataFrame]: The data that contains the list of significant genes, the fold changes, and pvalues.
    
    '''
    #perform ttest on the gene expression data (two tailed)
    tstat , pval = stats.ttest_ind(gsedata.normal.transpose(), gsedata.tumor.transpose())

    #create pval dataframe
    pval_df = pd.DataFrame(pval, columns=['P-Value'])

    pval_df.index = gsedata.index

    #get the average expression for normal samples for each gene
    normal_avg = (gsedata.normal).mean(axis = 1)

    #get the average expression for tumor samples for each gene
    tumor_avg = (gsedata.tumor).mean(axis = 1)

    #get the fold change (LOG2)
    #fold change = 2 ^ (tumor_avg - normal_avg)
    fold_change_df = pd.DataFrame(2 ** (tumor_avg - normal_avg), columns=['Fold Change'])


    #convert fold changes that are less than 1 to negative fold change
    fold_change_df[fold_change_df < 1] = -1 / fold_change_df[fold_change_df < 1]

    #concatenate fold change and pval together into results dataframe
    results = pd.concat([fold_change_df, pval_df], axis=1)

    #get the significant genes by setting a fold change and pval threshold
    sig_genes = results[(abs(results['Fold Change']) > fc_threshold) & (results['P-Value'] < pval_threshold)]

    return sig_genes

def get_metrics(mdl, xtest, ytest):
    '''
    Description: This function takes in the machine learning model, the xtest data, and ytest data to compute the performance metrics
    (accuracy, precision, recall, and confusion matrix)

    Input: mdl is the machine learning model. Ex: mdl = SVC(kernel='rbf')
           xtest is the data that contains the gene expression for each sample for testing
           ytest is the groups (tumor or normal) that the samples belong to
        
    Output: accuracy is the accuracy of the prediction
            precision is the precision metric based on the formula tp / (tp + fp)
            recall is the recall metric based on the formula tp / (tp + fn)
            disp is the confusion matrix that can be displayed. Ex: disp.plot()
    
    '''

    #use the xtest and the model to predict the y
    ypredicted = mdl.predict(xtest)

    #generate confusion matrix
    cm = confusion_matrix(ytest, ypredicted, labels=mdl.classes_)

    #get the true positive, false positive, false negative, & true positive metrics
    tn, fp, fn, tp = cm.ravel()

    #calculate the accuracy
    accuracy = (tp+tn)/(tp+fp+fn+tn)

    #if the denomimator is not 0
    if tp + fp != 0:

        #calculate precision
        precision = tp / (tp + fp)

    else:

        #set precision equal to NaN
        precision = float("NaN")
    
    #if the denomimator is not 0
    if tp + fn != 0:

        #calculate recall
        recall = tp / (tp + fn)

    else:

        #set recall equal to NaN
        recall = float("NaN")

    #generate the confusion matrix to display
    disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=mdl.classes_)

    return accuracy, precision, recall, disp