import math
import csv

smart_pole_name = []
start_coordiates_x = []
start_coordiates_y = []
init_bearing_degrres = []

distance = []
height = []
smart_pole_second_name = []

with open("C:\\Users\kjarada\Desktop\Copy of OCS RAKING 181214.csv") as csv_file:
    csv_reader = csv.reader(csv_file)
    for line in csv_reader:
        smart_pole_name.append(line[0])
        start_coordiates_x.append(line[1])
        start_coordiates_y.append(line[2])
        init_bearing_degrres.append(line[3])
        distance.append(line[4])
        height.append(line[5])
        smart_pole_second_name.append(line[6])


init_bearing_degrres= list(map(float,init_bearing_degrres))
start_coordiates_x= list(map(float,start_coordiates_x))
start_coordiates_y= list(map(float,start_coordiates_y))
distance= list(map(float,distance))
height= list(map(float,height))
init_bearing_radians = []

for i in init_bearing_degrres:
    init_bearing_radians.append(math.radians(i))

terminal_coordinates_x= []
terminal_coordinates_y= []

for i in range(len(distance)):

  terminal_coordinates_x.append(start_coordiates_x[i] + distance[i]*math.sin(init_bearing_radians[i]))
  terminal_coordinates_y.append(start_coordiates_y[i] + distance[i]*math.cos(init_bearing_radians[i]))

with open("C:\\Users\kjarada\Desktop\\result OCS RAKING 181214.csv", 'w+') as csv_file_results:
    csv_writer = csv.writer(csv_file_results, delimiter = ",")
    csv_writer.writerows(map(lambda x,y,z: [x,y,z],smart_pole_second_name, terminal_coordinates_x, terminal_coordinates_y))


