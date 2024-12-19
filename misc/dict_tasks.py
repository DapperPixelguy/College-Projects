f = open('data/hitchhiker.txt', 'r')

f = f.read()

words = f.split(' ')
word_freq_list = [{'word': "",
                   'count': 0
                   }]

for word in words:
    if word not in [word_freq_list[i]['word'] for i in range(len(word_freq_list))]:
        word_freq_list.append({'word': word,
                               'count': 1
                               })
    else:
        for i in range(len(word_freq_list)):
            if word_freq_list[i]['word'] == word:
                word_freq_list[i]['count'] += 1

results = [[word_freq_list[i]['word'], word_freq_list[i]['count']] for i in range(len(word_freq_list))]
#print(results)

counts = [result[1] for result in results]

print(max(counts))

print(results[counts.index(max(counts))])


