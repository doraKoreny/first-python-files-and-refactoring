numbers = []
n = 100
div_79 = []
for n in range (100,1000):
    numbers.append(n)
i = len(numbers)
j = 0
while j < i:
    j = j + 1
    if numbers[j-1] % 7 == 0 or numbers[j-1] % 9 == 0:
        div_79.append(numbers[j-1])
m25_div_79 = []
j = 1
while j != -26:
    j = j -1
    m = div_79[j-1]
    m25_div_79.append(m)
for elem in m25_div_79:
    print (elem)

