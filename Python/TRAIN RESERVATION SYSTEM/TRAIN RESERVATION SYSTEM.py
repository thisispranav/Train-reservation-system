import datetime
import random
import mysql.connector
import maskpass

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='1234',
    database='TRS'
)

mycursor = mydb.cursor(buffered=True)

today = datetime.date.today()
DAY, MONTH, YEAR = today.day, today.month, today.year
today = f"{YEAR}-{MONTH}-{DAY}"
today10 = f"{YEAR+10}-{MONTH}-{DAY}"
today100 = f"{YEAR-100}-{MONTH}-{DAY}"


def id():
    sql = 'SELECT MAX(ID) FROM INFO'
    mycursor.execute(sql)
    a = mycursor.fetchall()
    if a[0][0] == None:
        return 0
    else:
        return a[0][0]


def name():
    while True:
        Name = input('Name: ').upper()
        if Name != 'HOME()':
            if Name.isalpha() and len(Name) <= 25:
                return Name
            elif len(Name) >= 25:
                print('The character Exits 25 !!TRY AGAIN!!')
            else:
                print('Invalid Name !!TRY AGAIN!!')
        else:
            break


def dat(k):
    def format(x):
        return (f"{x[2]}-{x[1]}-{x[0]}")

    def check(x):
        j = format(x)
        try:
            mycursor.execute(f"insert into date values('{j}')")
            mycursor.execute(f"delete from date  where date='{j}'")
            mydb.commit()
            return True
        except:
            return False

    def after(x):
        if x >= today and x < today10:
            return True
        else:
            return False

    def before(x):
        if x <= today and x > today100:
            return True
        else:
            False

    def format1(x):
        while True:
            dat = x
            if dat.count('/') == 2:
                s = dat.split('/')
                if len(s) == 3:
                    return "Good"
                else:
                    return False
            elif dat.lower() == "home()":
                return "home()"
            else:
                return "Bad"
    while True:
        print()
        v = input(f"{k}(dd/mm/yy) :")
        if format1(v).lower() == "home()":
            return
        elif format1(v) == "Good":
            N = v.split('/')
            print(N)
            if check(N):
                if k == "Date of birth":
                    if before(f"{N[2]}-{N[1]}-{N[0]}"):
                        return N
                    else:
                        print(f"Enter a valid date the date should be from {DAY}-{MONTH}-{YEAR-100} to {DAY}-{MONTH}-{YEAR}")
                else:
                    if after(f"{N[2]}-{N[1]}-{N[0]}"):
                        return N
                    else:
                        print(f"Enter a valid date. The date should be from {DAY}-{MONTH}-{YEAR} to {DAY}-{MONTH}-{YEAR+10}")
            else:
                print(f"Enter a valid date in (dd/mm/yy) format")
        else:
            print("Invalid input Try again")
            continue


def age():
    x = dat('Date of birth')
    if x != None:
        a, b, c = x
        d, m, y = int(a), int(b), int(c)
        today = datetime.date.today()
        td, tm, ty = today.day, today.month, today.year
        age = ty-y
        if m == tm:
            if d <= td:
                return age
            else:
                return age-1
        elif m > tm:
            return age-1
        else:
            return age


def check18(x):
    if x >= 18:
        return True
    else:
        return False


def gen():
    s = ['M', 'F', 'N']
    while True:
        print("""
        --GENDER--
        M=Male
        F=Female
        N=Not to mention
        """)
        Gen = input(f'Gender: ').upper()
        if Gen != 'HOME()':
            if Gen.isalpha():
                l = len(Gen)
                if l == 1 and Gen in s:
                    return Gen
                else:
                    print('invalid Gender !Try entering M or F or N')
            else:
                print('invalid Gender !Try entering M or F or N')
        else:
            break


def mobno():
    while True:
        print()
        no = input('Mobile number: ')
        if no.lower() != "home()":
            if no.isnumeric():
                c = len(no)
                if c == 10:
                    no = int(no)
                    return no
                else:
                    print('Number is less or more than 10 !!TRY AGAIN!!')
            else:
                print('Invalid Number !!TRY AGAIN!!')
        else:
            break


