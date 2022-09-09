import uuid
data = {
            'brewery_id' : [10325, 10325],
            'brewery_name' : ['Vecchio Birralo', 'Vecchio Birralo'],
            'beer_style' : ['Hefeweizen', 'English Strong Ale'],
            'beer_name' : ['Sausa Weizen','Red Moon'] 
        }
print("Srineeta  1MJ19CS163")
print("Mac address: ", hex(uuid.getnode()))
for x, y in data.items():
    print(x,":",y)