import sys
import parserDescription
import requests


base_url='http://httpbin.org/'

main_parser = parserDescription.createParser()
namespace = main_parser.parse_args(sys.argv[1:])

def getRequest():
    if namespace.header:
        response = requests.get(base_url + '/headers')
        print(response.text)
    elif namespace.ip:
        response = requests.get(base_url + '/ip')
        print(response.text)
    elif namespace.useragent:
        response = requests.get(base_url + '/user-agent')
        print(response.text)


def postRequest():
    if namespace.header:
        response = requests.post(base_url + '/response-headers?freeform=' + namespace.header)
        print(response.text)
    elif namespace.delay:
        response = requests.post(base_url + '/delay/' + namespace.delay)
        print(response.text)

def putRequest():
    if namespace.status:
        response = requests.put(base_url + '/status/' + namespace.status)
        print(response.text)
    elif namespace.anything:
        response = requests.put(base_url + '/anything')
        print(response.text)