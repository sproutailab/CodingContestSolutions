num = input()

dict_r = {'I':1,
          'V':5, 
          'X':10,
          'L':50,
          'C':100,
          'D':500,
          'M':1000}

result = 0
next_r = 0
next_add = 0
for i in range(len(num)-1, 0, -2):
    curr_r = dict_r[num[i]]
    if curr_r < next_r:
        result -= curr_r * int(num[i-1])
    else:
        result += curr_r * int(num[i-1])
    next_r = curr_r
print(result)
