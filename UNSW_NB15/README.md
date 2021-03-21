# UNSW_NB15
- The raw network packets of the UNSW-NB 15 dataset was created by the IXIA PerfectStorm tool in the Cyber Range Lab of the Australian Centre for Cyber Security (ACCS) for generating a hybrid of real modern normal activities and synthetic contemporary attack behaviours.

- Tcpdump tool is utilised to capture 100 GB of the raw traffic (e.g., Pcap files). This dataset has nine types of attacks, namely, Fuzzers, Analysis, Backdoors, DoS, Exploits, Generic, Reconnaissance, Shellcode and Worms. The Argus, Bro-IDS tools are used and twelve algorithms are developed to generate totally 49 features with the class label.

# Dataset
-  UNSW-NB15 can be downloaded from
[here](https://www.unsw.adfa.edu.au/unsw-canberra-cyber/cybersecurity/ADFA-NB15-Datasets/)


- **Data files**

  - These features are described in **UNSW-NB15_features.csv** file.

  - The total number of records is two million and 540,044 which are stored in the four CSV files, namely, **UNSW-NB151.csv**, **UNSW-NB152.csv**, **UNSW-NB153.csv** and **UNSW-NB154.csv**.

  - The ground truth table is named **UNSW-NB15GT.csv** and the list of event file is called **UNSW-NB15LIST_EVENTS.csv**.

  - A partition from this dataset is configured as a training set and testing set, namely, **UNSWNB15training-set.csv** and **UNSWNB15testing-set.csv** respectively.

  - The number of records in the training set is **175,341 records** and the testing set is **82,332 records** from the different types, attack and normal.

# Models Used
- Logistic Regression.
- Decision Trees
- Random Forest (gini)
- Random Forest (Entropy or Information-gain)
- Gradient Boosting Classifier
- Gaussian Naive Bayes
- Support Vector Machine

# Results
| Model Name     | Cross-Validation Accuracy |
| ----------- | ----------- |
Random Forest Information-gain|92.60|
 Random Forest Gini|92.57|
 Gradient Boosting Classifier|	92.09|
 Decision Tree|91.44|
  Neural Network|90.53|
  SVM|89.23|
  Logistic Regression|89.02|
  Gaussian Naive Bayes|50.46|
