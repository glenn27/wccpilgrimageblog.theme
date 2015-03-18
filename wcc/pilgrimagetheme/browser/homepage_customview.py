from five import grok
from Products.CMFCore.utils import getToolByName
from Products.ATContentTypes.interface import IATFolder
from Products.CMFCore.interfaces import ISiteRoot

grok.templatedir('templates')

class homepage_customview(grok.View):
    grok.context(ISiteRoot)
    grok.require('zope2.View')

    @property
    def catalog(self):
        return getToolByName(self.context, 'portal_catalog')
    
    def contents(self):
        return self.catalog.unrestrictedSearchResults(portal_type='News Item',
                                                      sort_on='created',
                                                      sort_order='reverse',
                                                      review_state='published')[:4]
    
        
    