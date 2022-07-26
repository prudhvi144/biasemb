import os
import random


dataset_name = "ed4"
data_dir_path= './embryo/ed4/source/'



data_dir= os.listdir(data_dir_path)
# data_dir = data_dir.sort()



print(len(data_dir))

for classes in data_dir:

    print()

    images_dir= os.listdir(data_dir_path+classes)

    # random.Random(4).shuffle(images_dir)
    # images_dir = images_dir[0:40]

    images_dir = images_dir[int(len(images_dir) * 0): int(len(images_dir) * 7)]
    print(len(images_dir))

    for img_name in images_dir:
        # print(img_name,classes)


        with open('./embryo/ed4_new.txt', 'a') as the_file:
        # with open('../data/sd1/val.txt', 'a') as the_file:
            # the_file.write(data_dir_path+img_name+" "+img_name+'\n')
            the_file.write('data/'+"ed4"+"/source/"+classes+"/"+img_name+" "+str(int(classes)-1)+'\n')
        # break
            #
            #
            #
            # the_file.write(data_dir_path + classes + "/" + img_name + " " + img_name + '\n')
# print(len(data_dir))