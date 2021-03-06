import psycopg2
import psycopg2.extras


def format_array(size):
    return "(" + (",").join(["%s"] * size)  + ")"
    
def getPlaces(categories, tup):

    connection = psycopg2.connect(
        host= "ec2-52-0-114-209.compute-1.amazonaws.com",
        database="dbub6q0jgc89na",
        user="pwjrssymnfrajw",
        password="e521e18346ead9138d9df37d6787e38edce25e20c4ce8e95e9300b1ea3b2c7c1",
        sslmode='require')

    cursor = connection.cursor(cursor_factory=psycopg2.extras.RealDictCursor)

    filter_query = ''
    if categories:
        categories = format_array(len(categories))
        
        filter_query += f"and place.id in (select pc.place_id from place_categories pc inner join category c on pc.category_id = c.id where c.type in {categories})"
      
    place_query = f"select place.id, name, price_range, description, estimate_price, latitude, longtitude, \
    array_agg(distinct c.type) as category, array_agg(distinct im.image_url) as image from place \
    inner join place_categories pc on place.id = pc.place_id \
    inner join category c on pc.category_id = c.id \
    inner join place_image_urls im on place.id = im.place_id where \
    geodistance((%s), (%s), place.latitude, place.longtitude) < %s {filter_query} group by place.id" 

    cursor.execute(place_query, tup)
    
    places = cursor.fetchall()
    
    connection.close()

    return places