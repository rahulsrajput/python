import requests



def fetch_book_data():
    url = 'https://api.freeapi.app/api/v1/public/books/book/random'

    response = requests.get(url)
    print(response)
    
    data = response.json()
    # print(data)

    if data["success"] and "data" in data:
        book_data = data["data"]
        # print(book_data)
        title = book_data["volumeInfo"]["title"]
        
        author = book_data["volumeInfo"]["authors"]
        publishedDate = book_data["volumeInfo"]["publishedDate"]

        return title, author, publishedDate
        

    else:
        raise Exception("Failed To fetch BookData")
    

def main():
    try:
        title, author, publishedDate = fetch_book_data()
        print(f"Title: {title}\nAuthor: {author}\nPublishDate: {publishedDate}")

    except Exception as e:
        print(str(e))
        

if __name__ == '__main__':
    main()  