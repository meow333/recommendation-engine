import os
import math
import sqlite3
from access_db import cou
conn=sqlite3.connect('db.sqlite3')
l2=conn.cursor()
l3=conn.cursor()

def pear(u1,u2):
	p=[]
	pr1=[]
	pr2=[]
	v1=[]
	v2=[]
	sql1="select * from votes_votes where ppid_id=%s" % str(u1)
	l2.execute(sql1)
	sql2="select * from votes_votes where ppid_id=%s" % str(u2)
	l3.execute(sql2)
	for i in l2:
		pr1.append(i[1])
		v1.append(i[3])
	for j in l3:
		pr2.append(j[1])
		v2.append(j[3])
	#print 'pr1=',pr1
	#print 'pr2=', pr2
	psum=0
	for i in pr1:
		for j in pr2:
			if i==j:
				p.append(i)
	print p
	if len(p)==0:
		return 0
	sum1=0
	sum2=0
	sum12=0
	sum22=0
	for i in range(len(pr1)):
		if pr1[i] in p:
			sum1=sum1+int(str(v1[i]))+3
	
	for j in range(len(pr2)):
		if pr2[j] in p:
			sum2=sum2+int(str(v2[j]))+3
	
	for k in range(len(pr1)):
		if pr1[k] in p:
			sum12=sum12+pow(int(str(v1[k]))+3,2)
	
	for l in range(len(pr2)):
		if pr2[l] in p:
			sum22=sum22+pow(int(str(v2[l]))+3,2)
	
	print sum1, sum12
	print sum2, sum22
	
	for m in range(len(p)):
		#if p[i] in pr1 and p[i] in pr2:
		#print pr1.index(p[i]), pr2.index(p[i])
		#print int(str(v1[pr1.index(p[i])])), int(str(v2[pr2.index(p[i])]))
		psum=psum+((int(str(v1[pr1.index(p[m])]))+3)*(int(str(v2[pr2.index(p[m])]))+3))
	
	print psum
	
	num=psum-(sum1*sum2/len(p))
	den=math.sqrt((sum12-pow(sum1,2)/len(p))*(sum22-pow(sum2,2)/len(p)))
	if den==0:
		return 0
	r=num/den
	print r
	return r
	conn.commit()
	conn.close()

def gtr(u):
	sim=[]
	total=[]
	for i in range(cou()[2]):
		similarity=pear(i,u)
		if similarity<=0: continue
		sql="select * from votes_votes"
		l2.execute(sql)
		for i in l2:
			
	
	
		#total={}
        #similaritySum = {}
        #for other in projectRatings:
                #if (other==user): continue
                #similarity = calculatePearsonSimilarity(projectRatings,user,other)
                #if(similarity<=0): continue
                #for project in projectRatings[other]:
                        #if project not in projectRatings[user] or projectRatings[user][project]==0:
                                #total.setdefault(project, 0)
                                #total[project]+=projectRatings[other][project]*similarity
                                #similaritySum.setdefault(project, 0)
                                #similaritySum[project]+=similarity
 
        #recommendedMovies = [(totalRating/(similaritySum[project]), project) for project,totalRating in total.items()]
        #recommendedMovies.sort()
        #recommendedMovies.reverse()
        #return recommendedMovies

mimi=input("Enter btwn 1-209")
#x,y=map(int, raw_input().split(' '))
#pear(x,y)
gtr(mimi)
	
