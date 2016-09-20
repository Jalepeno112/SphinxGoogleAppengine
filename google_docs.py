"""
Use a directive to create a link to Google's appengine documentation.

Google does not have an obects.inv file that sphinx.intersphinx can use to create links to Google's appengine documentation.  However, their documentation falls a very simple pattern that is easy to manage with a directive.
There is a base URL for all of the documentation, and then each module's name is simply appended to the end of it.

Usage:
    >>> This function creates a :gae:`google.appengine.ext.ndb.model`

This will render into:
    >>> This function creates a `google.appengine.ext.ndb.model <https://cloud.google.com/appengine/docs/python/refdocs/google.appengine.ext.ndb.model>`_

.. note::
    This directive is modified from: https://bitbucket.org/dhellmann/sphinxcontrib-bitbucket/src/36be4abe62e594ad7d6673d62983c23c541d401d/sphinxcontrib/bitbucket.py?at=default&fileviewer=file-view-default
"""
from docutils import nodes, utils
from docutils.parsers.rst.roles import set_classes

def setup(app):    
    """
    Setup the directive.  It tells the directive what to use as the base URL for WePay documentation, and what the name of the directive is.
    """

    app.add_config_value("google_docs_home", "https://cloud.google.com/appengine/docs/python/refdocs/", "html")

    app.add_role("gae", google_appengine_role)

    return {"version": "0.1"}

def make_gae_link(app, rawtext, module, options):
    """
    Create a link to the Google Appengine Docs

    :param app:         the Sphinx application instance that is currently running
    :param module:      the name of the module that we want to create the link for (ex: google.appengine.ext.ndb.model)
    """
    try:
        # get the documentation URL
        base = app.config.google_docs_home
        if not base:
            raise AttributeError
    except AttributeError, err:
        raise ValueError('google_docs_home configuration value is not set (%s)' % str(err))

    # if the URL doesn't include a trailing slash, add one
    slash = '/' if base[-1] != '/' else ''

    # build the external url
    ref = "{0}{1}".format(base, module)

    # we will write the module name in the documentation, but it will be hyperlinked to the corresponding Google page
    insert_text = module

    set_clases(options)

    node = nodes.reference(rawtext, insert_text, refuri=ref, **options)
    return node

def gae_docs_role(name, rawtext, text, lineno, ininer, options={}, content=[]):
    """
    Process the Google appengine docs role
    """

    # get the application
    app = inliner.document.settings.env.app

    # the module we want to link to is contained in `text`
    # we can make the node right here
    node = make_gae_link(app, rawtext, text, options)
    return ([node], [])
