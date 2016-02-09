#author mohamed fawzy
#suppose you have a list of words and you want to sort them from longest to shortes
def sort_by_length(words):
    t = list()
    for word in words:
       t.append((len(word), word))
    t.sort(reverse=True)
    res = list()
    for length, word in t:
        res.append(word)
    return res

print sort_by_length(['abc','x','yasd','az'])