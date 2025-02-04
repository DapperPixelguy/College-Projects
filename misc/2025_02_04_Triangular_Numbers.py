def tri(num=1, step=1):
    if step < 100:
        print(num)
        tri(num+(step+1), step+1)

def print_tri(step):
    for i in range(step):
        mid = int(step/2)
        print(' '*(mid*2-i), end='')
        print('# '*i)

print_tri(10)