s=raw_input()
list=map(int,s.split())
min=list[0]
for a in list:
	if a<min:
		min=a
print min
