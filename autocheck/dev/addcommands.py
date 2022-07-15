from hcskr import asyncSelfCheck, QuickTestResult
import sys
import os
import asyncio

argvlist=sys.argv

flag='init'
dosc=False
addidx=0

userfile=open(r"C:\Users\DGSW\Desktop\autocheck\users.txt",'a',encoding='utf-8')
userfile.close()

for i in argvlist:
    if flag=='init':
        if i=='add':
            flag='add'
            if userfile.closed:
                userfile=open(r"C:\Users\DGSW\Desktop\autocheck\users.txt",'a',encoding='utf-8')
            userfile.write('\n')
        else:
            dosc=True
            break
    elif flag=='add':
        if i[0]=='-':
            if i[1:]=='sc':
                dosc=True
        else:
            userfile.write(i+' ')

if not userfile.closed:
    userfile.close()

if not dosc:
    sys.exit()

if __name__ == '__main__':
    py_ver = int(f"{sys.version_info.major}{sys.version_info.minor}")
    if py_ver > 37 and sys.platform.startswith('win'):
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

userfile=open(r"C:\Users\DGSW\Desktop\autocheck\users.txt",'r',encoding='utf-8')
lines = userfile.readlines()
stuinfo=[line.split() for line in lines]
userfile.close()

quicktest = argvlist[1]
# quicktest = "no"
# quicktest = "ne"

area = "대구광역시"
school = "대구소프트웨어마이스터고등학교"
sctype = "고등학교"
qtno = "none"
qtne = "negative"

global result

if quicktest == "no":
    qt = qtno
elif quicktest == "ne":
    qt = qtne


async def main():
    global result
    students = [asyncio.ensure_future(asyncSelfCheck(
        stu[0], stu[1], area, school, sctype, stu[2], quicktestresult=QuickTestResult[qt])) for stu in stuinfo]
    result = await asyncio.gather(*students, return_exceptions=True)

if __name__ == "__main__":
    asyncio.run(main())

logfile = open(r"C:\Users\DGSW\Desktop\autocheck\log.txt", 'w')
for i in range(len(stuinfo)):
    logfile.write(stuinfo[i][0]+' : '+str(result[i])+'\n')
logfile.close()
os.system(r"start C:\Users\DGSW\Desktop\autocheck\log.txt")