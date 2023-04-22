import requests
response = requests.get('https://www.flickr.com/services/rest/?method=flickr.photos.getPopular&api_key=ea0a483aff725fba2d7f7b2bed7aea36&user_id=198176017%40N06&format=json&nojsoncallback=1')

if(response.status_code == 200):
    print("OK")
    print(response.json())
else:
    print("Bad Request")