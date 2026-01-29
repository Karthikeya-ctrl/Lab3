import scipy.spatial


# calculating minkowski Distance using inbuilt function from scipy
for i in range(1,11):
  minkowski_dist = scipy.spatial.distance.minkowski(Price, Open , i)
  print(f"Minkowski distance of Price and Open with P as {i}: {minkowski_dist}")