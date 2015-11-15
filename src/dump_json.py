
import sqlite3

conn = sqlite3.connect('./data/glass.sqlite3')
c = conn.cursor()
s = "select * from t_glass_spec"
c.execute(s)
fetched = c.fetchall()

with open('./data/glass_spec.json', 'w') as f:
    f.write('[\n')
    for i in range(len(fetched)):
        row = fetched[i]
        ior = "["
        iors = row[4:65]
        for j in range(len(iors)):
            ior += "{0}".format(iors[j])
            if j != len(iors)-1:
                ior += ", "
            else:
                ior += "]"

        trans = "["
        transs = row[65:]
        for j in range(len(transs)):
            trans += "{0}".format(transs[j])
            if j != len(transs)-1:
                trans += ", "
            else:
                trans += "]"

        f.write("\t{")
        f.write("\"{0}\":{1}, ".format("id", row[0]))
        f.write("\"{0}\":\"{1}\", ".format("maker", row[1]))
        f.write("\"{0}\":\"{1}\", ".format("name", row[2].strip())) #><
        f.write("\"{0}\":{1}, ".format("code", row[3]))
        f.write("\"{0}\":{1}, ".format("ior", ior))
        f.write("\"{0}\":{1} ".format("transparency", trans))
        f.write("}")
        if i != len(fetched)-1:
            f.write(",\n")
        else:
            f.write("\n")
    f.write(']\n')
