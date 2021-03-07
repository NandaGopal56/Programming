"""
Write a Python program to add 'ing' at the end of a given string (length should be at least 3). If the given string already ends with 'ing' then add 'ly' instead. If the string length of the given string is less than 3, leave it unchanged. Go to the editor
Sample String : 'abc'
Expected Result : 'abcing'
Sample String : 'string'
Expected Result : 'stringly'
"""


def add_string(str):
	if len(str)>=3:
		s=len(str)
		if str[s-3:] != 'ing':
			str=str+'ing'
		elif str[s-3:] == 'ing':
			str=str+'ly'

	print(str)

add_string('abc')
add_string('string')
add_string('gh')
add_string('surpriseing')