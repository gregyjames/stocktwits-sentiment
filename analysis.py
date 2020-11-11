import stocktwits
import utils
import logging
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
logging.getLogger('tensorflow').disabled = True
import json
import pandas as pd
import numpy as np
import string
import re
from os import path
import keras
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
from keras.models import Sequential
from keras.layers import Embedding, LSTM, Dense, Dropout
from sklearn.model_selection import train_test_split

def process_data(raw_data):
    #preprocessing
    df = pd.DataFrame(columns={"Message","Sentiment"});

    for i in raw_json["messages"]:
        message = i["body"]
        # lowercase, standardize
        message = message.lower()
        # remove symbol names
        message = re.sub(r"\$[a-zA-Z0-9]+\s*", "", message)
        # Remove punctuation and nonalphanumeric characters
        message = message.translate(string.punctuation)
        pattern = re.compile('[\W_]+')
        message = pattern.sub(' ', message)

        try:
            sentiment = i["entities"]["sentiment"]["basic"]
            score = 0
            if sentiment == "Bullish":
                score = 1.0
            else:
                score = -1.0
            df = df.append({'Message': message, 'Sentiment':score}, ignore_index=True)
        except:
            df = df.append({'Message': message, 'Sentiment':np.nan}, ignore_index=True)
    is_NaN = df.isnull()
    row_has_NaN = is_NaN.any(axis=1)
    rows_with_NaN = df[row_has_NaN]
    df = df.dropna()

    return df,rows_with_NaN

def tokenize(df):
    X,y = (df['Message'].values, df['Sentiment'].values)
    tk = Tokenizer(lower = True)
    tk.fit_on_texts(X)
    X_seq = tk.texts_to_sequences(X)
    X_pad = pad_sequences(X_seq, maxlen=100, padding='post')
    return X_pad, y,tk

def train(tk, X_train,y_train, epochs,batchsize):
    if path.exists('./model/saved_model.pb'):
        print("MODEL WAS FOUND!")
        model = keras.models.load_model('./model')
        model.fit(X_train,y_train,batch_size=batchsize, epochs=epochs)
        model.save('./model')
        return model
    else:
        print("NO MODEL WAS FOUND, CREATING NEW MODEL!")
        vocabulary_size = len(tk.word_counts.keys())+1
        max_words = 100
        embedding_size = 32

        model = Sequential()
        model.add(Embedding(vocabulary_size, embedding_size, input_length=max_words))
        model.add(LSTM(200))
        model.add(Dense(1, activation='sigmoid'))
        model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
        model.fit(X_train,y_train,batch_size=batchsize, epochs=epochs, verbose=0)

        model.save('./model')
        return model

# Create a Twit Streamer
twit = stocktwits.Streamer()

# Pass in all parameters to query search
raw_json = twit.get_symbol_msgs(symbol_id="TSLA", since=0, max=0, limit=30, callback=None, filter=None)

# Return raw json as JSON file and process it
utils.return_json_file(raw_json, "get_symbol_msgs.json")
df, nullrows = process_data(raw_json);

#train the model on the new data
X_pad, y, tk = tokenize(df);
X_train, X_test, y_train, y_test = train_test_split(X_pad, y, test_size = 0.25, random_state = 1)
model = train(tk, X_train, y_train,100,10)
scores = model.evaluate(X_test, y_test, verbose=0)
print("Accuracy: ", scores[1])

#Predict sentiments with no value
Check_set = nullrows.Message.values
Check_seq = tk.texts_to_sequences(Check_set)
Check_pad = pad_sequences(Check_seq, maxlen = 100, padding = 'post')

# Predict sentiment
check_predict = model.predict_classes(Check_pad, verbose = 0)

# Prepare data frame
check_df = pd.DataFrame(list(zip(nullrows.Message.values, nullrows.Sentiment.values, check_predict)), columns = ['Message','Sentiment','Pred'])
check_df.Pred = [1 if x == [1] else -1 for x in check_df.Sentiment]
print(check_df)

current_sentiment = (df["Sentiment"].sum() + check_df["Pred"].sum())/(df.size+check_df.size)
print("Avg sentiment: ", current_sentiment)
