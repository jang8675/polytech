```
from tkinter import *
from tkinter.simpledialog import *

## 함수 선언 부분 ##
window = Tk()
window.geometry("400x100")

label1 = Label(window, text = "입력된 값")
label1.pack()

value = askinteger("확대배수", "주사위 숫자(1~6)을 입력하세요", minvalue = 1, maxvalue = 6)

label1.configure(text = str(value))
window.mainloop()
```
Label은 텍스트 뿌려주는 용도
askinteger : 숫자 받아와
value는 전역변수
configure로 숫자를 str로 형 변환을 해서 뿌려준다.

```
from tkinter import *
from tkinter.filedialog import *

## 함수 선언 부분 ##
window = Tk()
window.geometry("400x100")

label1 = Label(window, text = "선택된 파일 이름")
label1.pack()

filename = askopenfilename(parent = window, filetypes = (("PNG파일", "*.png"),("모든 파일", "*.*")))

label1. configure(text = str(filename))
window.mainloop()
```
filetype은 모든 파일을 불러올 수 있지만 base는 PNG 파일이다.

```
from tkinter import *
from tkinter.filedialog import askopenfilename

## 함수 선언 부분 ##
def func_open():
    filename = askopenfilename(parent=window, filetypes=(("PNG 파일", "*.png"), ("모든 파일", "*.*")))
    if filename:
        photo = PhotoImage(file=filename)
        pLabel.configure(image=photo)
        pLabel.image = photo

def func_exit():
    window.quit()
    window.destroy()

## 메인 코드 부분 ##
window = Tk()
window.geometry("500x500")
window.title("명화 감상하기")

photo = PhotoImage()
pLabel = Label(window, image=photo)
pLabel.pack(expand=1, anchor=CENTER)

mainMenu = Menu(window)
window.config(menu=mainMenu)
fileMenu = Menu(mainMenu)
mainMenu.add_cascade(label="파일", menu=fileMenu)
fileMenu.add_command(label="파일 열기", command=func_open)
fileMenu.add_separator()
fileMenu.add_command(label="프로그램 종료", command=func_exit)

window.mainloop()
```

```
from tkinter import *
from tkinter.filedialog import askopenfilename

## 함수 선언 부분 ##
def func_open():
    filename = askopenfilename(parent=window, filetypes=(("PNG 파일", "*.png"), ("모든 파일", "*.*")))
    photo = PhotoImage(file=filename)
    width = photo.width()
    height = photo.height()

    for i in range(height):
        for k in range(width):
            r, g, b = photo.get(k, i)
            grey = int((r+g+b)/3)
            photo.put("#%02x%02x%02x" % (grey, grey, grey), (k, i))

    pLabel.configure(image= photo)
    pLabel.image = photo

def func_exit():
    window.quit()
    window.destroy()

## 메인 코드 부분 ##
window = Tk()
window.geometry("500x500")
window.title("명화 감상하기")

photo = PhotoImage()
pLabel = Label(window, image=photo)
pLabel.pack(expand=1, anchor=CENTER)

mainMenu = Menu(window)
window.config(menu=mainMenu)
fileMenu = Menu(mainMenu)
mainMenu.add_cascade(label="파일", menu=fileMenu)
fileMenu.add_command(label="파일 열기", command=func_open)
fileMenu.add_separator()
fileMenu.add_command(label="프로그램 종료", command=func_exit)

window.mainloop()
```
위에 이미지를 검은, 회색으로 나타내기
2중 for문은 각각의 rgb값을 뽑아내기 위함
r,g,b

