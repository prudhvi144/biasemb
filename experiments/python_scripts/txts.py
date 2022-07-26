import os
import random
random.seed(1000)

def make_biased_dataset_emb():

    datasrt_name = "Embryo"
    data_type = ["train", "validation", "test"]

    source_data_dir_path = '../../data/embryo/'+'ed4'+'/alldata/'
    target_data_dir_path_1 = '../../data/embryo/' + 'ed2'+'/alldata/'
    target_data_dir_path_2 = '../../data/embryo/'+'ed1'+'/alldata/'
    data_list_source = os.listdir(source_data_dir_path)
    data_list_target_1 = os.listdir(target_data_dir_path_1)
    data_list_target_2 = os.listdir(target_data_dir_path_2)
    for data_type in data_type:

        if data_type== "train":
            for classes in data_list_source:
                images_dir = os.listdir(source_data_dir_path + classes)
                random.Random(4).shuffle(images_dir)
                # images_dir = images_dir[0:40]
                images_dir = images_dir[int(len(images_dir) * 0): int(len(images_dir) * 0.1)]
                for img_name in images_dir:
                    with open('../../data/embryo/' + "_train" + ".txt", 'a') as the_file:
                        # with open('../data/sd1/val.txt', 'a') as the_file:
                        # the_file.write(data_dir_path+img_name+" "+img_name+'\n')
                        the_file.write(source_data_dir_path + classes + "/" + img_name + " " + str(int(classes) - 1) + " " +'0'+'\n')
            for classes in data_list_target_1:
                images_dir = os.listdir(target_data_dir_path_1 + classes)
                random.Random(4).shuffle(images_dir)
                # images_dir = images_dir[0:40]
                images_dir = images_dir[int(len(images_dir) * 0): int(len(images_dir) * 0.1)]
                for img_name in images_dir:
                    with open('../../data/embryo/' + "_train" + ".txt", 'a') as the_file:
                        # with open('../data/sd1/val.txt', 'a') as the_file:
                        # the_file.write(data_dir_path+img_name+" "+img_name+'\n')
                        the_file.write(target_data_dir_path_1 + classes + "/" + img_name + " " + str(int(classes) - 1)+" "+'1' + '\n')
            for classes in data_list_target_2:
                images_dir = os.listdir(target_data_dir_path_2 + classes)
                random.Random(4).shuffle(images_dir)
                # images_dir = images_dir[0:40]
                images_dir = images_dir[int(len(images_dir) * 0): int(len(images_dir) * 0.1)]
                for img_name in images_dir:
                    with open('../../data/embryo/' + "_train" + ".txt", 'a') as the_file:
                        # with open('../data/sd1/val.txt', 'a') as the_file:
                        # the_file.write(data_dir_path+img_name+" "+img_name+'\n')
                        the_file.write(target_data_dir_path_2 + classes + "/" + img_name + " " + str(int(classes) - 1)+" "+'1' + '\n')
        if data_type == "test":

            for classes in data_list_source:
                images_dir = os.listdir(source_data_dir_path + classes)
                # images_dir = images_dir[0:40]
                images_dir = images_dir[int(len(images_dir) * 0.2): int(len(images_dir) * 1)]
                for img_name in images_dir:
                    with open('../../data/embryo/' + "_validation" + ".txt", 'a') as the_file:
                        # with open('../data/sd1/val.txt', 'a') as the_file:
                        # the_file.write(data_dir_path+img_name+" "+img_name+'\n')
                        the_file.write(source_data_dir_path + classes + "/" + img_name + " " + str(int(classes) - 1) +" "+'0'+ '\n')
            for classes in data_list_target_1:
                images_dir = os.listdir(target_data_dir_path_1 + classes)
                # images_dir = images_dir[0:40]
                images_dir = images_dir[int(len(images_dir) * 0.1): int(len(images_dir) * 0.2)]
                for img_name in images_dir:
                    with open('../../data/embryo/' + "_validation" + ".txt", 'a') as the_file:
                        # with open('../data/sd1/val.txt', 'a') as the_file:
                        # the_file.write(data_dir_path+img_name+" "+img_name+'\n')
                        the_file.write(
                            target_data_dir_path_1 + classes + "/" + img_name + " " + str(int(classes) - 1) +" "+'1'+ '\n')
            for classes in data_list_target_2:
                images_dir = os.listdir(target_data_dir_path_2 + classes)
                # images_dir = images_dir[0:40]
                images_dir = images_dir[int(len(images_dir) * 0.1): int(len(images_dir) * 0.2)]
                for img_name in images_dir:
                    with open('../../data/embryo/' + "_validation" + ".txt", 'a') as the_file:
                        # with open('../data/sd1/val.txt', 'a') as the_file:
                        # the_file.write(data_dir_path+img_name+" "+img_name+'\n')
                        the_file.write(
                            target_data_dir_path_2 + classes + "/" + img_name + " " + str(int(classes) - 1) +" "+'1'+ '\n')
        if data_type == "validation":

            for classes in data_list_source:
                images_dir = os.listdir(source_data_dir_path + classes)
                # images_dir = images_dir[0:40]
                images_dir = images_dir[int(len(images_dir) * 0.1): int(len(images_dir) * 0.2)]
                for img_name in images_dir:
                    with open('../../data/embryo/' + "_ed4_test" + ".txt", 'a') as the_file:
                        # with open('../data/sd1/val.txt', 'a') as the_file:
                        # the_file.write(data_dir_path+img_name+" "+img_name+'\n')
                        the_file.write(source_data_dir_path + classes + "/" + img_name + " " + str(int(classes) - 1)+" "+'0' + '\n')
            for classes in data_list_target_1:
                images_dir = os.listdir(target_data_dir_path_1 + classes)
                # images_dir = images_dir[0:40]
                images_dir = images_dir[int(len(images_dir) * 0.2): int(len(images_dir) * 1)]
                for img_name in images_dir:
                    with open('../../data/embryo/' + "_ed2_test" + ".txt", 'a') as the_file:
                        # with open('../data/sd1/val.txt', 'a') as the_file:
                        # the_file.write(data_dir_path+img_name+" "+img_name+'\n')
                        the_file.write(
                            target_data_dir_path_1 + classes + "/" + img_name + " " + str(int(classes) - 1) +" "+'1'+ '\n')
            for classes in data_list_target_2:
                images_dir = os.listdir(target_data_dir_path_2 + classes)
                # images_dir = images_dir[0:40]
                images_dir = images_dir[int(len(images_dir) * 0.2): int(len(images_dir) * 1)]
                for img_name in images_dir:
                    with open('../../data/embryo/' + "_ed1_test" + ".txt", 'a') as the_file:
                        # with open('../data/sd1/val.txt', 'a') as the_file:
                        # the_file.write(data_dir_path+img_name+" "+img_name+'\n')
                        the_file.write(
                            target_data_dir_path_2 + classes + "/" + img_name + " " + str(int(classes) - 1) +" "+'1'+ '\n')

