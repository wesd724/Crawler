import os, re
import urllib.request
from urllib.request import urlopen
from bs4 import BeautifulSoup
import tkinter

# GUI 설정
window=tkinter.Tk()
window.title("섬네일 다운로더")
window.geometry("800x500+200+200")
window.resizable(False, False)

#라벨 설정
label = tkinter.Label(window, text = "네이버 웹툰 요일 선택")
label.pack()

#리스트 박스 설정
weeks = ['mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun']
listbox = tkinter.Listbox(window, height = len(weeks), width = 10);
for x in weeks: listbox.insert(tkinter.END, x)
listbox.place(x = 350, y = 40)

#텍스트 화면 설정
text = tkinter.Text(window, width=80,height=10)
text.place(x = 35, y = 210)
	
#다운로더 설정
def downLoader():
	html = urlopen('https://comic.naver.com/webtoon/weekday.nhn')
	bs = BeautifulSoup(html, 'html.parser')
	if not(os.path.isdir('./image')):
			os.makedirs(os.path.join('./image'))

	dailyAll = bs.find(class_='list_area daily_all')
	day = dailyAll.find('h4', class_=weeks[listbox.curselection()[0]]).next_sibling.next_sibling
	for img in day.find_all('img'):
		text.insert(tkinter.END, str(img) + "\n")
		title = img['title']
		title = re.sub('[^0-9a-zA-Zㄱ-힣]', '', title)
		urllib.request.urlretrieve(img['src'], './image/' + title + '.jpg')
		
	text.insert(tkinter.END,"다운로드 완료...")

#버튼 설정
button = tkinter.Button(window, text = '다운로드', command = downLoader)
button.place(x = 353, y = 395)

window.mainloop()

html = urlopen('https://comic.naver.com/webtoon/weekday.nhn')
bs = BeautifulSoup(html, 'html.parser')
dailyAll = bs.find(class_='list_area daily_all')

'''
column = dailyAll.find_all('div', class_='col')
for a in column:
	for b in a.find('h4').next_siblings:
		print(b)
		'''