import os
import sqlite3
import random

conn=sqlite3.connect('db.sqlite3')
l2=conn.cursor()

def cou():
	global countv,countpt,countpl
	#count the number of people
	
	countpl=0
	l2.execute("select * from votes_people")
	for i in l2:
		countpl=countpl+1
	conn.commit()
	#print 'people ',countpl
	
	#count the number of projects
	
	countpt=0
	l2.execute("select * from votes_project")
	for i in l2:
		countpt=countpt+1
	conn.commit()
	#print 'projects ',countpl
	
	#count the number of votes
	
	countv=0
	l2.execute("select * from votes_votes")
	for i in l2:
		countv=countv+1
	conn.commit()
	#print 'votes ',countv
	
	#conn.close()
	
	return (countpt, countpl, countv)
print cou()
#lst=random.sample(range(1,15),random.randrange(1,4)

#filling up votes

i=countv+1
while i<1000:
	sql="insert into votes_votes values('%d','%s','%s','%s')" % (i+1,random.randrange(countpt),random.randrange(countpt),random.choice((-1,1,1)))
	l2.execute(sql)
	conn.commit()
	i=i+1
conn.close()
#-------------------------------------------------------------------------
#filling out peoples and projects

#f = open("rb.txt", "r+")
#rd=f.read();
#t=0
#c=2

#for i in range(len(rd)):
	#if rd[i]=='\n':
		#print '\n'
		#c=c+1
		#print c
		#company1=rd[t:i].split(' 	')[3]
		#project1=rd[t:i].split(' 	')[4]
		#name1=rd[t:i].split(' 	')[2]
		#print company1,'\n', project1,'\n', name1
		
		##sql="insert into votes_project values('%d','%s','%s','%d')" % (c, project1, company1, 0)
		##l1.execute(sql)
		##conn.commit()
		
		##sql="insert into votes_people values('%d','%s')" % (c, name1)
		##l2.execute(sql)
		##conn.commit()
		#t=i
#print c
#f.close()

#l1.execute("select * from votes_project")
#for i in l1:
	#print i
#conn.commit()
#conn.close()

#l2.execute("select * from votes_people")
#for i in l2:
	#print i
#conn.commit()
#conn.close()

#l2.execute("select * from votes_votes")
#for i in l2:
	#print i
#conn.commit()
#-----------------------------------------------------------------------------


