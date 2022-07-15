from time import sleep
import win32con
import win32api
import win32gui
import meal_api
import values

meal = meal_api.meal_menu()
meal_data=["","",""]

for i in range(3):
    if len(meal[values.meal_name[i]])==0:
        meal[values.meal_name[i]].append('없음')
    meal_data[i]=values.meal_name[i]+"\n"+"\n".join(meal[values.meal_name[i]])

global name
name = "ㅇㅅㅈ"

kakao_opentalk_name = name


def kakao_sendtext(chatroom_name, text):

    hwndMain = win32gui.FindWindow( None, chatroom_name)
    hwndEdit = win32gui.FindWindowEx( hwndMain, None, "RICHEDIT50W", None)

    win32api.SendMessage(hwndEdit, win32con.WM_SETTEXT, 0, text)
    SendReturn(hwndEdit)



def SendReturn(hwnd):
    win32api.PostMessage(hwnd, win32con.WM_KEYDOWN, win32con.VK_RETURN, 0)
    sleep(0.01)
    win32api.PostMessage(hwnd, win32con.WM_KEYUP, win32con.VK_RETURN, 0)


def open_chatroom(chatroom_name):

    hwndkakao = win32gui.FindWindow(None, "카카오톡")
    hwndkakao_edit1 = win32gui.FindWindowEx( hwndkakao, None, "EVA_ChildWindow", None)
    hwndkakao_edit2_1 = win32gui.FindWindowEx( hwndkakao_edit1, None, "EVA_Window", None)
    hwndkakao_edit2_2 = win32gui.FindWindowEx( hwndkakao_edit1, hwndkakao_edit2_1, "EVA_Window", None)
    hwndkakao_edit3 = win32gui.FindWindowEx( hwndkakao_edit2_2, None, "Edit", None)


    win32api.SendMessage(hwndkakao_edit3, win32con.WM_SETTEXT, 0, chatroom_name)
    sleep(1)
    SendReturn(hwndkakao_edit3)
    sleep(1)


def main():
    open_chatroom(kakao_opentalk_name)
    for i in range(3):
        print(meal[values.meal_name[i]])
        text = meal_data[i]
        kakao_sendtext(kakao_opentalk_name, text)


if __name__ == '__main__':
    main()