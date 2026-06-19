def space():
    while True:
        try:
            spaces=int(input("How many spaces do you have? : "))
        except ValueError:
            print("Enter only numbers!")
        else:
            break
    return spaces

def value():
    while True:
        values=input("What are the values you have? : ").split(',')
        if values==[""]:
            print("values can not be NIL!")
        else:break
    check=[]
    duplicate=[]
    for item in values:
        if item in duplicate:continue
        elif item in check:
            duplicate.append(item)
        else:
            check.append(item)
    return check

def process():
    sp=space()
    val=value()

    lists=[]
    for i in range (sp):
        fake=[]
        lists.append(fake)

    total= len(val) ** sp
    move = total// len(val)

    for i in range(sp):
        index = 0
        for j in range(len(val)**sp):
            if j%move==0:
                index=(j//move)%len(val)
            lists[i].append(val[index])
        move//=len(val)


    results=[]
    for i in range(len(val)**sp):
        output = []
        for j in range(len(lists)):
            output.append(lists[j][i])
        add=""
        for item in output:
            add+=item
        results.append(add)

    for i in range(len(val)**sp):
        print(f"{i+1}) {results[i]}")




process()