import pymysql

dbcon=pymysql.connect(host='localhost',user='root',passwd='',db='scrap')
cursor=dbcon.cursor()
print("db connected")

f = open("C:\\Users\\kunna\\PycharmProjects\\coursera\\delhihospitals.txt", "r")
hosp=list()
for x in f:
    hosp.append(x)
data=""
for i in range(len(hosp)):
    data=hosp[i]
    if(i!=len(hosp)-1):
        data = data[:len(data) - 1]
    query="insert into delhihospitals values('"+data+"');"
    cursor.execute(query)
    dbcon.commit()
    print(data)



