import os
import math
import sqlite3
from access_db import cou
conn=sqlite3.connect('db.sqlite3')
l2=conn.cursor()
l3=conn.cursor()

def loadProjectRatings():
	p="select * from votes_project"
	l2.execute(p)
	f=open("u.item","w+")
	for i in l2:
		f.write(str(i[0]))
		f.write(':')
		t=i[1]
		f.write(t.encode("utf8","ignore"))
		f.write('\n')
	f.close()
	v="select * from votes_votes"
	l3.execute(v)
	f1=open("u.data","w+")
	for j in l3:
		#f1.write(str(j[0]))
		#f1.write(',')
		f1.write(str(j[2]))
		f1.write(',')
		f1.write(str(j[1]))
		f1.write(',')
		f1.write(str(int(j[3])+3))
		f1.write('\n')
	f1.close()

	projects={}
	f2=open("u.item","r+")
	d=f2.read()[:-1].split('\n')
	for i in range(len(d)):
		#print d[i]
		x=d[i].split(":")
		projects[int(x[0])]=x[1]
	f2.close()
	for i in projects.keys():
		print projects[i]
	projectRatings={}
	f3=open("u.data","r+")
	d1=f3.read()[:-1].split('\n')
	for i in range(len(d)):
		#print d1[i].split(',')
		(userId, projectId, rating) = map(int,d1[i].split(','))
		projectRatings.setdefault(userId,{})
		projectRatings[userId][projects[projectId]]=float(rating)
	return projectRatings

def calculatePearsonSimilarity(projectRatings,u1,u2):
	projects={}
	for project in projectRatings[u1]:
		if project in projectRatings[u2]: projects[project]=1
	noOfprojects=len(projects)

	if noOfprojects==0:
		return 0
	sum1=sum([projectRatings[u1][project] for project in projects])
	sum2=sum([projectRatings[u2][project] for project in projects])

	sum1Sq=sum([pow(projectRatings[u1][project],2) for project in projects])
	sum2Sq=sum([pow(projectRatings[u2][project],2) for project in projects])

	pSum=sum([projectRatings[u1][project]*projectRatings[u2][project] for project in projects])

	# Calculate Pearson score
	num=pSum-(sum1*sum2/noOfprojects)
	den=math.sqrt((sum1Sq-pow(sum1,2)/noOfprojects)*(sum2Sq-pow(sum2,2)/noOfprojects))
	if den==0:
		return 0
	r=num/den
	return r

def getRecommendations(projectRatings, user):
	total={}
	similaritySum = {}
	for other in projectRatings:
		#if (other==user): continue
		similarity = calculatePearsonSimilarity(projectRatings,user,other)
		print user, other, similarity
		#if(similarity<=0): continue
		for project in projectRatings[other]:
			if project not in projectRatings[user] or projectRatings[user][project]==0:
				total.setdefault(project, 0)
				total[project]+=projectRatings[other][project]*similarity
				similaritySum.setdefault(project, 0)
				similaritySum[project]+=similarity
	recommendedProject = [(totalRating/(similaritySum[project]), project) for project,totalRating in total.items()]
	recommendedProject.sort()
	recommendedProject.reverse()
	return recommendedProject

p=loadProjectRatings()
for i in p.keys():
	print p[i]
	print '\n'

def executed(user,n):
    projectRatings = loadProjectRatings()
    return getRecommendations(projectRatings, user)[0:n]

print executed(18, 5)
conn.close()
