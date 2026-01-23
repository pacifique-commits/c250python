import sys
#check errors
if len(sys.argv) <2:
    sys.exit("Too few argument")


#print name tag
for arg in sys.argv[1:]:
    print("Hello, my name is ", arg)
