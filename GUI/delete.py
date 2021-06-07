inp = [2,3,6,0.1,0.2,-12,6]
k = 2

inp.sort()


inp_set = set(inp)
inp_list = list(inp_set)
inp_list.sort()

print(inp_list)

print(f"K th min is : {inp_list[k-1]} and max is: {inp_list[-k]} ")