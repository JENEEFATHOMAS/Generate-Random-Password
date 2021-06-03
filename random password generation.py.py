import random                      #import libraries
import string

lower_alpha=string.ascii_lowercase         # access the constants  in string modules        
upper_alpha=string.ascii_uppercase
num_ber=string.digits
sym_bols=string.punctuation

pass_len=int(input("Enter password length\n"))   # get the length of the password




pass_gen=[]                                                              #create a empty string to hold password

pass_gen.extend(list(lower_alpha))                       # concatenate
pass_gen.extend(list(upper_alpha))
pass_gen.extend(list(num_ber))
pass_gen.extend(list(sym_bols))



print("Random password is: ")
print("".join(random.sample(pass_gen,pass_len)))       #print password



