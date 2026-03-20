import math as m

def ellipse(x, y, w, h, angle):
    #returns a point along the edge of an ellipse
    #x,y: x and y of the origin point
    #w,h: multipliers to form an ellipse from a circle
    #angle: desired output angle in radians
    x_pos = (x + (w * m.cos(angle)))
    y_pos = (y + (h * m.sin(angle)))
    return((x_pos,y_pos))

def point_list(point_num, x, y, w, h):

    step_len = (2*m.pi)/point_num
    step_total = 0
    output = []

    for n in range(0, point_num):
        output.append(ellipse(x, y, w, h, step_total))
        
        step_total += step_len

    return(output)


#================================================================================================================================
#---------parameters-------------------------
point_number = 20
origin_x = 0
origin_y = 0
width = 100.0
height =  100.0
#--------------------------------------------

buf_string = ""

for n in point_list(point_number, origin_x, origin_y, width, height):
    buf_string += "\tlinear 1.0 xoffset " + str(int(n[0])) + " yoffset " + str(int(n[1])) + "\n"

print(buf_string)