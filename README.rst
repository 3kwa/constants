===================
constants.Constants
===================


The problem?
============

Most applications use constants. Many constants take different values based
on the environment the application is executed in.

Think database credentials over development, testing, staging, production or
stock market execution over development, testing, paper, production ...

A solution
==========

Shamelessly inspired by the app_constant gem, constants aims to solve that
problem (and that problem only).

.ini file
---------

Constants use the .ini file format to specify the application constants values
in each environment. DEFAULT values are available in every environment unless
specifically overridden in a section.

    [DEFAULT]
    something = a_default_value
    all =  1

    [a_section]
    something = a_section_value
    just_for_me = 5

To find out more about ini files and sections, check the Python standard
library documention on http://docs.python.org/library/configparser.html.

Environment
-----------

Define the environment the application will run in. The default environment
variable to store that value is __CONSTANTS__, but you can use any variable
name you want.

Most platform have a way to do that, in bash:

    export __CONSTANTS__=a_section

Instantiations
--------------

>>> import constants
>>> consts = constants.Constants()

On instantiation, constants looks for an environement variable named
__CONSTANTS__ whose value is used to find out which section of the
constants.ini file should be used.

Constants' constructor takes two (2) optional parameters. variable let's you
specify the name of the environment variable and filename the absolute path
to the .ini file containing the constants definitions.

>>> consts = Constants(variable='AN_ENVIRONMENT_VARIABLE',
...                    filename='constants.cfg') # doctest: +SKIP

Values
------

To access the values, the instance can be used like a dictionary (getitem).

>>> consts['something']
'a_section_value'

Values are cast into integer or float when possible.

>>> consts['all']
1

Values can also be accessed using the . operator (getattr)

>>> consts.all
1

