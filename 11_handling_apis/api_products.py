import requests

def fetch_all_products():
    base_url = "https://api.freeapi.app/api/v1/public/randomproducts?"
    
    limit = input('Enter limit how many products you want to see: ')
    
    url = base_url + f"limit={limit}"
    # print(url)

    reponse = requests.get(url)
    object = reponse.json()

    if object["success"] and "data" in object:
        product_objects = object["data"]
        totalitems = product_objects["totalItems"]
        print(f"\nTotalItems:{totalitems}")

        for i in product_objects["data"]:
            product_id = i["id"]
            product_title = i["title"]
            product_price = i["price"]
            product_category = i["category"]

            print(f"\nID:{product_id}\nTitle:{product_title}\nPrice:{product_price}\nCategory:{product_category}")


    else:
        raise Exception(object['message'])


def fetch_product_by_id():
    base_url = "https://api.freeapi.app/api/v1/public/randomproducts/"

    ID = input('Enter Product ID: ')
    url = base_url + ID
    # print(url)

    response = requests.get(url)
    print(response)

    data = response.json()

    if data["success"] and "data" in data:
        product_data = data["data"]
        product_id = product_data["id"]
        product_title = product_data["title"]
        product_price = product_data["price"]
        product_category = product_data["category"]
        
        return product_id, product_title, product_price, product_category
    
    else:
        raise Exception(data["message"])




def fetch_random_product():
    url = "https://api.freeapi.app/api/v1/public/randomproducts/product/random"

    response = requests.get(url)
    # print(response)

    data = response.json()
    # print(data)

    if data["success"] and "data" in data:
        product_data = data["data"]
        product_id = product_data["id"]
        product_title = product_data["title"]
        product_price = product_data["price"]
        product_category = product_data["category"]
        return product_id, product_title, product_price, product_category
    
    else:
        raise Exception(data["message"])



def main():
    try:
        while True:
            print('\n-----Products-----')
            print('1. List all products')
            print('2. Product By ID')
            print('3. Random Product')
            print('4. Exit App')
            choice = input("Enter your choice: ")

            if choice == '1':
                
                fetch_all_products()

            elif choice == '2':
                product_id, product_title, product_price, product_category = fetch_product_by_id()

                print(f"\nID:{product_id}\nTitle:{product_title}\nPrice:{product_price}\nCategory:{product_category}")


            elif choice == '3':
                product_id, product_title, product_price, product_category  = fetch_random_product()
                print(f"\nID:{product_id}\nTitle:{product_title}\nPrice:{product_price}\nCategory:{product_category}")


            elif choice == '4':
                break
            else:
                print("Invalid Choice")

    except Exception as e:
        print(str(e))
        # print('we crashed')

if __name__ == "__main__":
    main()