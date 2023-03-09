def capitalize(phrase):
    """Capitalize first letter of first word of phrase.

        >>> capitalize('python')
        'Python'

        >>> capitalize('only first word')
        'Only first word'
    """

    phrase_final = phrase.replace(phrase[0], phrase[0].upper(), 1)

    return phrase_final