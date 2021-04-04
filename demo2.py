


lst = [1,2,4,5,3,5,5,5,5,5]

dic = {}
for i in range(len(lst)):
	if lst[i] == 5:
		print(i,lst[i])
		dic[i] = lst[i]
print(dic)





