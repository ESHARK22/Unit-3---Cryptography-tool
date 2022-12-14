#################################
#By Thomas Turner 9SU, With notes
#################################

#Modules
import random 
import mysql.connector
from mysql.connector import Error
import pandas as pd
import time

#Connects to the SQL server
def create_server_connection(hostname,username,password):
    connection = None
    try:
        connection = mysql.connector.connect(host = hostname, user = username, passwd = password)
        print("MySQL Database connection successful")
    except Error as err:
        print(f"Error: '{err}'")
    return connection

pw = "22501asd"
db = "mysql_python"
connection = create_server_connection("localhost","root",pw)



#Empty variables used for storing data
encrypted = ""
decrypted = ""
number_list = ""
decrypted = ""
encrpted_message = []

#Encrypt or Decrypt message
encrypt_decrypt = input("Would you like to encrypt or decrypt a message?[E/D]: ").upper()

if "E" in encrypt_decrypt:
    
    #Asks the user to input a message to encrypt and asks for the name to store it as
    message = input("Enter a message to encrypt: ")
    number_list += input("What do you want to call the message?: ") + "|"
    
    
    #Option to save the encrypted data
    save_file = input("Do you want to save this encrypted message in a file [Y/N]:  ").upper()
    if "Y" in save_file:
        save_file = True
    else: 
        save_file = False


    #Adds a random number from 1,55295 (FULL ASCII TABLE) in ASCII to each character of the message
    for char in message:

        #Generates a random number in ASCII
        rand_num = random.randint(1,55295)

        #Converts the characters in the alphabet into an ASCII value then add the random number to it, then converts back from ASCII to form an encrypted message
        encrypted = chr(ord(char) + rand_num)

        #creates a variable which stores the encrypted character + the offset and adds a colon for the next character
        number_list += str(encrypted) + str(rand_num) + ":" 
    
        

        if ord(encrypted[-1]) > 55295:
            encrypted = chr(ord(char) + rand_num - 55295)
            # This adds the character to the end of the string BUT this time it is less than 55295
    
    
    
    #Creates a variable where it takes the name and where there is the pipe character it spilts in there and makes everything before it have the index value (0)
    #[1].split(":").pop(-1) makes everything before the colon have the index vaule (1) in the list and the .pop(-1) removes this for the last character as there is an empty colon at the end
    encrypted_list = number_list.split("|")[1].split(":").pop(-1)
    
    #New line to organise data
    number_list += "\n"
    
    for item in encrypted_list:
        #Sets the offset to the value in index value (1)
        offest = item[1:]
        #gets the character at index value(0) which is the encrypted character
        encrypted_letter = item[0]
        #Minus the offset to get the decrypted message back
        decrypted += chr(ord(encrypted_letter) - int(offest))
    #print(decrypted)
        
    if save_file: 
        #Saving system
        print("Saving...")
        #Sleep to make it look realistic
        time.sleep(2)
        print("Your message has been encrypted!")
        file = open("data.txt", "a", encoding="utf-8")
        file.write(number_list)
        file.write("\n")
        file.close()
        
    else:
        print("Messages was not saved!")

elif "D" in encrypt_decrypt:
    
    
    wanted = input("What is the name of the message to decrypt?: ") # What is the name of the message to decrypt?
    _found = False # has the message been found? 
    
    # open the file and add each line to a list
    with open("data.txt", "r", encoding="UTF-8") as _file:
        for new_line in _file: 
            encrpted_message.append(new_line) #Add to the end of the list

    # for each message in the list, check if the name is in the message
    for messsage in encrpted_message:
        
        if wanted in messsage: # if the name is in the message
            
            _found = True
            print("Message found:")
            
            
            word_list = messsage.split("|") # split up the message into the name [0] and the encrypted message [1]
            word_list = word_list[1] # select the encrypted message
            word_list = word_list.split(":") # split the message into the seoarate letters
            word_list.pop(-1) # remove the last item in the list (its empty)

             

            for letter in word_list: # for each letter
                
                encrypted_letter = letter[0] # get the letter, which is the fisrt character
                offest = letter[1:] # get the offset, which is the rest of the characters
                
                decrypted += chr(ord(encrypted_letter) - int(offest)) # add the decrypted letter to the decrypted message
                
            print("Your decrypted message is: ", decrypted)# print the decrypted message
            break # stop the loop, as the message has been found

    if not _found: # if the message has not been found
        print("Message not found")


else:
    print("Invalid input!")