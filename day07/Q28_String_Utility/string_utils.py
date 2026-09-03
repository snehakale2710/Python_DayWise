def reverse_string(text):

    return text[::-1]


def count_vowels(text):

    vowels = "aeiouAEIOU"

    count = 0

    for char in text:

        if char in vowels:

            count += 1

    return count


def is_palindrome(text):

    text = text.lower()

    return text == text[::-1]


def count_words(text):

    return len(text.split())