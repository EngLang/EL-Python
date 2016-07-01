import json
import nltk
import urllib2
from pprint import pprint
from nltk.corpus import *


response = urllib2.urlopen(
    "https://raw.githubusercontent.com/adambom/dictionary/master/dictionary.json")
raw = response.read().decode('utf8')


def word_links():
    # to_analyze = nltk.data.load(, format='auto', cache=true,
    # verbose=False, logic_parser=None, fstruct_reader=None, encoding=None)
    tokens = nltk.word_tokenize(raw)
    text = nltk.Text(tokens)
    tagged = nltk.pos_tag(text)
    entities = nltk.chunk.ne_chunk(tagged)
    return entities


def json_dictionary_loader():
    with open('dict.json') as json_data:
        d = json.load(json_data)
        json_data.close()
        return d

if __name__ == "__main__":
    print "This ran correctly %s" % word_links()
