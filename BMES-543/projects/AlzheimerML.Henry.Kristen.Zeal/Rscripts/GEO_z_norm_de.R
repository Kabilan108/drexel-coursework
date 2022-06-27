#!/usr/bin/env Rscript
##This script downloads the GEO acc numbers specific to our project using
##the geoQuery package. We use limma to do differential expression
##and output the top transcripts that meet the user defined cutoffs
##LFC cutoff is args[2] and p-val cutoff is args[3].
##Additionally, the geo series are z-normalized and output as 
##tables (numPatients x genes) for MATLAB. We also output the subject
##metadata, used for creating classification labels later.

args = commandArgs(trailingOnly=TRUE) #for running script from MATLAB/term

######## auto download packages if not already installed##########
list.of.packages = c( 'doParallel', 'tidyverse')
new.packages = list.of.packages[!(list.of.packages %in% installed.packages()[,"Package"])]
if(length(new.packages)) install.packages(new.packages, repos='http://cran.us.r-project.org')

if (!require("BiocManager", quietly = TRUE)){
    install.packages("BiocManager", repos='http://cran.us.r-project.org', quietly = T)
}
BiocManager::install("GEOquery")

library('GEOquery')
library('doParallel')
library('tidyverse')
library('limma')
##################################################################

#some geo files are big so increase connection size
Sys.setenv("VROOM_CONNECTION_SIZE" = 131072 * 100)

# test if there is at least one argument: if not, return an error
if (length(args)==0) {
  stop("Must supply outdir", call.=FALSE)
}

geo_list = c('GSE63060', 'GSE63061', 'GSE44772') #GEO ACC numbers
col_list = c('Accession', 'Accession', 'GB_ACC') #names of columns we want
setwd(args[1])  #setwd to bmes.datadir

#differentially expressed genes criteria
logfc_cutoff = as.numeric(args[2])
pval_cutoff = as.numeric(args[3])

######This code block finds the intersect of genes across all files####
gse = getGEO(geo_list[1]) #downloads data from GEO,
genes1 = gse[[paste0(geo_list[1], "_series_matrix.txt.gz")]]@featureData@data[[col_list[1]]]
gse = getGEO(geo_list[2])
genes2 = gse[[paste0(geo_list[2], "_series_matrix.txt.gz")]]@featureData@data[[col_list[2]]]
gse = getGEO(geo_list[3])
genes3 = gse[[paste0(geo_list[3], "_series_matrix.txt.gz")]]@featureData@data[[col_list[3]]]
genes1_f = str_extract(genes1, '[A-Za-z]*_[0-9]*') #only keeps gene names
genes2_f = str_extract(genes2, '[A-Za-z]*_[0-9]*')
genes3_f = str_extract(genes3, '[A-Za-z]*_[0-9]*')

tmp = intersect(genes1_f, genes2_f)
int = intersect(genes3_f, tmp)    #this is the intersection
####################

get_de_genes = function(geo, emat, conditions,LFC_cutoff = .58, p_cutoff = 0.05,
                        top = 500, write = T){
  #Function for running limma on emat and writing differentially expressed 
  #genes
  
  design = model.matrix(~factor(conditions))
  fit = lmFit(emat, design)
  fit = eBayes(fit)
  genes<- topTable(fit, coef=2, n=top, adjust="BH")
  genes = filter(genes, adj.P.Val < p_cutoff & abs(logFC) > LFC_cutoff )
  genes$ID =str_extract(genes$ID, '[A-Za-z]*_[0-9]*')
  write.table(genes, paste0(geo, '_CTL_AD_de_genes.csv'), sep = ',', col.names = NA)
  return(genes)
}


write_z_norm = function(geo, column){
  ##function takes in a geo number and a column corresponding to platform
  ##(i.e. GEO ACC, transcriptID, etc.)
  ## within, we call the differential expression function "get_de_genes"
  ##This function writes out the normed data and metadata
  gse = getGEO(geo)
  print(geo)
  print(column)
  
  #expression data
  emat = gse[[paste0(geo, "_series_matrix.txt.gz")]]@assayData[["exprs"]]
  #gene names
  genes = gse[[paste0(geo, "_series_matrix.txt.gz")]]@featureData@data[[column]]
  #metadata
  subjid_data = gse[[paste0(geo, "_series_matrix.txt.gz")]]@phenoData@data
  
  #handling diff geos separately b/c they annotate their meta data differently:
  if (geo == "GSE44772") {#reduce size of this specific metadata
    subjid_data = select(subjid_data, geo_accession, source_name_ch2,
                         characteristics_ch2, characteristics_ch2.1, characteristics_ch2.2)
    conditions = subjid_data$characteristics_ch2  #extract disease state
    de_emat = emat
    rownames(de_emat) = genes

  }else{  #one of first 2 geo series
    conditions = subjid_data$characteristics_ch1   #extract disease state
    keep = which(conditions == 'status: CTL' | conditions == 'status: AD')
    conditions = conditions[keep]
    de_emat = emat[,keep]
    rownames(de_emat) = genes
  }
  
  #call our differential expression function, which writes out by default
  de_genes = get_de_genes(geo, de_emat, conditions, logfc_cutoff, pval_cutoff)
 
  #write out the meta data
  write.csv(subjid_data, paste0(geo, "_subject_data.csv"))

  #tidy up the gene names to get true GEO ACC numbers
  genes_f = str_extract(genes, '[A-Za-z]*_[0-9]*') #makes genes comparable to "int"
  
  #keep only genes in interesection
  emat = emat[genes_f %in% int,]
  genes = genes_f[genes_f %in% int]
  emat = aggregate(emat, list(genes), mean) #average sgenes of same name

  #z-norm every gene for each column
  NormedEmat = foreach(i = 2:ncol(emat), .combine = cbind) %do% {
    z_normed = (emat[,i] -mean(emat[, i], na.rm = T))/sd(emat[, i], na.rm = T)
  }
  colnames(NormedEmat) = colnames(emat)[-1]  #make colnames GEO_subjectID
  NormedEmat = as.data.frame(NormedEmat)     #cast as data.frame

  #cleaning it up nicely for writing out to file:
  NormedEmat = cbind(emat[,1], NormedEmat)
  colnames(NormedEmat)[1] = 'genes'
  NormedEmat = NormedEmat[order(NormedEmat$genes),]
  NormedEmat = t(NormedEmat)   #save as subjects by genes for SVM later...
  
  #write out:
  write.csv(NormedEmat, paste0(geo, "_z_intersectGenes.csv"))


}

#run chain of functions on all GEOs in GEO_list
mapply(write_z_norm, geo_list, col_list)


