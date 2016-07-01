import json
import nltk
import urllib2
from prettylogger import plogger
from pprint import pprint
from nltk.corpus import *

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