def checkmobno1():  # create
    N = True
    while N:
        no = mobno()
        if no == None:
            N = False
            return False
        else:
            sql = f"select * from info where MOBNO = {no}"
            mycursor.execute(sql)
            check = mycursor.fetchall()
            if len(check) == 0:
                return no
            else:
                print('Number exists already')
                while True:
                    print()
                    key = input(
                        'Press 1 to enter new number or enter home() to exit : ')
                    if key == "1":
                        N = True
                        break
                    elif key.lower() == "home()":
                        N = False
                        return False
                    else:
                        print('Inavlid input !try again!')


def checkmobno2():  # login
    N = True
    while N:
        no = mobno()
        if no != None:
            sql = f"select * from info where MOBNO = {no}"
            mycursor.execute(sql)
            check = mycursor.fetchall()
            if len(check) != 0:
                return no
            else:
                print('Number does not exists')
                while True:
                    print()
                    key = input(
                        'Press 1 to enter new number or enter home() to exit : ')
                    if key == "1":
                        N = True
                        break
                    elif key.lower() == "home()":
                        N = False
                        return False
                    else:
                        print('Inavlid input !try again!')
        else:
            N = False


def email():
    c = True
    while c:
        print()
        email = (input('Email address(100char):')).lower()
        x = '@'
        y = '.com'
        if email != 'home()':
            if x and y in email and len(email) <= 100:
                e = email
                check = mycursor.execute(
                    f"select * from info where email = {e}")
                if check == None:
                    return e
                else:
                    print('Number already exists')
                    while True:
                        print()
                        key = input(
                            'Press 1 to enter new email or enter home() to exit : ')
                        if key == "1":
                            c = True
                            break
                        elif key.lower() == "home()":
                            c = False
                            break
                        else:
                            print('Inavlid input !try again!')
            else:
                print('Invalid Email address !!Try again!!')
        else:
            return False


def password():
    while True:
        passw = maskpass.askpass(prompt="Password: ", mask="*")
        if len(passw) <= 100 and len(passw) >= 6:
            return passw
        else:
            print('Invalid Password !!')
            print(
                'password should be atleast 6 characters and less than 100 charachters!!', '\n')


def logcheck():
    N = True
    while N:
        x = checkmobno2()
        mycursor.execute(f"select password from info where mobno = '{x}'")
        idk = mycursor.fetchall()
        N = True
        while N:
            if x:
                y = password()
                if y.lower() != 'home()':
                    if idk[0][0] == y:
                        return x
                    else:
                        print('Wrong password Try again', "\n")
                        print()
                        key = input(
                            'press any key to Try again or enter home() to exit: ')
                        if key.lower() == 'home()':
                            N = False
                            break
                else:
                    N = False
                    break
            else:
                N = False
                break

def login():
    x=logcheck()
    if x!=None:
        mycursor.execute(f"select ID from info where mobno = '{x}'")
        return mycursor.fetchall()[0][0]
    else:
        return


def createaccount():
    x, y = id()+1, name()
    if y != None:
        p = gen()
        if p != None:
            N = True
            while N:
                v = age()
                if v != None:
                    if check18(v):
                        z = v
                        break
                    else:
                        print('You are under 18', '\n')
                        while True:
                            print()
                            inp = input(
                                'press 1 to try another dob or enter home() to exit : ')
                            if inp.lower() == 'home()':
                                N = False
                                break
                            elif inp == '1':
                                break
                            else:
                                print('invalid input Try again', '\n')
                else:
                    N = False
            while N:
                r = checkmobno1()
                if r:
                    a = email()
                    print()
                    if a:
                        b = password()
                        if b.lower() != 'home()':
                            sql = f"insert into info value({x},'{y}','{p}',{z},{r},'{a}','{b}')"
                            mycursor.execute(sql)
                            mydb.commit()
                            print()
                            print('Account created Try loging in...')
                            N = False
                            break
                        else:
                            break
                    else:
                        break
                else:
                    break


