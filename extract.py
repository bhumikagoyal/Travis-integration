fp=open("del.txt","r")
fp1=open("commands.txt","w")
command_first="python manage.py test "
settings="--settings=conf.test_settings"
commands=[]
for line in fp: 
	print line
	line=line[0:-1].split("/")
	if len(line) > 1:
		if line[1]=="tests.py":
			command_middle=line[0]+"."+"tests "
			fp1.write(command_first+command_middle+settings+"\n")


		
		
