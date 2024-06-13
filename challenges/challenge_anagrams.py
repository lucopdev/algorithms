def bubble_sort_string(texto):
    n = len(texto)
    list_text = list(texto.lower())

    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if list_text[j] > list_text[j + 1]:
                list_text[j], list_text[j + 1] = (
                    list_text[j + 1],
                    list_text[j],
                )

    texto_ordenado = "".join(list_text)
    return texto_ordenado


def count_letters(string):
    letter_count = {}
    for letter in string.lower():
        if letter in letter_count:
            letter_count[letter] += 1
        else:
            letter_count[letter] = 1
    return letter_count


def is_anagram(first_string, second_string):
    first_string_result = bubble_sort_string(first_string)
    second_string_result = bubble_sort_string(second_string)

    if not first_string or not second_string:
        return (
            first_string_result.lower(),
            second_string_result.lower(),
            False,
        )

    letter_count_first = count_letters(first_string)
    letter_count_second = count_letters(second_string)

    isAnagram = letter_count_first == letter_count_second

    return (
        first_string_result.lower(),
        second_string_result.lower(),
        isAnagram,
    )

    raise NotImplementedError
