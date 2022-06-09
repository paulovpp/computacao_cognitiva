from operator import mod
from pydoc import doc
from get_dims import get_dimensions # import get_dims file
import cv2
import numpy as np
from pandas import array
from matplotlib import docstring, pyplot as plt
import csv

csv_height = []
csv_width = []
csv_max_height = []
csv_max_width = []
csv_area = []

# with open('Test\teste.csv', 'w') as csvfile:
# csv_max_height.insert(0,1)
# print(csv_max_height)

for i in range(0, 20):
    name = 'Test\img(' + str(i) + ')_gold.jpg'
    h, w = get_dimensions(name)
    csv_height.insert(i, h)
    csv_width.insert(i, w)
    
    csv_area.insert(i, csv_height[i] * csv_width[i])


print(csv_height, csv_width, csv_area)

with open('./Test/test.csv',mode= 'w') as csvfile:
    file = csv.writer(csvfile, delimiter=',')
    for i in range(0, 2):
        file.writerow([csv_height[i], csv_width[i], csv_area[i]])

# name = 'Test\img(' + str(0) + ')_gold.jpg'
# csv_height[0], csv_width[0] = get_dimensions(name)
# csv_area[0].append(csv_height[0] * csv_width[0])
# print(csv_height[0], csv_width[0], csv_area[0])




# [max_h, max_w] = get_dimensions(name)
# print(csv_height, csv_width, csv_area)

# print(image.shape[0])
# print(image.shape[1])
# print(cont)

# plt.figure()
# plt.plot(cont)
# plt.show()
# cv2.waitKey(0)
# final_image = read_proj.convert_to_gold(name)
# cv2.imwrite('Test\img(' + str(i+1) + ')_gold.jpg', final_image)
