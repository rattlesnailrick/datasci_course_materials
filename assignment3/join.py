import MapReduce
import sys

"""
Word Count Example in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # key: order_id (join by)
    # value: "label" followed by
    value = record      # all values *
    key = record[1]     # join by key "order id"
    mr.emit_intermediate(key, value)

def reducer(key, list_of_values):
    # key: order_id
    # value: list of occurrence counts
    for item in list_of_values:
        if item[0] == "order":
            for item2 in list_of_values:
                if item2[0] == "line_item":
                    mr.emit(item + item2)

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
