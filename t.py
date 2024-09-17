def r(file_type,key,val):
    with open(file_type,'r')as file:
        q=file.readlines()
    with open(file_type,'w') as file:
        for i in q:
            if key in i:
                file.write(key + "=" + val + "\n")
            else:
                file.write(i)
r('settings.conf','t','20s')