def make_biased_dataset_emb_all():

    datasrt_name = "Embryo"

    source_data_dir_path = '../../data/embryo/'+'ed4'+'/alldata/'
    target_data_dir_path_1 = '../../data/embryo/' + 'ed2'+'/alldata/'
    target_data_dir_path_2 = '../../data/embryo/'+'ed1'+'/alldata/'
    data_list_source = os.listdir(source_data_dir_path)
    data_list_target_1 = os.listdir(target_data_dir_path_1)
    data_list_target_2 = os.listdir(target_data_dir_path_2)

    for classes in data_list_source:
                images_dir = os.listdir(source_data_dir_path + classes)
                random.Random(4).shuffle(images_dir)
                # images_dir = images_dir[0:40]
                images_dir = images_dir[int(len(images_dir) * 0): int(len(images_dir) * 0.5)]
                for img_name in images_dir:
                    with open('../../data/embryo/' + "_all" + ".txt", 'a') as the_file:
                        # with open('../data/sd1/val.txt', 'a') as the_file:
                        # the_file.write(data_dir_path+img_name+" "+img_name+'\n')
                        the_file.write(source_data_dir_path + classes + "/" + img_name + " " + str(int(classes) - 1) + " " +'0'+'\n')
    for classes in data_list_target_1:
                images_dir = os.listdir(target_data_dir_path_1 + classes)
                random.Random(4).shuffle(images_dir)
                # images_dir = images_dir[0:40]
                images_dir = images_dir[int(len(images_dir) * 0): int(len(images_dir) * 1)]
                for img_name in images_dir:
                    with open('../../data/embryo/' + "_all" + ".txt", 'a') as the_file:
                        # with open('../data/sd1/val.txt', 'a') as the_file:
                        # the_file.write(data_dir_path+img_name+" "+img_name+'\n')
                        the_file.write(target_data_dir_path_1 + classes + "/" + img_name + " " + str(int(classes) - 1)+" "+'1' + '\n')
    for classes in data_list_target_2:
                images_dir = os.listdir(target_data_dir_path_2 + classes)
                random.Random(4).shuffle(images_dir)
                # images_dir = images_dir[0:40]
                images_dir = images_dir[int(len(images_dir) * 0): int(len(images_dir) * 1)]
                for img_name in images_dir:
                    with open('../../data/embryo/' + "_all" + ".txt", 'a') as the_file:
                        # with open('../data/sd1/val.txt', 'a') as the_file:
                        # the_file.write(data_dir_path+img_name+" "+img_name+'\n')
                        the_file.write(target_data_dir_path_2 + classes + "/" + img_name + " " + str(int(classes) - 1)+" "+'1' + '\n')

