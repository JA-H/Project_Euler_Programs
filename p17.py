single_digits = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine" ]
teens_digits =[ "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen" ]
double_digits = [ "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety" ]

with open( "p17_string.txt", "w" ) as f:
    for i in range(1, 1001):
        digits_of_i = [0, 0, 0, 0]
        number = i
        number_string = ""

        #Get the digits of the number
        counter = 0
        while number > 0:
            final_digit = number % 10
            digits_of_i[counter] = final_digit
            number = ( number - final_digit )//10
            counter += 1

        #Hundreds and Thousands
        if digits_of_i[3] != 0:
            number_string = "onethousand"
        elif digits_of_i[2] != 0 and digits_of_i[0:2] != [0, 0]:
            number_string += single_digits[ digits_of_i[2] ] + "hundred" + "and"
        elif digits_of_i[2] != 0 and digits_of_i[0:2] == [0, 0]:
            number_string += single_digits[ digits_of_i[2] ] + "hundred"    
        
        #Double digits
        if digits_of_i[1] >= 2:
            number_string += double_digits[ digits_of_i[1] - 2 ] + single_digits[ digits_of_i[0] ]
        elif digits_of_i[1] == 1:
            number_string += teens_digits[ digits_of_i[0] ]
        else:
            number_string += single_digits[ digits_of_i[0] ]
        
        f.write(number_string)
    
with open( "p17_string.txt", "r" ) as f:
    number_string = f.read()
    
    print( len(number_string) )
    
f.close()