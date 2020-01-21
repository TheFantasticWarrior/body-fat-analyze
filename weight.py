list=input("Enter Your Weight, Fat, Muscle, and BMR:\n").split()
list[0]=float(list[0])
h=180
def delpercent(x):
	try:
		#didn't enter %
		x=round(float(x),1)
		y=str(round(x*100/list[0],1))+"%"
		return y,x
	except:
		y=x
		x=round(float(x[:-1])*list[0]/100,1)
		return y,x
fp,fv=delpercent(list[1])
bp,bv=delpercent(list[2])
print("{}kg, BMI {} \n{} / {}kg body fat \n{} / {}kg muscle \nBMR {} kcal".format(list[0],round(list[0]/(h/100)**2,1),fp,fv,bp,bv,float(list[3])))
