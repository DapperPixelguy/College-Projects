def tri(num=1, step=1):
    if step < 100:
        print(num)
        tri(num+(step+1), step+1)

tri()