def chooseroute():
    while True:
        print("""
        CHOOSE THE ROUTE:
        1. CHENNAI TO BANGALORE
        2. BANGLORE TO CHENNAI
        3. CHENNAI TO THIRUVANANTHAPURAM
        4. THIRUVANANTHAPURAM TO CHENNAI
        """)
        route = input('=>>')
        if route.isnumeric():
            route = int(route)
            if route == 1:
                return "ctob"
            elif route == 2:
                return "btoc"
            elif route == 3:
                return "ctot"
            elif route == 4:
                return "ttoc"
            else:
                print("Invalid input. Enter home() to exit or Try again")
        elif route.lower() == "home()":
            break
        else:
            print("Invalid input. Enter home() to exit or Try again")


def exorpass():
    while True:
        print("""
        1. PASSENGER
        2. EXPRESS
        """)
        T = input('=>>>')
        if T.isnumeric():
            T = int(T)
            if T == 1:
                return "p"
            elif T == 2:
                return "e"
            else:
                print("Invalid input. Enter home() to exit or Try again")
        elif T.lower() == "home()":
            break
        else:
            print("Invalid input. Enter home() to exit or Try again")


def choosedate():
    return (dat("Journey Date"))


def choosestops(a, k):
    t = None
    if k == "e" and a != None:
        if a == "btoc":
            mycursor.execute(f"select * from (ctob) where eorp='{k}'")
            h = mycursor.fetchall()
            h.reverse()
            t = h
            x = 0
            for i in h:
                x += 1
                print(x, ".", i[0])
        elif a == "ttoc":
            mycursor.execute(f"select * from (ctot) where eorp='{k}'")
            h = mycursor.fetchall()
            h.reverse()
            t = h
            x = 0
            for i in h:
                x += 1
                print(x, ".", i[0])
        else:
            mycursor.execute(f"select * from ({a}) where eorp='{k}'")
            h = mycursor.fetchall()
            t = h
            x = 0
            for i in h:
                x += 1
                print(x, ".", i[0])

    elif k == "p" and a != None:
        if a == "btoc":
            mycursor.execute(f"select * from (ctob)")
            h = mycursor.fetchall()
            h.reverse()
            t = h
            x = 0
            for i in h:
                x += 1
                print(x, ".", i[0])
        elif a == "ttoc":
            mycursor.execute(f"select * from (ctot)")
            h = mycursor.fetchall()
            h.reverse()
            t = h
            x = 0
            for i in h:
                x += 1
                print(x, ".", i[0])
        else:
            mycursor.execute(f"select * from ({a})")
            h = mycursor.fetchall()
            t = h
            x = 0
            for i in h:
                x += 1
                print(x, ".", i[0])
    else:
        return
    start = 0
    end = 0
    while True:
        print()
        s = input("=start=>>")
        if s.isnumeric():
            s = int(s)
            if s < len(h) and s >= 1:
                start += s
                break
            else:
                print("Try again choose correct stop")
        elif s.lower() == "home()":
            return
        else:
            print("Invalid Input Try again")
    while True:
        print()
        e = input("=end=>>")
        if e.isnumeric():
            e = int(e)
            if (e <= len(h) and e >= 1) and e > start:
                end += e
                break
            else:
                print("Try again choose correct stop")
        elif e.lower() == "home()":
            return
        else:
            print("Invalid Input Try again")
    st = (((start-1)*30)/60)
    et = ((((end-1)*30)/60))
    if int(st) < st:
        if int(et) < et:
            return [start, end, (f"{int(st)}"+":"+"30"), (f"{int(et)}"+":"+"30"), t[start-1], t[end-1]]
        else:
            return [start, end, (f"{int(st)}"+":"+"30"), (f"{int(et)}"+":"+"00"), t[start-1], t[end-1]]
    else:
        if int(et) < et:
            return [start, end, (f"{int(st)}"+":"+"00"), (f"{int(et)}"+":"+"30"), t[start-1], t[end-1]]
        else:
            return [h[start-1], h[end-1], (f"{int(st)}"+":"+"00"), (f"{int(et)}"+":"+"00"), t[start-1], t[end-1]]


