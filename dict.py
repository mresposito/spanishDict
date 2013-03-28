import json, os, optparse
from scraper  import *
from model    import Dictionary

class Controller:

  jsonFile = "/Users/mre/myDict/dict.json"

  def __init__(self):
    self.dct = Dictionary()
    # read cmdline
    self.parseCmdline()

    actions = ['edit', 'delete', 'search', 'add', 'define', 'riddle', 'show']
    map( self.makeAction, actions )
    
    # close the dictionary after using it
    self.dct.close()

  # some dynamic magic
  def makeAction(self, act):
    value = getattr( self.options, act  )
    if  value != "":
      getattr(self, act)( value )

  def define( self, key ):
    scrap ( key )

  def add ( self, key  ):
    scrap ( key )
    value = raw_input("Enter meaning:\n")
    self.dct.add( key, value )

  def search ( self, word ):
    sortedKeys = self.dct.search( word ) 
    map ( self.printWord, sortedKeys )

  def show ( self, word ):
    keys = self.dct.dct.keys()
    for x in enumerate(keys):
      print "%d) %s: %s" %( x[0], x[1] , self.dct.value(x[1]))

  def riddle ( self, empty ):
    key =  self.dct.randomWord()
    print "What is the meaning of?:"
    print self.dct.inputKey( key )
    raw_input()
    print "Dictionary meaning:"
    print self.dct.value( key )
    right = raw_input("Did you get it right?\n")
    if len(right) > 0:
      self.dct.increaseCount( key )

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
    group.add_option("-r" , "--riddle"      , type="string" , default="", help="Do you know this?" , dest="riddle")
    group.add_option("-o" , "--show"        , type="string" , default="", help="Show words "       , dest="show")
    parser.add_option_group( group)
    self.options, self.args = parser.parse_args()

if __name__ == "__main__":
  cl = Controller()
