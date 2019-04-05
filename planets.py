def weight_on_planets():
   # write your code here
   normalWeight = int(input("What do you weigh on earth? "))
   marsWeight = normalWeight * 0.38
   jupiterWeight = normalWeight * 2.34

   #print(" \nOn Mars you would weigh {} pounds. \nOn Jupiter you would weigh {} pounds." .format(marsWeight, jupiterWeight))
   print("\nOn Mars you would weigh " +str(marsWeight)+ " pounds. \nOn Jupiter you would weigh "+str(jupiterWeight)+ " pounds." )
   
   
   
if __name__ == '__main__':
   weight_on_planets()