import json
import nltk
from urllib.request import urlopen
import utils.prettylogger as pl
from nltk.corpus import *

def word_links():
    # to_analyze = nltk.data.load(, format='auto', cache=true,
    # verbose=False, logic_parser=None, fstruct_reader=None, encoding=None)
    
    # Download dict.json word resource file
    pl.plogger.okblue("Downloading word list...")
    response = urlopen(
        "https://raw.githubusercontent.com/adambom/dictionary/master/dictionary.json")
    raw = response.read().decode('utf8')
    pl.plogger.okgreen("Finished downloading word list")
    
    pl.plogger.okblue("Creating entities...")
    tokens = nltk.word_tokenize(raw)
    text = nltk.Text(tokens)
    tagged = nltk.pos_tag(text)
    entities = nltk.chunk.ne_chunk(tagged)
    pl.plogger.okgreen("Finished creating entities...")
    return entities


def json_dictionary_loader():
    with open('dict.json') as json_data:
        d = json.load(json_data)
        json_data.close()
        return d

if __name__ == "__main__":
    print("This ran correctly %s", word_links())
