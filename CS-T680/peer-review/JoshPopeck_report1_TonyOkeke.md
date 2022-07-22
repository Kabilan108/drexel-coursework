
# Exploring the Impact of Autism Spectrum Disorder on the Structural Connectome

### Peer Review Comments

<hr>

- I think your introduction provides sufficient background information about connectomics and ASD.
  - I would suggest including some more information about recent studies using different ML
    techinques. The BranNetCNN paper that Yusuf included in the project resources is pretty
    interesting.

- In the third and fourth paragraphs of your introduction, you shouldn't be using biomarker and
  classifier interchangably.
  - A biomarker would be some parameter (e.g. a graph theory measure or some other metric)
    that can be used to distinguish between ASD and typiclly developing controls.
  - A classifier on the other hand would be the machine learning that takes in the data, and uses
    the features (like the biomarker) to distinguish between the two groups.

- In the Methods section, it would be helpful to clarify what the dataset looks like.
  - You should mention how many subjects had ASD and how many were controls.
  - It would also be useful to mention what the average ages of the subjects are, how many
    males/females there were, etc.

- You should also provide some justification as to why you are using SVM as your classifier. 
  There are other machine learning algorithms that might perform better (or worse) than SVM, so 
  including some references that support its use would be helpful.

- Also, I think you should separate your description of the SVM classifier from the identification 
  of a biomarker. Here's my suggestion for the approach you should take:
  - Use SVM as a classifier to distinguish between the two groups. You can evaluate the
    performance of the classifier using the metrics you mentioned.
  - For biomarker discovery, you can use different feature selection techniques to extract the
    most important features from the dataset you used to build the classifier.
    - The easiest place to start would be looking at the feature importances from the fitted
      SVM classifier.
    - sklearn has several in-built feature selection tools that you could use instead.
    - Also, there are several papers that discuss using machine learning for biomarker
      discovery.
    - [This paper](https://academic.oup.com/bioinformatics/article/21/11/2691/294960?login=true)
      discusses biomarker discover using SVM on gene expression data, but you might find their 
      approach helpful in planning your project.

- Overall, I think you did an excellent job with the first draft and I'm looking forward to seeing 
  what your final report looks like.
