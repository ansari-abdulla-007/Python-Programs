#loop through the kyes and values of all nestes dictionaries.
software={
    "mansi":{
        "name":"panchal",
        "age":17,
    },
    "muskan":{
        "name":"panchal",
        "age":19,
    },
}
for x,obj in software.items(): #items se key and values dono...
    print(x)
    for y in obj:
        print(y + ":",obj[y])