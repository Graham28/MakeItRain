class Drop:
  
  #initilizes class
  def __init__(self, x, y, width, height, velocity):
    self.x = x
    self.y = y
    self.width = width
    self.height = height
    self.velocity = velocity

  def get_x(self):
    return self.x 
  
  def get_y(self):
    return self.y 
  
  def get_width(self):
    return self.width

  def get_height(self):
    return self.height
  
  def get_velocity(self):
    return self.velocity

  def set_x(self, new_x):
    self.x = new_x
  
  def set_y(self, new_y):
    self.y = new_y

  def set_width(self, new_width):
    self.width = new_width

  def set_height(self, new_height):
    self.height = new_height
  
  def set_velocity(self, new_velocity):
    self.velocity = new_velocity

  def fall(self):
    self.set_y(self.get_y() + self.get_velocity())