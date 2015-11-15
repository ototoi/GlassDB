import sqlite3

id_origin = 40000
maker = "schott"

conn = sqlite3.connect('./data/glass.sqlite3')
c = conn.cursor()
s = "select * from t_glass_spec_{0}3".format(maker)
c.execute(s)
fetched = c.fetchall()

for i in range(len(fetched)):
    row = fetched[i]
    #print(row)
    code = row[1]
    name = row[2]

    values = ""
    values += "{0}, ".format(id_origin+i)          #id
    values += "\"{0}\", ".format(maker)      #maker
    values += "\"{0}\", ".format(name)       #name
    values += "{0}, ".format(code)       #code

    ll = row[3:]
    for j in range(len(ll)):
        values += str(ll[j])
        if (j != len(ll)-1):
            values += ", "

    s = "insert into t_glass_spec VALUES({0})".format(values)
    c.execute(s)

conn.commit()
