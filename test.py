import os
import doctest

os.environ['__CONSTANTS__'] = 'a_section'
doctest.testfile('README.rst')