def choosetrain():
    date = choosedate()
    if date == None:
        return
    route = chooseroute()
    if route == None:
        return
    eorp = exorpass()
    if eorp == None:
        return
    stops = choosestops(route, eorp)
    if stops == None:
        return
    if route == None or eorp == None:
        return
    else:
        st = stops[2].split(':')
        et = stops[3].split(':')
        tno = []
        tname = []
        time = []
        if route == "ctob" or route == "ctot":
            mycursor.execute(
                f"select tno,tname,time from train where troute='{route}{eorp}'")
            MN = 'M'
            for i in mycursor.fetchall():
                tno.append(i[0])
                tname.append(i[1])
                time.append(i[2])
        elif route == "btoc":
            j = f"ctob{eorp}"
            MN = 'N'
            mycursor.execute(
                f"select tno,tname,time2 from train where troute='{j}'")
            for i in mycursor.fetchall():
                tno.append(i[0])
                tname.append(i[1])
                time.append(i[2])
        else:
            j = f"ctot{eorp}"
            MN = 'N'
            mycursor.execute(
                f"select tno,tname,time2 from train where troute='{j}'")
            for i in mycursor.fetchall():
                tno.append(i[0])
                tname.append(i[1])
                time.append(i[2])
        if today == f"{date[2]}-{date[1]}-{date[0]}":
            trainnumber = []
            trainname = []
            time1 = []
            n = 0
            for i in time:
                if int(i)+int(st[0]) > int((datetime.datetime.now()).strftime("%H")):
                    i = int(i)
                    trainnumber.append(tno[n-1])
                    trainname.append(tname[n-1])
                    time1.append(time[n-1])
                n+1
            tno = trainnumber
            tname = trainname
            time = time1

    if tno == []:
        print("Sorry!!!!!!!!")
        print("No Trains are Available")
        return
    else:
        while True:
            a = 0
            for i in time:
                if (int(i)+int(et[0])) > 24:
                    d = int(i)+int(et[0])-24
                else:
                    d = int(i)+int(et[0])
                if (int(i)+int(st[0])) > 24:
                    k = int(i)+int(st[0])-24
                else:
                    k = int(i)+int(st[0])
                starttime = f"{k}:{st[1]}"
                endtime = f"{d}:{et[1]}"
                print(f"""
                ____________________________________________
                Train Number:{tno[a]}  
                Train Name:{tname[a]}
                {stops[4][0]}
      ({a+1})           ↓      Start time:{starttime}
                    ↓      
                    ↓      End time:{endtime}
                {stops[5][0]}
                ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ 
                """)
                a += 1
            key = input("=>")
            if key.isnumeric():
                key = int(key)
                if key <= len(tno) and key > 0:
                    return [tno[key-1], tname[key-1], date, route, stops[4][0], stops[5][0], starttime, endtime, MN]
                else:
                    print("Try again")
            elif key.lower() == "home()":
                return
            else:
                print("Try again")


def seatgenerator(tno, date, MN, no):
    mycursor.execute(
        f"select seatno from tickets where TNO={tno} and date='{date[0]}/{date[1]}/{date[2]}' and MN='{MN}'")
    booked = mycursor.fetchall()
    available = []

    def s(n):
        seats = []
        letter = chr(random.randint(ord('A'), ord('Z')))
        number = random.randint(1, 50)
        a = 0
        for i in range(n):
            seats.append(f"{letter}{number+a}")
            a += 1
        return seats
    if booked != []:
        for i in booked:
            n = i[0]
            book = n.split(",")
        booked = book
        while True:
            t = s(no)
            for i in t:
                if i in booked:
                    continue
                else:
                    available = t
                    return available
    else:
        return s(no)


