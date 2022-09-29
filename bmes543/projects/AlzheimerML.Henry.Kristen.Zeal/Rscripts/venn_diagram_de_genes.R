
#!/usr/bin/env Rscript
##script that takes in differentially expressed genes table
## such as output by limma package, and plots venn diagram of 
## genes. 
args = commandArgs(trailingOnly=TRUE) #for running via MATLAB or terminal

if (length(args)<1) {
  stop("Must supply outdir", call.=FALSE) #make sure given MATLAB datadir
}

###auto install packages#########################
list.of.packages = c( 'VennDiagram', 'stringr')
new.packages = list.of.packages[!(list.of.packages %in% installed.packages()[,"Package"])]
if(length(new.packages)) install.packages(new.packages, repos='http://cran.us.r-project.org')
library('VennDiagram')
##################################################

setwd(args[1]) #setwd to matlab datadir
files = list.files(pattern = '*_CTL_AD_de_genes.csv') #get de genes files

de_genes = c()
#loop through list of files, and grab gene names
for(i in 1:length(files)) {
  df = read.csv(files[i])
  genes = df$ID
  genes = list(genes[!is.na(genes)])
  name = stringr::str_extract(files[i], 'GSE[0-9]*')
  names(genes) = name
  de_genes = c(de_genes, genes)
}

#supress log
futile.logger::flog.threshold(futile.logger::ERROR, name = "VennDiagramLogger")

#call venn diaggram package
venn.diagram(
  x = de_genes,
  category.names = names(de_genes),
  filename = "GSE_series_de_genes_venn.png",
  output=T,
  imagetype="png", 
  height = 480,
  width = 480 ,
  resolution = 300,
  compression = "lzw",
  lwd = 1,
  col=c("#440154ff", '#21908dff', '#fde725ff'),
  cex = 0.5,
  fontfamily = "sans",
  cat.cex = 0.3,
  cat.default.pos = "outer",
  cat.pos = c(-27, 27, 135),
  cat.dist = c(0.055, 0.055, 0.085),
  cat.fontfamily = "sans",
  cat.col = c("#440154ff", '#21908dff', '#fde725ff'),
  rotation = 1
)
