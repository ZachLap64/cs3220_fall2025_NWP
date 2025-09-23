import json
import io
import os
import Dynasty
import GameOfThronesGraph

file_name = "data/game-of-thrones-characters-groups.json"
path="data"

json_files = [os.path.join(root, name) 
              for root, dirs, files in os.walk(path) 
              for name in files 
              if name.endswith((".json"))] #If we needed to read several files extensions: if name.endswith((".ext1", ".ext2"))

print('Number of JSON files ready to be loaded: ' + str(len(json_files)))

print('Path to the first file: '+json_files[0])

#Open the file using the name of the json file witn open() function
#Read the json file using load() and put the json data into a variable.
with open(json_files[0]) as f:
   json_data = json.load(f)
   #print(json_data)
   #print(json_data.keys)

for data in json_data['groups']:
  house=Dynasty.Dynasty(data['name'])
  for character in data['characters']:
    house.append(character)
  print(house)
  print("Our members:")
  for person in house:
    print(person)
  print(f"We have {house.getStrength()} family members!!!")

corpusData=json_data['groups']
GameOfThronesHouses=GameOfThronesGraph.GameOfThronesGraph(corpusData)
print(GameOfThronesHouses.houses)
if "Stark" in GameOfThronesHouses:
    print("stark is here!!!")
for house in GameOfThronesHouses:
    print(f"This is a House of {house}!")