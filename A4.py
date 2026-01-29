# function to calculate minkowski_distance without using inbuilt function
def minkowski_distance(A, B, p):
  if len(A) == len(B):
    sum = 0
    for i in range(len(A)):
      sum+=abs(A[i]-B[i])**p
    return sum**(1/p)
  else:
    return "Not compatible"


A = [1, 2, 3]
B = [4, 5, 6]

for i in range(1,11):
  print(f"Minkowski distance of Price and Open with P as {i}: {minkowski_distance(A, B, i)}")


