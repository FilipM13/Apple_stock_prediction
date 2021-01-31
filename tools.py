
def get_directions(current: list):
  '''
  Takes list of stock prices and return price direction list
  example:
  current: [1,2,2,3,4,5,6,3,3]
  direction: [1,0,1,1,1,1,-1,0]
  returns current[:-1], direction
  [1,2,2,3,4,5,6,3]
  [1,0,1,1,1,1,-1,0]
  '''
  rv = [1 if current[n+1] > current[n] else(0 if current[n+1] == current[n] else -1) for n, v in enumerate(current[:-1])]
  return rv