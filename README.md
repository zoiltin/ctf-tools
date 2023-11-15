# ctf-tools
Some tools may can be used in ctf.

### php异或代码执行生成
利用可用字符集内的字符生成可绕过waf的异或payload。 
字符集characters为不被过滤的字符的十进制ascii值。          
将脚本中str转换成异或payload。