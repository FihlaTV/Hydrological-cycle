import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style


def evapotranspiration():
	style.use('fivethirtyeight')
	file_object=open("data.txt","w")
	file_object.write("")
	file_object.close()
	fig=plt.figure()
	ax1=fig.add_subplot(1,1,1)
	ax1=plt.gca()
	ax1.set_ylim([1661,1717])
	ax1.set_xlim([2017,2040])
	ax1.set_title('Evapotranspiration')
	ax1.set_xlabel('Year')
	ax1.set_ylabel('Evapotranspiration Rate')
	ax1.xaxis.label.set_color('red')
	ax1.yaxis.label.set_color('red')
	ax1.title.set_color('red')

	tmin=[]
	tmax=[]
	tmin.append(11)
	tmax.append(50)

	i=1
	while i!=24:
		tmin.append(tmin[i-1]+0.34)
		tmax.append(tmax[i-1]+0.15)
		i=i+1

	xaxis=[]
	i=2017
	while i!=2041:
		xaxis.append(i)
		i=i+1
	i=0
	c=0
	answer=[]
	while i!=24:
		c=1367*0.0023*((tmax[i]-tmin[i])**(0.653))*(((tmax[i]+tmin[i])/2)+17.8)
		answer.append(c)
		i=i+1


	i=0

	def animate(j):
	
		file_object=open("data.txt","a")
		s=str(xaxis[j])+","+str(answer[j])+"\n"
		file_object.write(s)
		file_object.close()
		file_object=open("data.txt","r").read()
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
	
		ax1.set_ylim([1661,1717])
		ax1.set_xlim([2017,2040])
		ax1.set_title('Evapotranspiration')
		ax1.set_xlabel('Year')
		ax1.set_ylabel('Evapotranspiration Rate(mm/year)')
		ax1.xaxis.label.set_color('red')
		ax1.yaxis.label.set_color('red')
		ax1.title.set_color('red')

		ax1.plot(xs,ys)
		

	ani=animation.FuncAnimation(fig,animate,interval=1000)
	#ani.save('evapotranspiration.mp4', fps=1, extra_args=['-vcodec', 'libx264'])
	#ani.show()
	plt.show()

	# plt.plot(xaxis,answer)
	# plt.show()