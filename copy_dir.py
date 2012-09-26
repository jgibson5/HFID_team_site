import os
import re
import time
import paramiko

loc = "/var/www/virtual/hfid.olin.edu/html/sa2013/s_engr3220-fallera"
cmd = "scp"
server = "jgibson@linwebprod.olin.edu:"

filePattern = ".html|.jpg|.JPG|.png|.css|.js"
folderPattern = "\."
myDirPattern = "/home/jgibson/git/HFID_team_site"

def nav_folder(path = ""):
	cwd = os.popen("pwd")
	cwd = cwd.readline()[0:-1]
	if path != "":
		os.chdir(cwd+"/"+path)
		cwd = os.popen("pwd")
		cwd = cwd.readline()[0:-1]
	print cwd
		
	directory = os.popen("ls")
	
	for line in directory.readlines():
		dirObj = line[0:-1]
		files = re.findall(filePattern, dirObj)
		if len(files):
			print dirObj, "FILE"
		folders = re.findall(folderPattern, dirObj)
		if not len(folders):
			print dirObj, "FOLDER"
			nav_folder(dirObj)
	
	r = cwd.split("/")[0:-1]
	r = "/".join(r)
	os.chdir(r)
		
def make_copy(fileName = "", path = ""):
	c = cmd + " " + fileName + " " + server + loc + "/test" + fileName
	print c
	t = os.popen(c)
	for line in t.readlines():
		print line
	os.system(c)
	
	
make_copy("index.html")
	
	
#nav_folder()


