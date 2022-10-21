from sklearn.preprocessing import LabelEncoder
import pandas as pd

def automatize_one_hot_enc(dataset, column_name, prefix_to_append):
    '''automization of one hot encoder to transform non-logic categorical data into binary one'''
    le = LabelEncoder()
    dataset[f"{column_name}"] = le.fit_transform(dataset[f"{column_name}"])
    dummies = pd.get_dummies(dataset[f"{column_name}"], prefix=prefix_to_append)
    return dummies