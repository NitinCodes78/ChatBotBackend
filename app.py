from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from chat import get_response  # From chat.py, get this function

# Whenever you chnage intents.json, run python train.py in the terminal (can refer video)

app = Flask(__name__)
CORS(app)

#Step-1: Tokenization of words that is seperating each word, removing punctuations and then putting them in an array
#Step-2: Stemming the words i.e. removing some alphabets like organisations, oraganise will be treated as organ
#Step-3: We get bag of wrds in the form of 0 and 1 whom we train
#step-4: Now when we input any sentence, it will go to neural netwek and predict which tag it is closest to

@app.post("/predict")
def predict():
    text = request.get_json().get("message")
    response = get_response(text)
    message = {"answer": response}
    return jsonify(message)


if __name__ == "__main__":
    app.run(debug=True)

# Whenever you chnage intents.json, run python train.py in the terminal (can refer video)
##########  Do these in terminal
# py -m venv env
# .\env\Scripts\activate
# pip install flask_cors
# pip install Flask torch torchvision nltk
# python
# import nltk
# nltk.download('punkt')
