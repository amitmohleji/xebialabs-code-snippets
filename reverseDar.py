import com.xebialabs.deployit.plugin.api.udm.artifact.Artifact
import getopt, sys, time, ast



def reverseDar(id, propertiesFile):
	file = open(propertiesFile, "w")
	cis = [str(item) for item in repository.read(id).deployables]
	for item in cis:
		ci = repository.read(item)
		if isinstance(ci.values._ci, com.xebialabs.deployit.plugin.api.udm.artifact.Artifact):
			for entries in repository.read(ci).values._ci.getSyntheticProperties().entrySet():
				file.write("artifact" + entries.key + "=" + entries.value + "\n")
				file.write("fileLocation=\n")			
		else:
			for entries in repository.read(ci).values._ci.getSyntheticProperties().entrySet():
				file.write("resource" + entries.key + "=" + entries.value + "\n")
				file.write("fileLocation=\n")			
	file.close()	
	




try:
    opts, args = getopt.getopt(sys.argv[1:],'hd:p:',['id=','propertiesFile='])
except getopt.GetoptError:
    print 'cli.sh -host <XLDeployHost> -username <username> -password <password> -f $PWD/reverseDar.y -- -d <id> -p <propertiesFile>'
    sys.exit(2)
for opt, arg in opts:
    if opt == '-h':
        print 'cli.sh -host <XLDeployHost> -username <username> -password <password> -f $PWD/reverseDar.y -- -d <id> -p <propertiesFile>'
        sys.exit(-1)
    elif opt in ('-d', '--id'):
        id = arg
	elif opt in ('-p', '--propertiesFile'):
        propertiesFile = arg        

if id == None:
    print 'ERROR: appName and buildID are mandatory on the command line'
    print 'cli.sh -host <XLDeployHost> -username <username> -password <password> -f $PWD/reverseDar.py -- -d <id> -p <propertiesFile>'
    sys.exit(-1)
