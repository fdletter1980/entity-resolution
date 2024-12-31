from zingg.client import *
from zingg.pipes import *

#build the arguments for zingg
args = Arguments()
#set field definitions
CUSTOMER_ID = FieldDefinition("MLS_ID", "string", MatchType.EXACT)
LICENSE_NUM = FieldDefinition("LICENSE_NUM", "string", MatchType.EXACT)
FIRST_NAME = FieldDefinition("FIRST_NAME", "string", MatchType.EXACT)
LAST_NAME = FieldDefinition("LAST_NAME", "string", MatchType.EXACT)
HOME_PHONE = FieldDefinition("HOME_PHONE", "string", MatchType.EXACT)
MOBILE_PHONE = FieldDefinition("MOBILE_PHONE", "string", MatchType.EXACT)
OFFICE_PHONE = FieldDefinition("OFFICE_PHONE", "string", MatchType.EXACT)
EMAIL = FieldDefinition("EMAIL", "string", MatchType.EMAIL)
ADDRESS = FieldDefinition("ADDRESS", "string", MatchType.EXACT)
CITY = FieldDefinition("CITY", "string", MatchType.EXACT)
STATE = FieldDefinition("STATE", "string", MatchType.EXACT)
ZIP_CODE = FieldDefinition("ZIP_CODE", "string", MatchType.EXACT)

fieldDefs = [CUSTOMER_ID, LICENSE_NUM, FIRST_NAME, LAST_NAME, HOME_PHONE, MOBILE_PHONE, OFFICE_PHONE, EMAIL, ADDRESS, CITY, STATE, ZIP_CODE]

args.setFieldDefinition(fieldDefs)
#set the modelid and the zingg dir
args.setModelId("107")
args.setZinggDir("models")
args.setNumPartitions(4)
args.setLabelDataSampleSize(0.5)

#reading dataset into inputPipe and settint it up in 'args'
#below line should not be required if you are reading from in memory dataset
#in that case, replace df with input df
schema = "CUSTOMER_ID string, LICENSE_NUM string, FIRST_NAME string, LAST_NAME string, HOME_PHONE string, MOBILE_PHONE string, OFFICE_PHONE string, EMAIL string, ADDRESS string, CITY string, STATE string, ZIP_CODE string"
inputPipe = CsvPipe("testAgent", "models/er-customer/customer_er.csv", schema)
args.setData(inputPipe)
outputPipe = CsvPipe("resultAgent", "models/er-customer/CustomerOutput")

args.setOutput(outputPipe)

options = ClientOptions([ClientOptions.PHASE,"match"])

#Zingg execution for the given phase
zingg = Zingg(args, options)
zingg.initAndExecute()