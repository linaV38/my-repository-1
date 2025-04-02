greeting = "Hello, world!"

greeting_index = []
count = 0
for i in range(len(greeting)):
    if greeting[i] == "o":
        count +=1
        greeting_index.append(i)
print(count)
print(greeting_index)




