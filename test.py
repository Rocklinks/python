import requests
response=requests.get("https://api.github.com/repos/kubernetes/kubernetes/pulls")
det = response.json()

for i in range(len(det)):
    print(det[i]['user']['login'])
