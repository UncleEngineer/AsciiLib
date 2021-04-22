# mainascii.py

############FIND ASCII ART IN https://www.asciiart.eu/ ##############
class UncleEngineer:

	def __init__(self):
		self.name = 'Uncle'
		self.lastname = 'Engineer'

	def myart(self):
		art = '''
------------------------------------------
		                       .-'~~~-.
                     .'o  oOOOo`.
                    :~~~-.oOo   o`.
    Uncle Enginer    `. \ ~-.  oOOo.
                       `.; / ~.  OO:
                       .'  ;-- `.o.'
                      ,'  ; ~~--'~
                      ;  ;
_______\|/__________\\;_\\//___\|/________
------------------------------------------
		'''
		print(art)

class SPT:

	def __init__(self):
		self.name = 'SPT'
		self.lastname = 'THG'

	def myart(self):
		art = '''
------------------------------------------
		SPT-THG
              <<<      >>>
            <<<__________>>>
                 ll ll
------------------------------------------
		'''
		print(art)

if __name__ == '__main__':
	test = UncleEngineer()
	test.myart()
