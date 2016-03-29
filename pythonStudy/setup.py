'''''
Created on 2016年3月24日

@author: lyt

setup(
    name='charts',
    version='0.4.6',
    description='Use the highcharts js library in Python',
    url='https://github.com/arnoutaertgeerts/python-highcharts',
    author='Arnout Aertgeerts',
    author_email='arnoutaertgeerts@gmail.com',
    license='MIT',
    keywords='highcharts highstock plotting',
    packages=find_packages(),
    install_requires=[],
    package_data={
        'charts': ['*.html']
    }
)

真正的工作是由导入的distutils实现的，实际上是由setup()函数实现的；

distutils的魔力在于，创建模块分发包时，和安装模块分发包使用的是完全相同的setup.py文件。
一旦模块开发者创建了setup.py脚本，创建分发包所需要做的全部事情可能就是下面的几个步骤：
% python setup.py build
% python setup.py install
% python setup.py sdist
% python setup.py bdist_wininst
'''
from distutils.core import setup, Extension

module1 = Extension('PyMesh',
define_macros = [('PYMESH_EXPORTS', '1')],
libraries = ['MapSubdivision'],
library_dirs = [r'..\Test\Release'],
sources = ['PyMesh.cpp'])

setup(name='PyMesh',
version='1.0.0',
description ='This is a demo package',
ext_modules=[module1],
)