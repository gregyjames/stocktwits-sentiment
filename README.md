## The newer version of this project can be found [here.](https://github.com/gregyjames/stocksentllm)

# stocktwits-sentiment

Uses a Keras (tensorflow) based rnn and stocktwits message data on securites to predict market sentiment.

# Tutorial
1. Run pip install -r requirements.txt (Python 2), or pip3 install -r requirements.txt (Python 3)
2. Edit the call to get_symbol_msgs in analysis.py to modify the stock of choice.
2. python analysis.py

# Credits
Uses code from https://github.com/khmurakami/pystocktwits

# License
MIT License

Copyright (c) 2020 Greg James

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
