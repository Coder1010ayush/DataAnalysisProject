import numpy as np

def calculate(list):
  if len(list) != 9:
    raise ValueError("List must contain nine numbers.")
  
  arr = np.array(list).reshape((3,3))
  narr = np.array(list)
  # calculating mean
  result = {}
  result['mean'] = [arr.mean(axis=0).tolist(), arr.mean(axis=1).tolist(), narr.mean()]

  # calculating varience
  result['varience'] = [arr.var(axis=0).tolist(),arr.var(axis=1).tolist(), narr.var()]

  # calculating standard deviation
  result['standard deviation'] =[arr.std(axis=0).tolist(),arr.std(axis=1).tolist(),narr.std()]

  # calculating max and min values
  result['max'] = [arr.max(axis=0).tolist(),arr.max(axis=1).tolist(),narr.max()]
  result['min'] = [arr.min(axis=0).tolist(),arr.min(axis=1).tolist(),narr.min()]

  # calculating sum of given list after converting in matrix
  result['sum'] = [arr.sum(axis=0).tolist(),arr.sum(axis=1).tolist(),narr.sum()]
  
  return result