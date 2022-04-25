class Rectangle:
  def __init__(self, x, y, h, w):
    self.x = max(0,x)
    self.y =  max(0,y)
    self.height =  max(0,h)
    self.width =  max(0,w)

  '''
  this function takes coordinates and lengths as a parameter to test vales in main
  args: (self)- needs to be used to call atributtes
  (x) - x coodinate
  (y) - y coordinate 
  (h) - height of rectangle
  (w) - width of the rectangle 
  return the value 0 if any parameter values are less than 0 (the max)
  '''
    

  def __str__(self):
    return "x = "+str(self.x) + ", y = " + str(self.y) + ", width: " + str(self.width) + ", height: " + str(self.height) 
    
  '''
  function is used to pass a string to the console of the previous functions parameters 
  args: (self)- needs to be used to call atributtes 
  return a string of the parameter and its cordinated value 
  '''