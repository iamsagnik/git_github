# data fetch module
import urllib.request

data = urllib.request.urlopen("https://jsonplaceholder.typicode.com/users").read()
