# --------------
#Code starts here

#Function to read file
def read_file(path):
    #Opening of the file located in the path in 'read' mode
    file = open(path,'r')

    #Reading of the first line of the file and storing it in a variable
    sentence=file.readlines()
    #Closing of the file
    file.close()
    sentence=str(sentence).strip('[]')
    #Returning the first line of the file
    return sentence
    
#Calling the function to read file
sample_message=read_file(file_path)
#Printing the line of the file

message_1=(str(read_file(file_path_1)).strip('[]')).replace("'",'')
message_2=(str(read_file(file_path_2)).strip('[]')).replace("'",'')

print(message_1)
print(message_2)

def fuse_msg(message_a,message_b):
    message_a=int(message_a)
    message_b=int(message_b)
    quotient=round(message_a/message_b)
    quotient=str(quotient)
    return(quotient)

secret_msg_1=fuse_msg(message_1,message_2)

message_3=(str(read_file(file_path_3)).strip('[]')).replace("'",'')
print(message_3)

def substitute_msg(message_c):
    if message_c=='Red':
        sub='Army General'
    elif message_c=='Green':
        sub='Data Scientist'
    elif message_c=='Blue':
        sub='Blue'
    else:
        pass
    return sub

secret_msg_2=substitute_msg(message_3)

message_4=(str(read_file(file_path_4)).strip('[]')).replace("'",'')
message_5=(str(read_file(file_path_5)).strip('[]')).replace("'",'')

print(message_4)
print(message_5)

def compare_msg(message_d,message_e):
    a_list=[]
    b_list=[]
    c_list=[]
    a_list=message_d.split()
    b_list=message_e.split()
    c_list=[i for i in a_list if i not in b_list]
    final_msg = ' '.join([str(elem) for elem in c_list]) 
    
    return final_msg

secret_msg_3=compare_msg(message_4,message_5)
print(secret_msg_3)

message_6 =(str(read_file(file_path_6)).strip('[]')).replace("'",'')
print(message_6)

def extract_msg(message_f):
    a_list=[]
    a_list=message_f.split()

    even_word = lambda x : len(x) %2 ==0

    b_list=list(filter(even_word,a_list))
    final_msg = ' '.join([str(elem) for elem in b_list]) 

    return final_msg

secret_msg_4=extract_msg(message_6)

message_parts=[secret_msg_3, secret_msg_1, secret_msg_4, secret_msg_2]

final_path= user_data_dir + '/secret_message.txt'

secret_msg = " ".join(message_parts)
def write_file(secret_msg, path):
 fp = open(final_path, 'a+')
 fp.write(secret_msg)
 fp.close()

write_file(secret_msg, final_path)
print(secret_msg)
 



