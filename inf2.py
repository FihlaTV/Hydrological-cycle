
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style

def infiltration(s,k):
	style.use('fivethirtyeight')
	file_object=open("inf.txt","w")
	file_object.write("")
	file_object.close()
	fig=plt.figure()
	ax1=fig.add_subplot(1,1,1)
	ax1=plt.gca()
	ax1.set_ylim([0,90])
	ax1.set_xlim([0,70])
	ax1.set_title('Infiltration')
	ax1.set_xlabel('Time')
	ax1.set_ylabel('infiltraion Rate')
	ax1.xaxis.label.set_color('red')
	ax1.yaxis.label.set_color('red')
	ax1.title.set_color('red')


	#s=input("Enter sorptivity: ")
	#k=input("Enter hydrolic conductivity of the soil: ")
	s=float(s)
	k=float(k)
	t=0
	i=0
	c=0
	inc=0
	a=[]
	I=[]
	while i<500:
		a.append(t)
		if t <10:
			c=s*(t**(0.5))+(k*t)	
			I.append(c)
		elif t>=10 and t<25:
			s=s-0.001
			k=k-0.001
			c=s*(t**(0.5))+(k*t)	
			I.append(c)
		elif t>=25 and t<40:
			s=s-0.003
			k=k-0.006
			inc=s*((t-25)**(0.5))+(k*(t-25))	
			I.append(c+inc)	
		else:
			I.append(inc+c)
		
		t=t+0.1;
		i=i+1

	def animate(j):
	
		file_object=open("inf.txt","a")
		if a[j]<=150:
			s=str(a[j])+","+str(I[j])+"\n"
			file_object.write(s)
			file_object.close()
		file_object=open("inf.txt","r").read()
		lines=file_object.split('\n')
		xs=[]
		ys=[]
		for line in lines:
			if len(line)>1:
				x,y=line.split(',')
				xs.append(x)
				ys.append(y)
		
		ax1=plt.gca()
		ax1.clear()
	
		ax1.set_ylim([0,200])
		ax1.set_xlim([0,170])
		ax1.set_title('Infiltration')
		ax1.set_xlabel('Time(hr)')
		ax1.set_ylabel('infiltraion Volume at time t(mm)')
		ax1.xaxis.label.set_color('red')
		ax1.yaxis.label.set_color('red')
		ax1.title.set_color('red')


		ax1.scatter(xs,ys)
		

	ani=animation.FuncAnimation(fig,animate,interval=10)

	# ani.save('infiltration.mp4', fps=10, extra_args=['-vcodec', 'libx264'])
	#ani.show()
	plt.show()


