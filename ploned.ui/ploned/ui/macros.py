"""
$Id: macros.py 6262 2010-03-19 08:29:49Z mario.ruggier $
"""

from zope.publisher.browser import BrowserView
from zope.app.basicskin.standardmacros import StandardMacros as BaseMacros
from zope.app.pagetemplate import ViewPageTemplateFile

class PlonedLayout( BrowserView ):

    template = ViewPageTemplateFile('templates/ploned-template.pt')

    def __getitem__(self, key):
        return self.template.macros[key]

class StandardMacros( BaseMacros ):

    macro_pages = ['ploned-layout', 'alchemist-form']

