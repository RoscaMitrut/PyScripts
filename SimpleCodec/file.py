import random
encoded_text = []

print('Hello! Welcome to txt-encoder!')
what_do = input('Would you like to encode(0) or decode(1) a file?  ')
file_name = input("""What's the name of the file? eg. "haha.txt"  """)
what_do = int(what_do)

if what_do==0:
	random_number = random.randint(1,3)
	with open(file_name,"r")as file_object:
		contents = file_object.read()
	for i in contents:
		encoded_text.append(ord(i))
	for i in range(len(encoded_text)):
		encoded_text[i] = encoded_text[i]+random_number
		encoded_text[i] = chr(encoded_text[i])
	with open(file_name,'w') as file_object:
		for i in encoded_text:
			file_object.write(i)
		file_object.write(str(random_number))
elif what_do==1:
	with open(file_name,"r")as file_object:
		contents = file_object.read()
	the_number = contents[-1]
	for i in range(len(contents)-1):
		encoded_text.append(ord(contents[i]))
		encoded_text[i] = encoded_text[i]-int(the_number)
		encoded_text[i] = chr(encoded_text[i])
	with open(file_name,'w') as file_object:
		for i in encoded_text:
			file_object.write(i)