import re

with open("in.txt","r") as f:
	content = f.readlines()

content = [x.strip() for x in content] 
	
new = sorted(content, key=lambda x: int(re.search(r'\d+$',x).group()))

with open("out.txt","w") as f:
	for i in new:
		f.write(i + "\n")

with open("out.txt","r") as f:
	print(f.read())
