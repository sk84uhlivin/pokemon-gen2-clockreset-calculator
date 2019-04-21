#!/usr/bin/python3

print() 

print('Pokémon Gen 2 Clock Reset Calculator v1.0 by sk84uhlivin')

print()

arbval = 63
dcon = 256
magicnumber = 65535

class calc:
	def name(input_name):
		x = 0
		y = 0
		if len(input_name) > 4:
			for x in range(5):
				y+=ord(input_name[x])
				y+=arbval 
			return y
		else:
			for x in range(len(input_name)):
				y+=ord(input_name[x])
				y+=arbval
			return y
			
	def id(input_id):
		return (int(input_id)//dcon)+(int(input_id)%dcon)
		
	def cash(input_cash):
		if input_cash > magicnumber:
			modinput_cash = input_cash%magicnumber
			return ((modinput_cash)//dcon)+((modinput_cash)%dcon)
		else:
			return ((input_cash)//dcon)+((input_cash)%dcon)

#Prints results of calc functions			
def debug():
	print('Debug info:')
	print(calc.name(input_name),calc.id(input_id),calc.cash(input_cash))
	
def main():	
	input_name  = input("NAME? ")
	input_id    = int(input("ID#? "))
	input_cash  = int(input("CASH? "))
	password = calc.name(input_name) + calc.id(input_id) + calc.cash(input_cash)
	
	print()
	
	print(str(password).zfill(5))
	
	print()

if __name__ == '__main__':
	while True:
		main()
		if input('Restart? ') != 'y':
			break
		else:
			print()