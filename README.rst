
Introduction
============

The ``plonetheme.aqueouslight`` package uses the `plone.app.theming`_ to make `Aqueous Light`_ theme by `Six Shooter Media`_ easly available in `Plone 4.1`_

.. image:: https://github.com/prmtl/plonetheme.aqueouslight/raw/master/screenshot.png

Installation
============

Zipfile
-------

If you are an end user, you might enjoy installation via zip file import.

1. Download the zip file: https://github.com/prmtl/plonetheme.aqueouslight/raw/master/aqueouslight.zip
2. Import the theme from the Diazo theme control panel.

Buildout
--------

To install this with buildout:

* Add ``plonetheme.aqueouslight`` to your ``plone.recipe.zope2instance`` section's ``eggs`` parameter::
 
    [instance]
    recipe = plone.recipe.zope2instance
    ...
    eggs =
        ...
        plonetheme.aqueouslight
       
* Re-run buildout, e.g. with::
 
    $ ./bin/buildout

Author & Contact
================

 * Sebastian Kalinowski ``sebastian.kalinowski@stxnext.pl``

.. image:: http://stxnext.pl/open-source/files/stx-next-logo

**STX Next** Sp. z o.o.

http://stxnext.pl

info@stxnext.pl

License
=======

This package is licensed under the GPL Version 2.

.. _`plone.app.theming`: http://pypi.python.org/pypi/plone.app.theming
.. _`Aqueous Light`: http://www.sixshootermedia.com/ostemplates/aqueous_light
.. _`Six Shooter Media`: http://www.sixshootermedia.com/
.. _`Plone 4.1`: http://pypi.python.org/pypi/Plone/4.1rc2
