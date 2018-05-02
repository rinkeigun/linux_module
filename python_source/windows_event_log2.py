import csv
import wmi
c = wmi.WMI ()

writer = csv.writer (open ("logs.csv", "wb"))
#writer.writerows (
#   ((
#     log.Logfile,
#     log.RecordNumber,
#     log.Type,
#     log.EventCode,
#     log.Message,
#     log.Type,
#     log.TimeGenerated
#   ) for log in c.Win32_NTLogEvent ())
#)
for log in c.Win32_NTLogEvent ():
	print( "test")
	writer.writerows (
		log.Logfile,
		log.RecordNumber,
		log.Type,
		log.EventCode,
		log.Message,
		log.Type,
		log.TimeGenerated
		) 
