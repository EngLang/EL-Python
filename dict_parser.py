import json
from pprint import pprint


def json_dictionary_loader():
    with open('dict.json') as json_data:
        d = json.load(json_data)
        json_data.close()
        return d

if __name__ == "__main__":
    print "This ran correctly %s" % json_dictionary_loader()
