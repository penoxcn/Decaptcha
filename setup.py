from distutils.core import setup, Extension
from os import system

decaptcha_module = Extension('_decaptcha',
                             sources=['decaptcha_wrap.cxx', 'decaptcha.cpp'],
                             include_dirs=['/usr/local/include/tesseract/'],
                             library_dirs=['/usr/local/lib/'],
                             libraries=['tesseract']
                          )

system('swig -python -c++ ./decaptcha.i')
setup(name='decaptcha',
      version='1.0',
      author='ceagle',
      author_email='ceagle@gmail.com',
      description="""Python Decaptcha Module""",
      url='http://decaptcha.org/',
      platforms='Linux',
      ext_modules=[decaptcha_module],
      py_modules=['decaptcha'],
      license='GPL'
      )
