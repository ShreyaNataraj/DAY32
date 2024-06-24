def maxProd(arr):
  # Defining the minimum number possible with negative infinity
  max_num = float('-inf')
  for i in range(len(arr)):
    for j in range(i+1,len(arr)):
      max_prod = (arr[i] * arr[j])
      if(max_prod >max_num):
        max_num= max_prod
  return max_num
result = maxProd([1,2,3,4,5,6,7])
print(result)      