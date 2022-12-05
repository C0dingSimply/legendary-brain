#listmaker
userinfo = input("Enter your name and age")

userlist = []
userlist.append(userinfo)
print(userlist)

f = open("ListStore.py", "a")

# makes or opens a file called Liststore.py

f.write (str(userlist) + '\n')


f.close()