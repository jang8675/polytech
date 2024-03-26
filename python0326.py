## 함수 선언 부분 ##
def func1():
    global a # 이 함수 안에서 a는 전역 변수
    a = 10 # 지역 변수
    print("func1()에서 a값 %d" % a)
def func2():
    print("func2()에서 a값 %d" % a)
## 변수 선언 부분 ##
a = 20  # 전역 변수
## 메인 코드 부분 ##
func1()
func2()


## 함수 선언 부분 ##
def func1():
    result = 100
    return result
def func2():
    print("반환값이 없는 함수 실행")
## 변수 선언 부분 ##
hap = 0
## 메인 코드 부분 ##
hap = func1()
print("func1()에서 돌려준 값 ==> %d" % hap)
func2()


## 함수 선언 부분 ##
def multi(v1, v2):
    retList = []   # 반환할 리스트
    res1 = v1 + v2
    res2 = v1 - v2
    retList.append(res1)
    retList.append(res2)
    return retList
## 변수 선언 부분 ##
myList = []
hap, sub = 0, 0
## 메인 코드 부분 ##
myList = multi(100, 200)
hap = myList[0]
sub = myList[1]
print("multi()에서 돌려준 값 ==> %d, %d" % (hap, sub))


def para2_func( v1, v2):
    result = 0
    result = v1 + v2
    return result
def para3_func(v1, v2, v3):
    result = 0
    result = v1 + v2 + v3
    return result
## 변수 선언 부분 ##
hap = 0
## 메인 코드 부분 ##
hap = para2_func(10, 20)
print("매개변수가 2개인 함수를 호출한 결과 ==> %d" % hap)
hap = para3_func(10, 20, 30)
print("매개변수가 3개인 함수를 호출한 결과 ==> %d" % hap)


import random
## 함수 선언 부분 ##
def getNumber():
    return random.randrange(1, 46)
# 변수 선언 부분 ##
lotto = []
num = 0

## 메인 코드 부분 ##
print("**로또 추첨을 시작합니다.** \n");

while True:
    num = getNumber()

    if lotto.count(num) == 0:
        lotto.append(num)
    if len(lotto) >= 6 :
        break

print("추첨된 로또 번호 ==>", end = "")
lotto.sort()
for i in range(0, 6):
    print("%d" % lotto[i], end ="")


from tkinter import *

window = Tk()

## 이 부분에서 화면을 구성하고 처리함 ##
window.mainloop()


from tkinter import *

window = Tk()
window.title("윈도창 연습")
window.geometry("400x100")
window.resizable(width = FALSE, height = FALSE)   # 창 사이즈 조절 안됨

window.mainloop()


from tkinter import *
window = Tk()

label1 = Label(window, text = "COOKBOOK, 데이터분석을")
label2 = Label(window, text ="열심히", font = ("궁서체", 30), fg = "blue")
label3 = Label(window, text = "공부 중입니다.", bg = "magenta", width = 20, height =5, anchor = SE)
# bg는 배경을 지정할 때 사용, anchor은 <a> 태그와 똑같음

label1.pack()
label2.pack()
label3.pack()

window.mainloop()


from tkinter import *
window = Tk()

photo = PhotoImage(file = "dog.png") # 상대경로
label1 = Label(window, image = photo)

label1.pack()

window.mainloop()


from tkinter import *
window = Tk()

photo1 = PhotoImage(file ="dog.png") # 절대 경로
photo2 = PhotoImage(file = "youtube.png")

label1 = Label(window, image = photo1)
label2 = Label(window, image = photo2)

label1.pack(side=RIGHT)
label2.pack(side=LEFT)

window.mainloop()


from tkinter import *
window = Tk()

button1 = Button(window, text = "파이썬 종료", fg = "red", command = quit)

button1.pack()

window.mainloop()


from tkinter import *
from tkinter import messagebox

## 함수 선언 부분 ##
def myFunc():
    messagebox.showinfo("강아지 버튼", "강아지가 귀엽죠? ^^")

## 메인 코드 부분 ##
window = Tk()

photo = PhotoImage(file = "dog.png")
button1 = Button(window, image = photo, command = myFunc)

button1.pack()

window.mainloop()


from tkinter import *
from tkinter import messagebox
window = Tk()

## 함수 선언 부분 ##
def myFunc():
    if chk.get() == 0:
        messagebox.showinfo("", "체크버튼이 꺼졌어요.")
    else :
        messagebox.showinfo("","체크버튼이 켜졌어요.")

## 메인 코드 부분 ##
chk = IntVar()
cb1 = Checkbutton(window, text = "클릭하세요", variable = chk, command = myFunc)

cb1.pack()

window.mainloop()


from tkinter import *
window = Tk()

## 함수 선언 부분 ##
def myFunc():
    if var.get() == 1 :
        label1.configure(text = "파이선")
    elif var.get() == 2 :
        label1.configure(text = "C++")
    else :
        label1.configure(text = "Java")

## 메인 코드 부분 ##
var = IntVar()
rb1 = Radiobutton(window, text = "파이썬",
                  variable = var, value = 1, command = myFunc)
rb2 = Radiobutton(window, text = "C++", 
                  variable = var, value = 2, command = myFunc)
rb3 = Radiobutton(window, text = "Java", 
                  variable = var, value = 3, command = myFunc)

label1 = Label(window, text = "선택한 언어:", fg = "red")

rb1.pack()
rb2.pack()
rb3.pack()
label1.pack()

window.mainloop()


from tkinter import *

window = Tk()

mainMenu = Menu(window)
window.config(menu = mainMenu)

fileMenu = Menu(mainMenu)
mainMenu.add_cascade(label = "파일", menu = fileMenu)
fileMenu.add_command(label="열기")
fileMenu.add_separator()
fileMenu.add_command(label = "종료")

window.mainloop()


from tkinter import *
from tkinter import messagebox

## 함수 선언 부분 ##
def func_open():
    messagebox.showinfo("메뉴선택", "열기 메뉴를 선택함")

def func_exit():
    window.quit()
    window.destroy()

## 메인 코드 부분 ##
window = Tk()

mainMenu = Menu(window)
window.config(menu = mainMenu)

fileMenu = Menu(mainMenu)
mainMenu.add_cascade(label = "파일", menu = fileMenu)
fileMenu.add_command(label="열기", command = func_open)
fileMenu.add_separator()
fileMenu.add_command(label = "종료", command = func_exit)

window.mainloop()