This repository lists various scripts that are useful while working with XLD

exposeDeploymentVariables.ftl
=============================
The code snippet in this script can be copied into a script that is used with XLD artifacts as a createScript. It can be used with generic plugin and with XL-rules and any other plugins that have execution scripts specified such that they show up under plan analyzer can be opened.

This script would expose all the variables and the properties with them. It works recursively so you can specify the what level of depth you want to go to.
eg.

base depth is 0. so with depth=1, it will show properties like deployed.container.os.

It prints the value of literal properties, also lists the methods available with objects is captureMethod=true. 
For generic plugin, with captureMethod=false, output shows up like this.

VARIABLE LISTING TILL DEPTH: 0
=====================================
		Complex Object: deployed
		PROPERTY: ${deployed.createScript}  ||  VALUE: script/osscript.sh.ftl
		PROPERTY: ${deployed.remoteWorkingDirectoryPath}  ||  VALUE: (UNDEFINED/UNRESOLVED) 
		PROPERTY: ${deployed.inspectScript}  ||  VALUE: (UNDEFINED/UNRESOLVED) 
		PROPERTY: ${deployed.planOperation}  ||  VALUE: CREATE
		PROPERTY: ${deployed.modifyScript}  ||  VALUE: (UNDEFINED/UNRESOLVED) 
		PROPERTY: ${deployed.noopOrder}  ||  VALUE: 50
		PROPERTY: ${deployed.modifyOrder}  ||  VALUE: 50
		PROPERTY: ${deployed.noopScript}  ||  VALUE: (UNDEFINED/UNRESOLVED) 
		PROPERTY: ${deployed.$ciAttributes}  ||  VALUE: com.xebialabs.deployit.plugin.api.udm.CiAttributes@42472788
		PROPERTY: ${deployed.noopVerb}  ||  VALUE: Modify
		PROPERTY: ${deployed.destroyVerb}  ||  VALUE: Destroy
		PROPERTY: ${deployed.retainRemoteWorkingDirectory}  ||  VALUE: false
		PROPERTY: ${deployed.destroyScript}  ||  VALUE: (UNDEFINED/UNRESOLVED) 
		PROPERTY: ${deployed.createVerb}  ||  VALUE: Create
		PROPERTY: ${deployed.type}  ||  VALUE: test.scripttype1
		PROPERTY: ${deployed.restartRequired}  ||  VALUE: false
		PROPERTY: ${deployed.class}  ||  VALUE: class com.xebialabs.deployit.plugin.generic.deployed.ExecutedScript
		PROPERTY: ${deployed.createOrder}  ||  VALUE: 50
		PROPERTY: ${deployed.modifyVerb}  ||  VALUE: Modify
		PROPERTY: ${deployed.id}  ||  VALUE: Infrastructure/local/newtype
		PROPERTY: ${deployed.name}  ||  VALUE: newtype
		PROPERTY: ${deployed.destroyOrder}  ||  VALUE: 40
		PROPERTY: ${deployed.$token}  ||  VALUE: (UNDEFINED/UNRESOLVED) 
		PROPERTY: ${deployed.restartRequiredForNoop}  ||  VALUE: false
		Complex Object: step
		PROPERTY: ${step.uploadedArtifactPath}  ||  VALUE: (UNDEFINED/UNRESOLVED) 
		PROPERTY: ${step.hostFileSeparator}  ||  VALUE: /
		PROPERTY: ${step.localConnection}  ||  VALUE: local:
		PROPERTY: ${step.retainRemoteWorkingDirOnCompletion}  ||  VALUE: false
		PROPERTY: ${step.hostLineSeparator}  ||  VALUE: 

		PROPERTY: ${step.scriptTemplatePath}  ||  VALUE: script/osscript.sh.ftl
		PROPERTY: ${step.class}  ||  VALUE: class com.xebialabs.deployit.plugin.generic.step.ScriptExecutionStep
		PROPERTY: ${step.preview}  ||  VALUE: com.xebialabs.deployit.plugin.api.flow.Preview@552fae2e
		PROPERTY: ${step.remoteWorkingDirPath}  ||  VALUE: (UNDEFINED/UNRESOLVED) 
		PROPERTY: ${step.remoteConnection}  ||  VALUE: local:
		PROPERTY: ${step.scriptPath}  ||  VALUE: script/osscript.sh.ftl
		PROPERTY: ${step.artifact}  ||  VALUE: (UNDEFINED/UNRESOLVED) 
		PROPERTY: ${step.remoteWorkingDirectory}  ||  VALUE: local:/var/folders/mf/wyk69xfn6_nfg04s6vt4gjrw0000gn/T/ot-20150101T191228243/generic_plugin.tmp
		Complex Object: statics
		 Cannot be parsed as {statics} is not a hash or simple property

For XL-Rules, with captureMethod=true, output shows like this.

VARIABLE LISTING TILL DEPTH: 0
=====================================
		Complex Object: deployed
		METHOD: ${deployed.putSyntheticProperty(...)}
		METHOD: ${deployed.hasSyntheticProperty(...)}
		METHOD: ${deployed.get$ciAttributes(...)}
		METHOD: ${deployed.getSyntheticProperties(...)}
		METHOD: ${deployed.hashCode(...)}
		PROPERTY: ${deployed.type}  ||  VALUE: test.scripttype
		METHOD: ${deployed.putSyntheticProperties(...)}
		METHOD: ${deployed.setDeployable(...)}
		PROPERTY: ${deployed.id}  ||  VALUE: Infrastructure/local/osscript
		METHOD: ${deployed.getType(...)}
		METHOD: ${deployed.setContainer(...)}
		METHOD: ${deployed.getSyntheticProperty(...)}
		PROPERTY: ${deployed.name}  ||  VALUE: osscript
		METHOD: ${deployed.setId(...)}
		METHOD: ${deployed.get$token(...)}
		METHOD: ${deployed.getId(...)}
		METHOD: ${deployed.getClass(...)}
		METHOD: ${deployed.getContainer(...)}
		METHOD: ${deployed.hasProperty(...)}
		METHOD: ${deployed.equals(...)}
		METHOD: ${deployed.setType(...)}
		PROPERTY: ${deployed.class}  ||  VALUE: class com.xebialabs.deployit.plugin.api.udm.base.BaseDeployed
		METHOD: ${deployed.compareTo(...)}
		PROPERTY: ${deployed.$token}  ||  VALUE: (UNDEFINED/UNRESOLVED) 
		METHOD: ${deployed.setProperty(...)}
		METHOD: ${deployed.set$token(...)}
		PROPERTY: ${deployed.$ciAttributes}  ||  VALUE: com.xebialabs.deployit.plugin.api.udm.CiAttributes@54707e93
		METHOD: ${deployed.setSyntheticProperties(...)}
		METHOD: ${deployed.getName(...)}
		METHOD: ${deployed.getProperty(...)}
		METHOD: ${deployed.set$ciAttributes(...)}
		METHOD: ${deployed.getDeployable(...)}
		METHOD: ${deployed.toString(...)}


exposeJythonVariables.py
========================
This code snippet helps expose all the jython variables available while using Jython Step in XL-rules

checkXLDPermissions.py
======================
This code snippet can be used in XLR in a script task to validate the credentials of all XLD tasks in the release to make sure they are good for deploy#initial permission
![checkXLDFromXLR.png](checkXLDFromXLR.png)




