class Rectangle:
  def __init__(self, x, y, h, w):
    self.x = max(0,x)
    self.y =  max(0,y)
    self.height =  max(0,h)
    self.width =  max(0,w)

  def __str__(self):
    s="(x: {}, y: {}) width: {}, height: {}"
    return s.format(self.x, self.y, self.width, self.height)
    # return "(x:)"+str(self.x) + ", y=" + str(self.y) + ", width:" + str(self.w) + ", height:" + str(self.h) 
    
  