import requests

resteraunts = [
    {
        "image_url": "https://imageio.forbes.com/specials-images/imageserve/5d77914da3159c0008a93d96/Wendy-s-breakfast-menu-/960x0.jpg?format=jpg&width=960",
        "resteraunt_name": "Wendy's",
        "delivery_fee": 3.99,
        "location": "2355 Trafalgar Rd Bldg A1",
        "cuisine_type": "Fast Food",
        "opening_hours": "8:00",
        "closing_hours": "22:00"
    }
]

items = [
        {
            "image_url": "https://mma.prnewswire.com/media/1227532/Wendys_4_for_4_Spicy_Chicken.jpg",
            "product_name": "Spicy Crispy Sandwhich Combo",
            "calorie_count": 900,
            "price": 6.50,
            "resteraunt_id": 1
        },
        {
            "image_url": "https://media.npr.org/assets/img/2017/05/09/10-piece-chicken-nuggets-ss_0_custom-db31f599b4b36050d9a26986abaf75c76c655f37-s1100-c50.jpg",
            "product_name": "Breaded Chicken Nuggets",
            "calorie_count": 350,
            "price": 3.00,
            "resteraunt_id": 1
        },
        {
            "image_url": "https://people.com/thmb/SfTdO0MCEUX1h7v6sBZ3tX0Ylo8=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc():focal(277x0:279x2)/Wendys_Hot_Crispy_Fries-62b1b426bec34ea2b97d3c5c6041c82d.jpg",
            "product_name": "French Fries",
            "calorie_count": 600,
            "price": 2.50,
            "resteraunt_id": 1
        },
        {
            "image_url": "https://www.wendys.com/sites/default/files/styles/max_325x325/public/2021-05/combos-305_medium_US_en.png?itok=TFnjsi9f",
            "product_name": "Dave's Triple Combo",
            "calorie_count": 1200,
            "price": 12.99,
            "resteraunt_id": 1
        },
        {
            "image_url": "https://www.foodbusinessnews.net/ext/resources/2022/11/16/wendys-chicken-sandwich_LEAD.jpg?height=667&t=1668623216&width=1080",
            "product_name": "Cheesy Mozerella Sandwhich",
            "calorie_count": 1025,
            "price": 8.75,
            "resteraunt_id": 1
        },
        {
            "image_url": "https://www.wendys.com/sites/default/files/styles/max_325x325/public/2021-05/wendys-kids-meal-129_medium_US_en.png?itok=OrSE2T4o",
            "product_name": "Wendy's Kids Meal",
            "calorie_count": 460,
            "price": 6.50,
            "resteraunt_id": 1
        },  
        {
            "image_url": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRLYhIYiuNffUebAWvfEe67s3JGrUGjP9Vk4w&usqp=CAU",
            "product_name": "Sausage Breakfast Sandwhich",
            "calorie_count": 850,
            "price": 6.75,
            "resteraunt_id": 1
        },
        {
            "image_url": "https://www.wendys.com/sites/default/files/styles/max_325x325/public/2021-05/frosty-126_medium_US_en.png?itok=kMWt88LW",
            "product_name": "Vanilla Frosty",
            "calorie_count": 600,
            "price": 1.25,
            "resteraunt_id": 1
        },
                {
            "image_url": "https://thequietgrove.com/wp-content/uploads/2020/05/Untitled-design-91.jpg",
            "product_name": "Cool Gatorade Slush",
            "calorie_count": 900,
            "price": 6.50,
            "resteraunt_id": 1
        },
        {
            "image_url": "https://upload.wikimedia.org/wikipedia/commons/a/a5/Garlic_Fingers.jpg",
            "product_name": "Crazy Garlic Fingers",
            "calorie_count": 350,
            "price": 3.00,
            "resteraunt_id": 1
        },
        {
            "image_url": "https://s3-media0.fl.yelpcdn.com/bphoto/IvaZ5Ua-0YsesrMRij8mYQ/348s.jpg",
            "product_name": "Lazeez On the Rocks",
            "calorie_count": 600,
            "price": 2.50,
            "resteraunt_id": 1
        },
        {
            "image_url": "https://media-cdn.tripadvisor.com/media/photo-s/10/fc/74/89/lazeez-shawarma.jpg",
            "product_name": "Lazeez On the Sticks",
            "calorie_count": 1200,
            "price": 12.99,
            "resteraunt_id": 1
        },
        {
            "image_url": "https://nypost.com/wp-content/uploads/sites/2/2021/10/ebrahim-mohamed-bodega-chopped-cheese-bacon.jpg?quality=90&strip=all",
            "product_name": "Grilled Sandwich the Ocky Way",
            "calorie_count": 1025,
            "price": 8.75,
            "resteraunt_id": 1
        },
        {
            "image_url": "https://www.seriouseats.com/thmb/-_mziT2tl0F63I4kfji4S6bE-cA=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/__opt__aboutcom__coeus__resources__content_migration__serious_eats__seriouseats.com__2018__10__20181015-state-of-slice-delmar-clay-williams-2de043fa5a0d4475b6c567e4a974b13b.jpg",
            "product_name": "New York Slice of Pizza",
            "calorie_count": 460,
            "price": 6.50,
            "resteraunt_id": 1
        },  
        {
            "image_url": "data:image/jpeg;base64,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",
            "product_name": "Tim Hortons Ice Coffee",
            "calorie_count": 850,
            "price": 6.75,
            "resteraunt_id": 1
        },
        {
            "image_url": "https://images.ctfassets.net/xlzobf9ybr6d/547z0wFkvEl4r8YMRyTxrE/724ff0e94b655e59d850660eb0811e94/Home_Hero_Mobile_Cover.jpg",
            "product_name": "Nando's Spicy Chicken",
            "calorie_count": 600,
            "price": 1.25,
            "resteraunt_id": 1
        },
                {
            "image_url": "https://ca-times.brightspotcdn.com/dims4/default/358cfd4/2147483647/strip/true/crop/2000x1333+0+9/resize/2000x1333!/quality/80/?url=https%3A%2F%2Fcalifornia-times-brightspot.s3.amazonaws.com%2Fb6%2F97%2Faadf0c6b487b839e2dfad29ed255%2F20230130-fo-costco-vs-sams-club-hot-dog-combo-these-are-costco-dogs-lwp-01.jpg",
            "product_name": "Costco Hotdog",
            "calorie_count": 900,
            "price": 6.50,
            "resteraunt_id": 1
        },
        {
            "image_url": "https://soranews24.com/wp-content/uploads/sites/3/2022/09/Japanese-sweet-food-taiyaki-pancake-Golden-10-Won-Bread-cheese-yen-coin-Shibuya-Tokyo-Don-Quijote-news-photos-10.jpeg",
            "product_name": "10 Yen Cheese Coin",
            "calorie_count": 350,
            "price": 3.00,
            "resteraunt_id": 1
        },
        {
            "image_url": "https://www.therecord.com/content/dam/localcommunities/waterloo_chronicle/opinion/2022/05/20/experience-excellent-eggplant-parm-and-more-from-waterloo-region-food-purveyor/10628837_Baked_eggplant_parm.jpg",
            "product_name": "Waterloo Star Eggplant",
            "calorie_count": 600,
            "price": 2.50,
            "resteraunt_id": 1
        },
        {
            "image_url": "https://images.squarespace-cdn.com/content/v1/5d67c72dba6a1a00013067c9/1568037892737-TH4PM2UDDSP7VY8RS4II/MelsDiner2019TTG-590.jpg?format=1500w",
            "product_name": "Mel's Breakfast",
            "calorie_count": 1200,
            "price": 12.99,
            "resteraunt_id": 1
        },
        {
            "image_url": "https://www.platingsandpairings.com/wp-content/uploads/2022/11/lobster-ravioli-sauce-recipe-5-scaled.jpg",
            "product_name": "Scaddabush Ravioli",
            "calorie_count": 1025,
            "price": 8.75,
            "resteraunt_id": 1
        },
        {
            "image_url": "https://media.npr.org/assets/img/2022/12/02/gettyimages-1097796342-943eb8db689d4ab655679b743a5053f39627e301-s1100-c50.jpg",
            "product_name": "Literal Dirt",
            "calorie_count": 460,
            "price": 6.50,
            "resteraunt_id": 1
        },  
        {
            "image_url": "https://images.chickadvisor.com/item/37753/original/233eb8f1f5e44a640ba67b4eab6fdcc7.jpg",
            "product_name": "Chocolate Frosty",
            "calorie_count": 850,
            "price": 6.75,
            "resteraunt_id": 1
        },
        {
            "image_url": "https://cloudfront-us-east-1.images.arcpublishing.com/advancelocal/ECJ6ZJUV5VEUHDGSLK2AZJU7UM.jpg",
            "product_name": "Strawberry Frosty",
            "calorie_count": 600,
            "price": 1.25,
            "resteraunt_id": 1
        }
]

