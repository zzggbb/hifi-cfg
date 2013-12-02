with open("cvar_list_07-21-13_03-16.log","r") as r:
	with open("cvar_list_without_spaces.txt","w") as w:
		content = r.readlines()
		for i in content:
			w.write(i.split(":")[0] + '\n')