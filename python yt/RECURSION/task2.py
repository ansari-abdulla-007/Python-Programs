def show(x):
    if(x==11):
        return
    print(x)
    show(x+1)
show(1)