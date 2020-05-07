
import numpy as np

#Use to display vision, not used in program
def view_new(x,y,width,drops):
  wall_left = False
  wall_right = False
  above_200_left = False
  above_200_right = False
  right_100 = False
  left_100 = False

  for drop in drops:
    x_drop = drop.get_x()
    y_drop = drop.get_y()
    drop_width = drop.get_width()
    
    if ((y >= y_drop + drop_width) and y_drop > 0) and (x + (width/2) >= x_drop and x <= x_drop + drop_width):
      above_200_left = True

    if ((y >= y_drop + drop_width) and y_drop > 0) and (x + width >= x_drop and x + (width/2) <= x_drop + drop_width):
      above_200_right = True
    
    if x==0:
      wall_left = True

    if x ==470:
      wall_right = True

    if ((x >= x_drop + drop_width) and (x -(x_drop + drop_width)) < 75) and (y + width >= y_drop and y <= y_drop + drop_width):
      left_100 = True

    if ((x + width <= x_drop) and (x_drop -(x + width)) < 75) and (y + width >= y_drop and y <= y_drop + drop_width):
      right_100 = True
    
    

    

  return "Above: "+str(above_200_right)


#Creates view of drops in vacinity of man
def view(x,y,width,drops):
  view = ['0','0','0','0','0','0']
  for drop in drops:
    x_drop = drop.get_x()
    y_drop = drop.get_y()
    drop_width = drop.get_width()

    if ((y >= y_drop + drop_width) and y_drop > 200) and (x + (width/2) >= x_drop and x <= x_drop + drop_width):
      view[0] = '1'
    
    if x < 30:
      view[1] = '1'

    if x > 470:
      view[2] = '1'

    if ((x >= x_drop + drop_width) and (x -(x_drop + drop_width)) < 75) and (y + width >= y_drop and y <= y_drop + drop_width):
      view[3] = '1'

    if ((x + width <= x_drop) and (x_drop -(x + width)) < 75) and (y + width >= y_drop and y <= y_drop + drop_width):
      view[4] = '1'

    if ((y >= y_drop + drop_width) and y_drop > 200) and (x + width >= x_drop and x + (width/2) <= x_drop + drop_width):
      view[5] = '1'
    
    view_string = ''
    for char in view:
      view_string += char

    
    output = int(view_string, base=2)


  return output
  

