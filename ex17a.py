from sys import argv
from os.path import exists

script, from_file, to_file = argv

print "Copying from %s to %s" % (from_file, to_file)

# we could do thse two on one line, how?
# in_file = open(from_file)
# indata = in_file.read()

indata = open(from_file).read()

# print "The input file is %d bytes long" % len(indata)

# print "Does the output file exist? %r" % exists(to_file)
#print "Ready, hit RETURN to continue, or  CTRL-C to abort"
#raw_input()

out_file = open(to_file, 'w').write(indata)

print "Alright, all done."

# below code no longer required as changes made to how
# out_file and in_file are handled
# out_file.close()
# in_file.close()
