import org.codehaus.jettison.json.JSONObject
import os

def exportSecurityToJSON():

	obj = org.codehaus.jettison.json.JSONObject()
	assignments = dict()
	permissions = dict()

	for role in security.getRoleNames():
		assignments[role] = security.getRoleAssignments(role)
		permissions[role] = security.getPermissions(role)
	
	obj.put("assignments", assignments)
	obj.put("permissions", permissions)
	return obj
	
def importSecurityFromJSON(obj):
	assignments = obj.get("assignments")
	for role in assignments.keys():
		for id in range(0,assignments.get(role).length()):
			print "assigning role:" + role + "_" + assignments.get(role).getString(id)
			security.assignRole(role, assignments.get(role).getString(id))
	permissions = obj.get("permissions")
	for role in permissions.keys():
		for ci in permissions.get(role).keys():
			for id in range(0,permissions.get(role).get(ci).length()):
				print "granting permission:" + permissions.get(role).get(ci).getString(id) +"_" +role +"_" + str([str(ci)]) 
				security.grant(permissions.get(role).get(ci).getString(id),role,[str(ci)])
		
def ensureDirectory(directory):
	if not os.path.exists(directory):
		print "Creating Directory :" + directory
		os.makedirs(directory)
		
def writeToFile(fileName, data):
	print "\nWriting to file " + fileName + "..."
	f = open(fileName, "w")
	f.write(data)
	f.close()

def exportSecToFile(directory):
	ensureDirectory(directory)
	obj = exportSecurityToJSON()
	writeToFile(directory + "/security.json", obj.toString())

def importSecFromFile(fileName):
	f = open(fileName,"r")
	json = f.read()
	importSecurityFromJSON(org.codehaus.jettison.json.JSONObject(json))
	
