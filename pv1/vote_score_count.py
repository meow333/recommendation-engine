import os
import sqlite3
from access_db import cou

conn=sqlite3.connect('db.sqlite3')
l2=conn.cursor()
l3=conn.cursor()
#countv=cou()[2]
#print countv
#l2.execute("select * from votes_project")
#s=[]
#mem=[]
#for i in l2:
	#score=0
	#m=[]
	#sql="select * from votes_votes where pid_id="+str(i[0])
	#l3.execute(sql)
	#for j in l3:
		#score=score+int(str(j[3]))
		#if str(j[3])=='1':
			#m.append(j[2])
	#print score, m
	#mem.append(m)
	#s.append(score)
#conn.commit()
##print s
#print mem[0]

#l2.execute("select * from votes_project")
#for i in range(len(s)):
	#sql="update votes_project set score = '%d' where id = '%s'" % (s[i],i+1)
	#l2.execute(sql)
#conn.commit()

l2.execute('select * from votes_people')
for i in l2:
	sql="select * from votes_votes where ppid_id=%d and vote=%d" % (i[0]-1, 1)
	l3.execute(sql)
	u=0
	for j in l3:
		u=u+1
	sql="select * from votes_votes where ppid_id=%d and vote=%d"%(i[0]-1,-1)
	l3.execute(sql)
	d=0
	for j in l3:
		d=d+1		
	print i[1],u,d
conn.close()
