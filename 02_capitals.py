import os
states_capitals = {
        "Alabama":"Montgomery",
        "Alaska":"Juneau",
        "Arizona":"Phoenix",
        "Arkansas":"Little Rock",
        "California":"Sacramento",
        "Colorado":"Denver",
        "Conneticut":"Hartford",
        "Delaware":"Dover",
        "Florida":"Tallahassee",
        "Georgia":"Atlanta",
        "Hawaii":"Honolulu",
        "Idaho":"Boise",
        "Illinois":"Springfield",
        "Indiana":"Indianapolis",
        "Iowa":"Des Moines",
        "Kansas":"Topeka",
        "Kentucky":"Frankfort",
        "Lousiania":"Baton Rouge",
        "Maine":"Augusta",
        "Maryland":"Annapolis",
        "Massachusetts":"Boston",
        "Michigan":"Lansing",
        "Minnesota":"Saint Paul",
        "Mississippi":"Jackson",
        "Missouri":"Jefferson City",
        "Montana":"Helena",
        "Nebraska":"Lincoln",
        "Nevada":"Carson City",
        "New Hampshire":"Concord",
        "New Jersey":"Trenton",
        "New Mexico":"Santa Fe",
        "New York":"Abany",
        "North Carolina":"Raleigh",
        "North Dakota":"Bismark",
        "Ohio":"Columbus",
        "Oklahoma":"Okalahoma City",
        "Oregon":"Salem",
        "Pennsylvania":"Harrisburg",
        "Rhode Island":"Providence",
        "South Carolina":"Columbia",
        "South Dakota":"Pierre",
        "Tennessee":"Nashville",
        "Texas":"Austin",
        "Utah":"Salt Lake City",
        "Vermont":"Montpelier",
        "Virginia":"Richmond",
        "Washington":"Olympia",
        "West Virgnia":"Charleston",
        "Wisconsin": "Madison",
        "Wyoming":"Cheyenne",
}

while True:
    key_list = list(states_capitals.keys())
    val_list = list(states_capitals.values())
    x = input("Ready: ")
    if x in list(states_capitals.values()):
        print(key_list[val_list.index(x)])
    if x in list(states_capitals.keys()):
        print(states_capitals[x])
    if x not in states_capitals.values() and x not in states_capitals.keys():
        if x != "Done":
            print("Nil")
    if x == "Done":
        os._exit(0)
        

