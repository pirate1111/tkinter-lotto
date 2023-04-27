import tkinter                          # 그래픽 패키지 tkinter 가져오기
import tkinter.font                     # tkinter의 font메소드 가져오기
import random                           # random함수 가져오기

lotto_num = range(1, 46)                # 로또 번호가 될 1~45의 숫자를 lotto_num 변수에 저장

def buttonClick():                      # 버튼 클릭시 5개의 랜덤한 숫자를 Label을 사용해 출력하는 사용자정의함수 만듦
    label = tkinter.Label(window, text=str(random.sample(lotto_num, 6)))
    label.pack()

window=tkinter.Tk()                     # 윈도우창 생성
window.title("lotto")                   # 창 이름 설정
window.geometry("400x200")              # 창 크기 설정
window.resizable(False, False)          # 창 크기 수평, 수직 고정

button = tkinter.Button(window, overrelief="solid", text="번호 확인", width=15, 
                        command=buttonClick, repeatdelay=1000, repeatinterval=100) 
# 버튼 생성. 버튼에 쓰여진 글자는 "번호 확인", 버튼 너비 15, 버튼 누르면 buttonClick 함수 실행, 처음 명령 수행 딜레이 1000, 그 다음 명령 수행시 100

button.pack()                           # 버튼 메소드 쓰는 명령어인듯

window.mainloop()                       # 창 바로 안 꺼지는 거였던 거 같음