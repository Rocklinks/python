def m(file_path,key,value):
    with open(file_path,'r') as file:
        a=file.readlines()
    with open(file_path,'w') as file:
        for i in a:
            if key in i:
                file.write(key + "=" + value + "\n")
            else:
                file.write(i)
m('settings.conf','me','2')
