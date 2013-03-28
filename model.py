import json, os, optparse
import unicodedata
from random   import choice
from scraper  import *

KEY   = "key"
VALUE = "value"
COUNT = "count"

class Dictionary:

  jsonFile = "/Users/mre/myDict/dict.json"
  dct = {}

  def __init__(self):
    # read json
    with open( self.jsonFile, "r" ) as f:
      self.dct = json.loads(f.read())
  
  def close ( self ):
    with open( self.jsonFile, "w" ) as f:
      f.write(json.dumps( self.dct ))

  def add ( self, key, value  ):
    searchKey = self.normalize( key )
    self.dct[searchKey] = {KEY: key, VALUE: value, COUNT: 0 }

    # p = re.compile( word.lower() + "*" )
    # lowKeys = map ( lambda x: x.lower(), self.dct.keys() )
    # matchingKeys = filter ( p.match, lowKeys )

  def search ( self, word ):
    # find all matches
    p = re.compile( word + "*" )
    matchingKeys = filter ( p.match, self.dct.keys() )
    sortedKeys = sorted ( matchingKeys )
    return sortedKeys 
    
  def normalize ( self, word ):
    title = word.lower()
    return title

  def inputKey ( self, key ):
    return self.dct[key][KEY]

  def value ( self, key ):
    return self.dct[key][VALUE]

  def increaseCount ( self, key ):
    self.dct[key][COUNT] += 1

  def randomWord ( self ):
    keys = self.dct.keys()
    return choice( keys )

if __name__ == "__main__":
  dc = Dictionary()
