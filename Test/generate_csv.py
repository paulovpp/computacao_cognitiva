from get_dims import get_dimensions # import get_dims file
import csv

csv_height = []
csv_width = []
csv_max_height = []
csv_max_width = []
csv_area = []
file_names = []

# Create a folder named Golden imgs
# File name of the gold pattern image: img(n)_gold.jpg, where n = {0..19}

for i in range(0, 2):
    name = './Golden imgs/img(' + str(i) + ')_gold.jpg'
    file_names.insert(i, name[5:])
    h, w, mh, mw = get_dimensions(name)
    csv_height.insert(i, h)
    csv_width.insert(i, w)
    csv_max_height.insert(i, mh)
    csv_max_width.insert(i, mw)
    
    csv_area.insert(i, csv_height[i] * csv_width[i])


# print(csv_height, csv_width, csv_area)

with open('./Golden imgs/data.csv',mode= 'w') as csvfile:
    file = csv.writer(csvfile, delimiter= ',', quoting= csv.QUOTE_MINIMAL)
    file.writerow(['File_name','Original_height','Original_width','Max_height','Max_width','Area'])
    for i in range(0, 2):
        file.writerow([file_names[i], csv_height[i], csv_width[i], csv_height[i], csv_width[i], csv_area[i]])

print('Done!')