```
inFp = None # 입력 파일
inStr = "" # 읽어 온 문자열

inFp = open("C:\Temp\data1.txt", "r", encoding = "utf-8")

inStr = inFp.readline()
print(inStr, end = "")

inStr = inFp.readline()
print(inStr, end = "")

inStr = inFp.readline()
print(inStr, end = "")

inFp.close()
```
```
inFp = None # 입력 파일
inStr = "" # 읽어 온 문자열

inFp = open("C:\Temp\data1.txt", "r", encoding = "utf-8")

while True :
    inStr = inFp.readline()
    if inStr == "":
        break;
    print(inStr, end="")
    
inFp.close()
```
```
inFp = None # 입력 파일
inStr = "" # 읽어 온 문자열

inFp = open("C:\Temp\data1.txt", "r", encoding = "utf-8")

inList = inFp.readlines()
print(inList)

inFp.close()
```
while True문과 다르게 파일에 대한 접근이 가능하다.

```
outFp = None
outStr = ""

outFp = open("C:/Temp/data2.txt", "w")

while True :
    outStr = input("내용 입력 :")
    if outStr != "":
        outFp.writelines(outStr + "\n")
    else:
        break

outFp.close()
print("---정상적으로 파일에 씀 ---")
```
w는 쓰기 모드
자동으로 메모장을 만들고 input의 내용에 따라 
outStr에 저장을 해줌
"공백이 아니면 저장해주기"
if문을 받아 글을 작성함

```
from tkinter import *

## 험수 선언 부분 ##
def loadImage(fname):
    global inImage, XSIZE, YSIZE
    fp = open(fname, 'rb')

    for i in range(0, XSIZE):
        tmpList = []
        for k in range(0, YSIZE):
            data = int(ord(fp.read(1)))
            tmpList.append(data)
        inImage.append(tmpList)

    fp.close

def displayImage(image):
    global XSIZE, YSIZE
    rgbString = ""
    for i in range(0, XSIZE):
        tmpString = ""
        for k in range(0, YSIZE):
            data = image[i][k]
            tmpString += "#%02x%02x%02x" % (data, data, data) # x 뒤에 한칸 공백
        rgbString += "{"+ tmpString +"}"
    paper.put(rgbString)

## 전역 변수 선언 부분 ##
window = None
canva = None
XSIZE, YSIZE = 256, 256
inImage = []   # 2차원 리스트 (메모리)

## 메인 코드 부분 ##
window = Tk()
window.title("흑백 사진 보기")
canvas = Canvas(window, height = XSIZE, width = YSIZE)
paper = PhotoImage(width = XSIZE, height = YSIZE)
canvas.create_image((XSIZE / 2, YSIZE / 2), image = paper, state = "normal")

# 파일 --> 메모리
filename = 'RAW/tree.raw' # C:/CookAnalysis/RAW/tree.raw
loadImage(filename)

# 메모리 --> 화면
displayImage(inImage)

canvas.pack()
window.mainloop()
```

```
from PIL import Image

def convert_to_grayscale(input_image_path, output_image_path):
    # 이미지 열기
    image = Image.open(input_image_path)

    # 이미지를 흑백으로 변환
    grayscale_image = image.convert("L")

    # 흑백 이미지 저장
    grayscale_image.save(output_image_path)

if __name__ == "__main__":
    # 입력 및 출력 이미지 경로 설정
    input_image_path = "C:/Users/user141/Desktop/dog.png"
    output_image_path = "C:/Users/user141/Desktop/class/output_image.png"

    # 이미지를 흑백으로 변환하여 저장
    convert_to_grayscale(input_image_path, output_image_path)
```
흑백으로 지정 변환하는

```
def read_text_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        contents = file.read()
    return contents

def write_text_file(file_path, contents):
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(contents)

if __name__ == "__main__":
    file_path = "C:\Temp\data1.txt"

    # 텍스트 파일 읽기
    file_contents = read_text_file(file_path)

    # 화면에 출력
    print("원본 내용:")
    print(file_contents)

    # 수정된 내용 입력
    modified_contents = input("수정된 내용을 입력하세요:\n")

    # 수정된 내용을 텍스트 파일에 저장
    write_text_file(file_path, modified_contents)

    print("수정된 내용이 파일에 저장되었습니다.")
```
txt파일 지정해서 수정하는

