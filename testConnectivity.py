import socket
#############################################################
# Return true if we are able to successfully connect to the given host
def ensureHost(infrastuctureType, address):
    
    if (infrastuctureType == 'overthere.CifsHost'):
        return testConnection(address, 445)
        
        #for now, assume that all other types are just unix hosts and
        #	we should be able to connect to port 22
        #In the futture we could try to connect to the websphere port, etc
        #elif (infrastuctureType =='overthere.SshHost'):
        else:
            return testConnection(address, 22)

#############################################################
# Return true if we are able to successfully connect to the given host and port

def testConnection(address, port):

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.connect((address, port))
        s.shutdown(2)
        print("Success connecting to ")
        print(address," on port: ",str(port))
    except socket.error as e:
        print("Cannot connect to ")
        print(address," on port: ",str(port))
        print(e)

    return True


for item in repository.search("overthere.SshHost"):
    address = repository.read(item).address
        ensureHost("overthere.SshHost", address)
for item in repository.search("overthere.CifsHost"):
    address = repository.read(item).address
        ensureHost("overthere.CifsHost", address)