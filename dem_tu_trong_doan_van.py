def count_word(text):
    cnt = {}
    words = text.lower().split()
    for word in words:
        word = word.strip(",.!?;:\"'")
        if word in cnt:
            cnt[word] += 1
        else:
            cnt[word] = 1
    return cnt

text = input()
res = count_word(text)
for word, count in res.items():
    print(f"{word}: {count}")