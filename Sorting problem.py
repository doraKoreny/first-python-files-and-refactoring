import random
N = int(input("how many numbers do you want?"))
numbers = []
for i in range (N):
    numbers.append(int(input("Give your numbers:")))
print(numbers)
iterations = 1
def loop_c():
    temp = numbers[j +1]
    numbers[j+1] = numbers[j]
    numbers[j] = temp

while iterations < N:
    j = 0 
    while j <= N - 2:
        if numbers[j] > numbers[j + 1]:
            loop_c()
        j = j + 1
        
    iterations=iterations+1
print(numbers)
