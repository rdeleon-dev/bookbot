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

def separate_key_value(dict):
    separated = []

    for i in dict:
        separated.append({"char": i, "num": dict[i]})
    
    return separated

def sort_on(items):
    return items["num"]

def sort_items(items):
    separated = separate_key_value(items)
    separated.sort(reverse = True, key = sort_on)
    return separated