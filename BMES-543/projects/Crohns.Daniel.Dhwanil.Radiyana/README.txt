BMES 543 Final Project
Title: Predicting Crohn's Disease using Terminal Ileum Tissue Samples
Group 10: Daniel Thompson, Dhwanil Patel, Radiyana Mancheva


Folder Structure:

img ---------------------------------------------- directory containing all images from DAVID gene set enrichment
clean-data.ipynb --------------------------------- notebook to clean data and perform DGE analysis 
gather-dataset.ipynb ----------------------------- notebook to gather all 3 GSE used for this project
GSE112366 Week 0, 8, and 44 Patients.ipynb ------- notebook to extract W8 and W44 samples from GSE for validation set
model.ipynb -------------------------------------- notebook containing all ML models used for project
wk44pickle.pkl ----------------------------------- pickle file used in models.ipynb
wk8pickle.pkl ------------------------------------ pickle file used in models.ipynb
final-model-notebook.pdf ------------------------- notebook run with data used for presentation
project.sh --------------------------------------- script to run all 3 notebooks automatically

Packages needed for analysis:

* Access to Dr. Sacan bmes library * 
Geoparse --------------------------- https://geoparse.readthedocs.io/en/latest/
pandas ----------------------------- https://pandas.pydata.org
numpy ------------------------------ https://numpy.org
mygene ----------------------------- https://sulab.org/2013/10/quick-id-mapping-using-mygene-info/
scipy ------------------------------ https://scipy.org/install/
sklearn ---------------------------- https://scikit-learn.org/stable/
matplotlib ------------------------- https://matplotlib.org
matplotlib_venn -------------------- https://pypi.org/project/matplotlib-venn/
jupyter notebook ------------------- https://jupyter.org/install
nbconvert -------------------------- https://nbconvert.readthedocs.io/en/latest/

How to Use:

Install All Packages Above

Run the notebooks in this order to repeat analysis 

1. gather-datasets.ipynb
2. clean-data.ipynb
3. model.ipynb

Or you can run 

project.sh
