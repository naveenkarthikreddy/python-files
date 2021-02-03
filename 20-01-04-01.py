# File1.py

import File1
print("File1 __name__ = %s" % __name__)

if __name__ == "__main__":
    print("File1 is being run directly")
else:
    print("File1 is being imported")

# if we want to execute any method only if we are executing the file
# where that function contains if we are importing any file the
# funnction {if __name__ == "__main__":  }  present in that imported
# file will not be executed only this function {if __name__ == "__main__":  }
# will be executed if and only if it is in that own file


print("File2 __name__ = %s" % __name__)

if __name__ == "__main__":
    print("File2 is being run directly")
else:
    print("File2 is being imported")
