#!/usr/bin/python
__author__ = 'shaycraft'

import cgi

def htmlHeader():
    print 'Content-type: text/html\n\n'
    print '<!DOCTYPE HTML>'
    print '<html>'
    print '<head lang="en">'
    print '<meta charset="utf-8"/>'
    print '</head>'
    print '<body>'

def htmlFooter():
    print '</body>'
    print '</html>'


try:
    htmlHeader()

    print '<h2>blah you suck</h2>'
    htmlFooter()
except:
    cgi.print_exception()