__author__ = 'ylucas'

import pandas
import re
from sets import Set

titanic = pandas.read_csv("train.csv")
titles = []

for index, row in titanic.iterrows():
    name = row["Name"]
    title = re.split("\.",re.split(",",name)[1])[0].strip().title()
    titles.append(title)

titanic.insert(4,"Title",titles)

print titanic