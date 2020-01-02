from playsound import playsound
from time import sleep

# get the morse chart and convert into python dictionary
def get_chart(file="morse_chart.txt"):
	data = []
	with open(file) as chart:
		for line in chart:
			data.append(line.split("\n")[0].split(":"))
	char_dictionary = dict(data)
	return char_dictionary

# play "dot" and "dash" sounds
def play(code):
	if(code=="-"):
		playsound('morse_dash.mp3')
	elif(code=="."):
		playsound('morse_dot4.mp3')

# convert text into morse code
def text_to_morse(text):
	my_morse = []
	code = []
	for t in list(text):
		for key , value in d.items():
			if t.lower() == key:
				code.append(value)
	return code	

# convert morse code into text
def morse_to_text(morse):
	text = ""
	# print(morse)
	for morse_code in morse:
		for key , value in d.items():
			if morse_code == value:
				# print(key)
				text += key
	return text

def print_chart():
	print("Printing the morse chart :")
	print("Text\tMorse Code ")
	for key , value in d.items():
		print(key,"\t",value)	


# generate sound for the morse code
def play_morse(morse):
	sleep(.5)
	for morse_code in morse:
		for code in morse_code:
			print(code,end="")
			play(code)
			# sleep(.1)
		print("  ",end="")
		sleep(1)


# driver program
if __name__ == "__main__":
	# do note remove it
	# needed for the morse chart dictionary
	d = get_chart() 

	run = True
	print("\n\n****WelCome To MorseMan ****")
	print("*The Morse Code Encoder - Decoder*")
	print("Developed by : Vikas Patel at https://www.villageprogrammer.com\n\n")
	# *print chart*
	# print("Printing the morse chart :")
	# for key , value in d.items():
	# 	print("\t",key,"\t",value)	

	# ****Choice Based Operations****
	while(run):
		ch = int(input("1. Text to Morse \n2. Morse to text \n3. Print Morse Code Chart \n4. Exit\n---> "))
		if ch == 1:
			ch1 = int(input("Text to Morse--> \n\t1. Get Morse Code \n\t2. Listen Morse Code \
				\n\t3. any to go back\n---> "))
			if ch1 == 1:
				morse = ""
				text = input("Enter text (split by space) : ").split()
				for t in text:
					for code in text_to_morse(t):
						morse += code
						morse += " "
				print(morse)
			elif(ch1 == 2):
				text = input("Enter text (split by space) : ").split()
				for t in text:
					play_morse(text_to_morse(t))
		elif ch == 2:
			morse = input("Enter morse code (split by space) : ").split()
			print(morse_to_text(morse))
		elif ch == 3:
			print_chart()
		elif ch == 4:
			print("Exitting the program...")
			run = False # exit
		print("")