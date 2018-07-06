def get_numbers_div_7_9(list):
    div_79 = []
    j = 0
    while j < len(list):
        if list[j] % 7 == 0 or list[j] % 9 == 0:
            div_79.append(list[j])
        j = j + 1
    return div_79


def main():
    numbers = []
    for n in range(100, 1000):
        numbers.append(n)
    get_numbers_div_7_9(numbers)
    for items in (get_numbers_div_7_9(numbers)[-27:])[::-1]:
        print(items)


if __name__ == "__main__":
    main()
