import pymysql
counter = 1
conn = pymysql.connect(host='127.0.0.1', user='fadi', password='fadiadmin', db='newdb')

data_file = open("C:\json\pkgnames.txt", "r")

for line in data_file:
##[:-2] to remove \n
    cursor = conn.cursor()
    pkgname, genre , reviewsavg, price, downloads, andversion = line[:-2].split('\t')
    reviewsavg = float(reviewsavg)
    downloads = downloads.strip()
    if price =="0":
        price = float(price)
    else:
        price = float(price.split('$')[1])
    
    sql = "insert into allapps (appno, packagename, genre, reviewsaverage, price, downloads, androidversion) VALUES(%d, '%s', '%s', '%s', '%s', '%s', '%s')" %(counter, pkgname, genre , reviewsavg, price, downloads, andversion)
    cursor.execute(sql)
    conn.commit()
    counter+=1
conn.close()    

  
    
##
##a = conn.cursor()
##
####sql = 'SELECT * from `applications`;'
####
######a.execute(sql)
####countrow= a.execute(sql)
####print("Number of rows: ", countrow)
####data= a.fetchone()
####print(data)
##

## 
##number_of_rows = cursor.execute(sql)
##db.commit()
## 
##db.close()
