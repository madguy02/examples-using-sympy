import sympy
from sympy import Symbol,cos,sin,pprint

def main():
	x=Symbol('x')
	e=cos(x)
	print()
	print ("series for cos(x):")
	pprint(e.series(x,0,10))
	print ("\n")

	e=sin(x)
	print()
	print ("series for sin(x):")
	pprint(e.series(x,0,4))
	print ("\n")
	
	e=1/cos(x)
	print()
	print("series for sec(x) :")
	pprint(e.series(x,0,10))
	print("\n")

	e=1/sin(x)
	print()
	print("series for cosec(x):")
	pprint(e.series(x,0,10))
	print("\n")

	e=sin(x)+cos(x)
	print()
	print("series for sin(x)+cos(x):")
	pprint(e.series(x,0,10))
	print("\n")

	e=sin(x)+cos(x)+1/sin(x)+1/cos(x)
	print()
	print("series for sin(x)+cos(x)+1/sin(x)+1/cos(x):")
	pprint(e.series(x,0,10))
	print("\n")

	
	
if  __name__=="__main__":
	main()
