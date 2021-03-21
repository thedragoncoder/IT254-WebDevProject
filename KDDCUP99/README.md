# KDD CUP '99

IDS monitors a network or systems for malicious activity and protects a computer network from unauthorized access from users,including perhaps insider.
The motive of this study is to propose a predictive model (i.e. a classifier) capable of distinguishing between 'bad connections' (intrusions/attacks) and a 'good
(normal) connections' after applying some feature extraction on KDD Cup 1999 dataset by DARPA.

# Dataset
- KDD Cup 1999 dataset by DARPA
The whole dataset can be downloaded from
[here](http://kdd.ics.uci.edu/databases/kddcup99/kddcup99.html)

- We have also added the dataset files into this folder for reference.

# Models Used
- A total of seven models is trained and tested.

 - The performance of all the algorithms is examined based
on accuracy and computational time.

- Derived results show that **Decision Tree**
outperforms the best on measures like Accuracy and Computational Time.

# Results
| Model Name     | Training Accuracy | Testing Accuracy |
| ----------- | ----------- | ----------- |
Gaussian Naive Bayes|87.951|87.903|
 Decision Tree|99.058|99.052|
 Random Forest|99.997|99.969|
 SVM|99.875|99.879|
  Logistic Regression|99.352|99.352|
  Gradient Boosting|99.793|99.771|
   ANN|98.485|98.472|
