__author__ = 'ylucas'

import pandas
import re
from sets import Set
import numpy as np


def update_file(file):
    titanic = pandas.read_csv(file + ".csv")
    titles = []
    alias = []
    cabin_floor = []
    cabin_number = []
    ticket_type = []
    age_mean = np.mean(titanic["Age"])
    titanic["Cabin"] = titanic["Cabin"].fillna("U")

    for index, row in titanic.iterrows():

        name = row["Name"]
        title = re.split("\.",re.split(",",name)[1])[0].strip().title()
        titles.append(title)

        if "\"" in row["Name"] or "(" in row["Name"]:
            alias.append("1")
        else:
            alias.append("0")

        cabin = row["Cabin"]
        cabins = re.split(" ",row["Cabin"])

        if len(cabins) == 0:
            cabin_floor.append("U")
            cabin_number.append("0")
        elif len(cabins) == 1:
            cabin_floor.append(cabin[0])
            if (cabin == "U") or (cabin[1:] == ""):
                cabin_number.append("0")
            else:
                cabin_number.append(cabin[1:])
        elif len(cabins) == 2:
            if len(cabins[0]) == 1:
                cabin_floor.append(cabins[0]+cabins[1][0])
                cabin_number.append(cabins[1][1:])
            else:
                cabin_floor.append(cabin[0])
                cabin_number.append(cabins[0][1:])
        elif len(cabins) == 3:
            cabin_floor.append(cabin[0])
            cabin_number.append(cabins[0][1:])
        else:
            cabin_floor.append(cabin[0])
            cabin_number.append(cabins[0][1:])

        ticket = row["Ticket"].strip()

        try:
            ticket += 1
        except TypeError:
            ticket_type.append(re.split(" ",ticket)[0])



    titanic.insert(5,"Title",titles)
    titanic.insert(6,"Alias",alias)
    titanic.insert(10,"Fam", titanic["SibSp"] + titanic["Parch"])
    titanic.insert(13,"Cabin_Floor", cabin_floor)
    titanic.insert(14,"Cabin_Nb", cabin_number)
    titanic.insert(15,"Ticket_Type",ticket_type)
    titanic["Age"] = titanic["Age"].fillna(age_mean)

    titanic.to_csv(file + "_updated.csv")

update_file("train")
update_file("test")