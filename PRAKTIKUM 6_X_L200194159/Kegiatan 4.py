Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 19:29:22) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> Nama = 'Juniar Darma Yati'
>>> NIM = 159
>>> Tinggi = 155
>>> Berat = 45
>>> TahunLahir = 2001
>>> Aku = (TahunLahir, Berat, Tinggi, NIM, Nama)
>>> Data = [TahunLahir, Berat, Tinggi, NIM, Nama]
>>> type(Aku)
<class 'tuple'>
>>> #because the "Aku" data is written is parantheses.
>>> Aku[0]
2001
>>> #because the first object in "Aku" is "TahunLahir", the value of "TahunLahir" is 2001
>>> a = NIM % 4; Aku[a]
159
>>> #because the remaining result of 159 divided by 4 is 3, so the result of Aku[3] is "NIM" is 159
>>> type(Aku[a])
<class 'int'>
>>> #because the value of "Aku[a]" is 159, and 159 is integer data type.
>>> Aku[a:4]
(159,)
>>> #because the object of "Aku[a:4]" data is start from 3, So "[3:4]" is 159
>>> type(Aku[4])
<class 'str'>
>>> #because its begins and ends with quotation marks.
>>> Aku[0] = 'ok'
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    Aku[0] = 'ok'
TypeError: 'tuple' object does not support item assignment
>>> #because the "Aku" data type is a "tuple". And the "tuple" cannot change.
>>> type(Data)
<class 'list'>
>>> #because the "Data" use brackets.
>>> type(Data[4])
<class 'str'>
>>> #because the fourth object in "Data" is "Nama", the value of "Nama" use a quotation marks.
>>> Data[4][5]
'r'
>>> #because the fourth object of "Data" is "Nama", and the fifth object of "Nama" is 'r'.
>>> Data[4][a:6]
'iar'
>>> #because the fourth object of "Data" is "Nama", and the [a:6] from "Nama" is 'iar'.
>>> Data[0] = 'ok' ; Data
['ok', 45, 155, 159, 'Juniar Darma Yati']
>>> #because the "Data[0]" has change by 'ok', and it call all list of "Data".
>>> Data[-a]
155
>>> #because the value of "Data[-a]" is "-3" ,and the answer is 155
>>> range(a)
range(0, 3)
>>> #because range of "a" is (0,3)
