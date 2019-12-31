## import wolfram stuff
from wolframclient.evaluation import WolframLanguageSession
from wolframclient.language import wl, wlexpr
session = WolframLanguageSession('D:\\Program Files\\Wolfram Research\\Wolfram Engine\\12.0\\WolframKernel.exe')

# msg = 'none'
# while msg != 'exit':
# 	counter = 0
# 	msg = input(f'In[{counter}]:= ')
# 	print(f'Out[{counter}]:= {session.evaluate(msg)}')
# 	counter = counter + 1
# session.terminate()

begin = r'Export["D:\\dev\\discordbots\\Wolfram\\output\\output.jpg",'
end = ']'

msg = 'none'
while msg != 'exit':
	counter = 0
	msg = input(f'In[{counter}]:= ')
	export = begin + msg + end
	#expression = wlexpr(msg)
	output = session.evaluate(export)
	print(export)
	#print(f'Out[{counter}]:= {output}')
	counter = counter + 1
session.terminate()



