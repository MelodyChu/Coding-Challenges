'''
Divide two integers. Surround repeating sequence in decimal part with parentheses. 
For example,

divide(4, 2) = "2"
divide(2, 4) = "0.5"   2 / 4 => 0.5
divide(1, 3) = "0.(3)" 1 / 3 = 0.333333333 => 0.(3) <--
divide(2, 11) = "0.(18)" <--
divide(112, 999) = "0.(112)"
divide(1, 7) = "0.(142857)" 1 / 7 = 0.142857142857 ... => 0.(142857)
'''

'''
     0.181 
11 | 2
     0
     --
     20 <--
     11
      --
      90
      88
       --
       20 <--
       11
        --
        ...
'''

'''
        0.112
999 | 112
        0
      ---
      1120
       999
       ---
       1210
        999
        ---
        2110
        1998
         ---
         1120
          999
          ---
          ...
'''
# given 2 integers; output is a string
# if the number divides evenly, return string of that integer (modula)
# if not:
# output is a float
# create variable to store digit(s) after the decimal
# def say_hello():
#     print 'Hello, World'

# for i in xrange(5):
#     say_hello()

def find_repeats(int1,int2):
    if int1 % int2 == 0:
        return str(int1/int2)
    else:
        quotient = float(int1/int2)
        final_answer = str(int(quotient)) + '.' # take quotient up until the decimal until repeats exist
        remainder_set = set()
        remainder = int1 # 121
        # numerator = int1
        #repeat = False
        while remainder not in remainder_set:
            remainder_set.add(remainder)
            remainder = (remainder*10) % int2
            if remainder == 0:
                return final_answer
            decimal = ((remainder*10)/int2)
            final_answer += str(decimal)
        
            
        
    print remainder_set
    
find_repeats(112,999)
            
            
            
            