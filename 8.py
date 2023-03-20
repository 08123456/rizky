def linear_search(lst, match):
  matches = []
  for idx in range(len(lst)):
    if lst[idx] == match:
      matches.append(idx)
  if matches:
    return matches
  else:
    raise ValueError("{0} not in list".format(match))
    
scores = [55, 65, 32, 40, 55]
print(linear_search(scores, 55))