tags = [
    {
        "resteraunt_id": 1,
        "tag_name": "Most Popular"
    },
    {
        "resteraunt_id": 1,
        "tag_name": "Picked for You"
    },
    {
        "resteraunt_id": 1,
        "tag_name": "Limited Time Offers"
    },
    {
        "resteraunt_id": 1,
        "tag_name": "Combos"
    }
]

user_data = {"username": "admin", "password": "password123", "email": "admin@gmail.com"}
request = requests.post("http://127.0.0.1:5000/auth/add-user", data=user_data)
print(request.text)

request = requests.post("http://localhost:5000/auth/login", data=user_data)
if request.status_code == 200:
    token = request.json()["token"]
    print("Token: " + token)
else:
    token = ""
    print(request.text)
headers = {
    "Authorization": token
}

for resteraunt in resteraunts:
    request = requests.post("http://127.0.0.1:5000/resteraunt/add", data=resteraunt, headers=headers)
    print(request.text)

for item in items:
    request = requests.post("http://127.0.0.1:5000/product/add", data=item, headers=headers)
    print(request.text)

for tag in tags:
    request = requests.post("http://127.0.0.1:5000/tag/add", data=tag, headers=headers)
    print(request.text)

for i in range(1, 25):
    if (i % 2 == 0):
        obj = {"product_id": i, "tag_id": 1}
        request = requests.post("http://127.0.0.1:5000/product-tags/add", data=obj, headers=headers)
        print(request.text)
    if (i % 3 == 0):
        obj = {"product_id": i, "tag_id": 2}
        request = requests.post("http://127.0.0.1:5000/product-tags/add", data=obj, headers=headers)
        print(request.text)
    if (i % 4 == 0):
        obj = {"product_id": i, "tag_id": 3}
        request = requests.post("http://127.0.0.1:5000/product-tags/add", data=obj, headers=headers)
        print(request.text)
    if (i % 5 == 0):
        obj = {"product_id": i, "tag_id": 4}
        request = requests.post("http://127.0.0.1:5000/product-tags/add", data=obj, headers=headers)
        print(request.text)
    
