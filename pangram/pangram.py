def is_pangram(sentence):
    alphabets = 'abcdefghijklmnopqrstuvwxyz'
    alphabets_list = list(alphabets)
    for i in alphabets_list:
        if i not in set(sentence.lower()):
            return False
    return True

