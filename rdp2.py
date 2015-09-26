'''
Author: Adesh Atole, Abhshek Bera, Piyush Galphat
Recursive Descent Parser for Sample Language

Grammar is: E->iE'
			E'->+iM/e			(e=epsilon)
			M->kE'/e
			
			
			This grammar accepts strings of the from: i+ik+ik+ik+i... and so on...
To inpmlement the program,
We write Function for each Non-Terminal like E and E'
and match() function to verify the terminal symbol

If a non-terminal has more than one production, then if-else cases are used
'''
string='i+ik+ik+i$'			#'$' indicates termination of string
p=0
flag=True

def E():
	global p			#indicating that p is global var
	if(string[p]=='i'):
		match('i')
		Ed()

def Ed():
	global p
	if(string[p]=='+'):
		match('+')
		match('i')
		M()
	else:
		return
def M():
	global p
	if(string[p]=='k'):
		match('k')
		Ed()
	else:
		return

def match(t):
	global p
	global flag
	if(string[p]==t):
		print('Accepted::',  t)
		p+=1
	else:
		print("Error: expected:: ",t, "at position:: ",p)
		flag=False

E()
if(string[p]=='$' and flag):
	print("String Accepted!!")
else:
	print("String Not Accepted!!")

