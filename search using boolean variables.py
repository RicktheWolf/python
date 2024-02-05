found = False
print("Before", found)

for thing in [45,14,25,36,49,69]:
    if thing == 14:
        found = True
        print(found,thing)
print("After", found)