# EngLang [![Build Status](https://travis-ci.org/EngLang/EL-Python.svg?branch=structuring)](https://travis-ci.org/EngLang/EL-Python)
![EngLang](http://s31.postimg.org/d7mshul0r/master.png "EngLang")

##Introduction
EngLang is a syntax-lenient programming language that essentially takes human text and parses it into executable code. For example, the sentence:
```EngLang
You should create a text file in /users/me/docs with the contents 'I love chicken'
```
Will create a file in the directory `/users/me/docs` with the filename `chicken.txt` and the contents `I love chicken.`

However, it is possible to create even more complex sentences that do some spectcular things.
```EngLang
Let's count to five, saying each number aloud as we go, and send the result to http://mywebsite.com/api/count as 'mycount'
```
This statement is equivalent to creating a variable, running through a loop 5 times that increments the number and prints it to the console, and then makes a `POST` call to `http://mywebsite.com/api/count` with JSON content `{mycount: 5}`.

Fancy right? Well using our goal of super-abstraction, you can even write code that is very minimal but outputs complex results, such as the following:
```EngLang
Take the population of the US and create an ascii bar graph showing the change over time.
```
Using resources such as the Wolfram|Alpha API and Wikipedia, this method with gather the population information and show the desired graph in the console.

Impressed yet? Let's get started.

## Open Source Contributions

Want to contribute to the project? Feel free to check out our wiki, issues, and list of tasks on Trello. Fix a bug or implement a feature and submit a merge request!

Trello: [https://trello.com/b/YNJBR43k/englang](https://trello.com/b/YNJBR43k/englang)

Wiki: [https://github.com/vontell/EngLang/wiki](https://github.com/vontell/EngLang/wiki)

Issues: [https://github.com/vontell/EngLang/issues](https://github.com/vontell/EngLang/issues)

## Key Terminology
There are some key terms used within the documentation of EngLang that is considered unconventional. Therefore, below is a list of terminology that may be helpful:


* Sentence - 
* Verb - 
* Subject -
* Parameter - 
* Chapter -
* Paragraph - 
* Alias - 

## Running the code
There are a few dependencies that must be installed before using the library. Run the commands below to make sure that everything is installed correctly:
1. Install packages: `sudo pip3 install -r requirements.txt`
2. Install nltk resources: `python3 setup.py` -> `d` to download -> `all` to download all packages

## License
The MIT License (MIT)
Copyright (c) 2016 EngLang

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.