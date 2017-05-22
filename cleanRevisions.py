# usage :  provide  Application Package ID as "Applications/MyApp/1.0.39"  as the first parameter
# usage : bin/cli.sh -expose-proxies -username <user> -password <pass> -f cleanRevisions.py "Applications/MyApp/1.0.39"
import sys
yourDP = sys.argv[1]
for revision in proxies.getHistoryService().readRevisions(yourDP):
	if revision.getRevisionName() == "current" :
		yourRevTime = revision.getCreatedAt().getTimeInMillis()
print "Deleting all revisions before this Revision : " + yourDP 
		 
packages = repository.search("udm.DeploymentPackage",yourDP.rpartition("/")[0])
for package in packages:
	for revision in proxies.getHistoryService().readRevisions(package):
		if revision.getRevisionName() == "current" :
			revTime = revision.getCreatedAt().getTimeInMillis()
			if  revTime < yourRevTime:
				print "This package : " + package + " is being deleted"
				repository.delete(package)

