import os
import imageio

file_list =sorted(os.listdir("Assignment8/gif_frame"))

IMAGES=[]

for file_name in file_list:
    file_path="Assignment8/gif_frame/" + file_name
    # print(file_path)

    image= imageio.v2.imread (file_path)
    IMAGES.append(image)

# print(IMAGES)

imageio.mimsave("Assignment8/one_punch_man.gif", IMAGES)