def chooseseat(ID):
    train = choosetrain()
    if train == None:
        return
    while True:
        print()
        print("How many seats do you need.")
        print("You can only book 5 tickets at a time")
        seat = input("=> ")
        if seat.isnumeric():
            seat = int(seat)
            if seat < 5 and seat > 0:
                x = seatgenerator(train[0], train[2], train[-1], seat)
            else:
                print("Invalid input")
        elif seat.lower() == "home()":
            return
        else:
            print("Invalid input")
            continue
        n = (", ".join(x))
        print(f"""
        Seats alloted for you :: {n}
         """)
        mycursor.execute('select tickno from tickets')
        q = mycursor.fetchall()
        o = []
        for i in q:
            i = i[0]
            o.append(i)
        while True:
            y = random.randint(1, 9223372036854775807)
            if y in o:
                continue
            else:
                tickno = y
                break

        while True:
            confirm = input("To confirm your Tickets Click Type Confirm or home() to exit : ")
            if confirm.lower() == "confirm":
                return [ID, train[0], train[1], train[2], seat, n, train[4], train[5], f"{train[6]},{train[7]}", train[8], tickno]
            elif confirm.lower() == 'home()':
                return
            else:
                print('Invalid input')


def bookticket(ID):
    x = chooseseat(ID)
    if x != None:
        g = x[3]
        g = f"{g[0]}/{g[1]}/{g[2]}"
        mycursor.execute(
            f"insert into tickets values({x[0]},{x[1]},'{x[2]}','{g}',{x[4]},'{x[5]}','{x[6]}','{x[7]}','{x[8]}','{x[9]}',{x[10]})")
        #        return [ID,train[0],train[1],train[2],seat,n,train[4],train[5],f"{train[6]},{train[7]}",train[8],tickno]
        #        return [tno[key-1], tname[key-1], date, route, stops[4][0], stops[5][0], starttime, endtime, MN]
        mydb.commit()
        print("Your Tickets are successfully booked")
        print("To check the tickets you can go to Check Tickets Option(2)")


def checkticket(ID):
    mycursor.execute(f"select * from tickets where ID={ID}")
    x = mycursor.fetchall()
    for i in x:
        t = i[-3].split(",")
        print(f"""
        !#$@%&$&^*(*)%^$@#!@$%&^*()&^%$#@!$%&^*$%#@$#!$#%%^*$#@!#$%^%$%#@$!#$#%%$#%$@!#
        Ticket Number :{i[10]}
        Train Number :{i[0]}
        Train Name :{i[1]}
        Journey Starts :{i[6]} {t[0]}
        Journey Ends : {i[7]} {t[1]}
        Number of seats: {i[4]}
        Seat Numbers:{i[5]}
        $#%$@%^#^*&*(*^%$#%@$!@~$%$^$#@$!#$#%$^&*^%^$%#$@##)@!#$%@%^*%$%@#!$@#$%%&^*(*&
        """)
    if x==[]:
        print("No tickets have been booked")

