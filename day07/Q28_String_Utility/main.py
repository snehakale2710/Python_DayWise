import string_utils


text = input("Enter a string: ")


print(
    "Reverse:",
    string_utils.reverse_string(text)
)


print(
    "Vowels:",
    string_utils.count_vowels(text)
)


print(
    "Palindrome:",
    string_utils.is_palindrome(text)
)


print(
    "Words:",
    string_utils.count_words(text)
)