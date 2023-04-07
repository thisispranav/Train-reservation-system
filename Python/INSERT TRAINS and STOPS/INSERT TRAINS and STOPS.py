import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='1234',
    database='TRS'
)

mycursor = mydb.cursor(buffered=True)

def train():
    tno=[1,2,3,4,5,6,7,8,9,10,11,12]
    tnames=["Double Decker","Brindavan Express","Shadapti Express","Sangamitra SF express","Bengaluru Mail","Passenger Memu 1","Guruvayur Express","Ananthapuri Express","Thiruvananthapuram Central Mail","Passenger Memu 2",'Taliban Express','Fidel Castro Express']
    troutes=["ctobe","ctobe","ctobe","ctobe","ctobp","ctobp","ctote","ctote","ctotp","ctotp","ctote","ctote"]
    times=[4,5,6,7,8,9,4,5,6,7,8,9]
    time2=[16,17,18,19,20,21,16,17,18,19,20,21]
    a=0
    while a<len(tno):
        sql=f"insert into train values({tno[a]},'{tnames[a]}','{troutes[a]}','{times[a]}','{time2[a]}')"
        mycursor.execute(sql)
        mydb.commit()   
        a+=1


def ctob():
    stops=["MGR Chennai Central","Perambur","Arakkonam Junction","Sholaingnallur","Walajah Road Junction","Katpadi Junction","Gudiyatham","Ambur","Vaniyambadi","Jolarpettai Junction","Patchur","Malanur","Kuppam","Gudupalli","Kamasamudram","Bangarpet Junction","Tyakal","Malur","Devangonthi","White Field","Krishnarajapuram","Bengaluru East","Bengaluru Cantt.","KSR Bengaluru City junction"]
    eorp=['e', 'p', 'e', 'p', 'p', 'e', 'p', 'e', 'e', 'e', 'p', 'p', 'e', 'p', 'p', 'e', 'p', 'p', 'p', 'p', 'e', 'p', 'e', 'e']
    a=0
    for i in range(len(stops)):
        sql=f"insert into ctob values('{stops[a]}','{eorp[a]}')"
        mycursor.execute(sql)
        mydb.commit()
        a+=1

def ctot():
    stops=["Chennai Central (MAS)", "Arakkonam (AJJ)", "Katpadi Junction (KPD)", "Vaniyambadi (VN)", "Jolarpettai (JTJ)", "Salem Junction (SA)", "Erode Junction (ED)", "Tiruppur (TUP)", "Coimbatore Junction (CBE)", "Palakkad (PGT)", "Thrisur (TCR)", "Ernakulam Town (ERN)", "Kottayam (KTYM)", "Changanaseri (CGY)", "Tiruvalla (TRVL)", "Chengannur (CNGR)", "Mavelikara (MVLK)", "Kayankulam Junction (KYJ)", "Kollam Junction (QLN)", "Varkala (VAK)", "Trivandrum Cntl (TVC)"]
    eorp=['e', 'p', 'p', 'p', 'p', 'e', 'e', 'p', 'e', 'e', 'p', 'e', 'e', 'p', 'p', 'p', 'p', 'p', 'e', 'p', 'e']
    a=0
    for i in range(len(stops)):
        sql=f"insert into ctot values('{stops[a]}','{eorp[a]}')"
        mycursor.execute(sql)
        mydb.commit()
        a+=1   

train()
ctob()
ctot()