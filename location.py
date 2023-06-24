import geocoder
def getLocation():
    g = geocoder.ip('me')
    lat , lng = g.latlng
    return(lat,lng)