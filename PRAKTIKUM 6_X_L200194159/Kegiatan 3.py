Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 19:29:22) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> Nama = 'Juniar Darma Yati'
>>> NIM = 'L200194159'
>>> X = '1' + NIM[7:]
>>> a = int(X)
>>> b = len(Nama)
>>> type(a)
<class 'int'>
>>> #because the "a" data had changed to integer data type.
>>> type(b)
<class 'int'>
>>> #because the "Nama" data has a "len" instruction.
>>> a/b
68.17647058823529
>>> #because the result of 1159 divided by 17 is 68.17647058823529
>>> a//b
68
>>> #because the meaning of "//" is divission with rounding down.
>>> 10*(a-999)
1600
>>> #because the value of "a" minus 999 is 160. After that 160 will multiplied by 10 and the answer is 1600.
>>> b**2
289
>>> #because the value of "b" multiplied by "b". So 17 multiplied by 17 and the answer is 289.
>>> a%b
3
>>> #because 3 is left over from 1159 divided by 17.
>>> c = 12.5
>>> type(c)
<class 'float'>
>>> #because the "c" data is desimal and desimal is float type.
>>> a/c
92.72
>>> #because the result of 1159 divided by 12.5 is 92.72
>>> a//c
92.0
>>> #because the meaning of "//" is divission with rounding down.
>>> a%c
9.0
>>> #because 2 is left over from 1159 divided by 12.5
>>> c>b
False
>>> #because the value of "b" is 17 and "c" is 12.5. So 17 greater than 12.5 and the answer is false.
>>> type(c>b)
<class 'bool'>
>>> #because use the answer beetwen True or False. This is called "boolean".
>>> a>b and b>c
True
>>> #because the value of "a" is 1159 "b" is 17 and "c" is 12.5. So 1159 greater than 17 and 17 greater than 12.5 and the answer is True.
>>> a>1100 or b<10
True
>>> #because the answer of a>1100 is true and the answer of b<10 false. Because true or false the correct answer is True. it use logic of Or.
