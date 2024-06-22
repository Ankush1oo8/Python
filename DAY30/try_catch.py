
#file not found error
# with open("data.py") as file:
#     data=file.read()

# keyError
# a_dic={"key":"value"}
# value=a_dic["non_existing_key"]

'''
try: something that might go wrong
except: do this if there was an exception
else: do this if there were no exception
finally: do this no matter what happens
'''
try:
    with open("data.py") as file:
        data=file.read()
except:
    print("ERROR")
else:
    print(data)
finally:
    file.close()
    print("FILE is CLOSED")