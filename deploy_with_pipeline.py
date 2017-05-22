import sys
# gives the deployment package by unique workitem
workitem = repository.searchByName(sys.argv[1])
# make sure its unique
if workitem.__len__() != 1:
	print "Not a unique work item number : "+ sys.argv[1]
	sys.exit(1)
# pull up the package to find application name
ci = repository.read(workitem[0])
# pull up application
ciapp = repository.read(ci.application)
# pull up the pipeline
pipeline = repository.read(ciapp.pipeline)
# get the environment list in pipeline
envlist = pipeline.values["pipeline"]
# find the right environment
env = [item for item in envlist if item.lower().find(sys.argv[2].lower()) > -1]
if env.__len__() != 1:
	print "Multiple environments matching : "+ sys.argv[2] + " in pipeline"
	sys.exit(1)
print "Starting Deployment for " + str(ci.id) + " to Environment " +  str(env[0])
deploy(ci.id, env[0])