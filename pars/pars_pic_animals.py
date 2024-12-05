import requests

CAT_URL = 'https://api.thecatapi.com/v1/images/search'
DOG_URL = 'https://random.dog/woof.json'
FOX_URL = 'https://randomfox.ca/floof/'


def return_url_cat():
    cat = requests.get(CAT_URL)

    status_code = cat.status_code

    if status_code == 200:
        for i in cat.json():
            return i['url']
    
    else:
        while status_code != 200:
            cat = requests.get(CAT_URL)

            status_code = cat.status_code

            if status_code == 200:
                for i in cat.json():
                    return i['url']
                break
    

def return_url_dog():     
    dog = requests.get(DOG_URL)

    status_code = dog.status_code

    if status_code == 200:
        return dog.json()['url']

    else:
        while status_code != 200:
            dog = requests.get(DOG_URL)

            status_code = dog.status_code

            if status_code == 200:
                return dog.json()['url']


def return_url_fox():
    fox = requests.get(FOX_URL)

    status_code = fox.status_code

    if status_code == 200:
        return fox.json()['image']

    else:
        while status_code != 200:
            fox = requests.get(FOX_URL)

            status_code = fox.status_code

            if status_code == 200:
                return fox.json()['url']
