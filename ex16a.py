from sys import argv

script, filename = argv

print """I am attempting to read file %s\n
and print it to the console\n
hit the RETURN key to continue""" % filename

raw_input(">")

a = open(filename, 'r')

print a.read()
