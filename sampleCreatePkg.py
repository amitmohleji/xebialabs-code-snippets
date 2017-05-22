def mapDeployedToDeployable(appId,deployed,deployableType):
	descriptor = DescriptorRegistry.getDescriptor(deployableType)
	deployable = factory.configurationItem("%s/%s" %(appId,deployed.name),str(deployableType))
	for pd in descriptor.propertyDescriptors:
		pdName = str(pd.name)
		if pd.transient or str(pd.kind) == "MAP_STRING_STRING" or str(pd.kind) == "SET_OF_STRING"  or str(pd.kind) == "LIST_OF_STRING" or str(pd.kind) == "SET_OF_CI" or str(pd.kind) == "LIST_OF_CI":
			continue
		if hasattr(deployed,pdName) and hasattr(deployable,pdName):
			#print("Handling ",str(deployableType),pdName)
			deployable[pdName] = str(deployed[pdName])
	return deployable

def findDeployableType(deployedType):
	descriptor = DescriptorRegistry.getDescriptor(deployedType)
	return descriptor.getDeployableType()

def createOrUpdate(deployable):
	if repository.exists(deployable.id):
		repository.update(deployable)
	else:
		repository.create(deployable)

def createDeployable(pkgId, deployedId):
	print ("Converting [%s]" % deployedId)
	deployed = repository.read(deployedId)
	deployableType = findDeployableType(deployed.type)
	print ("From type [%s] to [%s]" % (deployed.type,deployableType))
	deployable = mapDeployedToDeployable(pkgId, deployed,deployableType)
	return deployable
	
def createSamplePkg(pkgId,parent):
	deployeds = repository.search(None,parent)
	for deployedId in deployeds:
		deployable = createDeployable(pkgId, deployedId)
		print ("Saving [%s]" % deployable.id)
		createOrUpdate(deployable)
		print ("Saved")

pkgId = "Applications/sample/1.0"


		
	
