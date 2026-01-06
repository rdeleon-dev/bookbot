def count_words(text):
    return len(text.split())

def count_characters(text):
    characters = {}
    
    for c in text:
        c = c.lower()
        if c in characters:
            characters[c] += 1
        else:
            characters[c] = 1

    return characters