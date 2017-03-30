fp=open("del.txt","r")
fp1=open("commands.txt","w")
command_first="pytest "
settings="--settings=conf.test_settings"
commands=[]
for line in fp:
	if line[-1]=="\n":
		line=line[0:-1] 
	line=line.split("/")
	print line
	if len(line) > 1:
		if line[1]=="tests.py":
			command_middle=line[0]+"/"+"tests.py"
			fp1.write(command_first+command_middle+"\n")


		
		
