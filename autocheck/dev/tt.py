userfile=open(r"C:\Users\DGSW\Desktop\autocheck\users.txt",'r',encoding='utf-8')
lines = userfile.readlines()
stuinfo=[line.split() for line in lines]
userfile.close()