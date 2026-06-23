#it is unordered , mutable, indexed
d={} # empty dictornary
marks = {
    "Masum":100,
    "Rafik":99,
    "shafik":98
}


print(marks)

print(marks["Masum"])

marks["Masum"]=99.5

print(marks["Masum"])


keys=marks.keys()

print(keys)

values=marks.values()

print(values)

print(len(values))


print(len(marks))

marks.popitem()

print(marks)

marks.update({"Masum":98, "kalakar":100})

print(marks)

masums_marks=marks.get("Masum")  # ekhane jodi "Masum" er kono key na thak trpro error dibe na

print(masums_marks)