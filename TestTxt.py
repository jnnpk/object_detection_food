import os

path_dir = '/home/tutor/bpm/dataset/validation'

file_list = os.listdir(path_dir)

f = open('/home/tutor/bpm/darknet/data/obj/test.txt', 'w')
for i in file_list:
    if len(i) != 8:
        continue
    food_list = os.listdir(path_dir + '/' + i)
    for j in food_list:
        if j[-4:] != '.txt':
            f.write('/home/tutor/bpm/dataset/validation/' + i + '/' + j + '\n')

f.close()

python TrainTxt.py