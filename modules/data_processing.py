from sklearn.preprocessing import LabelEncoder
import pandas as pd

def automatize_enconding(dataset, column_name, prefix_to_append):
    '''automization of enconding to transform non-logic categorical data into binary one, the returned value will be a dummies dataframe'''
    le = LabelEncoder()
    dummies = pd.get_dummies(dataset[f"{column_name}"], prefix=prefix_to_append)
    return dummies


def remove_outlier_iqr_technique(dataset, var_name):
    '''a outlier value can be defined as some value that is not in range of an interquantile value\nFor processing data with it, use: dataset = dataset[(dataset[var_name]>lower)&(dataset[var_name]<upper_limit)]'''
    q1 = dataset[var_name].quantile(0.25)
    q3 = dataset[var_name].quantile(0.75)
    #interquantile is the diff between 75% and 25%
    iqr = q3 - q1
    upper = q3 + (1.5 * iqr)
    lower = q1 - (1.5 * iqr)
    print(f"Lower limit for {var_name} is {lower} \nUpper limit for {var_name} is {upper}")
    return lower, upper