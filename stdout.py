import sys
import recon

query = sys.argv[1].replace("-","`")
query = query.replace("_"," ")
query = query.replace("!","'")


row = sys.argv[2]
try:
    count = int(sys.argv[3])
    query += " LIMIT " + str(count) + ";"
except:
    pass
dbresults = recon.recon().mysql_show(query)
for dbresult in dbresults:
    print(dbresult[row])
