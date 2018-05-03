#!/usr/bin/evn python 
#coding:utf-8 

import os
import sys
import cv2
import random

webface_list_dir = 'webface_list.txt'
webface_pair_left_list_dir = 'webface_left_list.txt'
webface_pair_right_list_dir = 'webface_right_list.txt'

fr = open(webface_list_dir, "r")
fw_left = open(webface_pair_left_list_dir,'w')
fw_right = open(webface_pair_right_list_dir,'w')

lines = fr.readlines()
list_dict = {i : [] for i in range(10575)}
for i in range(len(lines)):
    left_dir, left_label = lines[i].strip().split()
    list_dict[int(left_label)].append(left_dir)

for i in range(10575):
    list_num = len(list_dict[i])
    for j in range(list_num):
        left_index = random.randint(0,list_num - 1)
        left_dir = list_dict[i][left_index]
        right_index = random.randint(0,list_num - 1)
        right_dir = list_dict[i][right_index]
        fw_left.write(left_dir + ' 1' + '\n')
        fw_right.write(right_dir + ' 1' + '\n')

        left_index = random.randint(0,list_num - 1)
        left_dir = list_dict[i][left_index]
        rest_identity = range(10575)
        rest_identity.remove(i)
        right_identity_index = random.randint(0,list_num - 2)
        right_index = random.randint(0,len(list_dict[rest_identity[right_identity_index]]) - 1)
        right_dir = list_dict[rest_identity[right_identity_index]][right_index]
        fw_left.write(left_dir + ' 0' + '\n')
        fw_right.write(right_dir + ' 0' + '\n')

fr.close()
fw_left.close()
fw_right.close()

