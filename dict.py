import json, os, optparse
from scraper  import *

class Dictionary:

  jsonFile = "/Users/mre/myDict/dict.json"
  dct = {}

  def __init__(self):
    # read json
    with open( self.jsonFile, "r" ) as f:
      self.dct = json.loads(f.read())
  
    # read cmdline
    self.parseCmdline()

    actions = ['edit', 'delete', 'search', 'add', 'define']
    map( self.makeAction, actions )

    with open( self.jsonFile, "w" ) as f:
      f.write(json.dumps( self.dct ))

  def makeAction(self, act):
    value = getattr( self.options, act  )
    if  value != "":
      getattr(self, act)( value )

  def define( self, key ):
    scrap ( key )

  def add ( self, key  ):
    scrap ( key )
    value = raw_input("Enter meaning:\n")
    self.dct[key] = value

    # p = re.compile( word.lower() + "*" )
    # lowKeys = map ( lambda x: x.lower(), self.dct.keys() )
    # matchingKeys = filter ( p.match, lowKeys )

  def search ( self, word ):
    # find all matches
    p = re.compile( word + "*" )
    matchingKeys = filter ( p.match, self.dct.keys() )
    sortedKeys = sorted ( matchingKeys )
    map ( self.printWord, sortedKeys )
    
  def printWord( self, word ):
    print word + ": ",
    print self.dct[word]

  def parseCmdline( self ):

    usage = \
    """
    Usage: %prog <mode> <log_files>
    Examples:
        python ./manage.py stats
    """
    parser = optparse.OptionParser( usage)
    group  = optparse.OptionGroup ( parser, "Options")

    group.add_option("-e" , "--edit"        , type="string" , default="", help="Edit word"         , dest="edit")
    group.add_option("-l" , "--delete"      , type="string" , default="", help="Delete word"       , dest="delete")
    group.add_option("-d" , "--define"      , type="string" , default="", help="Lookup def of word", dest="define")
    group.add_option("-s" , "--search"      , type="string" , default="", help="Search for a word" , dest="search")
    group.add_option("-a" , "--add"         , type="string" , default="", help="Add a word"        , dest="add")
    parser.add_option_group( group)
    self.options, self.args = parser.parse_args()

if __name__ == "__main__":
  dc = Dictionary()
