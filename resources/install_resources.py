# Downloads the following resources:
#   nltk resource files
#   dictionary.json file

from ..utils.prettylogger import plogger

# Install dict.json word resource file
plogger.okblue("Downloading word list")
response = urllib2.urlopen(
    "https://raw.githubusercontent.com/adambom/dictionary/master/dictionary.json")
raw = response.read().decode('utf8')
plogger.okgreen("Finished downloading word list")

# Install the nltk resource files
plogger.okblue("Downloading nltk resources")
nltk.download()
plogger.okgreen("Finished downloading nltk resources")