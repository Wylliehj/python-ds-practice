def vowel_count(phrase):
    """Return frequency map of vowels, case-insensitive.

        >>> vowel_count('rithm school')
        {'i': 1, 'o': 2}
        
        >>> vowel_count('HOW ARE YOU? i am great!') 
        {'o': 2, 'a': 3, 'e': 2, 'u': 1, 'i': 1}
    """

    vowels = ['a', 'e', 'i', 'o', 'u']
    vowels_map = {}

    for char in phrase:
        vowel = char.lower()
        if vowel in vowels:
            if vowel not in vowels_map:
                vowels_map[vowel] = 1
            else:
                vowels_map[vowel] = vowels_map[vowel] + 1

    return vowels_map

