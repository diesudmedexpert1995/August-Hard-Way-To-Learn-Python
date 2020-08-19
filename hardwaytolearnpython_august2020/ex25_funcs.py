def break_words(sentence):
    """split the intake sentence and return word sequence from sentence"""
    words = sentence.split(' ')
    return words


def sort_words(words):
    """return sorted sequence """
    return sorted(words)


def print_first(words):
    """take first words and print it """
    word = words.pop(0)
    print(word)


def print_last(words):
    """take last words and print it """
    word = words.pop(-1)
    print(word)


def sort_sentence(sentence):
    words = break_words(sentence)
    return sort_words(words)


def print_first_last(sentence):
    """ take last words and print it """
    words = break_words(sentence)
    print_first(words)
    print_last(words)


def print_first_last_sorted(sentence):
    """ take last words and print it """
    words = sort_sentence(sentence)
    print_first(words)
    print_last(words)
