

def FindTheTextBetween(part_1, part_2, main_text):
	search_index = 0
	part_1_index = 0
	part_2_index = 0
	part_1_length = len(part_1)
	part_2_length = len(part_2)
	possible_match = 0 
	string_to_find = ""
	for letter_main in main_text:
		search_index = search_index + 1
		if(possible_match == 0):
			if(letter_main == part_1[part_1_index]):
				part_1_index = part_1_index + 1
				
				if(part_1_length == part_1_index): #PART 1 Completely found
					possible_match = 1
			else:
				#print "Wront path"
				part_1_index = 0
		else:
			string_to_find = string_to_find + letter_main
			#print string_to_find
			if(letter_main == part_2[part_2_index]):
				part_2_index = part_2_index + 1
				if(part_2_length == part_2_index + 1): #PART 2 Completely found
					return string_to_find[0 : len(string_to_find) - part_2_length + 1] #Substring to get the part just we need
					break #Exit the loop just in case
				
	return ""

file1 = open("the_truman_show_script.txt","r") 
script_content = file1.readlines() #script_content is now holding the text from the file the_truman_show_script.txt as string
file1.close() 

file2 = open("statements.txt","r") 
statements_content = file2.readlines() #statements_content is now holding the text from the file statements.txt as a string array
file2.close() 





for item in statements_content:
	#print(item)
	#items is now holding a single statement
	
	data = item.split("___") #data[0] is now holding the first part before "___" of the statement. data[1] is hodling the second part
	found_text = FindTheTextBetween(data[0], data[1] , script_content[0])
	print item
	if(found_text):
		print data[0] + found_text + data[1]
	else:
		print "Statement Not Found"
