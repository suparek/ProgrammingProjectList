import os
import string

yuanyin = {'a','e','i','o','u'}

def backit(astring):
    for i,value in enumerate(astring):
        if value not in yuanyin and value.isalpha():
        	print i
        	return ''.join(astring[0:i] + astring[i+1:len(astring)] + '-' + value + 'ay') 

def main():
	stringa = raw_input("Enter your input: ");
	print "result is", backit(stringa)

		

if __name__ == '__main__':
	main()