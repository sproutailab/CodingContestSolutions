import sys
freq = dict()
max_freq = 0
second_freq = 0
max_list = set()
second_list = set()

N = int(sys.stdin.readline())
for i in range(N):
    num = int(sys.stdin.readline())
    freq[num] = freq.get(num, 0) + 1
    if freq[num] > max_freq:
        if len(max_list)>1:
            second_freq = max_freq
            second_list = max_list
            second_list.discard(num) # remove current num from second list
        max_freq = freq[num]
        max_list = set([num])
    elif freq[num] == max_freq:
        max_list.add(num)
    elif freq[num] > second_freq:
        second_freq = freq[num]
        second_list = set([num])
    elif freq[num] == second_freq:
        second_list.add(num)
            


if len(max_list)>1:
    max_list = sorted(max_list, reverse=True)
    result = max_list[0] - max_list[1]
else:
    max_freq_value = max_list.pop()
    result = max([abs(s - max_freq_value) for s in second_list])
print(result)