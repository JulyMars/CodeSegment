import csv
import re

#通过抛出异常
def is_num_by_except(str):
    try:
        num = int(str)
        if num > 10000 and num < 99999:
        	return True
        else:
        	return False
    except ValueError:
#        print "%s ValueError" % num
        return False

f = open("中文id.txt", "w+")
    
#打开文件，用with打开可以不用去特意关闭file了，python3不支持file()打开文件，只能用open()
with open("word.csv","r",encoding="utf-8") as csvfile:
#读取csv文件，返回的是迭代类型
	read = csv.reader(csvfile)
	for i in read:
		if len(i) > 1:
			if len(i[0]) == 5 and is_num_by_except(i[0]):
				#一个小应用，判断一段文本中是否包含简体中：
				zhPattern = re.compile(u'[\u4e00-\u9fa5]+')
				contents = i[1]
				match = zhPattern.search(contents)
				if match:
					print(i[0],i[1])
					f.write(i[0] + "\t" + i[1] + "\n")
f.close()