import codecs
from django.db import models
uv=[]
dv=[]
class People(models.Model):
	name = models.CharField(max_length=200)
	def __unicode__(self):
		return self.name
	
	def up_voted_to(self):
		return len(Votes.objects.filter(ppid=self.id-1, vote=1))
	up_voted_to.short_description='UP'
	
	#def ppuv(self):
		#return str(Votes.objects.filter(ppid=self.id-1, vote=1))
	#ppuv.short_description='UP Voted Projects'
		
	def down_voted_to(self):
		return len(Votes.objects.filter(ppid=self.id-1, vote=-1))
		#return len(p)
	down_voted_to.short_description='DOWN'
	
	#def ppdv(self):
		#return str(Votes.objects.filter(ppid=self.id-1, vote=-1))
	#ppdv.short_description='DOWN Voted Projects'
	
	def up_down_ratio(self):
		up=float(Votes.objects.filter(ppid=self.id-1, vote=1).count())
		down=float(Votes.objects.filter(ppid=self.id-1, vote=-1).count())
		r=round(float(up/down),2)
		return r
	up_down_ratio.short_description='Likeability'

uv1=[]
dv1=[]
class Project(models.Model):
	name = models.CharField(max_length=200)
	category = models.CharField(max_length=200)
	score = models.IntegerField(default=0)
	
	def __unicode__(self):
		return self.name
	
	def highest_10(self):
		t=Project.objects.all().count()
		c=Project.objects.order_by('score')[t-10::-1][9].score
		for i in range(10):
			if self.score>c-1:
				return True
			else:
				return '-'
	highest_10.boolean=False
	highest_10.short_description='Top 10'
	def up_voted(self):
		return len(Votes.objects.filter(pid=self.id-1, vote=1))
	up_voted.short_description='UP'
	
	#def puv(self):
		#return str(Votes.objects.filter(pid=self.id-1, vote=1)[::-1])
	#puv.short_description='UP Voted by'

	def down_voted(self):
		return len(Votes.objects.filter(pid=self.id-1, vote=-1))
		#return len(p)
	down_voted.short_description='DOWN'
	
	#def pdv(self):
		#return str(Votes.objects.filter(pid=self.id-1, vote=-1)[::-1])
	#pdv.short_description='DOWN Voted by'
	
    
class Votes(models.Model):
	pid = models.ForeignKey(Project)
	ppid = models.ForeignKey(People)
	vote = models.CharField(max_length=2)
	
	def __unicode__(self):
		s=str(self.pid)#+' voted to '+str(self.pid)
		return s
