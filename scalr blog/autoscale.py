#!/usr/bin/python
import urllib2, base64, sys,time
import xml.etree.ElementTree as ET

USERNAME = "admin"
PASSWORD = "admin"
URL1 = "http://localhost:4516/deployit/control"
URL2 = "http://localhost:4516/deployit/task/%s/start"
URL3 = "http://localhost:4516/deployit/task/%s/step/1"
URL4 = "http://localhost:4516/deployit/task/%s/archive"
REQUEST_BODY = '''<control method="getAutoScaleUpdates">
  <controllable>
    <scalr.Configuration id="Configuration/scalrConfig">
      <authVersion>3</authVersion>
      <version>2.0.0</version>
      <keyID>c0b3c2025762fc0e</keyID>
      <accessKey>VEVI/WB7CRcnLct2yOcTZXKvoMKUMFfXOMmnk3B/LAgZUu2qBfAPep7c3U8GQHIEGdcIoGB6/ERgbkZv+w5qHHZKTO3nazumHu0N5ln+MUweg8s/sqBEZtXMhSWDen7U</accessKey>
      <apiURL>http://ec2-107-21-196-227.compute-1.amazonaws.com/api/api.php</apiURL>
      <templatesRootFolder ref="Infrastructure/role_templates"/>
      <infrastructureRootFolder ref="Infrastructure/scalr"/>
      <environmentRootFolder ref="Environments/scalr"/>
      <username>hi</username>
      <password>hi</password>
    </scalr.Configuration>
  </controllable>
  <parameters>
    <scalr.Configuration_getAutoScaleUpdates id="parameters">
      <envid>%s</envid>
      <farmid>%s</farmid>
      <role>%s</role>
    </scalr.Configuration_getAutoScaleUpdates>
  </parameters>
</control>
'''


def prepareControlTask(farmid, envid, role):
	req = urllib2.Request(url=URL1, 
                      data=REQUEST_BODY % (farmid,envid,role), 
                      headers={'Content-Type': 'application/xml'})
	base64string = base64.encodestring('%s:%s' % (USERNAME, PASSWORD)).replace('\n', '')
	req.add_header("Authorization", "Basic %s" % base64string) 
	res = urllib2.urlopen(req)
	return res.read()

def startControlTask(id):
	req = urllib2.Request(url=URL2 % (id), data="<empty/>", 
                      headers={'Content-Type': 'application/xml'})
	base64string = base64.encodestring('%s:%s' % (USERNAME, PASSWORD)).replace('\n', '')
	req.add_header("Authorization", "Basic %s" % base64string) 
	res = urllib2.urlopen(req)

def waitForCompletion(id):
	state = "EXECUTING"
	log = ""
	while not state == "DONE":
		req = urllib2.Request(url=URL3 % (id))
		base64string = base64.encodestring('%s:%s' % (USERNAME, PASSWORD)).replace('\n', '')
		req.add_header("Authorization", "Basic %s" % base64string) 
		res = urllib2.urlopen(req)
		xml =  res.read()
		root= ET.fromstring(xml)
		state = root.get('state')
		log =  root.findall('./step/log')
		time.sleep(2)
	return log	

def archiveTask(id):
	req = urllib2.Request(url=URL4 % (id), data="<empty/>", 
                      headers={'Content-Type': 'application/xml'})
	base64string = base64.encodestring('%s:%s' % (USERNAME, PASSWORD)).replace('\n', '')
	req.add_header("Authorization", "Basic %s" % base64string) 
	res = urllib2.urlopen(req)

id = prepareControlTask(sys.argv[1],sys.argv[2],sys.argv[3])
startControlTask(id)
result = waitForCompletion(id)
archiveTask(id)
print  sys.argv[1]+ "_" + sys.argv[2]