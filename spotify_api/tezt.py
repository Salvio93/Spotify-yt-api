tmp1 = []
a = {'z': '26', 'y':'25'}

res = list(a.values())[0]
print(res)  
for k, v in a.items():
    y = k + ' - ' + v
    tmp1.append(y)
print(tmp1)

print(type(42.0))

ptn = [1,2,3]
for key in ptn:
    if key != 0:
        print(key)
        