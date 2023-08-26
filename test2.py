a = [4,2,6,7,1,2,9,1,2]

print(lambda x: "No Even" if len([i for i in a if i%2==0])==0 else "Even")
result = (lambda x: "No Even" if len([i for i in a if i % 2 == 0]) == 0 else "Even")(a)
print(result)