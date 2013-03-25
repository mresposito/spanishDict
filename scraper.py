#!/usr/bin/env python
# coding: utf-8

###      @file:  scraper.py
###
###    @author:  Michele Esposito
###    Company:  myself!

import sys, os, string, re
import urllib2, unicodedata
from bs4 import BeautifulSoup, SoupStrainer

# class EngScraper: 
# 
#   SpanishUrl = 'http://www.spanishdict.com/translate/'

SpanishUrl = "http://www.spanishdict.com/translate/"

def scrap( word ):

  pageUrl = SpanishUrl + word
  page   = loadHTMLUrl ( pageUrl )

  print simpleGet ( page.findAll( 'h2', {'class': 'quick_def'} ) ) + "." 
  print "Type: " + simpleGet ( page.findAll( 'span', {'class': 'quick_pos'} ) )

class ItalianScraper:

  ScrapeUrl = 'http://www.grandidizionari.it/%s/parola/G/geloso.aspx?query='
  ItaSpa    = 'Dizionario_Italiano-Spagnolo'
  SpaIta    = 'Dizionario_Spagnolo-Italiano'

  def scrap( self, word, SpaIta = True ):

    if SpaIta:
      ScrapeUrl = self.ScrapeUrl % self.SpaIta
    else:
      ScrapeUrl = self.ScrapeUrl % self.ItaSpa

    pageUrl = ScrapeUrl + word.lower()
    page   = loadHTMLUrl ( pageUrl )

    simpleGet( page.findAll( 'div', {'style': 'padding:0 10px;'} ) )

def simpleGet ( definition ):
  for df in definition: 
    return stripHtml( str(df) )
  else:
    return ""

def stripHtml(data):
  p = re.compile(r'<.*?>')
  return p.sub('', data)

### Functions to read pages ###
def loadHTMLUrl ( url ): 
  print url
  page = urllib2.urlopen(url)
  page = page.read()
  return BeautifulSoup( page, "html5lib" )

if __name__=='__main__':
  # words = ["siquiera",  "Cuajaba",  "Huía"]
  words = ["siquiera" ]
  it = ItalianScraper (  )
  map ( it.scrap, words )
