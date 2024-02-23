import requests


def fetch_random_product():
    url = "https://api.freeapi.app/api/v1/public/randomproducts/product/random"

    response = requests.get(url)
    # print(response)

    data = response.json()
    # print(data)

    if data["success"] and "data" in data:
        product_data = data["data"]
        id = product_data["id"]
        title = product_data["title"]
        price = product_data["price"]
        rating = product_data["rating"]
        category = product_data["category"]

        return id,title,price,rating,category
    else:
        raise Exception('Failed to fetch data...')
    

def main():
    try:
        id,title,price,rating,category = fetch_random_product()
        print(f"ID:{id}\nTitle:{title}\nPrice:{price}\nRating:{rating}\nCategory:{category}")
        
    except Exception as e:
        print(str(e))


if __name__ == '__main__':
    main()