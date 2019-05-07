# 打開檔案
def read(file):
	Line = []
	with open(file, 'r', encoding = 'utf-8-sig') as f:
		for line in f:
			Line.append(line.strip())
	return(Line)
		# if line.strip() is 'Allen':
		# 	print('name')
		# else:
		# 	print('chat')
# outcome = read('input.txt')
# print(outcome)

def calculate(Line):
	person = None
	Allen_word = 0
	Viki_word = 0
	Allen_picture = 0
	Viki_picture = 0 
	Allen_stick = 0
	Viki_stick = 0
	for line in Line:
		s = line.split(' ')
		time = s[0]
		name = s[1]
		if name == 'Allen':
			if s[2] == '貼圖':
				Allen_stick += 1	
			elif s[2] == '圖片':
				Allen_picture += 1
			else:
				for m in s[2:]:
					Allen_word += len(m)
		elif name == 'Viki':
			if s[2] == '貼圖':
				Viki_stick += 1
			elif s[2] == '圖片':
				Viki_picture += 1
			else:
				for m in s[2:]:
					Viki_word += len(m)
	return (Allen_word, Viki_word, Allen_stick, Viki_stick, Allen_picture, Viki_picture)

		


# 目前圖片跟貼圖的計數仍然有誤，要修正


		

	
# 這邊有可以調整的部分，None練習

def output(New_Line):
	with open('output.txt', 'w', encoding = 'utf-8-sig') as f:
		for line in New_Line:
			f.write(line + '\n')







# 寫成檔案
def main(file):
	Line = read(file)
	# outcome = calculate(Line)
	# print(outcome)
	outcome1, outcome2, outcome3, outcome4, outcome5, outcome6 = calculate(Line)
	print('Allen\'s word:',outcome1,'Viki\'s word:', outcome2, 'Allen\'s stick:',outcome3, 'Viki\'s stick:', outcome4,'Allen\'s picture:', outcome5, 'Viki\'s picture:', outcome6)
	# output(outcome)

main("-LINE-Viki.txt")
