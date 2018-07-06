def sorting_numbers(list, user_input):
    for i in range(user_input):
        j = 0
        for j in range(user_input - 2):
            if list[j] > list[j + 1]:
                temp = list[j + 1]
                list[j+1] = list[j]
                list[j] = temp
    return list


def main():
    N = int(input("how many numbers do you want?"))
    numbers = []
    for i in range(N):
        numbers.append(int(input("Give your numbers:")))
    print(sorting_numbers(numbers, N))


if __name__ == "__main__":
    main()
