# request

# import requests

# pl_url= "https://sdp-prem-prod.premier-league-prod.pulselive.com/api/v1/competitions/8/seasons/2025/players?competition=8&season=2025&_limit=20"

# r = requests.get(pl_url)
# if r.status_code == 200:
#     data = r.json()
#     player_data = data['data']
#     page = data['pagination']['_next']
#     print (page)
#     for i in player_data:
#         print(i['name']['firstName'], i['name']['lastName'])


# eyJjb21wZXRpdGlvbl9pZCI6ICI4IiwgInBsYXllcl9pZCI6ICIyMTE5NzUiLCAic2Vhc29uX2lkIjogIjIwMjUifV9fQWthbmpp    
        


# import requests

# base_url = "https://sdp-prem-prod.premier-league-prod.pulselive.com/api/v1/competitions/8/seasons/2025/players"
# dict1 ={
#     "competitions": 8,
#     "seasons":2025,
#     "_limit":20,
#     "_page":1,
    
# }
# current_page = 1
# while True:
#     dict1['_page']=current_page

#     r = requests.get(base_url,dict1)
#     if r.status_code == 200:
#         data = r.json()
#         player_data = data['data']
#         page = data['pagination']['_next']
        
#         for player in player_data:
#             print(player['name']['firstName'], player['name']['lastName'])
        
#         if page == None:
#             break
            
#         else:
#             current_page += 1
#     else:
#         print(f"Error fetching data: HTTP {r.status_code}")
#         break



# import requests
 
# team_url ="https://sdp-prem-prod.premier-league-prod.pulselive.com/api/v1/competitions/8/seasons/2025/teams?_limit=20"
# id = int(input("enter team id:"))
# r = requests.get(url=team_url)
# if r.status_code == 200:
#     resp = r.json()
#     club_data = resp['data']
 
    
#     for i in club_data:
#         print(i['name'],i['id'])
#         if id != 43:
#             print(url ="https://sdp-prem-prod.premier-league-prod.pulselive.com/api/v1/competitions/8/seasons/2025/teams=(id)&limit=20")
#         else:
#             print("id found")


# import requests
# from tabulate import tabulate



# team_dict={}
# player_list = []
# team_url = "https://sdp-prem-prod.premier-league-prod.pulselive.com/api/v1/competitions/8/seasons/2025/teams?_limit=20"
# team = requests.get(url=team_url)
# if  team.status_code == 200:
#     team_result = team.json()['data']
#     for i in team_result:
#         team_dict.update({i['id']:i['name']})

# for key, value in team_dict.items():
#     print(key, value)


# user_data = input("enter a club id to get the history of club: ")

# if user_data.isdigit():
#     user_input = team_dict.get(user_data)

#     if user_input:
#         url = f"https://sdp-prem-prod.premier-league-prod.pulselive.com/api/v1/competitions/8/seasons/2025/players?competition=8&season=2025&team={user_data}&_limit=100"
#         r = requests.get(url=url)
#         if r.status_code == 200:
#             data = r.json()['data']

#             for j in data:
#                 player_list.append([j['name']['firstName'], j['name']['lastName'] , j['country']['country']])

#         headers= ["First Name", "Last Name" ,"Country"]
#         print(tabulate(player_list, headers=headers, tablefmt="grid"))  # Using fancy grid format
#     else:
#         print("Club doesnot exists")
#         exit()


# import requests
# link =  "https://restcountries.com/v3.1/name/nepal"

# r = requests.get(link)
# if r.status_code == 200:
#     data = r.json()
#     nepal =data
    
    
#     for i in nepal:
#         print(i['name']['official'],i['capital'],i['currencies'])


            
            
        

        

        




    



