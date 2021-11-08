from tkinter import *
from tkinter import messagebox
import os
import datetime


def screen():
    os.system("C:\\Windows\\System32\\Ribbons.scr")


def shutdownow():
    os.system("shutdown -s -t 0")


now = datetime.datetime.now()
root = Tk()
root.title("컴퓨터 종료")
bios = 0
ab = Button(root, text="즉시 재시작").pack()
bb = Button(root, text="즉시 종료", command=shutdownow).pack()
cb = Button(root, text="종료 설정").pack()
db = Button(root, text="재시작 설정").pack()
eb = Button(root, text="즉시 로그아웃").pack()

gb = Button(root, text="절전").pack()
hb = Button(root, text="최대절전").pack()
ib = Button(root, text="다음 부팅때 바이오스 진입").pack()

e1 = Entry(root)
e1.insert(0, '컴퓨터가 종료 되는 시간을 적어주세요!(예)현재시각:1:00:00->종료시각(희망시각):1:30:00)')
e1.pack()
nowTime = now.strftime('%H:%M:%S')


def status1_print():
    print(CheckVar1.get())


def status2_print():
    print(CheckVar2.get())


def status3_print():
    print(CheckVar2.get())
    root.messagebox.showinfo(title="작업 성공!", message="[로그아웃]옵션을 성공적으로 추가하였습니다!")


def status4_print():
    if CheckVar1.get() + CheckVar2.get() + CheckVar3.get() == 1:
        print(CheckVar4.get())
        root.messagebox.showinfo(title="작업 성공!", message="[바이오스 부팅]옵션을 성공적으로 추가하였습니다!")
    else:
        root.messagebox.showerror(title=None, message="작업이 성공적으로 실패하였습니다! 옵션은 한 가지만 선택 할 수 있습니다!(모든 옵션을 초기 값으로 변경합니다! "
                                                      "그 이외의 오류는 제작자의 메일로 보내 주세요!)")


CheckVar1 = IntVar()
CheckVar2 = IntVar()
CheckVar3 = IntVar()
CheckVar4 = IntVar()

c1 = Checkbutton(root, text="종료", variable=CheckVar1, command=status1_print).pack()
c2 = Checkbutton(root, text="재시작", variable=CheckVar2, command=status2_print).pack()
c3 = Checkbutton(root, text="로그아웃", variable=CheckVar3, command=status3_print).pack()
c4 = Checkbutton(root, text="바이오스 부팅", variable=CheckVar4, command=status4_print).pack()

root.mainloop()
