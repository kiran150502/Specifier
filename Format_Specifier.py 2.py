k=3; a=5.5; m='kalyan'
print(type(k),type(a),type(m))
print(k)
print('%d' %k)
print('%i' %k)
print('%f' %a)
print('%.1f' %a)
print('%.6f' %a)

k=1
print(float(k))
print(str(k))
print('%f' %k)
print('%s' %k)

k=6.3
print(int(k))
print(float(k))

k='kalyan'
print(type(k))
a=int(k)
print(a,type(a))
f=float(k)
print(f,type(f))

k='3.9'
print(type(k))
print(int(k)) #valueerror
a=float(k)
print(a,type(a))
i=int(a)
print(i,type(i))
