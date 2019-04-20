#!/usr/bin/python
# created by: yoddax
# greetz: gux

e = input('opt: ')
s = input('str: ')

if e == 'enc':
	for c in s:
		print(str(bin(ord(c))).replace('b', ''), end=' ')
elif e == 'dec':
	for i in s.split():
		if i == '0100000': # 0100000 == space char
			print('', end=' ')
		else:
			print(chr(int(i[0]+'b'+i[1:], 0)), end='')