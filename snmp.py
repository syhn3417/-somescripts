# For NOC Use Only
# Written by Aaron - Infra NOC, with thanks to thispointer.com, stackoverflow
# Special thanks to Tingting for suggesting to pull data directly from DB

import pymysql
import datetime
import pprint
import os

setting = {
  "sql_host":"*.*.*.*",
  "sql_username":"***",
  "sql_password":"***",
  "sql_database":"***",
  "Email_from":"***@s.com",
  "smtp_server":"s.d*.g.com",
  "holders":"n@sea.com",
  "subject":"***"
}

# set the DB connection to read
conn = pymysql.connect(host=setting['sql_host'],port=****,user=setting['sql_username'],passwd=setting['sql_password'],db='monitoring')

preceding =  datetime.datetime.now()
last_time = "'"+preceding.strftime("%Y-%m-%d")+' 06:00:00'+"'"


# Return results in form of tuples for unpacking (df.iterows are considered to be inefficient for runtime as per documentation)
cursor = conn.cursor()
sql = '''select distinct reg, dc, i,le from lg1 where l='unknown' and create_time >= '''+last_time + "order by reg"
cursor.execute(sql)
result = list(cursor.fetchall())
conn.close()


regionlist = ["S", "C", "B", "U"]

# Loop through list of devices and perform snmpwalk
for region,idc,ipaddr,_ in result:
  
  # Do nothing if ipaddr is in ignorelist
  if ipaddr in ignorelist:
    pass

  elif region in regionlist or idc == "X":
    commstr = "xxx"
    os.system(f"snmpwalk -v 2c -c {commstr} {ipaddr} sysname")

  elif region == "I":
    commstr = "yyy"
    os.system(f"snmpwalk -v 2c -c {commstr} {ipaddr} sysname")

  elif region == "V":
    commstr = "zzz"
    os.system(f"snmpwalk -v 2c -c {commstr} {ipaddr} sysname")

  elif region == "TX":
    commstr = "aaa"
    os.system(f"snmpwalk -v 2c -c {commstr} {ipaddr} sysname")

  elif region == "T" and idc != "X":
    commstr = "bbb"
    os.system(f"snmpwalk -v 2c -c {commstr} {ipaddr} sysname")

  elif region == "M":
    commstr = "ccc"
    os.system(f"snmpwalk -v 2c -c {commstr} {ipaddr} sysname")

# To check query result from DB
#print.pprint(result)

