import requests
import datetime

pixela_endpoint="https://pixe.la/v1/users"
TOKEN= TOKEN
USER=USER

user_params ={
    "token":TOKEN,
    "username":USER,
    "agreeTermsOfService":"yes",
    "notMinor": "yes"
}

#  --------create user on Pixela
# response=requests.post(url=pixela_endpoint,json=user_params)
# print(response.text)

##---------Create graph
graph_endpoint=f"{pixela_endpoint}/{USER}/graphs"
graph_config={
    "id":"graph1",
    "name": "Coding Graph",
    "unit":"days",
    "type": "int",
    "color":"shibafu"
}
## user headers for authentication, rather than API Keys
headers={
    "X-USER-TOKEN": TOKEN
}
# response=requests.post(url=graph_endpoint,json=graph_config,headers=headers)
# print(response.text)

#### graph will be created here: https://pixe.la/v1/users/{USER}/graphs/graph1.html

pix_endpoint = f"https://pixe.la/v1/{USER}/kateangela/graphs/graph1"
#today=datetime.datetime.today()
today=datetime.datetime(year=2022,month=4,day=9)

print(today.strftime("%Y%m%d"))



pix_config={
    "date":today.strftime("%Y%m%d"),
    "quantity":"1",
}

# response=requests.post(url=pix_endpoint,json=pix_config,headers=headers)
# print(response.text)

##-----Update a pixel
update_endpoint=f"https://pixe.la/v1/users/{USER}/graphs/graph1/{today.strftime('%Y%m%d')}"
update={
    "quantity":"2"
}
response=requests.put(url=update_endpoint,json=update,headers=headers)
print(response.text)






