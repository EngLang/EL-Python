# Downloads the following resources:
#   nltk resource files
#   dictionary.json file

import nltk
import utils.prettylogger as pl

# Install the nltk resource files
pl.plogger.okblue("Downloading nltk resources")
nltk.download()
pl.plogger.okgreen("Finished downloading nltk resources")