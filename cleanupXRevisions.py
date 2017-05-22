# usage :  provide  number of revisions to keep as the first parameter
# usage : bin/cli.sh -username <user> -password <pass> -f cleanupXRevisions.py 4
import re
import sys

numbertokeep = sys.argv[1]

def appOldVersionCleanup(numbertokeep):
	applist = [item for item in repository.search("udm.Application") if item.startswith("Applications/")]
	if len(applist) > 0:
		for appid in applist:
			verlist = sorted([item for item in repository.search("udm.DeploymentPackage",appid)], key=key_func)
			candidate = verlist[0:(0 - int(numbertokeep))]
			for ver in candidate:
				try:
					repository.delete(ver)
					print "Successully deleted version : " + ver
				except:
					print "Couldn't delete version :" + ver + " since it is being used"

def key_func(s):
    return [int(x) if x.isdigit() else x for x in re.findall(r'\D+|\d+', s)]