def tri(num=1, step=1, display=False, max_iter=100):
    if step < max_iter:
        if display:
            print(num)
            print_tri(step)
            print('-' * step*2)
        else:
            print(num)
        tri(num+(step+1), step+1, display=display, max_iter=max_iter)

def print_tri(step):
    for i in range(step):
        i=i+1
        mid = int(step/2)
        print(' '*(mid*2-(i-1)), end='')
        print('# '*i)

tri(display=True, max_iter=10)