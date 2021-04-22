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


class DekchaiTortao:

	def __init__(self):
		self.name = 'Dekchai'
		self.lastname = 'Tortao'

	def myart(self):
		art = '''
------------------------------------------
		                       .-'~~~-.
                     .'o  oOOOo`.
                    :~~~-.oOo   o`.
    Dekchai Tortao   `. \ ~-.  oOOo.
                       `.; / ~.  OO:
                       .'  ;-- `.o.'
                      ,'  ; ~~--'~
                      ;  ;
_______\|/__________\\;_\\//___\|/________
------------------------------------------
		'''
		print(art)



if __name__ == '__main__':
	test = UncleEngineer()
	test.myart()