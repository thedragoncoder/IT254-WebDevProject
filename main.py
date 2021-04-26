import numpy as np
import pandas as pd
from flask import Flask, request, jsonify, render_template, flash
import pickle
from sklearn import model_selection
from sklearn import metrics
import joblib

app = Flask(__name__)
model = joblib.load('model_files/RandomForest_IG_IDS.pkl')
app.secret_key = "super secret key"

def Remove_dump_values(data, cols):
    for col in cols:
        data[col] = np.where(data[col] == '-', 'None', data[col])
    return data

@app.route('/')
def home() :
    return render_template('index.html') 

@app.route('/custom')
def custom() :
    return render_template('custom.html') 

@app.route('/intrusion_test_case')
def intrusion() :
    return render_template('intrusion_test_case.html') 

@app.route('/non_intrusion_test_case')
def non_intrusion() :
    return render_template('non_intrusion_test_case.html') 

@app.route('/predict',methods=['POST'])
def predict():
    test = pd.read_csv('UNSW_NB15/dataset/UNSW_NB15_testing-set.csv')
    dict_datatype = test.dtypes.to_dict()
    print(dict_datatype)


    dataR = dict()
    dataR = request.form.to_dict()
    dataR['attack_cat'] = 'None'
    dataR['label'] = 0
    dataT = {"id" : 0}
    dataT.update(dataR)
    dataTemp = pd.DataFrame(dataT,index=[0])
    print(dataTemp)
    for i,v in dict_datatype.items():
        dataTemp[i] = dataTemp[i].astype(v)    
    
    
    print(dataTemp.dtypes)
    train = pd.read_csv('UNSW_NB15/dataset/UNSW_NB15_training-set.csv')
    
    print()
    print("hello")
    print(type(test.dtypes[0]))
    print(test.shape)
    data = pd.concat([train,test,dataTemp]).reset_index(drop=True)
    print(data.dtypes)
    print(data.shape)
    cols_cat = data.select_dtypes('object').columns # To be explained later
    cols_numeric = data._get_numeric_data().columns # To be explained later
    
    data['service'].unique()
    data['service']= np.where(data['service'] == '-', 'None', data['service'])
    cols = data.columns
    data_bin = Remove_dump_values(data, cols)

    data_bin = data_bin.drop(['id'], axis=1) 
    data_bin.drop(['attack_cat'], axis=1, inplace=True)
    cols_cat = cols_cat.drop(['attack_cat'])
    data_bin_hot = pd.get_dummies(data_bin,columns=cols_cat)

    cols_numeric = list(cols_numeric)
    cols_numeric.remove('label')
    cols_numeric.remove('id')
    data_bin_hot[cols_numeric] = data_bin_hot[cols_numeric].astype('float')
    data_bin_hot[cols_numeric] = (data_bin_hot[cols_numeric] - np.min(data_bin_hot[cols_numeric])) / np.std(data_bin_hot[cols_numeric])
    X = data_bin_hot.drop('label', axis=1)
    # Y = data_bin_hot['label']

    df2 = X.tail(1)
    print(df2.shape)
    result = model.predict(df2)
    print(result)
    
    if result[0] == '1': 
        flash('it is an intrustion', 'info')
    else:
        flash('it is not an intrustion', 'danger')

    return render_template('index.html')


@app.route('/result',methods=['POST'])
def result():
    train = pd.read_csv('UNSW_NB15/dataset/UNSW_NB15_training-set.csv')
    test = pd.read_csv('UNSW_NB15/dataset/UNSW_NB15_testing-set.csv')

    data = pd.concat([train,test]).reset_index(drop=True)
    cols_cat = data.select_dtypes('object').columns 
    cols_numeric = data._get_numeric_data().columns 
    
    data['service'].unique() 
    data['service']= np.where(data['service'] == '-', 'None', data['service'])
    cols = data.columns
    data_bin = Remove_dump_values(data, cols)

    data_bin = data_bin.drop(['id'], axis=1)
    data_bin.drop(['attack_cat'], axis=1, inplace=True)
    cols_cat = cols_cat.drop(['attack_cat'])
    data_bin_hot = pd.get_dummies(data_bin,columns=cols_cat)

    cols_numeric = list(cols_numeric)
    cols_numeric.remove('label')
    cols_numeric.remove('id')
    data_bin_hot[cols_numeric] = data_bin_hot[cols_numeric].astype('float')
    data_bin_hot[cols_numeric] = (data_bin_hot[cols_numeric] - np.min(data_bin_hot[cols_numeric])) / np.std(data_bin_hot[cols_numeric])
    X = data_bin_hot.drop('label', axis=1)
    Y = data_bin_hot['label']

    result = model.score(X, Y)
    print(result)
    return render_template('index.html')
