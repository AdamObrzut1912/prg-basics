sentence = 'I completely agree with you'
sentecne_split = sentence.split(" ")
print(sentecne_split)
result = list(map(lambda x: len(x), sentence_split))
print(result)