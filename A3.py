import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# function to clean and convert the data from String to Integer
def clean_and_convert_to_float(arr):
    cleaned_arr = np.array([float(str(x).replace(',', '')) for x in arr])
    return cleaned_arr.astype(float)

df = pd.read_csv('Lab Session Data(IRCTC Stock Price).csv')
x = clean_and_convert_to_float(df['Price'])
Price = list(x[0:249])


# plotting the price using hist function from matplotlib
plt.hist(np.histogram(Price))