-----------------------------------------
CSV
```
with open("C:\Users\user141\Downloads\source\CSV\singer1.csv", "r", encoding="UTF-8") as inFp:

    inStr = inFp.readline()
    print(inStr, end="")

    inStr = inFp.realine()
    print(inStr, end="")

```
csv 파일 한줄씩 읽기

```
def printList(pList):
    for data in pList:
        print(data, end='\t')
    print()

with open(r"C:\Users\user141\Downloads\source\CSV\singer1.csv", "r") as inFp:
    header = inFp.readline()
    header = header.strip()
    header_list = header.split(',')
    printList(header_list)
    for inStr in inFp:
        inStr = inStr.strip()
        row_list = inStr.split(',')
        printList(row_list)
```
csv 파일 헤더를 별도로 읽어서 처리한 후 나머지 모든 행을 리스트로 저장하고 각 항목을 분리해서 출력하는 코드

```
import tkinter as tk

def printList(pList):
    return '\t'.join(pList)

def readCSV(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    header = lines[0].strip().split(',')
    data = [line.strip().split(',') for line in lines[1:]]
    return header, data

def displayCSV(header, data):
    root = tk.Tk()
    root.title("CSV Viewer")

    header_str = printList(header)
    tk.Label(root, text=header_str, font=("Helvetica", 10, "bold")).pack()

    for row in data:
        row_str = printList(row)
        tk.Label(root, text=row_str).pack()

    root.mainloop()

if __name__ == "__main__":
    file_path = r"C:\Users\user141\Downloads\source\CSV\singer1.csv"
    header, data = readCSV(file_path)
    displayCSV(header, data)
```
GUI 창에 해당 내용을 뿌려주는 코드 

```
import tkinter as tk
from tkinter import filedialog
from tkinter import ttk

def readCSV(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    header = lines[0].strip().split(',')
    data = [line.strip().split(',') for line in lines[1:]]
    return header, data

def displayCSV(header, data):
    root = tk.Tk()
    root.title("CSV Viewer")

    tree = ttk.Treeview(root, columns=header, show="headings")
    for col in header:
        tree.heading(col, text=col)
    for row in data:
        tree.insert("", "end", values=row)
    tree.pack(expand=True, fill="both")

    root.mainloop()

def selectCSV():
    file_path = filedialog.askopenfilename(filetypes=[("CSV 파일", "*.csv"), ("모든 파일", "*.*")])
    if file_path:
        header, data = readCSV(file_path)
        displayCSV(header, data)

if __name__ == "__main__":
    selectCSV()
```
GUI 표로 보여주는것

```
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QAction, QFileDialog

def readCSV(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    header = lines[0].strip().split(',')
    data = [line.strip().split(',') for line in lines[1:]]
    return header, data

class CSVViewer(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("CSV Viewer")
        self.setGeometry(100, 100, 800, 600)

        openAct = QAction("&Open", self)
        openAct.triggered.connect(self.openFile)

        menubar = self.menuBar()
        fileMenu = menubar.addMenu("&File")
        fileMenu.addAction(openAct)

        self.tableWidget = QTableWidget()
        self.setCentralWidget(self.tableWidget)

    def openFile(self):
        options = QFileDialog.Options()
        file_path, _ = QFileDialog.getOpenFileName(self, "Open CSV File", "", "CSV Files (*.csv);;All Files (*)", options=options)
        if file_path:
            header, data = readCSV(file_path)
            self.populateTable(header, data)

    def populateTable(self, header, data):
        self.tableWidget.clear()
        self.tableWidget.setColumnCount(len(header))
        self.tableWidget.setHorizontalHeaderLabels(header)
        self.tableWidget.setRowCount(len(data))
        for row_idx, row in enumerate(data):
            for col_idx, col in enumerate(row):
                item = QTableWidgetItem(col)
                self.tableWidget.setItem(row_idx, col_idx, item)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = CSVViewer()
    mainWindow.show()
    sys.exit(app.exec_())
```
PyQt5로 보여주기

