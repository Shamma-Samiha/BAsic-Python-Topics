FlowerInfo = {
    "Rose": {
        "Colour": "Red",
        "Scientific name": "Rosa",
        "Price": "15 taka"
    },
    "Sunflower": {
        "Colour": "Yellow",
        "Scientific name": "Helianthus annuus",
        "Price": "50 taka"
    },
    "Water Lily": {
        "Colour": "White",
        "Scientific name": "Nymphaeaceae",
        "Price": "35 taka"
    }
}

#print (FlowerInfo)
#print (FlowerInfo["Sunflower"])
#print (FlowerInfo["Sunflower"]["Scientific name"])
x= (FlowerInfo.get("Water Lily"))
#print(x)
y= (FlowerInfo.keys())
#print(y)
z= (FlowerInfo.values())
#print(z)
#Looping in dictionary
"""for x in FlowerInfo:
    print(x)"""
for c in FlowerInfo.items():
    print(c)