import json
import math
import numpy as np
import sys

file_data = []
with open(str(sys.argv[1]), 'r') as input:
    file_data = input.read()

file_data = file_data.splitlines()

bitdata = file_data[4:]
bitdata = np.array(bitdata)
bitdata = np.reshape(bitdata,(-1,3))

dimensions = file_data[2].split(" ")

y_dimension = int(dimensions[0])
x_dimension = z_dimension = int(math.sqrt(int(dimensions[1])))

data = {}
data['Structure'] = []

id = 0
average_orientation = [0,0,0]
for z in range(x_dimension):
    for x in range(z_dimension):
        for y in range(y_dimension):
            rot_direction_value = int(bitdata[id][1])
            if(0 <= rot_direction_value <= 11):
                orientation = (1,0,0)
                rotation = 0
            elif( 11 < rot_direction_value <= 22):
                orientation = (1,0,0)
                rotation = 90
            elif( 22 < rot_direction_value == 33):
                orientation = (1,0,0)
                rotation = 180
            elif( 33 < rot_direction_value <= 44):
                orientation = (1,0,0)
                rotation = 270
            elif( 44 < rot_direction_value <= 55):
                orientation = (0,1,0)
                rotation = 0
            elif( 55 < rot_direction_value <= 66):
                orientation = (0,1,0)
                rotation = 90
            elif( 66 < rot_direction_value <= 77):
                orientation = (0,1,0)
                rotation = 180
            elif( 77 < rot_direction_value <= 88):
                orientation = (0,1,0)
                rotation = 270
            elif( 88 < rot_direction_value <= 99):
                orientation = (0,0,1)
                rotation = 0
            elif( 99 < rot_direction_value <= 110):
                orientation = (0,0,1)
                rotation = 90
            elif( 110 < rot_direction_value <= 121):
                orientation = (0,0,1)
                rotation = 180
            elif( 121 < rot_direction_value <= 132):
                orientation = (0,0,1)
                rotation = 270
            elif( 132 < rot_direction_value <= 143):
                orientation = (-1,0,0)
                rotation = 0
            elif( 143 < rot_direction_value <= 154):
                orientation = (-1,0,0)
                rotation = 90
            elif( 154 < rot_direction_value <= 165):
                orientation = (-1,0,0)
                rotation = 180
            elif( 165 < rot_direction_value <= 176):
                orientation = (-1,0,0)
                rotation = 270
            elif( 176 < rot_direction_value <= 187):
                orientation = (0,-1,0)
                rotation = 0
            elif( 187 < rot_direction_value <= 198):
                orientation = (0,-1,0)
                rotation = 90
            elif( 198 < rot_direction_value <= 209):
                orientation = (0,-1,0)
                rotation = 180
            elif( 209 < rot_direction_value <= 220):
                orientation = (0,-1,0)
                rotation = 270
            elif( 220 < rot_direction_value <= 231):
                orientation = (0,0,-1)
                rotation = 0
            elif( 231 < rot_direction_value <= 242):
                orientation = (0,0,-1)
                rotation = 90
            elif( 242 < rot_direction_value <= 253):
                orientation = (0,0,-1)
                rotation = 180
            elif( 253 < rot_direction_value <= 255):
                orientation = (0,0,-1)
                rotation = 270
            else:
                orientation = (1,0,0)
                rotation = 0
            
            average_orientation[0]+=orientation[0]
            average_orientation[1]+=orientation[1]
            average_orientation[2]+=orientation[2]

            data['Structure'].append({
                'id' : id,
                'Position' : (x,z,y),
                'Type' : int(bitdata[id][0]),
                'Orientation' : orientation,
                'Rotation' : rotation,
                'Texture' : int(bitdata[id][2]),
            })
            id += 1

with open('data.json','w') as output:
    json.dump(data,output)