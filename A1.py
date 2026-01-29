
# function to calculate dot product
def dotProduct(A, B):
  if len(A) == len(B):
    c = 0
    for i in range(len(A)):
      c+=A[i]*B[i]
    return c
  else:
    return "Not compatible"

# function to calculate EuclideanNorm
def EuclideanNorm(A):
  sum = 0
  for i in range(len(A)):
    sum+=A[i]**2
  return np.sqrt(sum)


A = [1, 2, 3]
B = [4, 5, 6]
print(f"Dot product of A and B are: {dotProduct(A, B)}")
print(f"Euclidean norm of A: {EuclideanNorm(A)}")
