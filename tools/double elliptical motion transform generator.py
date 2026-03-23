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

def point_list_DynO(point_num, origin_list, w, h):
    #point_list but with dynamic origin points
    #meant to be used with the output of point_list

    step_len = (2*m.pi)/point_num
    step_total = 0
    output = []
    x = []
    y = []

    for n in origin_list:
        x.append(n[0])
        y.append(n[1])

    for n in range(0, point_num):
        output.append(ellipse(x[n], y[n], w, h, step_total))
        
        step_total += step_len

    return(output)

#================================================================================================================================
#---------parameters-------------------------
point_number = 60
origin_x = 0
origin_y = 0
width = 400.0
height =  100.0
time_modifier = "0.5"

width_2 = 40.0
height_2 = 10.0
#--------------------------------------------

buf_string = ""

n = point_list(point_number, origin_x, origin_y, width, height)
j = point_list_DynO(point_number, n, width_2, height_2)

for i in range(0, len(n)):
    buf_string += "\tlinear "+ time_modifier + " xoffset " + str(int(j[i][0])) + " yoffset " + str(int(j[i][1])) + "\n"

print(buf_string)