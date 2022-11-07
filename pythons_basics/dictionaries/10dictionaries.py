inuiz =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1969
}
x = inuiz["year"]
print(x)

inuiz["year"] = 2018  #to change some value
inuiz["color"] = "purple"
inuiz.pop("model")

print(inuiz)
pens = {"maths" : 98,
"science" : 99,
"english" : 100,
"rain" : [99,99,99,99,"brilliant"]}
print(pens["rain"])
print(pens)
print(type(pens))
print(list(pens.keys()))
print(pens.values())
print(type(list(pens.keys())))
print(pens.items())
# dict methods
