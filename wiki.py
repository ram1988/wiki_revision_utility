import mwclient
import json
import time

companies = ["BP","Berkshire_Hathaway","McKesson_Corporation","Glencore","Industrial_and_Commercial_Bank_of_China",
		"Daimler_AG","UnitedHealth_Group","CVS_Health","Exor_(company)","General_Motors","Ford_Motor_Company",
		"China_Construction_Bank","AT&T","Total_S.A.","Foxconn","General_Electric","Verizon_Communications"]


for company in companies:
	print("Processing the company-->"+company)
	site = mwclient.Site('en.wikipedia.org')
	page = site.Pages[company]
	revisions = page.revisions(start='2016-04-01T00:00:00Z',
                           end='2017-04-01T23:59:59Z',
						   dir='newer',
						   prop='ids|timestamp|flags|comment|user',
						   limit=500)
	
	count = 0
	month_count = {}
	while True:
		try:
			rev = revisions.next()
			timestamp = rev["timestamp"]
			month = time.strftime("%m",timestamp)
			year = time.strftime("%Y",timestamp)
			key = month+"-"+year
			#print(key)
			month_count[key] = month_count[key]+1 if key in month_count else 0
		except Exception as e:
			print(e)
			break
			
		if rev!=None:
			count = count + 1
		else:
			break
			
	number_of_mons = len(month_count)
	avg = count/12
	avg = "%.2f" % round(avg,2)
	is_feb = 1 if "02-2017" in month_count else 0
	is_apr = 1 if "04-2017" in month_count else 0
	if is_apr == 1:
		is_feb = 0
	
	with open("Final Count.txt","a") as revision_count_file:
		revision_count_file.write(company+"----"+str(count)+"----"+str(avg)+"----"+str(number_of_mons)+"---"+str(is_feb)+"---"+str(is_apr)+"\n")
