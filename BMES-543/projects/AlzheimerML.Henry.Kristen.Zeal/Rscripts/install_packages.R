##This script is meant to install required packages if you encounter the
##permission error where you cannot write to "R/library"
##To run this script on Windows, right click on R or R studio and
##hit "Run as Administrator" which allows write permissions to the folder.
## then paste this code or open this file and run it.
## Then run Project.mlx as normal

 
list.of.packages = c( 'stringr', 'doParallel', 'tidyverse', 'VennDiagram')
new.packages = list.of.packages[!(list.of.packages %in% installed.packages()[,"Package"])]
if(length(new.packages)) install.packages(new.packages, repos='http://cran.us.r-project.org')

if (!require("BiocManager", quietly = TRUE)){
  install.packages("BiocManager", repos='http://cran.us.r-project.org', quietly = T)
}
BiocManager::install("rrvgo")
BiocManager::install("org.Hs.eg.db")
BiocManager::install("GEOquery")