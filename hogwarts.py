students=[
    {
        "name" : "Hermione",
        "house" : "Gryfindore",
        "patronous" : "Otter"
     },
     {
       "name" : "Harry",
       "house" : "Gryfindore",
       "patronous" : "Stag"
     },
     {
      "name" : "Ron",
      "house" : "Gryfindore",
      "patronous" : "Jack Russel terrier"
      },
      {
      "name" : "draco",
      "house" : "slytherine",
      "patronous" : None,
      }

]

for student in students:
    print(student["name"], student["house"], student["patronous"] , sep=", ")