```
# 입력 파일과 출력 파일을 동일한 경로에서 열고 내용을 변경하여 다시 저장하는 코드입니다.

# 입력 파일을 읽기 모드로 엽니다.
with open(r"C:\Users\user141\Downloads\source\CSV\singer1.csv", "r") as inFp:
    # 출력 파일을 쓰기 모드로 엽니다.
    with open(r"C:\Users\user141\Downloads\source\CSV\singer1.csv", "w") as outFp:
        # 헤더를 읽어와서 처리합니다.
        header = inFp.readline()
        header = header.strip()  # 좌우 공백 제거
        header_list = header.split(',')  # 쉼표로 분리하여 리스트로 변환
        header_str = ','.join(map(str, header_list))  # 리스트를 문자열로 변환하여 다시 쉼표로 연결
        outFp.write(header_str + '\n')  # 헤더를 출력 파일에 씁니다.

        # 행별로 데이터를 읽어와서 처리합니다.
        for inStr in inFp:
            inStr = inStr.strip()  # 좌우 공백 제거
            row_list = inStr.split(',')  # 쉼표로 분리하여 리스트로 변환
            row_list[-1] = row_list[-1].replace('.', '/')  # 마지막 열의 .을 /로 변경
            height_str = "{0:.2f}".format(int(row_list[-2]))  # 끝에서 두 번째 열을 소수점 두 자리로 변환
            row_list[-2] = height_str  # 변환한 문자열로 열을 대체
            row_str = ','.join(map(str, row_list))  # 리스트를 문자열로 변환하여 다시 쉼표로 연결
            outFp.write(row_str + '\n')  # 수정된 행을 출력 파일에 씁니다.

print('save.OK~')  # 저장 완료 메시지 출력
```

```
myStr = "2025-5-5"
newStr = myStr.replace('-', '#')
print(newStr)
```
```
num1, num2 =1234.555, 100
formatted_str = "{0:0.0f}{1:0.2f}".format(num1, num2)
print(formatted_str)
```
```
myList = ['파이썬', '데이터', '분석']
joined_str = '#'.join(myList)
print(joined_str)
```
```
myList = [100, 200, 300]
str_list = list(map(str, myList))
print(str_list)
```
```
myList = [2025, 8, 8]
joined_str = '/'.join(map(str, myList))
print(joined_str)
```

```
# 입력 파일과 출력 파일을 동일한 경로에서 열고 내용을 변경하여 다시 저장하는 코드입니다.

# 입력 파일을 읽기 모드로 엽니다.
with open(r"C:\Users\user141\Downloads\source\CSV\singer165.csv", "r") as inFp:
    # 출력 파일을 쓰기 모드로 엽니다.
    with open(r"C:\Users\user141\Downloads\source\CSV\singer2.csv", "w") as outFp:
        # 헤더를 읽어와서 처리합니다.
        header = inFp.readline()  # 첫 줄을 읽어옵니다.
        header = header.strip()  # 좌우 공백을 제거합니다.
        header_list = header.split(',')  # 쉼표로 분리하여 리스트로 변환합니다.
        # 필요한 열의 인덱스를 찾습니다.
        idx1 = header_list.index('아이디')
        idx2 = header_list.index('이름')
        idx3 = header_list.index('평균 키')
        # 필요한 열만을 남기기 위해 새로운 헤더 리스트를 만듭니다.
        header_list = [header_list[idx1], header_list[idx2], header_list[idx3]]
        header_str = ','.join(map(str,header_list))  # 리스트를 문자열로 변환합니다.
        outFp.write(header_str + '\n')  # 헤더를 출력 파일에 씁니다.

        # 행별로 데이터를 읽어와서 처리합니다.
        for inStr in inFp:
            inStr = inStr.strip()  # 좌우 공백을 제거합니다.
            row_list = inStr.split(',')  # 쉼표로 분리하여 리스트로 변환합니다.
            # 특정 조건을 만족하는 행만을 남깁니다.
            if int(row_list[idx3]) >= 165:  # 평균 키가 165 이상인 행만을 선택합니다.
                row_list = [row_list[idx1], row_list[idx2], row_list[idx3]]  # 필요한 열만을 선택합니다.
                row_str = ','.join(map(str, row_list))  # 리스트를 문자열로 변환합니다.
                outFp.write(row_str + '\n')  # 선택된 행을 출력 파일에 씁니다.

print('save.OK~')  # 저장 완료 메시지를 출력합니다.
```

