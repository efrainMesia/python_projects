words = ["adopt", "bake", "beam", "cook", "time", "grill", "waved", "hire"]
past_tense=[]
for word in words:
    if 'ed' != word[-2:]:
        if 'e' == word[-1:]:
            word = word +'d'
        else:
            word = word+'ed'
    past_tense.append(word)
print(past_tense)