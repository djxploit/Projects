from clarifai.rest import ClarifaiApp
app = ClarifaiApp(api_key="dae1929dd4bd4c17b7d2dba889589226")
'''model = app.models.get("food-items-v1.0")
response = model.predict_by_url("http://knowledgeoverflow.com/wp-content/uploads/2013/03/food_photography_burger_by_masterdev777-d3h1ryk.jpg")
print response
for temp in response['outputs']:
    print temp['data']
    for item in temp['data']['concepts']:
        print item
'''
image = []
#image.append('http://3.bp.blogspot.com/-AjEJ_0_IzK8/VcnOyGuGV1I/AAAAAAAAApA/d73amqeyTZk/s1600/DIRTY.jpg')
image.append("http://static1.bigstockphoto.com/thumbs/3/0/5/large2/5037500.jpg")
image.append('https://betterdelhi.files.wordpress.com/2013/12/wpid-20131206_085602.jpg')
image.append('http://educationwithfun.com/pluginfile.php/727/mod_page/intro/sw.PNG')
image.append('http://media2.intoday.in/indiatoday/images/stories/wrestling647_051217032902.jpg')
image.append('https://i.onthe.io/vllkyt6hapfprb3kd.0070e148.jpg')
image.append('https://i.onthe.io/vllkyt3uaert3icie.35797ddf.jpg')
image.append('http://4.bp.blogspot.com/-qFThVkB17pk/VjhWzhSqaDI/AAAAAAAAM7o/xzrJJC4ubeI/s1600/20150823_114620.jpg')
image.append('https://www.telegraphindia.com/1160921/images/21RanHarmu1.jpg')
ima = 'https://us.123rf.com/450wm/sdimitrov/sdimitrov1502/sdimitrov150200005/36488660-illegal-landfill-in-an-asian-city.jpg?ver=6'

#for temp in image:
 #   app.inputs.create_image_from_url(url = temp,concepts=['dirt'])
#models = app.models.create('dirty',concepts=['dirt'])
#response = models.predict_by_url("http://media2.intoday.in/indiatoday/images/stories/wrestling647_051217032902.jpg")
#response = app.inputs.search_by_predicted_concepts(concept='people')
#print response
