from hcskr import asyncSelfCheck, QuickTestResult
from os import system
from os import path
import sys
import asyncio

if __name__ == '__main__':
    py_ver = int(f"{sys.version_info.major}{sys.version_info.minor}")
    if py_ver > 37 and sys.platform.startswith('win'):
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

def find_comment(element):
    if element[0][:2]=='//':
         return False
    return True

dir=path.split(path.abspath(__file__))[0]

userfile=open(dir+"\\users.txt",'r',encoding='utf-8')
lines = userfile.readlines()
stuinfo=[line.split() for line in lines]
stuinfo=list(filter(find_comment,stuinfo))
userfile.close()

quicktest = sys.argv[1]
# quicktest = "no"
# quicktest = "ne"

area = "대구광역시"
school = "대구소프트웨어마이스터고등학교"
sctype = "고등학교"
qtno = "none"
qtne = "negative"

qt = ""
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

f = open("log.txt", 'w')
for i in range(len(stuinfo)):
    f.write(stuinfo[i][0]+' : '+str(result[i])+'\n')
f.close()
system(dir+"\\log.txt")