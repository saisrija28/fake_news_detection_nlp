from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

# Sample training data (minimal but valid)
texts = [
    "Government announces new education policy",
    "Breaking: Celebrity caught in scandal fake news",
    "Scientists discover new planet",
    "Fake cure for cancer spreads online"
]

labels = [0, 1, 0, 1]  # 0 = Real, 1 = Fake

vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(texts)

model = LogisticRegression()
model.fit(X, labels)

def predict_news(text):
    vector = vectorizer.transform([text])
    prediction = model.predict(vector)
    return "Fake" if prediction[0] == 1 else "Real"
