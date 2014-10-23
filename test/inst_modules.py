# coding=utf-8
__author__ = 'F.Marouane'

import subprocess as sp

requirements = ['xlwt', 'psycopg2', 'PyQt4', 'scipy', 'numpy', 'matplotlib', 'xlrd']


def main():
    for pkg in requirements:
        sp.Popen(['pip', 'install', pkg])

if __name__ == '__main__':
    main()