def even_odd(integers, evens, odds, outlier):
  for i in integers:
      if i%2 ==0:
        evens.append(i)
      else:
        odds.append(i)

  outlier = count(evens, odds)
  
  return outlier

def count(evens, odds):
  if len(evens) > len(odds):
      outlier = odds[0] 
  else:
      outlier = evens[0]

  return(outlier)


def find_outlier(integers):
  evens = []
  odds = []
  outlier = []
  out = even_odd(integers, evens, odds, outlier)
  return out
