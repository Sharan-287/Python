import requests

def fetchdata(url):
    
    try:
        response=requests.get(url)
        data=response.json()
        return data
    except requests.exceptions.HTTPError as httperr:
        print(f"It was an http Error:{httperr}")
    except requests.exceptions.RequestException as reqerr:
        print(f"It was an req Error:{reqerr}")
    except ValueError:
        print("It was an non valid json")

url="https://jsonplaceholder.typicode.com/posts/4"
result=fetchdata(url)
print(result)