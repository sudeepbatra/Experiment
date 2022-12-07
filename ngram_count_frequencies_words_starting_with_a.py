import time

freqs = {}

with open('/home/sb/Data/googlebooks-eng-all-1gram-20120701-a', encoding='utf-8') as f:
    lines = f.readlines()

    start = time.time()
    for line in lines:
        words = line.split("\t")
        word = words[0]
        count = int(words[2])
        if word in freqs:
            freqs[word] += count
        else:
            freqs[word] = count
    end = time.time()
    print(f'{end - start:.4f} seconds')
    print(dict(freqs=freqs))
