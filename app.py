from flask import Flask, request, jsonify
from model import predict_news

app = Flask(__name__)

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    news = data.get("news", "")
    result = predict_news(news)
    return jsonify({"prediction": result})

if __name__ == "__main__":
    app.run(debug=True)
