n = [[1, 2, 3], [4, 5, 6, 7, 8, 9]]
# Add your function here
def flatten(lists):
  results = []
  for i in lists:
      for item in i:
          results.append(item)
  return results        
    #   print lists[i]
    # numbers = lists[i]
    # for k in numbers:
    #   print numbers[k]
    #   results.append(numbers[k])

print flatten(n)