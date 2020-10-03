

#Dictionaries Idiom
#---------------------------------------------
# Grabs values from the list "names" and appends them to the
# Dictionary "count".

count = dict()
names = ["csev", "cwen", "zqian", "cwen"]

for name in names :
    count[name] = count.get(name, 0) + 1

print(count)
