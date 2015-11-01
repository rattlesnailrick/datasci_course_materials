import MapReduce
import sys

"""
Word Count Example in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line


# c_ik = sum_j=1_m (a_ij * b_jk)

def mapper(record):
    # key: document identifier
    # value: document contents

    #MATRIX DIMENSIONS:
    # assumed 10x10

    m = 10

    if record[0] == "a":
        for i in range(m):
            key = (record[1], i)

            mr.emit_intermediate(key, record)
    elif record[0] == "b":
        for i in range(m):
            key = (i, record[2])
            mr.emit_intermediate(key, record)

def reducer(key, list_of_values):
    # key: "cell"
    # value: "data"
    total = 0
    #if key[0] == 0 and key[1] == 0:
    #    for row in list_of_values:
    #        print row
    for first_value in list_of_values:
        if first_value[0] == "a":
            for second_value in list_of_values:
                if second_value[0] == "b":
                    if first_value[2] == second_value[1]:
                        total += first_value[3] * second_value[3]
    if total > 0:
        mr.emit((key[0], key[1], total))


# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
