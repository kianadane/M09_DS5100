from distutils.core import setup

setup(name='Test',
    version='1.0',

    packages=['mainpkg', 'sub'], 
    install_requires=['click']
)