import csv
airport_codes = open("/home/rohit/Downloads/airport-codes.csv")
airport_codes_reader = csv.reader(airport_codes)

codes_dict = {}

for code in airport_codes_reader:
    data = {"city":code[9],"latitude":code[3],"longitude":code[4]}
    iata = code[11]

    if iata!="iata_code" and len(iata)>2:
        codes_dict[code[11]]=data

#print(codes_dict)

airport_codes_2 = open("/home/rohit/Hackathons/DataDriven/add_airport_codes.csv")
airport_codes_reader_2 = csv.reader(airport_codes_2)

for code in airport_codes_reader_2:
    aircode = code[0]
    #print(aircode)
    city = code[1]
    country = code[2]
    codes_dict[aircode] = {"city":city,"country":country,"latitude":code[3],"longitude":code[4]}

unique_codes = open("/home/rohit/PycharmProjects/Hackathon/test/code.csv")
unique_codes_reader = csv.reader(unique_codes)

ucode_dict = {}
#print(codes_dict.keys())
for ucode in unique_codes_reader:
    if len(ucode)>0:
        if ucode[0] in codes_dict.keys():
            ucode_dict[ucode[0]] = codes_dict[ucode[0]]
        else:
            print(ucode[0])

print(ucode_dict)
'''
for code in ucode_dict:
    dict = ucode_dict[code]
    if "country" not in dict:
        print(code)'''


skyscanner_airtraffic = open("/home/rohit/Downloads/in.c-skyscanner.au-6m.csv")
air_traffic_reader = csv.reader(skyscanner_airtraffic)


with open('syscannerdata_6m.csv', 'w') as csvfile:
    fieldnames = [
        "ID",
        "travel_date", 
        "originairport", 
        "origincitycode", 
        "origincityname", 
        "origincountryname", 
        "origincountry", 
        "destinationairport", 
        "destinationcitycode", 
        "destinationcityname", 
        "destinationcountryname", 
        "destinationcountry", 
        "usercity", 
        "userregion", 
        "usercountry", 
        "carriercode", 
        "dayslengthofstay", 
        "trip_type", 
        "priceusd", 
        "seats"
        ]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    counter = 0 #primary key

    for row in air_traffic_reader:
        counter+=1
        origincode = row[2]
        destinationcode = row[5]
        origincity=""
        destinationcity=""
        origincountry = ""
        destcountry= ""

        if origincode in ucode_dict:
            dict = ucode_dict[origincode]
            origincity = dict["city"]
            if "country" in dict:
                origincountry = ucode_dict[origincode]["country"]

        if destinationcode in ucode_dict:
            dict = ucode_dict[destinationcode]
            destinationcity = dict["city"]
            if "country" in dict:
                destcountry = ucode_dict[destinationcode]["country"]

        writer.writerow(
            {"ID":counter,
             "travel_date":row[0],
             "originairport":row[1],
             "origincitycode":origincode,
             "origincityname":origincity,
             "origincountryname":origincountry,
             "origincountry":row[3],
             "destinationairport":row[4],
             "destinationcitycode":row[5],
             "destinationcityname":destinationcity,
             "destinationcountryname":destcountry,
             "destinationcountry":row[6],
             "usercity":row[7],
             "userregion":row[8],
             "usercountry":row[9],
             "carriercode":row[10],
             "dayslengthofstay":row[11],
             "trip_type":row[12],
             "priceusd":row[13],
             "seats":row[14]})




