import requests
import datetime

current_date = datetime.datetime.now()

# Format the date as yyyyMMdd
formatted_date = current_date.strftime('%Y%m%d')


TOKEN= "jkasjdh32uiddssa"
USERNAME= "pranu432"

pixela_endpoint= "https://pixe.la/v1/users"


user_params= {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsofService": "yes",
    "notMinor": "yes",
}

graph_endpoint= f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config={
      "id": "graph1",
      "name": "Cycling Graph",
      "unit": "km",
      "type": "float",
      "color": "momiji",
}
graph_headers= {
    "X-USER-TOKEN": TOKEN,
}

post_graph_endpoint= f"https://pixe.la/v1/users/{USERNAME}/graphs/graph1"

post_graph_headers= {
    "X-USER-TOKEN": TOKEN,
}

post_params= {
    "date": "20230712",
    "quantity": "12.43",
}


data_it= requests.post(url= post_graph_endpoint,json=post_params, headers= post_graph_headers )
print(data_it.text)

