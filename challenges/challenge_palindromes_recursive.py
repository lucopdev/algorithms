def is_palindrome_recursive(word, low_index, high_index):
    if not word:
        return False

    if len(word) <= 1:
        return True

    if low_index + 1 == high_index or low_index + 1 == high_index - 1:
        if word[low_index] == word[high_index]:
            return True
        else:
            return False
    else:
        return is_palindrome_recursive(word, low_index + 1, high_index - 1)

    raise NotImplementedError
