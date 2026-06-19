def overhead_count():
    while True:
        try:
            no_of_overheads=int(input("How many overheads do you have? : "))
            break
        except ValueError:
            print("Accept only integers!")
    return no_of_overheads

overhead_count_=overhead_count()
print("Enter your overhead names(Please do not enter space at the very beginning of the cost name)")
def overhead_names():
    name_list=[]
    for i in range(overhead_count_):
        while True:
           names=input(f"Overhead No.{i+1} : ")
           count=0
           if len(names)==0:
               print("Enter the name!")
           else:
               for items in names:
                   try:
                       to_str=int(items)
                   except ValueError:
                       count+=1
               if count==len(names):
                   if names in name_list:
                       print("You have already entered that cost name!")
                   else:
                       name_list.append(names)
                       break
               else:
                   print("How your overhead cost name include integers? Try Again!")
    print("Enter values of costs,")
    return name_list

def values():
    for names in (overhead_names()):
        while True:
            try:
                values=float(input(f"{names} : "))
                break
            except ValueError:
                print("Try Again! (Numbers only)")

values()

def departments():
    while True:
        try:
            no_of_departments=int(input("How many departments do you have? : "))
            break
        except ValueError:
            print("Accept only integers!")
    return no_of_departments
def department_names():
    department_name_list = []
    for i in range(departments()):
        while True:
            names = input(f"Department No.{i + 1} : ")
            count = 0
            if len(names) == 0:
                print("Enter the name!")
            else:
                for items in names:
                    try:
                        to_str = int(items)
                    except ValueError:
                        count += 1
                if count == len(names):
                    if names in department_name_list:
                        print("You have already entered that department name!")
                    else:
                        department_name_list.append(names)
                        break
                else:
                    print("How your department name include integers? Try Again!")
    return department_name_list

print(department_names())