def cancelticket(ID):
    mycursor.execute(f"select * from tickets where ID={ID}")
    x = mycursor.fetchall()
    a = 0
    for i in x:
        t = i[-3].split(",")
        print(f"""
        !#$@%&$&^*(*)%^$@#!@$%&^*()&^%$#@!$%&^*$%#@$#!$#%%^*$#@!#$%^%$%#@$!#$#%%$#%$@!#
        Ticket Number :{i[10]}
        Train Number :{i[0]}
({a+1})        Train Name :{i[1]}
        Journey Starts :{i[6]} {t[0]}
        Journey Ends : {i[7]} {t[1]}
        Number of seats: {i[4]}
        Seat Numbers:{i[5]}
        $#%$@%^#^*&*(*^%$#%@$!@~$%$^$#@$!#$#%$^&*^%^$%#$@##)@!#$%@%^*%$%@#!$@#$%%&^*(*&
        """)
        a += 1
    ticket = None
    if x!=[]:
        while True:
            key = input("=>")
            if key.isnumeric():
                key = int(key)
                if key > 0 and key <= len(x):
                    ticket = x[key-1]
                    break
                else:
                    print("Invalid Input Try again")
            elif key.lower() == 'home()':
                return
            else:
                print("Invalid Input Try again")

        while True:
            confirm = (
                'To confirm your Tickets Click Type Confirm or home() to exit : ')
            confirm = input(f"{confirm}")
            if confirm.lower() == "confirm":
                mycursor.execute(f"delete from tickets where tickno={ticket[-1]}")
                mydb.commit()
                print("Ticket is successfully cancelled")
                break
            elif confirm.lower() == 'home()':
                return
            else:
                print('Invalid input')
    else:
        print("You have not booked any Tickets")
        return


def clearticket():
    mycursor.execute(f"select date,time,tickno from tickets")
    x = mycursor.fetchall()
    a = 0
    tickets = []
    for i in x:
        t = i[0]
        t = t.split('/')
        v = i[1]
        v = v.split(',')
        v = v[0]
        v = v.split(":")
        if f"{t[2]}-{t[1]}-{t[0]}" == today:
            if int(v[0]) <= int((datetime.datetime.now()).strftime("%H")):
                tickets.append(i[-1])
        elif f"{t[2]}-{t[1]}-{t[0]}" < today:
            tickets.append(i[-1])
    if tickets != []:
        for i in tickets:
            mycursor.execute(f"delete from tickets where tickno={i}")
            mydb.commit()


clearticket()


def accountdetails(ID):
    mycursor.execute(f"SELECT * FROM INFO WHERE ID={ID}")
    a = mycursor.fetchall()
    a = a[0]
    print(f"""
    ID: {a[0]}
    Name: {a[1]}
    AGE: {a[3]}
    GENDER: {a[2]}
    MOB.NO: {a[4]}
    EAMIL: {a[5]}
    """)


def deleteaccount(ID):
    while True:
        confirm = input("Are you ''sure'' you want to delete the account.\n If any tickets where booked they will be cancelled\n:=> ")
        if confirm.lower() == "sure":
            mycursor.execute(f"delete from info where ID={ID}")
            mydb.commit()
            mycursor.execute(f"delete from tickets where ID={ID}")
            mydb.commit()
            print("Successfully deleted")
            return "Logout"
        elif confirm.lower() == 'home()':
            return
        else:
            print('Invalid input')


def user(ID):
    while True:
        print("""
        1. Book Tickets
        2. Check Tickets
        3. Cancell Tickets
        4. Account Details
        5. Delete account
        Enter logout to LOGOUT
        """)
        i = input("=>")
        if i.isnumeric():
            i = int(i)
            if i == 1:
                clearticket()
                bookticket(ID)
            elif i == 2:
                clearticket()
                checkticket(ID)
            elif i == 3:
                clearticket()
                cancelticket(ID)
            elif i == 4:
                clearticket()
                accountdetails(ID)
            elif i == 5:
                clearticket()
                x=deleteaccount(ID)
                if x=="Logout":
                    return
            else:
                print("Invalid Input.... Choose a Proper Option")
        elif i.lower() == "logout":
            return
        else:
            print("Invalid Input.... Choose a Proper Option")


def main():
    while True:
        print("""
        1. Log IN
        2. Sign IN
        Enter exit() to Exit
        """)
        i = input("=>")
        if i.isnumeric():
            i = int(i)
            if i == 1:
                ID=login()
                if ID!=None:
                    clearticket()
                    user(ID)
            elif i == 2:
                clearticket()
                createaccount()
            else:
                print("Invalid Input.... Choose a Proper Option")
        elif i.lower() == "exit()":
            print("Thank You!! visit again")
            return
        else:
            print("Invalid Input.... Choose a Proper Option")

main()