```
import csv

with open(r"C:\Users\user141\Downloads\source\CSV\singer2.csv", "r") as inFp:
    csvReader = csv.reader(inFp)
    header_list = next(csvReader)
    print(header_list[1], header_list[6])
    for row_list in csvReader:
        # YouTube 조회수 데이터를 처리합니다.
        youtube = int(row_list[6].replace(',', ''))  # 쉼표를 제거하고 정수로 변환합니다.
        youtube = int(youtube / 10000)  # 1만 단위로 변환합니다.
        # 가수 이름과 YouTube 조회수를 출력합니다.
        print(row_list[1], str(youtube) + "만")

```
csv 파일 안 10000단위를 '만'이라고 표기하여 표시하게 함

```
from tkinter import *
import csv

## 함수 선언 부분 ##
def makeEmptySheet(r, w):
    """
    주어진 행과 열 수에 맞게 빈 시트를 생성하는 함수입니다.
    :param r: 행 수
    :param w: 열 수
    :return: 생성된 시트
    """
    retList = []
    for i in range(0, r):
        tmpList = []
        for k in range(0, w):
            ent = Entry(window, text='', width=10)
            ent.grid(row=i, column=k)
            tmpList.append(ent)
        retList.append(tmpList)
    return retList

## 전역 변수 부분 ##
csvList = []  # CSV 데이터를 저장할 리스트
rowNum, colNum = 0, 0  # CSV 데이터의 행과 열 수
workSheet = []  # GUI에서 사용할 작업 시트

## 메인 코드 부분 ##
window = Tk()  # 윈도우 생성

# CSV 파일 열기 및 데이터 읽기
with open(r"C:\Users\user141\Downloads\source\CSV\new_singer1.csv", "r") as inFp:
    csvReader = csv.reader(inFp)
    header_list = next(csvReader)  # 헤더 읽기
    csvList.append(header_list)  # 헤더를 CSV 데이터 리스트에 추가
    for row_list in csvReader:
        csvList.append(row_list)  # 나머지 행 데이터를 CSV 데이터 리스트에 추가

rowNum = len(csvList)  # 행 수 설정
colNum = len(csvList[0])  # 열 수 설정
workSheet = makeEmptySheet(rowNum, colNum)  # GUI에서 사용할 작업 시트 생성

# 특정 열의 데이터를 확인하여 배경색 변경
idx = 6  # 변경할 열의 인덱스
for i in range(0, rowNum):
    for k in range(0, colNum):
        # 숫자인 경우 배경색 변경
        if csvList[i][idx].isnumeric() and int(csvList[i][idx]) >= 167:
            ent = workSheet[i][k]
            ent.configure(bg='yellow')
        workSheet[i][k].insert(0, csvList[i][k])  # 데이터 입력

window.mainloop()  # GUI 실행

```
평균 키 167이상인 가수 그룹의 행 색상도 변경, GUI 환경으로 출력