def make_biased_dataset_emb_all_train():

    datasrt_name = "Embryo"

    source_data_dir_path = '../../data/embryo/'+'ed4'+'/alldata/'
    target_data_dir_path_1 = '../../data/embryo/' + 'ed2'+'/alldata/'
    target_data_dir_path_2 = '../../data/embryo/'+'ed1'+'/alldata/'
    data_list_source = os.listdir(source_data_dir_path)
    data_list_target_1 = os.listdir(target_data_dir_path_1)
    data_list_target_2 = os.listdir(target_data_dir_path_2)

    for classes in data_list_source:
                images_dir = os.listdir(source_data_dir_path + classes)
                # random.Random(4).shuffle(images_dir)
                # images_dir = images_dir[0:40]
                images_dir = images_dir[int(len(images_dir) * 0): int(len(images_dir) * 0.5)]
                for img_name in images_dir:
                    with open('../../data/embryo/' + "_all_train" + ".txt", 'a') as the_file:
                        # with open('../data/sd1/val.txt', 'a') as the_file:
                        # the_file.write(data_dir_path+img_name+" "+img_name+'\n')
                        the_file.write(source_data_dir_path + classes + "/" + img_name + " " + str(int(classes) - 1) + " " +'0'+'\n')
                images_dir = images_dir[int(len(images_dir) * 0.5): int(len(images_dir) * 1)]
                for img_name in images_dir:
                    with open('../../data/embryo/' + "_all_val" + ".txt", 'a') as the_file:
                        # with open('../data/sd1/val.txt', 'a') as the_file:
                        # the_file.write(data_dir_path+img_name+" "+img_name+'\n')
                        the_file.write(source_data_dir_path + classes + "/" + img_name + " " + str(int(classes) - 1) + " " +'0'+'\n')
    for classes in data_list_target_1:
                images_dir = os.listdir(target_data_dir_path_1 + classes)
                random.Random(4).shuffle(images_dir)
                # images_dir = images_dir[0:40]
                images_dir = images_dir[int(len(images_dir) * 0): int(len(images_dir) * 0.1)]
                for img_name in images_dir:
                    with open('../../data/embryo/' + "_all_train" + ".txt", 'a') as the_file:
                        # with open('../data/sd1/val.txt', 'a') as the_file:
                        # the_file.write(data_dir_path+img_name+" "+img_name+'\n')
                        the_file.write(target_data_dir_path_1 + classes + "/" + img_name + " " + str(int(classes) - 1)+" "+'1' + '\n')
    for classes in data_list_target_2:
                images_dir = os.listdir(target_data_dir_path_2 + classes)
                random.Random(4).shuffle(images_dir)
                # images_dir = images_dir[0:40]
                images_dir = images_dir[int(len(images_dir) * 0): int(len(images_dir) * 0.1)]
                for img_name in images_dir:
                    with open('../../data/embryo/' + "_all_train" + ".txt", 'a') as the_file:
                        # with open('../data/sd1/val.txt', 'a') as the_file:
                        # the_file.write(data_dir_path+img_name+" "+img_name+'\n')
                        the_file.write(target_data_dir_path_2 + classes + "/" + img_name + " " + str(int(classes) - 1)+" "+'1' + '\n')


make_biased_dataset_emb_all_train()