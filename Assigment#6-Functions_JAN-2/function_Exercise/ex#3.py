#You are building a contact management system. Write a Python script that allows the user to add names to a list.
#After adding three names, print the list and check if a specific name is in the list.
workers = []
for i in range (3):
    w = input("Enter a name to registerd : ")
    workers.append(w)

for i in range(2):
 check = input("Enter a name to check : ")
 if check in workers:
    print(check, "is register")
 else:
    print(check, "not register")
