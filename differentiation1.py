import sympy
from sympy import pprint

def main():
	a=sympy.Symbol('a')
	b=sympy.Symbol('b')
	c=sympy.Symbol('c')
	e=(a+b+c)**5
	print("\n Expression:")
	print()
	pprint(e)
	print ("\n derivation:")
	print()
	pprint(e)
	pprint (e.diff(a))
	pprint(e.diff(b))
	pprint(e.diff(c))
	pprint (e.diff(a).diff(b).diff(c))
	print()
	pprint (e.expand().diff(a).diff(b).diff(c))
	

if __name__=="__main__":
	main()
	
