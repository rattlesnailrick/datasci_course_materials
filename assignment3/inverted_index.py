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
    words = record[1].split()
    for key in words:
        mr.emit_intermediate(key, record[0])

def reducer(key, list_of_values):
    # key: word
    # value: list of occurrence counts
    total = set()
    for v in list_of_values:
        total.add(v)
    total = list(total)
    mr.emit((key, total))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
