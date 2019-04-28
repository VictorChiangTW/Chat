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

def convert(Line):
	New = []
	person = None
	for line in Line:
	    if line == 'Allen':
	    	person = 'Allen'
	    	continue
	    elif line == "Tom":
	    	person = 'Tom'
	    	continue
	    if person:
	    	New.append(person + ':' + line)
	return New

# 這邊有可以調整的部分，None練習

def output(New_Line):
	with open('output.txt', 'w', encoding = 'utf-8-sig') as f:
		for line in New_Line:
			f.write(line + '\n')







# 寫成檔案
def main(file):
	Line = read(file)
	outcome = convert(Line)
	output(outcome)

main("input.txt")
