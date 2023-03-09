def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
    

    if to_swap in phrase:
        if to_swap.isupper():
            phrase_temp = phrase.replace(to_swap, '1').replace(to_swap.lower(), '2')
            phrase_flip = phrase_temp.replace('1', to_swap.lower()).replace('2', to_swap.upper())

        else:
            phrase_temp = phrase.replace(to_swap, '1').replace(to_swap.upper(), '2')
            phrase_flip = phrase_temp.replace('1', to_swap.upper()).replace('2', to_swap.lower())
            
    else:
        return None

    return phrase_flip
    
    