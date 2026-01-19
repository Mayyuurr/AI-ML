import requests

def fetch_random_user_freeApi():
    url="https://api.freeapi.app/api/v1/public/randomusers/user/random"
    responce=requests.get(url)
    data=responce.json()

    if data["success"] and "data" in data:
        user_data=data["data"]
        username=user_data["login"]["username"]
        country=user_data["location"]["country"]
        return username,country
    else:
        print("Failed to fetch API data. ")


def main():
    try:
        username, contry=fetch_random_user_freeApi()
        print(f"username is :{username}, \n from :{contry}")
    except Exception as e:
        print(str(e))
    

if __name__=="__main__":
    main()