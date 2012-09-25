import os
import re

loc = "/var/www/virtual/hfid.olin.edu/html/sa2013/s_engr3220-fallera"
cmd = "scp"

cwd = ""

filePattern = ".html|.jpg|.JPG|.png|.css|.js"
folderPattern = "\."

def nav_folder(path = ""):
	if path != cwd:
		cwd = path
		
	directory = os.popen("ls")
	
	for line in directory.readlines():
		dirObj = line[0:-1]
		files = re.findall(filePattern, dirObj)
		if len(files):
			print dirObj, "FILE"
		folders = re.findall(folderPattern, dirObj)
		if not len(folders):
			print dirObj, "FOLDER"
		
		
nav_folder()
