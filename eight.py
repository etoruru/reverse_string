def reverse_sting(string):
    reversed_string = ''
    index = len(string) - 1

    while index >= 0:
        current_char = string[index]
        reversed_string = reversed_string + string[index]
        index -= 1

    return reversed_string

