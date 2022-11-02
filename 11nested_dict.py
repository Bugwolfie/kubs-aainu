myfamily = {
  "child1" : {
    "name" : "puchu",
    "birth_year" : 2023,
    "breed" : "golden retriever"
  },
  "child2" : {
    "name" : "coco",
    "birth_year" : 2017,
    "breed" : "Indian pariah"
  },
  "child3" : {
    "name" : "pixel",
    "birth_year" : 2012,
    "breed" : "rottweilar"
  }
}
print(myfamily)
print(myfamily.keys())
for x in myfamily:
    print(x)
futurefamily = myfamily.copy()
print(futurefamily)
for keysss, valuesss in myfamily.items():
    print(keysss, valuesss)
print(myfamily.get("child3"))