from votes.models import Project, People, Votes
from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.template import Context, Template, RequestContext, loader

from pydoc import help
from scipy.stats.stats import pearsonr

def index(request):
	people_all=People.objects.all()
	context = {'latest_Votes_list': people_all}
	return render(request, 'votes/index.html', context)

def detail(request, votes_id):
	people = get_object_or_404(People, pk=votes_id)
	return render(request, 'votes/re.html', {'people': people})

def details(request, votes_id):
	votess_id=int(str(votes_id))-1
	context={'vot': Votes.objects.filter(ppid=votess_id), 'ppl':People.objects.all(), 'proj':Project.objects.all(),}
	return render(request, 'votes/details.html', context )

def result(request, votes_id):
	votess_id=int(str(votes_id))
	up={}
	ud={}
	v=[]
	u=[]
	p=People.objects.all()
	for i in p:
		if len(Votes.objects.filter(ppid=i.id, vote=-1))!=0:
			v.append((i.id,round(float(len(Votes.objects.filter(ppid=i.id, vote=1)))/float(len(Votes.objects.filter(ppid=i.id, vote=-1))),3)))
	u1=sorted(v,key=lambda x: x[1])
	po=0
	for i in u1:
		if i[0]==votess_id :
			pos=po+1
		po=po+1
	u2=u1[pos-5:6+pos]
	for i in u2:
		if i[0]!=votess_id :
			u.append(i[0])
	ab=[]
	for l in u:
		#k=People.objects.get(id=i).id
		for j in Votes.objects.filter(ppid=int(str(i))):
			if j.pid not in ab:
				ab.append(j.pid)
	
	context ={'ab': ab, 'p': People.objects.get(id=votess_id),'peop': People.objects.all(), 'l': u}
	return render(request, 'votes/results.html', context)
