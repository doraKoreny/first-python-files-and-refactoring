def get_threedigits_numbers(lowest, highest):
    numbers = []
    for n in range(lowest, highest):
        numbers.append(n)
    return numbers


def get_max_25(list):
    max_25_divisable_7_9 = list[-27:]
    max_25_divisable_7_9.reverse()
    return max_25_divisable_7_9


def main():
    numbers_divisable_7_9 = []
    numbers = get_threedigits_numbers(500, 5000)
    for i in range(len(numbers)):
        if numbers[i] % 7 == 0 or numbers[i] % 9 == 0:
            numbers_divisable_7_9.append(numbers[i])
    max_25_divisable_7_9 = get_max_25(numbers_divisable_7_9)
    for item in max_25_divisable_7_9:
        print(item)


if __name__ == '__main__':
    main()
