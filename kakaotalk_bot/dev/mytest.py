import win32gui, win32con, win32api

room = win32gui.FindWindow(None, "ㅇㅅㅈ")
inBox = win32gui.FindWindowEx(room, None , "RICHEDIT50W" , None)  # 채팅창의 메세지 입력창

def kakao_sendtext(inText):
    win32api.SendMessage(inBox, win32con.WM_SETTEXT, 0, inText) # 채팅창 입력
    win32api.PostMessage(inBox, win32con.WM_KEYDOWN, win32con.VK_RETURN, 0)
    win32api.PostMessage(inBox, win32con.WM_KEYUP, win32con.VK_RETURN, 0) # 엔터키

kakao_sendtext("test")