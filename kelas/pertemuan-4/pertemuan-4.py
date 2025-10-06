ulangi = 10
for i in range (1, 10, 4):
    print(f'perulangan ke {i}')
print('') #biar ada jarak tiap iterasi

simpan = [1, 'Dapupu', 4.00, True]
for i in simpan:
    print(i)

for i, nilai in enumerate(simpan):
    print(nilai)
print('') #biar ada jarak tiap iterasi

for i in range(1, 4):
    for j in range(1, 5):
        print(f'{i} x {j} = {i * j}')
    print('') #biar ada jarak tiap iterasi

for i in range(2, 20, 5) :
    print(i)
print('') #biar ada jarak tiap iterasi

for i in range(1, 4):
    print(f'(i: {i})')
    for j in range(1, 3):
        print(f'j: {j}')
        for k in range(1, 3):
            print(f'i: {i}, j: {j}, (k: {k})')
    print('') #biar ada jarak tiap iterasi

for i in range(1, 4):
    print(f'(i: {i})')
    for j in range(1, 7):
        print(f'j: {j}')
        for k in range(1, 8):
            print(f'i: {i}, j: {j}, (k: {k})')
    print('') #biar ada jarak tiap iterasi

for i in range(1, 5):
    for j in range(1, 7):
        print(f'{i} x {j} = {i * j}')
    print('') #biar ada jarak tiap iterasi

jawab = 'ya'
hitung = 0
while(jawab == 'ya'):
    hitung += 1
    jawab = input("Ulang lagi? ")
print(f"Total perulangan: {hitung}")

hitung = 0
while (True):
    print(hitung)
    hitung += 1
    if hitung == 10:
        break  
        continue
print(f"Total perulangan: {hitung}")

