def sendcordinate(request):
    import re
    from urllib.request import urlopen
    import json




    url = 'http://ipinfo.io/json'
    response = urlopen(url)
    data = json.load(response)

    IP = data['ip']
    org = data['org']
    city = data['city']
    country = data['country']
    region = data['region']