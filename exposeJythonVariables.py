import inspect

def dig(i,obj):
	if not inspect.ismodule(obj) and not inspect.isclass(obj) and not inspect.isroutine(obj):
		if isinstance(obj, str) or isinstance(obj, unicode):
			print "STRING OBJECT : " + i + " || VALUE : " + str(obj)
		else:
			print "COMPLEX OBJECT : " + i + " || TYPE : " + str(type(obj))	
		if dir(obj).__contains__("_delegate"):
			try:
				for item in inspect.getmembers(obj._delegate):
					if not inspect.isroutine(item[1]) and not inspect.isclass(item[1]) and (str(item[0]) not in ["__doc__"]):
						print "Property : "  + i + "." + item[0] + " || VALUE : " + str(item[1])
					if inspect.ismethod(item[1]) and (str(item[0]) not in ["hashCode","getClass","notify","notifyAll","equals","toString","wait","__init__","compareTo"]):
						print "Method : "  + i + "." + item[0] + "(...)"
			except :
				print "ERROR : Can't review properties on object " + i + " due to exception" 			
for i in globals():
	dig(i, globals()[i])