def my(file_path,key,value):
    with open(file_path,'r') as file:
        m=file.readlines()
    with open(file_path,'w') as file:
        for i in m:
            if key in i:
                file.write(key + "=" + value + "\n")
            else:
                file.write(i)
my('settings.conf','my','40s')