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


class TeeRama7:

	def __init__(self):
		self.name = 'Tee'
		self.lastname = 'Rama7'

	def myart(self):
		art = '''
------------------------------------------
.
      ":"
    ___:____     |"\/"|   
  ,'        `.    \  /		TeeRama7
  |  O        \___/  |
~^~^~^~^~^~^~^~^~^~^~^~^~

------------------------------------------
		'''
		print(art)


if __name__ == '__main__':
	test = UncleEngineer()
	test.myart()