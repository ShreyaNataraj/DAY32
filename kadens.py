def kadens(arr):
  maxsum = float('-inf')
  currsum =arr[i]
  for i in range(len(arr)):
    currsum *= arr[i]
    if currsum>maxsum:
      maxsum = currsum
  return maxsum    
arr = [1,2,-1,3,4]       
print(kadens(arr))