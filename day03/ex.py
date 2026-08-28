# Q1. List Creation & Element Insertion

numbers = []

numbers.append(10)
numbers.append(20)
numbers.append(30)

numbers.insert(1, 15)

numbers.extend([40, 50])

print(numbers)


# Q2. Element Removal & Retrieval

items = ["Python", "Java", "C++", "JavaScript", "Ruby"]

items.remove("C++")
last_item = items.pop()

print(items)
print(last_item)


# Q3. Element Frequency & Index Lookup

scores = [85, 92, 75, 92, 88, 92, 70]

count_92 = scores.count(92)
index_88 = scores.index(88)

print("Count of 92:", count_92)
print("Index of 88:", index_88)


# Q4. Sorting & Reversing

marks = [67, 12, 89, 45, 95, 34]

marks.sort()
print("Ascending:", marks)

marks.reverse()
print("Descending:", marks)


# Q5. List Slicing Challenge

arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print(arr[:5])
print(arr[-3:])
print(arr[1:9:2])
print(arr[::-1])


# Q6. Sum and Average of List Elements

numbers = []

for i in range(5):
    num = int(input("Enter an integer: "))
    numbers.append(num)

total = 0

for num in numbers:
    total += num

average = total / len(numbers)

print("Sum:", total)
print("Average:", average)


# Q7. Find Largest and Smallest Number

def find_min_max(numbers):
    maximum = numbers[0]
    minimum = numbers[0]

    for num in numbers:
        if num > maximum:
            maximum = num
        if num < minimum:
            minimum = num

    return maximum, minimum


numbers = [34, 12, 89, 5, 67]

maximum, minimum = find_min_max(numbers)

print("Max =", maximum)
print("Min =", minimum)


# Q8. Remove Duplicates (Preserve Order)

numbers = [1, 3, 2, 3, 4, 1, 5, 2]

unique_numbers = []

for num in numbers:
    if num not in unique_numbers:
        unique_numbers.append(num)

print(unique_numbers)


# Q9. Separate Even and Odd Numbers

numbers = [10, 15, 22, 33, 40, 55, 60]

even_list = []
odd_list = []

for num in numbers:
    if num % 2 == 0:
        even_list.append(num)
    else:
        odd_list.append(num)

print("Even:", even_list)
print("Odd:", odd_list)


# Q10. Second Largest Element

numbers = [10, 45, 20, 99, 80, 99]

largest = float("-inf")
second_largest = float("-inf")

for num in numbers:
    if num > largest:
        second_largest = largest
        largest = num
    elif num > second_largest and num != largest:
        second_largest = num

print("Second Largest:", second_largest)


# Q11. List Comprehension: Square Odds

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]

squares = [num ** 2 for num in nums if num % 2 != 0]

print(squares)


# Q12. Rotate List Elements Left by K Positions

def rotate_left(lst, k):
    k = k % len(lst)
    return lst[k:] + lst[:k]


lst = [1, 2, 3, 4, 5]
k = 2

print(rotate_left(lst, k))


# Q13. Merge Two Sorted Lists

list1 = [1, 3, 5, 7]
list2 = [2, 4, 6, 8, 10]

merged = []

i = 0
j = 0

while i < len(list1) and j < len(list2):
    if list1[i] < list2[j]:
        merged.append(list1[i])
        i += 1
    else:
        merged.append(list2[j])
        j += 1

while i < len(list1):
    merged.append(list1[i])
    i += 1

while j < len(list2):
    merged.append(list2[j])
    j += 1

print("Merged Output:", merged)


# Q14. Flatten a Nested List

def flatten(nested_list):
    result = []

    for item in nested_list:
        if isinstance(item, list):
            result.extend(flatten(item))
        else:
            result.append(item)

    return result


nested_list = [1, [2, 3], [4, [5, 6]], 7]

print(flatten(nested_list))


# Q15. Pair Sum Target

def find_pairs(nums, target):
    pairs = []
    seen = set()

    for num in nums:
        complement = target - num

        if complement in seen:
            pair = (complement, num)
            if pair not in pairs:
                pairs.append(pair)

        seen.add(num)

    return pairs


nums = [2, 4, 3, 5, 7, 8, 9]
target = 7

print("Pairs:", find_pairs(nums, target))


# Q16. Longest Consecutive Subsequence

def longest_consecutive(nums):
    numbers = set(nums)
    longest = 0

    for num in numbers:
        if num - 1 not in numbers:
            current = num
            length = 1

            while current + 1 in numbers:
                current += 1
                length += 1

            if length > longest:
                longest = length

    return longest


numbers = [100, 4, 200, 1, 3, 2]

print("Length:", longest_consecutive(numbers))


# Q17. Group Anagrams

def group_anagrams(words):
    groups = {}

    for word in words:
        key = "".join(sorted(word))

        if key not in groups:
            groups[key] = []

        groups[key].append(word)

    return list(groups.values())


words = ["eat", "tea", "tan", "ate", "nat", "bat"]

print(group_anagrams(words))


# Q18. Predict the Output (Shallow Copy vs Reference)

a = [1, 2, [3, 4]]
b = a.copy()

b[0] = 99
b[2][0] = 77

print("a:", a)
print("b:", b)


# Q19. Debugging Challenge (Modifying List While Iterating)

numbers = [-5, -2, 3, -4, -1, 6, 8]

numbers = [num for num in numbers if num >= 0]

print(numbers)


# Q20. Matrix Transposition using List Comprehension

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

transpose = [[matrix[row][col] for row in range(len(matrix))]
             for col in range(len(matrix[0]))]

print(transpose)