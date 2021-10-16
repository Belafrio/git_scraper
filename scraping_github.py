import sys
import requests

# we crete a function that calls the API for details of the User

def findUserInfo(username):
    url="https://apl.github.com/users/" + username
    html=requests.get(url)
    return html.json()

# a function to handle errors if data is not provided

def getfield(key,dic):
    if dic[key] is None:
        return 'Not Available'
    return dic[key]


# calling of the functions

if __name__=='_main_':
    username=input('Enter the username: ')
    userDetails=findUserInfo(username)
    if 'message' in userDetails.keys():
        print('Usetname not found')
        sys.exit()
    else:
        print('"Name " \n'+userDetails['name'], '\n')
        print('"About"\n')
        print('Bio: ', getfield('bio',userDetails))
        print('Email: ',getfield('email', userDetails))
        print('"Profile Details"\n')
        print('Public Repositories: ', userDetails['public_repos'])
        print('Public Gists: ',userDetails['public_gists'])
        print('Followere: ',userDetails['followers'])
        print('Following: ',userDetails['following'])