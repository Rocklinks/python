def fh(file_path,key,value):
    with open(file_path,'r') as file:
        f=file.readlines()
    with open(file_path,'w') as file:
        for i in f:
            if key in i:
                file.write(key + "=" + value + "\n")
            else:
                file.write(i)
fh('settings.conf','max','200')