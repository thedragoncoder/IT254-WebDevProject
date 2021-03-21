# NSL KDD
- The NSL-KDD data set has the following advantages over the original KDD data set:
It does not include redundant records in the train set, so the classifiers will not be biased towards more frequent records.

- There is no duplicate records in the proposed test sets; therefore, the performance of the learners are not biased by the methods which have better detection rates on the frequent records.

- The number of selected records from each difficultylevel group is inversely proportional to the percentage of records in the original KDD data set. As a result, the classification rates of distinct machine learning methods vary in a wider range, which makes it more efficient to have an accurate evaluation of different learning techniques.

- The number of records in the train and test sets are reasonable, which makes it affordable to run the experiments on the complete set without the need to randomly select a small portion. Consequently, evaluation results of different research works will be consistent and comparable.

# Dataset
- NSL-KDD dataset dataset by UNB
The whole dataset can be downloaded from
[here](https://www.unb.ca/cic/datasets/nsl.html)

- We have also added the dataset files into this folder for reference.

- **Data files**

  - **KDDTrain+.ARFF**: The full NSL-KDD train set with binary labels in ARFF format

  - **KDDTrain+.TXT**: The full NSL-KDD train set including attack-type labels and difficulty level in CSV format

  - **KDDTrain+_20Percent.ARFF**: A 20% subset of the KDDTrain+.arff file

  - **KDDTrain+_20Percent.TXT**: A 20% subset of the KDDTrain+.txt file

  - **KDDTest+.ARFF**: The full NSL-KDD test set with binary labels in ARFF format

  - **KDDTest+.TXT**: The full NSL-KDD test set including attack-type labels and difficulty level in CSV format

  - **KDDTest-21.ARFF**: A subset of the KDDTest+.arff file which does not include records with difficulty level of 21 out of 21

  - **KDDTest-21.TXT**: A subset of the KDDTest+.txt file which does not include records with difficulty level of 21 out of 21

# Models Used
- Random Forest Classifier
- Logistic Regression
- K Neigbours Classifer
