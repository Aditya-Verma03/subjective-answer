def jaccard_similarity(doc1, doc2):
  # List the unique words in a document
  words_doc1 = set(doc1.lower().split())
  words_doc2 = set(doc2.lower().split())

  # Find the intersection of words list of doc1 & doc2
  intersection = words_doc1.intersection(words_doc2)

  # Find the union of words list of doc1 & doc2
  union = words_doc1.union(words_doc2)

  # Calculate Jaccard similarity score
  # using length of intersection set divided by length of union set
  return float(len(intersection)/len(union))

doc1 = "I am girl and loves choco"
doc2 = "I am girl and loves cake"
ans = jaccard_similarity(doc1, doc2)
print(ans)