# Data Basics Assignment

In this assignment you are going to analyze this [Immunotherapy dataset](http://archive.ics.uci.edu/ml/datasets/Immunotherapy+Dataset). The study that has produced the dataset is described [here](https://www.ncbi.nlm.nih.gov/pubmed/28086200). The dataset contains only the immunotherapy subset of patients. Review the paper for description of the attributes.

- Create a `hwdatabasics.mlx`, `hwdatabasics.ipynb` or `hwdatabasics.rmd` file to perform the following tasks.
- For each attribute, find its correlation with the result of treatment. Exclude result of treatment as an attribute so you do not find its correlation with itself. Note that correlation is not the best measurement for categroical features, especially if there are more than 2 categories. But, for this assignment, we'll ignore this caveat and calculate correlation anyway. You do not need to convert categorical features for this assignment, just use the numbers as they are.
- For each attribute, find if there is a statistically significant difference in that attribute, between successful and failed treatments. Use *two-sample t-test* for the comparison and find the p-value. Report the names of attributes that you found to be statistically significantly different. You need to decide your own p-value threshold.
- Report the significant correlation coefficients and p-values of **all of** the attributes in a tabular format [First column containing variable names, second column containing correlation values, and third column containing pvalues). The reported table must be sorted in increasing order by p-values.
- For the attributes with the most significant p-value, create a box plot showing a summary of the values of that attribute, for successfule and failed treatments.
