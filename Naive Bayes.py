# Import necessary modules 
from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline

# dataset
cat = fetch_20newsgroups().target_names
train = fetch_20newsgroups(subset="train", categories=cat)
test = fetch_20newsgroups(subset="test", categories=cat)

# model training
nbmodel = make_pipeline(TfidfVectorizer(), MultinomialNB())
nbmodel.fit(train.data, train.target)

# model testing
label = nbmodel.predict([test.data[1]])
print(test.data[1])
print(fetch_20newsgroups().target_names[label[0]])