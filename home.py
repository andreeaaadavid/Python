
import random


def generateArray(n):
    array = []

    for i in range(n):
        array.append(random.randint(0, 1000))

    return array


def searchArray(array, target):
    low = 0
    high = len(array) - 1

    while low <= high:
        if array[low] == array[high]:
            if array[low] == target:
                return low
            return -1

        if target < array[low] or target > array[high]:
            return -1

        pos = low + int(
            (target - array[low]) * (high - low)
            / (array[high] - array[low])
        )

        if array[pos] == target:
            return pos
        elif array[pos] < target:
            low = pos + 1
        else:
            high = pos - 1

    return -1


def SortCocktail(array, step):
    print("\nCocktail Sort")
    print(f"Initial array: {array}")

    left = 0
    right = len(array) - 1
    counter = 0

    while left < right:
        swapped = False

        for i in range(left, right):
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
                swapped = True
                counter += 1

                if step > 0 and counter == step:
                    print(f"Array after {step} swaps: {array}")
                    counter = 0

        if not swapped:
            break

        right -= 1
        swapped = False

        for i in range(right, left, -1):
            if array[i - 1] > array[i]:
                array[i - 1], array[i] = array[i], array[i - 1]
                swapped = True
                counter += 1

                if step > 0 and counter == step:
                    print(f"Array after {step} swaps: {array}")
                    counter = 0

        if not swapped:
            break

        left += 1

    print(f"Sorted array: {array}")
    return array


def SortComb(array, step):
    print("\nComb Sort")
    print(f"Initial array: {array}")

    gap = len(array)
    shrink = 1.3
    swapped = True
    counter = 0

    while gap > 1 or swapped:
        gap = max(1, int(gap / shrink))
        swapped = False

        for i in range(len(array) - gap):
            if array[i] > array[i + gap]:
                array[i], array[i + gap] = array[i + gap], array[i]
                swapped = True

            counter += 1

            if step > 0 and counter == step:
                print(f"Array after {step} comparisons: {array}")
                counter = 0

    print(f"Sorted array: {array}")
    return array


def readInteger(message, minimum=None):
    while True:
        try:
            value = int(input(message))

            if minimum is not None and value < minimum:
                print(f"Please enter a value greater than or equal to {minimum}.")
            else:
                return value

        except ValueError:
            print("Invalid input. Please enter an integer.")


def main():
    is_array = False
    is_sorted = False
    answ = '0'
    array = []

    while answ != '5':

        if answ == '0':
            print('''Welcome to the program

                    0: Display the menu.
                    1: Generate a list of n random natural numbers.
                    2: Search for an item using interpolation search.
                    3: Sort the list using Cocktail Sort.
                    4: Sort the list using Comb Sort.
                    5: Exit the program.

                    The search algorithm requires a sorted list.
                    Before each sorting operation, specify the step interval.
                    Enter 0 to display only the initial and final arrays.
                    ''')

        elif answ == '1':
            n = readInteger("Enter the number of elements: ", 1)
            array = generateArray(n)
            print(f"Generated array: {array}")
            is_array = True
            is_sorted = False

        elif answ == '2':
            if not is_array:
                print("Generate an array before searching.")
            elif not is_sorted:
                print("Sort the array before performing interpolation search.")
            else:
                target = readInteger("Enter the number to search for: ")
                index = searchArray(array, target)

                if index != -1:
                    print(f"Value {target} found at index {index}.")
                else:
                    print(f"Value {target} was not found in the array.")

        elif answ == '3':
            if not is_array:
                print("Generate an array before sorting.")
            else:
                step = readInteger(
                    "Enter the number of swaps between displays: ", 0
                )
                array = SortCocktail(array.copy(), step)
                is_sorted = True

        elif answ == '4':
            if not is_array:
                print("Generate an array before sorting.")
            else:
                step = readInteger(
                    "Enter the number of comparisons between displays: ", 0
                )
                array = SortComb(array.copy(), step)
                is_sorted = True

        elif answ != '5':
            print("Invalid option. Please select a value from 0 to 5.")

        if answ != '5':
            answ = input("Enter your option: ").strip()

    print("Program terminated successfully.")


if __name__ == "__main__":
    main()