```
from tkinter import *
import csv

## 함수 선언 부분 ##
def makeEmptySheet(r, w):
    """
    주어진 행과 열 수에 맞게 빈 시트를 생성하는 함수입니다.
    :param r: 행 수
    :param w: 열 수
    :return: 생성된 시트
    """
    retList = []
    for i in range(0, r):
        tmpList = []
        for k in range(0, w):
            ent = Entry(window, text='', width=10)
            ent.grid(row=i, column=k)
            tmpList.append(ent)
        retList.append(tmpList)
    return retList

## 전역 변수 부분 ##
csvList = []  # CSV 데이터를 저장할 리스트
rowNum, colNum = 0, 0  # CSV 데이터의 행과 열 수
workSheet = []  # GUI에서 사용할 작업 시트

## 메인 코드 부분 ##
window = Tk()  # 윈도우 생성

# CSV 파일 열기 및 데이터 읽기
with open(r"C:\Users\user141\Downloads\source\CSV\new_singer1.csv", "r") as inFp:
    csvReader = csv.reader(inFp)
    header_list = next(csvReader)  # 헤더 읽기
    csvList.append(header_list)  # 헤더를 CSV 데이터 리스트에 추가
    for row_list in csvReader:
        csvList.append(row_list)  # 나머지 행 데이터를 CSV 데이터 리스트에 추가

rowNum = len(csvList)  # 행 수 설정
colNum = len(csvList[0])  # 열 수 설정
workSheet = makeEmptySheet(rowNum, colNum)  # GUI에서 사용할 작업 시트 생성

# 특정 열의 데이터를 확인하여 배경색 변경
idx = 6  # 변경할 열의 인덱스
for i in range(0, rowNum):
    for k in range(0, colNum):
        # 숫자인 경우 배경색 변경
        if csvList[i][idx].isnumeric() and int(csvList[i][idx]) >= 167:
            ent = workSheet[i][k]
            ent.configure(bg='yellow')
            if csvList[i][1] == "트와이스":
                csvList[i][idx] = "168"
        workSheet[i][k].insert(0, csvList[i][k])

new_file_path = r"C:\Users\user141\Downloads\source\CSV\new_singer_modified.csv"
with open(new_file_path, "w", newline='') as outFp:
    csvWriter = csv.writer(outFp)
    csvWriter.writerows(csvList)

window.mainloop()  # GUI 실행
```
트와이스 키를 168로 변경해보기

```
import xlrd

workbook = xlrd.open_workbook(r"C:\Users\user141\Downloads\source\Excel\singer.xls")
sheetCount = workbook.nsheets
print('워크시트는 %d개 입니다' % (sheetCount))

wsheetList = workbook.sheets()
for worksheet in wsheetList:
    print('**워크시트의 이름 : %s' % (worksheet.name))
    print("행 수는 %d, 열 개수는 %d 입니다." % (worksheet.nrows, worksheet.ncols))
```
xls 파일의 행과 열

```
import xlrd

workbook = xlrd.open_workbook(r"C:\Users\user141\Downloads\source\Excel\singer.xls")
sheetCount = workbook.nsheets

wsheetList = workbook.sheets()
for worksheet in wsheetList:
    print('** 워크시트의 이름: %s' % (worksheet.name))
    for row in range(worksheet.nrows):
        for col in range(worksheet.ncols):
            print("%s" % worksheet.cell_value(row, col), end = '\t')
        print()
    print()
```
엑셀 파일의 모든 내용을 출력하는 코드

```
import xlrd

# Excel 파일 열기
workbook = xlrd.open_workbook(r"C:\Users\user141\Downloads\source\Excel\singer.xls")

# 시트 수 확인
sheetCount = workbook.nsheets

# 전체 인원 수와 행 수 초기화
personNum = 0
rowCount = 0

# 가수 그룹 인원 정보가 있는 열 인덱스
personIdx = 2

# 시트 리스트 가져오기
wsheetList = workbook.sheets()

# 각 시트에서 가수 그룹 인원 합계 계산
for worksheet in wsheetList:
    rowCount += worksheet.nrows - 1  # 헤더를 제외한 행 수
    for row in range(1, worksheet.nrows):  # 헤더는 건너뛰고 데이터부터 시작
        personNum += int(worksheet.cell_value(row, personIdx))  # 각 행의 가수 그룹 인원 수 더하기

# 결과 출력
print("전체 가수 그룹 인원 합계:", personNum)
print("가수 그룹 인원 평균:", personNum / rowCount)
```
모든 워크시트에서 인원의 총합과 평균을 계산