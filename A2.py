import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# function to clean and convert String values to Integer
def clean_and_convert_to_float(arr):
    cleaned_arr = np.array([float(str(x).replace(',', '')) for x in arr])
    return cleaned_arr.astype(float)


# function to calculate mean manually 
def mean(A):
  length = len(A)
  if length>0:
    sum = 0
    for i in range(length):
      sum+=A[i]
    return sum/length
  else:
    return "Enter a list"

# function to calculate variance manually 
def variance(A):
  length = len(A)
  xbar = mean(A)
  if length>0:
    sum = 0
    for i in range(length):
      sum+=(A[i]-xbar)**2
    return sum/length
  else:
    return "Enter a list"
    
# function to calculate standardDeviation manually 
def standardDeviation(A):
  length = len(A)
  if length>0:
    return np.sqrt(variance(A))
  else:
    return "Enter a list"


# Data set used- IRCTC stock price
df = pd.read_csv('Lab Session Data(IRCTC Stock Price).csv')
x = clean_and_convert_to_float(df['Price'])
y = clean_and_convert_to_float(df['Open'])
Price = list(x[0:249])
Open = list(y[0:249])
print(f"Mean of Price Class: {mean(Price)}")
print(f"Variance of Price Class: {variance(Price)}")
print(f"Standard Deviations of Price Class: {standardDeviation(Price)}")
print(f"Mean of Open Class: {mean(Open)}")
print(f"Variance of Open Class: {variance(Open)}")
print(f"Standard Deviations of Open Open: {standardDeviation(Open)}")