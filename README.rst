Google Appengine Docs Sphinx Directive
=============================================
This is a plugin for `Sphinx <http://www.sphinx-doc.org/en/stable/>`_ documentation that allows you to create a link to Google's appengine documentation  without needing to write out the URL each time.

All you need is the module name that you want to link to.  The directive takes care of the rest.  It also helps protect your documentation against changes in the Google documentation.  If google changes the location of their docs, all you have to do is update the configuration variable for this directive.  You don't need to find every link you ever created that references Google's appengine docs.

How to Use
-------------
Using the extension is very simple:
    >>> When creating accounts, we use :gae:`google.appengine.ext.ndb.model`.

This would render into:
    When creating accounts, we use `google.appengine.ext.ndb.model <https://cloud.google.com/appengine/docs/python/refdocs/google.appengine.ext.ndb.model>`_ 

Installation
-------------
1) Create a directory in the same directory where your ``conf.py`` file lives to hold the extension (most tutorials say to call it *sphinxext*)
2) Create a *__init__.py* file so that the modules can be imported from the directory 
   >>> touch __init__.py
3) Download the repository and place the folder into the directory you created in step 1
4) Open your ``conf.py`` file and:
   
   a) add the following line in order to add the directory to your path
       >>> sys.path.insert(0,os.path.abspath('sphinxext'))
   
   b) add this extension into the list of existing extensions
        >>> extensions  = ["SphinxGoogleAppengine.google_docs"]

Configuration Variables
-------------------------
This directive only comes with one configuration variable:
    - google_docs_home: base URL for the Google appengine docs

If Google changes the URL to their documentation, you can update this variable in your `conf.py`.
