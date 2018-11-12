from collections import defaultdict

with open('data/倚天屠龙记.txt', encoding='gbk', errors='ignore') as f:
    text = f.read()


max_word_len = 5
min_count = 30

word_infos = {}

for granularity in range(1, max_word_len+1):
    for i in range(len(text)):
        word_string = text[i: i+granularity]
        if word_string not in word_infos:
            word_infos[word_string] = defaultdict(int)
        word_infos[word_string]['count'] += 1

filtered_word_infos = {}
for word_string, info in word_infos.items():
    if info['count'] >= min_count and len(word_string) > 1:
        min_aggr = None
        for i in range(1, len(word_string)):
            sub_str_a = word_string[:i]
            sub_str_b = word_string[i:]
            count_a = word_infos[sub_str_a]['count']
            count_b = word_infos[sub_str_b]['count']
            aggregation = info['count'] / (count_a * count_b) * len(text)
            if min_aggr is None:
                min_aggr = aggregation
            elif min_aggr < aggregation:
                min_aggr = aggregation
        if min_aggr > 100:
            print(word_string, info['count'], min_aggr)

