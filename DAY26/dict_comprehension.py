'''
new_dict={new_key:new_value for item in list}
new_dict={new_key:new_value for(key,value) in dict.items()}

#with condition
new_dict={new_key:new_value for(key,value) in dict.items() if test}

'''
import random
names=["Alex","Beth","Ankush","Sanjay","Chudiwal"]

students_scores={name:random.randint(1,100) for name in names}

passed_students={key:value for (key,value) in students_scores.items() if value>60}
print(passed_students)

#exercise
sentence="What is the Airspeed Velocity of an Unladen Swallow?"
list=sentence.split()
letter_count={key :len(key) for key in list}
print(letter_count)