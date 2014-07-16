from votes.models import Project, People, Votes
def gen_txt():
	#pp=People.objects.all()
	p=Project.objects.all()
	v=Votes.objects.all()
	f=open("u.item","w+")
	for i in p:
		f.write(str(i.id))
		f.write('|')
		t=i.name
		f.write(t.encode("utf8","ignore"))
		f.write('\n')
	f.close()
	f1=open("u.data","w+")
	for j in v:
		f1.write(str(j.ppid.id))
		f1.write(',')
		f1.write(str(j.pid.id))
		f1.write(',')
		f1.write(str(int(str(j.vote))+3))
		f1.write('\n')
	f1.close()

def loadProjectRatings():
	global projects, projectRatings
	projects={}
	for line in open("/home/mosymeow/pv1/u.item"):
		(id,project)=line.split("|")
		projects[id]=project
	projectRatings={}
	for line in open("/home/mosymeow/pv1/u.data"):
		(userId, projectId, rating, ts) = line.split("\t")
		projectRatings.setdefault(userId,{})
		projectRatings[userId][projects[projectId]]=float(rating)
	return projectRatings

#gen_txt()
#projectRatings=loadProjectRatings()
