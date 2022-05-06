from flask import Flask, request, jsonify
from .query import getPlaces
app = Flask(__name__)
    
@app.route('/hello')
def hello():
    return "hello"
    
@app.route('/travel/spots')
def getTravelSpots():
    latitude = request.args.get('lat')
    longitude = request.args.get('long')
    categories = request.args.getlist('categories')
    search_range = request.args.get('search')
    
    if search_range is None:
        search_range = 3

    tup = tuple([float(latitude), float(longitude)] + categories + [search_range])

    if search_range is None:
        search_range = 3
    print(tup)
    
    places = getPlaces(categories, tup)
    
    res = jsonify(places)

    res.headers.add("Access-Control-Allow-Origin", "*")

    return res
