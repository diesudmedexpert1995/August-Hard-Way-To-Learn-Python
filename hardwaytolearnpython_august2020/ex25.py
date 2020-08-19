import ex25_funcs as core

sentence = "ты увидишь лучшее в мире привидение с мотором."

words = core.break_words(sentence)
print(words)

sorted_words = core.sort_words(words)
print(sorted_words)
core.print_first(words)
core.print_last(words)

core.print_first_last(sentence)
core.print_first_last_sorted(sentence)
