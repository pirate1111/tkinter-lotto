import tkinter              # 그래픽 tkinter 가져오기
import tkinter.font         # tkinter의 font메소드 가져오기
import random

lotto_num = range(1, 46)

def buttonClick():
    print(random.sample(lotto_num, 6))

window=tkinter.Tk()
window.title("lotto")
window.geometry("400x200")
window.resizable(False, False)

button = tkinter.Button(window, overrelief="solid", text="번호 확인", width=15,
                        command=buttonClick, repeatdelay=1000, repeatinterval=100)
button.pack()

window.mainloop()