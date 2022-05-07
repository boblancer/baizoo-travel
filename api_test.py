from main import app;
import unittest
from unittest.mock import MagicMock
from mock import patch

r = [
    {
        "category": [
            "cafe",
            "historical",
            "shopping"
        ],
        "description": "Touted as the world's largest golden teak building, this palace was the home of King Rama V in the early 20th century. It was originally a summer retreat on the island of Ko Si Chang, but has been transported to Bangkok in small parts in 1901. A guided tour is compulsory and tells you all about the life of King Rama V, and about his collection of fin de siecle royal memorabilia placed inside the building. As King Rama V tried to modernise Thailand along European lines, you can also see the first Thai indoor bathroom, the first typewriter with Thai characters and some of the first portrait paintings of Thailand.",
        "estimate_price": None,
        "id": 1,
        "image": [
            "google.com",
            "http://d2e5ushqwiltxm.cloudfront.net/wp-content/uploads/sites/59/2016/11/08034922/04-Vimanmek-Mansion.jpg",
            "https://cdn.tripplannera.com/media/images/original/vi/n2/vi/a/vi/vimanmek-mansion.jpg",
            "http://static.asiawebdirect.com/m/bangkok/portals/bangkok-com/homepage/attraction-palace/vimanmek-mansion/allParagraphs/BucketComponent/ListingContainer/00/image/vimanmek-mansion.jpg",
            "http://static.asiawebdirect.com/m/bangkok/portals/bangkok-com/homepage/attraction-palace/vimanmek-mansion/pagePropertiesImage/vimanmek-mansion.jpg"
        ],
        "latitude": 13.774048,
        "longtitude": 100.5124,
        "name": "Vimanmek Mansion",
        "price_range": "low"
    },
    {
        "category": [
            "historical",
            "shopping"
        ],
        "description": "Built in the year 1904, this beautiful hall was formerly used for royal meetings and banquets. Its exterior is unique as it is clearly a mix of Victorian and Islamic influences. Home to the largest part of HM Queen Sirikit's SUPPORT Museum, it shows a collection of handicraft masterpieces created by skillful people from the countryside. Some of the items on show are handbags, baskets, pots, jewellery, figurines and silk, all created using traditional techniques. HM Queen Sirikit set up this foundation to preserve and revitalise these traditional Thai handicrafts and techniques, as demand for them has significantly lowered in modern Thai society.",
        "estimate_price": None,
        "id": 2,
        "image": [
            "http://3.bp.blogspot.com/-eVhqnorgtiI/UYa5w_OL9HI/AAAAAAAAAOM/woUi_zFiuBw/s1600/Bangkok+Thailand+AD+Throne+Hall+KB.JPG",
            "https://cache-graphicslib.viator.com/graphicslib/page-images/742x525/347099_Viator_Shutterstock_174377.jpg",
            "https://upload.wikimedia.org/wikipedia/commons/c/cc/Abhisek_Dusit_Throne_Hall_(6646989131).jpg",
            "http://upload.wikimedia.org/wikipedia/commons/6/60/Abhisek_Dusit_Throne_Hall_in_Dusit_District,_Bangkok,_Thailand.jpg"
        ],
        "latitude": 13.773519,
        "longtitude": 100.513115,
        "name": "Abhisek Dusit Throne Hall",
        "price_range": "low"
    }
]
class ApiTest(unittest.TestCase):

    def test_execution(self):
        tester = app.test_client(self)
        response = tester.get("/hello")
        status_code = response.status_code
        self.assertEqual(status_code, 200)
    
    def test(self):
        tester = app.test_client(self)
        response = tester.get("/travel/spots?lat=13.783142&long=100.505866")
        self.assertEqual(status_code, 200)
if __name__ == "__main__" :
    unittest.main()
