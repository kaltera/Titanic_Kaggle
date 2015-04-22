__author__ = 'ylucas'

import pandas
import re
from sets import Set

titanic = pandas.read_csv("train.csv")
titles = []
alias = []

for index, row in titanic.iterrows():
    name = row["Name"]
    title = re.split("\.",re.split(",",name)[1])[0].strip().title()
    titles.append(title)

    if "\"" in row["Name"] or "(" in row["Name"]:
        alias.append("1")
    else:
        alias.append("0")


titanic.insert(5,"Title",titles)
titanic.insert(6,"Alias",alias)
titanic.insert(10,"Fam", titanic["SibSp"] + titanic["Parch"])

print titanic