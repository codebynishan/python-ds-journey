# python dictionary
# a ={
#     'name':"Nishan",
#     'age' :23,
#     'address':"ktm",
# }
# print(type(a))
# print(a['name'])
# print(a['age'])
# print(a['address'])
# print(len(a)) --lenght of dict
# print(a.keys()) --keys stores in dict
# print(a.values())-- values store in dict
# data =(a.get('school')) -- none key
# if data is None:
#     print("data not found")

# user_info ={
#     "name":"suman",
#     "phone":[
#         {
#             "name":"NTC",
#             "no":"985678"
#         },
#         {
#             "name":"Ncell",
#             "no":"980",
#         }
#     ]
# }
# Phone number JIO of suman: 98213
# Phone number NCell of suman: 98213


# Phone number JIO of suman: 98213
# Phone number NCell of suman: 98213


# phone_identifier =user_info['phone']
# print("-------->",phone_identifier)
# phone_identifier_0 = phone_identifier[0]
# phone_identifier_0_name = phone_identifier_0['name']
# phone_identifier_0_no = phone_identifier_0['no']


# phone_identifier_1 = phone_identifier[1]
# phone_identifier_1_name = phone_identifier_1['name']
# phone_identifier_1_no = phone_identifier_1['no']
# print("-<", phone_identifier_1_no)

# user_name = user_info['name']

# print(f'Phone number {user_info['phone'][0]['name']} of {user_info['name']}: {user_info['phone'][0]['no']} ')
# print(f'Phone number {user_info['phone'][1]['name']} of {user_info['name']}: {user_info['phone'][1]['no']} ')

# print(f'Phone number {phone_identifier_0_name} of {user_name}: {phone_identifier_0_no} ')




# profile =[
#     {
#     "user_id":"kj4546",
#     "name":"Nishan RANA",
#     "address":[{
#         "Temporary":"Koteshwor",
#         "permanent":"Palpa"
#     }],
#     "contact":[
#         {"phone":876523455},
#         {"mobile":8754637},   
#     ]  
# },
# {
#     "user_id": "USER45t",
#     "name": "Sanjay Rana",
#     "address":[{
#         "Temporary":"New Baneshwor",
#         "permanent":"Butwal"
#     }],
#     "contact":[
#         {"phone":3655336},
#         {"mobile":3636346}, ] 
    
# },
# {
#       "user_id": "fks35245",
#     "name": "Anmol kc",
#     "address":[{
#         "Temporary":"Old Baneshwor",
#         "permanent":"Ktm"
#     }],
#       "contact":[
#         {"phone":3747474},
#         {"mobile":363463}, ] 
# }
# ]

# name =profile[0].get("name")
# user_id =profile[0].get("user_id")
# address =profile[0].get("address")
# tep_address=address[0].get("Temporary")
# print(name)
# print(user_id)
# print(tep_address)

# print(f'{name} who live in {tep_address} with {user_id}')

# Here are direct dictionary challenge questions for Python learning:
#  1.⁠ ⁠Create a dictionary with keys: "name", "age", and "courses" (a list). Print the name and the first course.
#  2.⁠ ⁠Add a new contact to a phonebook dictionary and update an existing contact's phone number.

    
# dic ={
#     "name":"Nishan Rana",
#     "age":23,
#     "course":["Maths","Pyhton","System Thinking"]  
# }
# print(dic["course"][0])
# print(dic["name"])
# dic["contact"]=26367
# print("before update",dic)
# dic["contact"]=23637
# print("after update",dic)










print(dic)