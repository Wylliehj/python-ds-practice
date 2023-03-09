def reverse_vowels(s):
    """Reverse vowels in a string.

    Characters which re not vowels do not change position in string, but all
    vowels (y is not a vowel), should reverse their order.

    >>> reverse_vowels("Hello!")
    'Holle!'

    >>> reverse_vowels("Tomatoes")
    'Temotaos'

    >>> reverse_vowels("Reverse Vowels In A String")
    'RivArsI Vewols en e Streng'

    reverse_vowels("aeiou")
    'uoiea'

    reverse_vowels("why try, shy fly?")
    'why try, shy fly?''
    """

    vowels = {'a', 'e', 'i', 'o', 'u'}

    string = list(s)

    start = 0
    end = len(string) - 1

    while start < end:
        if string[start].lower() not in vowels:
            start += 1
        elif string[end].lower() not in vowels:
            end -= 1
        else:
            string[start], string[end] = string[end], string[start]
            start += 1
            end -= 1

    return ''.join(string)