import os

def backit(astring):
	return astring[::-1]

def main():
	stringa = raw_input("Enter your input: ");
	print "result is", backit(stringa)

if __name__ == '__main__':
	main()