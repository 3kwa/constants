"""
constants.Constants

Making dealing with application constants which change with the environment the
application runs in ... straightforward if not easy.

>>> consts = Constants()

Looks for an environement variable named __CONSTANTS__ whose value is used
to find out which section of the constants.ini file should be used.

To find out more about ini files and sections, check the Python standard
library documention on http://docs.python.org/library/configparser.html.

>>> consts['something']
'a_section_value'

Values are cast into integer or float when possible.

>>> consts['all']
1

Values can also be accessed using the . operator.

>>> consts.all
1

The sensible defaults can be overwritten via the constructor...

>>> consts = Constants(variable='AN_ENVIRONMENT_VARIABLE',
...                    filename='constants.cfg') # doctest: +SKIP

... after instantiation but remember to call load().

>>> consts = Constants()
>>> consts.variable = 'AN_ENVIRONMENT_VARIABLE'
>>> consts.filename = 'constants.cfg'
>>> consts.load() # doctest: +SKIP
"""

import os
import ConfigParser


VARIABLE = '__CONSTANTS__'
FILENAME = 'constants.ini'

class Constants(object):

    def __init__(self, variable=VARIABLE, filename=FILENAME):
        """
        variable is the name of the environment variable to read the
        environment / config section from default to __CONSTANTS__
        filename is the config filename
        """
        self.variable = variable
        self.filename = filename
        self.load()

    def load(self):
        """
        load the section self.variable from the config file self.filename
        """
        self.get_environment()
        self.read_config()
        self.load_dict()

    def get_environment(self):
        """
        returns the value of the environement variable self.variable
        """
        self.environment = os.environ[self.variable]

    def read_config(self):
        """
        returns a ConfigParser instance from self.filename
        """
        self.config = ConfigParser.ConfigParser()
        with open(self.filename) as f:
            self.config.readfp(f)

    def load_dict(self):
        """
        load the config items into self.dict
        """
        self.dict = dict (self.config.items(self.environment))


    def __getitem__(self, item):
        """
        access to environment specific constants in a dictionary manner
        casts to int, float or keep as string
        """
        return self.cast(self.dict[item])

    def __getattr__(self, item):
        """
        syntactic sugar, .item rather than ['item']
        """
        return self[item]

    @staticmethod
    def cast(string):
        """
        cast string to int, float or keep as string

        >>> Constants.cast('1')
        1
        >>> Constants.cast('3.14')
        3.14
        >>> Constants.cast('a_string')
        'a_string'
        """
        try:
            return int(string)
        except ValueError:
            pass
        try:
            return float(string)
        except ValueError:
            pass
        return string
