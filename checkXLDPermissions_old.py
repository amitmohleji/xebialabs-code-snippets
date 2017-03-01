import httplib
import base64
import json
def  hasPermission(t):
      de = t.pythonScript.getProperty("deploymentEnvironment") 
      if de != None:
        u =  t.pythonScript.getProperty("username")
        p =  t.pythonScript.getProperty("password")
        dp = t.pythonScript.getProperty("deploymentPackage")
        s = t.pythonScript.getProperty("server")
        if u == None:
          u = s.username
        if p == None:
          p = s.password
        conn = httplib.HTTPConnection(s.url.split("//")[1])
        authcode = str("Basic " + base64.b64encode(str(u) + ":" + str(p)))
        headers = {"Authorization": authcode}
        conn.request("GET", "/deployit/security/check/deploy%23initial/Environments/"+ de, headers=headers)
        res = conn.getresponse()
        if res.status == 200:
          res_text = res.read()
          if res_text.find("false") > -1:
            return False
          else:
            return True
        else:
          return False    
      else :
        return False

finalState = True
print "Phase Name|XL Deploy Task Title| Environment | Creds can Deploy (Y/N)"
print "---|---|---|---"
for p in release.phases:
  for t in p.tasks:
    if str(t.taskType) == "xldeploy.Deploy":
      status = hasPermission(t)
      print "%s|%s|%s|%s" % (p.title,t.title ,t.pythonScript.getProperty("deploymentEnvironment"), status)
      finalState = finalState and status
if finalState == False:
  raise ValueError("Some Credentials need to be corrected")