# FILE NAME - grade_converter.py

# NAME: Shanelle Alvarez
# DATE: March 2, 2026
# BRIEF DESCRIPTION: Grade Converter



# 1. Make sure you fill out the comments above
# 2. Write your code in the proper spot
# 3. Be sure to answer the Reflection Questions and Attestation below
# 4. The Sample Output has been included in this code for your convenience



########## ENTER YER CODE BELOW THIS LINE ##########

def main():
    grade_converter()

def grade_converter():
    
   print('===== Grade Converter =====')
   
   user_grade = int(input('Enter a numerical grade (1-100): '))

   if user_grade < 65:
      print('F')
   elif user_grade in range (65, 70): 
      print('D')
   elif user_grade in range (70 ,80):
      print('C')
   elif user_grade in range (80, 90):
      print('B')
   elif user_grade in range (90, 101):
      print('A')
   elif user_grade > 100:
      print('A+')
  
main()


########### END YER CODE ABOVE THIS LINE ###########

    



########################################
#          SAMPLE OUTPUT
########################################

'''
===== Grade Converter =====
Enter a numerical grade (1-100): 101
A+
'''


'''
===== Grade Converter =====
Enter a numerical grade (1-100): -78
F
'''


'''
===== Grade Converter =====
Enter a numerical grade (1-100): 64
F
'''


'''
===== Grade Converter =====
Enter a numerical grade (1-100): 65
D
'''


'''
===== Grade Converter =====
Enter a numerical grade (1-100): 66
D
'''

########################################
#          REFLECTION QUESTIONS
########################################

'''

1. What is something you would tell a future student to be careful about when
   doing this lab?

 Pay attention to the ranges and indentations.






'''
