import time
import os
import ctypes
import numpy as np
import msvcrt

background = np.array([[1,1,1,1,1,1,1,1,1,1,1,1],
                       [1,0,0,0,0,0,0,0,0,0,0,1],
                       [1,0,0,0,0,0,0,0,0,0,0,1],
                       [1,0,0,0,0,0,0,0,0,0,0,1],
                       [1,0,0,0,0,0,0,0,0,0,0,1],
                       [1,0,0,0,0,0,0,0,0,0,0,1],
                       [1,0,0,0,0,0,0,0,0,0,0,1],
                       [1,0,0,0,0,0,0,0,0,0,0,1],
                       [1,0,0,0,0,0,0,0,0,0,0,1],
                       [1,0,0,0,0,0,0,0,0,0,0,1],
                       [1,0,0,0,0,0,0,0,0,0,0,1],
                       [1,0,0,0,0,0,0,0,0,0,0,1],
                       [1,0,0,0,0,0,0,0,0,0,0,1],
                       [1,0,0,0,0,0,0,0,0,0,0,1],
                       [1,0,0,0,0,0,0,0,0,0,0,1],
                       [1,0,0,0,0,0,0,0,0,0,0,1],
                       [1,0,0,0,0,0,0,0,0,0,0,1],
                       [1,0,0,0,0,0,0,0,0,0,0,1],
                       [1,0,0,0,0,0,0,0,0,0,0,1],
                       [1,0,0,0,0,0,0,0,0,0,0,1],
                       [1,0,0,0,0,0,0,0,0,0,0,1],
                       [1,1,1,1,1,1,1,1,1,1,1,1]
                       ])

block_L = np.array([[0,0,0,0],
                    [0,1,0,0],
                    [0,1,1,1],
                    [0,0,0,0]])

#============================================================

def cls():
    os.system('cls')
     

def gotoxy(x,y):
    ctypes.windll.kernel32.SetConsoleCursorPosition(ctypes.windll.kernel32.GetStdHandle(-11),(((y&0xFFFF)<<0x10)|(x&0xFFFF)))

def draw_background():
    for j in range(0, 22):
        for i in range(0,12):
            if(background[j,i] == 1):
                print("*",end="")
            else:
                print("-",end="")
        print()

def make_block():
    for j in range(0,4):
        for i in range(0,4):
            if(block_L[j,i] == 1):
                gotoxy(i+x, j+y)
                print("*")
            
        
def delete_block():
    for j in range(0,4):
        for i in range(0,4):
            if(block_L[j,i] == 1):
                gotoxy(i+x, j+y)
                print("-")
            #else:
             #   gotoxy(i+x, j+y)
              #  print("-")
        #print()
        
def overlap_checka(tmp_x, tmp_y):#1번
    overlap_cnt = 0
    for i in range(0, 4):
        for j in range(0, 4):
            if(y + tmp_y + i < 22):
                if(block_L[i,j] == 1 & background[i+tmp_y+y,j+tmp_x+x] == 1):
                    overlap_cnt+=1
    return overlap_cnt

def overlap_check(tmp_x, tmp_y):#2번
    
    if(y + tmp_y + 4 <= 22 and x+tmp_x>=0):
        return (background[tmp_y+y:tmp_y+y+4,tmp_x+x:tmp_x+x+4]&block_L).sum()
    return 1

x = 3
y = 3
count = 0

#============================================================

#print(background.shape)            
              
draw_background()

while True:
    if msvcrt.kbhit():
        key = msvcrt.getch()
        
        if key == b'a':
            if (overlap_check(-1,0) == 0):
                delete_block()
                x-=1
                make_block()
            
        if key == b'd':
            if (overlap_check(1,0) == 0):
                delete_block()
                x+=1
                make_block()
            
        if key == b's':
            if (overlap_check(0,1) == 0):
                delete_block()6
                y+=1
                make_block()
    
#============================================================
    if count == 100:
        if (overlap_check(0,1) == 0):
            delete_block()
            y+=1
            make_block()
        count = 0
        
    count+=1
    time.sleep(0.01)