  
from setuptools import setup, find_packages
import codecs
# import os
import pathlib

# The directory containing this file
# here = os.path.abspath(os.path.dirname(__file__))
HERE = pathlib.Path(__file__).parent

# The text of the README file
# with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
#     long_description = "\n" + fh.read()
README = (HERE / "README.md").read_text()

VERSION = '0.0.4'
DESCRIPTION = 'A Package Which allows to access and perform Operations on Different Relational and Non-Relational DataBases '
# LONG_DESCRIPTION = 'A Package that allows to access Cloud as well as Local Databases and allows user to Performs Operationusing prebuilt functions Currently the available Databases are MySql and MongoDB.'

# Setting up
setup(
    name="DBTron",
    version=VERSION,
    author="Suraj Jaiswal",
    author_email="<surajaiswal13@gmail.com>",
    description=DESCRIPTION,
    long_description=README,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=['flask', 'pandas', 'pymongo', 'mysql-connector-python','pymongo[srv]'],
    license="MIT",
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)