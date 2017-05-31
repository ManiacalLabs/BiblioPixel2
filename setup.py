from setuptools import setup
import sys
from sys import version_info as vi

if vi.major != 2:
    ver = '{}.{}.{}'.format(vi.major, vi.minor, vi.micro)
    error = (
        'INSTALLATION ERROR!\n'
        'BiblioPixel v2 requires Python 2.7 and you are using {}!\n'
        'This is an older BiblioPixel and if that was intentional '
        'you will have to install it under Python 2.7\n'
        'However, we highly recommend using the latest BiblioPixel '
        '(v3+) with Python 3.4+\n'
        '> python3 -m pip install bibliopixel'
        '\n'
    )
    print(error.format(ver))
    sys.exit(1)

import bibliopixel

setup(
    name='BiblioPixel',
    version=bibliopixel.VERSION,
    description='BiblioPixel is a pure python library for manipulating a wide variety of LED strip based displays, both in strip and matrix form.',
    author='Adam Haile',
    author_email='adam@maniacallabs.com',
    url='http://github.com/maniacallabs/bibliopixel/',
    license='MIT',
    packages=['bibliopixel', 'bibliopixel.drivers'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
    ],
)
