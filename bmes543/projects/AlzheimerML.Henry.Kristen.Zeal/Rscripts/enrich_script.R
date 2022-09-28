#!/usr/bin/env Rscript
##This script takes in tables of GO:BP terms enriched in a gene list
## and outputs a pretty tree picture with the rrvgo library

args = commandArgs(trailingOnly=TRUE)  #for running through MATLAB

if (length(args) < 2) {
  stop("Must supply outdir", call.=FALSE) #make sure directories specified
}

##### auto downloading packages ############
list.of.packages = c( 'stringr')
new.packages = list.of.packages[!(list.of.packages %in% installed.packages()[,"Package"])]
if(length(new.packages)) install.packages(new.packages, repos='http://cran.us.r-project.org')

if (!require("BiocManager", quietly = TRUE)){
  install.packages("BiocManager", repos='http://cran.us.r-project.org', quietly = T)
}
BiocManager::install("rrvgo")
BiocManager::install("org.Hs.eg.db")
library('rrvgo')
###########################################

setwd(args[1]) #set wd to project subfolder to read

files = list.files(pattern = '*_results.txt$', ) #get the GO:BP results


if(length(files) != 0){
#for each file...
for (i in 1:length(files)) {
  #retrieve the GOBP number for rrvgo to work its magic
  DAVID_results = read.delim(files[i])
  term  = stringr::str_extract(DAVID_results$Term , "GO:[0-9]*")
  simMatrix <- calculateSimMatrix(term,
                                  orgdb="org.Hs.eg.db",
                                  ont="BP",
                                  method="Rel")
  scores <- setNames(-log10(DAVID_results$PValue), term)
  reducedTerms <- reduceSimMatrix(simMatrix,scores, threshold=0.7,
                                  orgdb="org.Hs.eg.db")
  
  setwd(args[2]) #set wd to datadir
  #save the png to the working directory
  png(file=paste0(files[i], ".png"), width=600, height=350)
  treemapPlot(reducedTerms)
  dev.off()
  setwd(args[1])

}

}else{
  print('Error, no DE gene lists found...')
}
