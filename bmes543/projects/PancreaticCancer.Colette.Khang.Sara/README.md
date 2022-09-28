# README

## How to run project code
1. Donwload Python and Jupyter Notebook (Anaconda)
2. Open the Anaconda command prompt (you can create a new virtual environment if you know how to or just use the base environment)
3. Run the following commands (skip this if you have these modules downloaded)

    ```
    pip install pandas  
    pip install numpy  
    pip install matplotlib  
    pip install matplotlib-venn  
    pip install scipy  
    pip install scikit-learn  
    pip install GEOparse  
    ```

4. Open Jupyter Notebook and ensure that you have successfully imported all of the modules (NOTE: make sure you have Dr. Sacan's bmes.ahmet Dropbox folder and that his functions are imported correctly)
5. Open project.ipynb and run the code from the start


## List of Files
**project.ipynb** - This is the main project file containing the differential gene expression and machine learning analysis. Run this file.

**functions.py** - This file contains all of the functions that were developed for the project and used in the project.ipynb file. 

**sig_genes1.csv** - This csv file contains all of the significant genes found in Dataset 1 with a fold change threshold of > 1.5 and pvalue threshold of < 0.02

**sig_genes2.csv** - This csv file contains all of the significant genes found in Dataset 2 with a fold change threshold of > 1.5 and pvalue threshold of < 0.02

**sig_genes3.csv** - This csv file contains all of the significant genes found in Dataset 3 with a fold change threshold of > 1.5 and pvalue threshold of < 0.02

**sig_genes_all3_.csv** - This csv file contains all of the significant genes that are found in all three datasets. This file is used for the David Functional Annotation Analysis
