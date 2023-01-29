import sys
lines = sys.stdin.read().split('\n')
# lines = sys.stdin.readlines()
N = int(lines[0])
samples = [[int(i) for i in line.split(' ')] for line in lines[1:N+1]]

confirmed_crystal = set([(1, 0), (2, 0), (3, 0), (2, 1)]) # crystals known for sure
possible_crystal = set([(1, 1), (2, 2), (3, 1)]) # possible crystals. zoom in to check.

def is_l1_crystal( cell ):
    return cell in confirmed_crystal

def is_l2_crystal(cell):
    if (cell[0]//5, cell[1]//5) in confirmed_crystal:
        return True
    elif (cell[0]//5, cell[1]//5) in possible_crystal:
        return is_l1_crystal((cell[0]%5, cell[1]%5))
    return False


def is_crystal(m, x, y):
    if m==1:
        return is_l1_crystal((x, y))
    elif m==2:
        return is_l2_crystal( (x, y) )
    else:
        return is_l2_crystal( (x//(5**(m-2)), y//(5**(m-2))) )
    
for sample in samples:
    print('crystal' if is_crystal(sample[0], sample[1], sample[2]) else 'empty')