import os
import multiprocessing
import time
import threading
i = 0          # the num of Threads is already  (in need of changing to Threads)


def copy(file_name, old_path, new_path):
    ti1 = time.time()
    # print("PROCESSING IS TO START！PID IS %d" % os.getpid())
    with open(os.path.join(old_path, file_name), "br") as rstream:
        file_content = rstream.read()
    with open(os.path.join(new_path, file_name), "bw") as wstream:
        wstream.write(file_content)
    ti2 = time.time()
    print(f"{file_name}_DOC(PID：{os.getpid()})IS ALREADY DUPLICATED！TIME ASSUMING:{ti2-ti1}")


def fetch_dir(dir_name):
    # 1.获取文件夹名，以及文件夹下的文件名
    doc_name_list = os.listdir(dir_name)
    return doc_name_list


def main(dir_name, dir_create, doc_list):
    global i, dir_name_init
    waitting_list = []

    # 3.Build processing pool
    po = duplicate_multiprocessing.Pool(3)
    # 4.Add process
    for file in doc_list:    # judge the doc is dir or not
        if os.path.isdir(dir_name + '\\' + file) and file != dir_name.split('\\')[-1]:
            waitting_list.append(file)
            try:
                os.mkdir(dir_create + '\\' + waitting_list[-1])
            except:
                pass
        else:
            po.apply_async(copy, args=(file, dir_name, dir_create))
    # 5.create loop and recursion for dir inside layer
    if waitting_list:
        for dir_file in waitting_list:
            if dir_file != dir_name.split('\\')[-1]:
                dirs = dir_name + '\\' + dir_file
                doc_name_list_update = fetch_dir(dirs)
                if dir_create.split('\\')[-1] != dir_name.split('\\')[-1]:    # redirect the path
                    dir_create = dir_name + '\\' + dir_name.split('\\')[-1]
                dir_create += '\\' + dir_file
                main(dirs, dir_create, doc_name_list_update)
        #       i += 1
        # for count in range(i - len(doc_name_list_update), i):        # in need of changing to treads
        #     print("开始")
        #     locals()[f"t{count}"].start()
    else:
        dir_create = dir_name_init + '\\' + dir_name_init.split('\\')[-1]
        print("复制已完毕！")

    # 6.close the pool
    po.close()
    po.join()           # let main process waiting for other process


if __name__ == "__main__":
    # 1.get the name of path and dirs under the path
    dir_name_init = input("Please enter the path to copy:")
    doc_name_list_init = fetch_dir(dir_name_init)
    try:                    # create same dir at first time
        os.mkdir(dir_name_init + '\\' + dir_name_init.split('\\')[-1])
    except:
        pass
    dir_create_new = dir_name_init + '\\' + dir_name_init.split('\\')[-1]
    main(dir_name_init, dir_create_new, doc_name_list_init)
