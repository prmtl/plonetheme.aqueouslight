from setuptools import setup, find_packages
import os

version = '1.0'

long_description = (
    open('README.rst').read()
    + '\n' +
    open(os.path.join('docs', 'HISTORY.txt')).read()
    )

setup(name='plonetheme.aqueouslight',
      version=version,
      description="An installable Diazo theme for Plone 4.1",
      long_description=long_description,
      classifiers=[
        "Programming Language :: Python",
        "Framework :: Plone",
        ],
      keywords='python plone diazo theme',
      author='STX Next Sp. z o.o, Sebastian Kalinowski',
      author_email='info@stxnext.pl',
      license='gpl',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['plonetheme'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'plone.app.theming',
      ],
      entry_points="""
      # -*- Entry points: -*-
  	  [z3c.autoinclude.plugin]
  	  target = plone
      """,
      )
