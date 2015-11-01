import MapReduce
import sys

"""
Word Count Example in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # key: document identifier
    # value: document contents
    key = record[0]
    value = ["likes", record[1]]
    mr.emit_intermediate(key, value)
    key = record[1]
    value = ["is_liked", record[0]]
    mr.emit_intermediate(key, value)

def reducer(key, list_of_values):
    # key: word
    # value: list of occurrence counts
    likes = set()
    is_liked = set()

    for v in list_of_values:
        if v[0] == "likes":
            likes.add(v[1])
        elif v[0] == "is_liked":
            is_liked.add(v[1])

    for asym in is_liked - likes:
        mr.emit((asym, key))
        mr.emit((key, asym))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
