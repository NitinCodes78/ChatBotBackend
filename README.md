# ChatBot_ShoppingWebsite
Run the app.py and then run the html in standalone-frontend on live server to run on your local device.

ChatBot is using the concept of tokenization and stemming

1. Tokenization is basically breaking down the sentence into seperate words, punctuations etc.
2. Then these words are stemmed i.e. made shorter so that good and gooddd, both are good, punctuations are removed and these seperate words are stored in an array
3. These words take the form of 0 and 1( bag of words) and then they are trained
4. In intent.json we have given tags to certain category of questions. When we ask any question from chatbot, then it takes the word and find the particular tag that question belongs to( closest to which tag i.e. unsupervised learning) and then outputs response corresponding to that tag( any random response from a list of responses)
