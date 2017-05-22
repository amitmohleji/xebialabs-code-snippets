from com.xebialabs.deployit.plugin.api.reflect import Type, DescriptorRegistry

def getDeploymentPackage(appId, appVersion):
	dpId = ("%s/%s" % (appId, appVersion))
	if (repository.exists(dpId)):
		print "[%s] exists and will be modified." % dpId
		return repository.read(dpId)
	print "[%s] does not exist and will be created." % dpId
	dp = factory.configurationItem(dpId, "udm.DeploymentPackage")
	dp = repository.create(dp)
	return dp

def search(ciType, parentId):
	ciIds = proxies.getRepository().query(Type.valueOf(ciType), parentId, None, None, None, 0, -1)
	ids = []
	for ciId in ciIds:
		ids.append(str(ciId.id))
	return ids

def searchDeployeds(containerId):
	return search("udm.Deployed", containerId)
	
def convertToDeployable(deployedId, pkgId):
	deployed = repository.read(deployedId)
	deployedDescriptor = DescriptorRegistry.getDescriptor(deployed.type)
	if (deployedDescriptor.type.instanceOf(Type.valueOf("udm.DeployedArtifact"))):
		print "Cannot convert artifact deployed [%s]. Ignoring " %(deployable.id)
		return None
	
	deployableDescriptor = DescriptorRegistry.getDescriptor(deployedDescriptor.deployableType)
	deployable = factory.configurationItem("%s/%s" % (pkgId, deployed.name), str(deployableDescriptor.type))
	if (repository.exists(deployable.id)):
		print "[%s] already exists. Ignoring " %(deployable.id)
		return None
	
	print "Converting [%s] to type [%s]" % (deployedId, str(deployable.type))
	for pd in deployableDescriptor.propertyDescriptors:
		deployedPd = deployedDescriptor.getPropertyDescriptor(pd.name)
		if (deployedPd):
			try:
				deployable[pdName] = deployed[pdName]
			except:	
				deployable.values[pdName] = deployed[pdName]
	
	return deployable

def reversePkg(appId, appVersion, containerId):
	dp = getDeploymentPackage(appId, appVersion)
	print "Searching resources that a scoped to container [%s]." % containerId
	deployedIds = searchDeployeds(containerId)
	for deployedId in deployedIds:
		deployable = convertToDeployable(deployedId, dp.id)
		if (deployable):
			print "Creating [%s] in repository." % deployable.id
			repository.create(deployable)

#reversePkg("Applications/ReverseApp", "1.0", "Infrastructure/was-70-host/was-70Cell01")	
#reversePkg(params.app.id, params.appVersion, thisCi.id)	