def runoff(intensity,area,soil_type):

	intensity=float(intensity)
	area=float(area)


	k=0
	while True:
		soil_type=int(soil_type)
		if soil_type==1:
			k=0.65
			break
		elif soil_type==2:
			k=0.7
			break
		elif soil_type==3:
			k=0.5
			break
		elif soil_type==4:
			k=0.35
			break
		elif soil_type==5:
			k=0.25
			break
		elif soil_type==6:
			k=0.15
			break
		else:
			print("Enter valid number")
	file_object=open("ans.txt","w")
	file_object.write(str(k*area*intensity))
	file_object.close()
	return float(k*area*intensity)
	
