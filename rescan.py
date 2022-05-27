# For NOC Use Only
# Written by Aaron - Infra NOC, with thanks to thispointer.com, stackoverflow
# Special thanks to Tingting for suggesting to pull data directly from DB and Gao Li for providing access to the script for generating unknown_device email

import pymysql
import datetime
import pprint # For output checking purposes
import os

class create_dict(dict):
   # __init__ function
  def __init__(self):
    self = dict()

setting = {
  "sql_host":"***",
  "sql_username":"***",
  "sql_password":"***",
  "sql_database":"monitoring",
  "Email_from":"n@s.com",
  "smtp_server":"s****.***.g.com",
  "holders":"***@s.com",
  "subject":"****"
}

# Set the DB connection to read
conn = pymysql.connect(host=setting['***'],port=***,user=setting['sql_username'],passwd=setting['sql_password'],db='monitoring')


preceding =  datetime.datetime.now()
last_time = "'"+preceding.strftime("%Y-%m-%d")+' 06:00:00'+"'"

# Query SQLPro table and return results in a dictionary
mydict = create_dict()
cursor = conn.cursor()
#Query data and concatenate region and IDC
sql = '''select distinct reg, dc, i, l, concat(reg,'-',dc) AS regdc from `logmessage1` where l like 'unknown' and create_time >=  '''+last_time + "order by regdc"
cursor.execute(sql)
result = list(cursor.fetchall())
conn.close()

# For each row in SQL query result, set regdc as 'key' and append all i as 'value' to that 'key' pair
for row in result:
  # Check if regionidc exists in dict
  if row[4] in mydict:
    # Append each row to the value
    mydict[row[4]].append(row[2])
  else:
    # Create new row in value otherwise
    mydict[row[4]] = [row[2]]

# Create a list of regions using same community strings
regionlist = ["A", "B", "C", "D"]

# Loop through each row in mydict
for key,value in mydict.items():
  # Set region and IDC variables by slicing keys
  region = key[0:2]
  idc = key[3::]

  # Empty idcdevicelist file
  os.system("echo '' > idcdevicelist")

  # Loop through the list contained in each value and append each IP in the list to idcdevicelist file
  for ipaddr in value:
    with open("idcdevicelist","a+") as f:
      f.seek(0)
      data = f.read(100)
      if len(data) > 0:
        pass
      f.write(f"{ipaddr}\n")

  # Check region to set community string
  if region in regionlist or idc == "D":
    commstr = "xxx"

  elif region == "H":
    commstr = "yyy"

  elif region == "N":
    commstr = "zzz"

  elif region == "G":
    commstr = "aaa"

  elif region == "U":
    commstr = "bbb"

  elif region == "T" and idc is not "D":
    commstr = "ccc"

  # Run this command for each key in the dictionary
  os.system(f"python re-scan-basic.py {region} {idc} {commstr}")
