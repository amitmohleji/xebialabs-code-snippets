
# custom report method generates a custom report with desired fields
# startDate/enddate format : mm/dd/yyyy
def customReport(startDate, endDate, targetfile):
 file = open(targetfile, "w")	
 queryResult = task2.query(startDate, endDate)
 tuple = "Change, QA Task, PROD Task, ApplicationVersion, Environment, Deployment Type, Owner, Status, StartDate, CompletionDate"
 file.write(tuple + "\n")
 print tuple
 for item in queryResult:
  mdata = item.getMetadata()
  versionObj =  repository.read(repository.read(mdata["environment_id"] + "/" + mdata["application"]).version)
  tuple = versionObj.satisfiesChangeTicketNumber  + "," + versionObj.satisfiesChangeTaskNumberQA + "," + versionObj.satisfiesChangeTaskNumberPROD + ","
  tuple = tuple + mdata["application"] + "/" + mdata["version"] + "," + mdata["environment_id"] + "," + mdata["taskType"] + "," + item.getOwner() + "," +item.getState().toString() + "," + item.getStartDate().toString() + "," + item.getCompletionDate().toString()
  file.write(tuple + "\n")
  print tuple
 file.close()
