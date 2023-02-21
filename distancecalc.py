class GPS():
    import googlemaps
    from datetime import datetime
    import math
    def distance(location):
        gmaps = googlemaps.Client(key="AIzaSyDx0hqBcpeYguHBpQnEAOsXPQwWsMfahGw")
        geocode_result = gmaps.geocode(location)
        lat = int(geocode_result[0]["geometry"]["location"]["lat"])
        lng = int(geocode_result[0]["geometry"]["location"]["lng"])
        distaance = (math.sqrt(((latitude-41.99716871295172)**2)+((longtitude-(-87.69950440305266))**2)))
        print(distaance)
        return(distaance)
