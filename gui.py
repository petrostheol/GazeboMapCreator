from tkinter import *
from math import pi, cos, sin

from pip._vendor.distlib.compat import raw_input


def createSkidpadTrack():
    global inner_circle
    global outer_circle
    global circle_distance
    inner_circle_diameter = float(inner_circle.get())
    outer_circle_diameter = float(outer_circle.get())
    circle_distance_num = float(circle_distance.get())
    theta = pi/8
    a = """
<?xml version="1.0"?>
<sdf version="1.4">
<world name="default">
<include>
<uri>model://sun</uri>
</include>
<include>
<uri>model://ground_plane</uri>
</include>        
"""
    b = """
</world>
</sdf>
"""
    c = """
<include>
<uri>model://cone_orange</uri>
</include>
"""
    skidpad = open("skidpad.world", "w+")
    skidpad.write(a)
    for i in range(16):
        x = (outer_circle_diameter/2)*sin(i*theta)
        skidpad.write('<model name="cone%d">\n'%i)
        skidpad.write(c)
        skidpad.write("<pose>%f %f 0 0 0 0</pose>\n"%(((inner_circle_diameter/2)*sin(i*theta)), (((inner_circle_diameter)/2)*cos(i*theta))))
        skidpad.write("</model>\n")
        if x < (inner_circle_diameter/2):
            skidpad.write('<model name="cone%d">\n' %(32+i))
            skidpad.write(c)
            skidpad.write("<pose>%f %f 0 0 0 0</pose>\n" % (x, ((outer_circle_diameter/2) * cos(i * theta))))
            skidpad.write("</model>\n")
    for i in range(16):
        _x = circle_distance_num+(outer_circle_diameter/2)*sin(i*theta)
        skidpad.write('<model name="cone%d">\n'%(16+i))
        skidpad.write(c)
        skidpad.write("<pose>%f %f 0 0 0 0</pose>\n"%((circle_distance_num+(inner_circle_diameter/2)*sin(i*theta)), (inner_circle_diameter/2*cos(i*theta))))
        skidpad.write("</model>\n")
        if _x>(outer_circle_diameter/2):
            skidpad.write('<model name="cone%d">\n' % (48 + i))
            skidpad.write(c)
            skidpad.write("<pose>%f %f 0 0 0 0</pose>\n" % ((_x), ((outer_circle_diameter/2) * cos(i * theta))))
            skidpad.write("</model>\n")

    skidpad.write(b)
    skidpad.close()


def createAccelerationTrack():
#    number_of_cones = int(raw_input("Give number of cones: "))
#    track_distance = int(raw_input("Give track distance in meters: "))
#    distance_between_cones = int(track_distance/number_of_cones)
    global cones
    global distance
    number_of_cones = int(cones.get())
    track_distance = int(distance.get())
    distance_between_cones = int(track_distance/number_of_cones)

    a="""
<?xml version="1.0"?>
<sdf version="1.4">
<world name="default">
<include>
<uri>model://sun</uri>
</include>
<include>
<uri>model://ground_plane</uri>
</include>        
"""
    c="""
<include>
<uri>model://cone_orange</uri>
</include>
"""

    b="""
</world>
</sdf>
"""



    f = open("acceleration.world", "w+")
    f.write(a)
    for i in range(number_of_cones):                                       #right_side_of_cones
        f.write('<model name="cone%d">\n'%i)
        f.write(c)
        f.write("<pose>2 %d 0 0 0 0</pose>\n"%(i*distance_between_cones))
        f.write("</model>\n")

    for j in range(number_of_cones):                                       #left_side_of_cones
        f.write('<model name="cone%d">\n'%(number_of_cones+j))
        f.write(c)
        f.write("<pose>-2 %d 0 0 0 0</pose>\n"%(j*distance_between_cones))
        f.write("</model>\n")

    f.write(b)
    f.close()


#GUI with TKinter
root = Tk()

label_1 = Label(root, text="Number of cones")
label_2 = Label(root, text="Track distance")
label_3 = Label(root, text="Inner circle diameter")
label_4 = Label(root, text="Outer circle diameter")
label_5 = Label(root, text="Distance between inner circles")
inner_circle = Entry(root)
outer_circle = Entry(root)
circle_distance = Entry(root)
cones = Entry(root)
distance = Entry(root)
label_1.grid(row=0, sticky=E)
label_2.grid(row=1, sticky=E)
label_3.grid(row=3, sticky=E)
label_4.grid(row=4, sticky=E)
outer_circle.grid(row=4, column=1)
label_5.grid(row=5, sticky=E)
circle_distance.grid(row=5, column=1)
cones.grid(row=0, column=1)
distance.grid(row=1,column=1)
inner_circle.grid(row=3, column=1)
button_1 = Button(root, text="Create Acceleration Track", command=createAccelerationTrack)
button_1.grid(row=2, columnspan=2)
button_3 = Button(root, text="Create Skidpad Track", command=createSkidpadTrack)
button_3.grid(columnspan=2)
button_2 = Button(root, text="Quit", command=root.quit)
button_2.grid(columnspan=2)
root.mainloop()


#if __name__=="__main__":
 #   createAccelerationTrack()