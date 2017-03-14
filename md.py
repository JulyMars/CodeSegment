import os
import os.path
import filecmp
import shutil

# foldProject = r"D:\work\awf\resource"
# foldGame = r""


def copyFile(sourceFileName, targetFileName):
	shutil.copy (sourceFileName, targetFileName)

def checkFiles(sourcFolder, targetFolder):
	for parent,dirnames,filenames in os.walk(sourcFolder):    #三个参数：分别返回1.父目录 2.所有文件夹名字（不含路径） 3.所有文件名字
		# for dirname in  dirnames:                       #输出文件夹信息
			# print("parent is:" + parent)
			# print("dirname is:" + dirname)

		for filename in filenames:                        #输出文件信息
			# print("parent is:" + parent)
			# print("filename is:" + filename)
			# print("the full name of the file is:" + os.path.join(parent,filename)) #输出文件路径信息
			fullFileName = os.path.join(parent,filename)
			gameFileName = targetFolder + fullFileName[len(sourcFolder):len(fullFileName)]

			if os.path.exists(fullFileName) and os.path.exists(gameFileName):
				if not filecmp.cmp(fullFileName.replace('\\','/'), gameFileName.replace('\\','/')):
					copyFile(fullFileName, gameFileName)
			
foldProject = r"D:\work\awf\resource\lua"
foldGame = r""
checkFiles(foldProject, foldGame)

foldProject = r"D:\work\awf\resource\csv_com"
foldGame = r""
checkFiles(foldProject, foldGame)

foldProject = r"D:\work\awf\resource\csv_en"
foldGame = r""
checkFiles(foldProject, foldGame)