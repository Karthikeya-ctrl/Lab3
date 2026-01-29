import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split

# function to clean and convert the data from String to Integer
def clean_and_convert_to_float(arr):
    cleaned_arr = np.array([float(str(x).replace(',', '')) for x in arr])
    return cleaned_arr.astype(float)

df = pd.read_csv('Lab Session Data(IRCTC Stock Price).csv')
x = clean_and_convert_to_float(df['Price'])
y = clean_and_convert_to_float(df['Open'])

# Unsing Scipy's inbuilt function to split the data
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.3)
print(X_train)