# Decaptcha
这是一个基于tesseract API而封装的用于识别图形验证码的python模块。
结合PIL（Python Image Library），可以很方便地识别很多不太复杂的验证码。

#依赖条件
本模块适用于Linux系统，python版本2.7。暂不提供对python 3上的支持。
本模块依赖于tesseract，需要首先安装tesseract(使用默认路径是/usr/local)
本模块需要使用swig，gcc/g++进行代码生成和编译。

#如何安装
在库目录下，直接执行
python setup.py install即可。

#如何使用
请参考 decaptcha_test.py
