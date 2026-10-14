N = int(input())
s = 0
c = 0
for i in range(1, N + 1):
    if i % 3 == 0:
        s += i
        c += 1

    if i % 5 == 0:
        s += i
        c += 1

print(f'Сума = {s}')
print(f'Кількість = {c}')
if c > 0:
    av = s / c
    print(f'Середне = {av}')
else:
    print("Немае")




N = int(input())
if N < 0:
    tpn = -N
else:
    tpn = N
c = 0
s = 0
max_digit = 0
min_digit = 9
if tpn == 0:
    c =1
    s = 0
    max_digit = 0
    min_digit = 0
else:
    while tpn > 0:
        digit = tpn % 10
        c += 1
        s += digit
        if max_digit < digit:
            max_digit = digit
        if min_digit > digit:
            min_digit = digit
        tpn //= 10
print(c)
print(s)
print(max_digit)
print(min_digit)



width = int(input())
height = int(input())
border = input()
fill = input()
if width <3 or height < 3:
    print("error")
else:
    for i in range(height):
        r = ""
        for j in range(width):
            if i == 0 or i == height -1 or j == width - 1 or j ==0:
                print(border, end=" ")
            else:
                print(fill, end=" ")
        print(r)

