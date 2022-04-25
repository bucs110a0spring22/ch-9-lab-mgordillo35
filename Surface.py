from Rectangle import Rectangle

class Surface:
  def  __init__(self, filename, x, y, h, w):
    self.rect = Rectangle (x, y, h, w)
    self.image = str(filename) 


  '''
  function is used to pass the instance variables from the file rectangle
  args: (self)- needs to be used to call atributtes 
  (filename) - refrence the file we will use
  (x,y,h,w) - (x,y) cordinates and (height, width) - to create the rectangle object
  return nada (nothing)
  '''

  def getRect(self):
    return self.rect

  '''
  function is used to pass the function prior to this one to the console
  args: (self)- needs to be used to call atributtes 
  return the rectangle object
  '''