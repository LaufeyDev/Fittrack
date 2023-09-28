import mysql.connector

# Connect to MySQL database
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="ninte passwd adik",
    database="gym_database"
)

cursor = db.cursor()
cursor.execute("""
    CREATE TABLE IF NOT EXISTS Members (
        
        name VARCHAR(255) NOT NULL,
        height DECIMAL(5, 2),
        weight DECIMAL(5, 2),
        level VARCHAR(50)
    )
""")
cursor.execute("CREATE TABLE IF NOT EXISTS users ( username VARCHAR(255), password VARCHAR(255))")

# register
def register():
    username = input("Enter a username: ")
    password = input("Enter a password: ")

    # Check if the username already exists in the database
    cursor.execute("SELECT * FROM users WHERE username = %s", (username,))
    if cursor.fetchone():
        print("Username already exists. Please choose a different one.")
    else:
        # Insert the new user into the database
        cursor.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, password))
        db.commit()
        print("Registration successful!")

    # Add member information
    mid = int(input("Enter member id: ")) 
    name = input("Enter name: ")
    ht = int(input("Enter height in cm: "))
    wt = int(input("Enter weight in kg: "))
#    lvl = input("Enter level (beginner, intermediate, pro): ")

    # Insert member data into the Members table
    cursor.execute("INSERT INTO Members (member_id, name, height, weight) VALUES (%s, %s, %s, %s)",
                    (mid, name, ht, wt,))
    db.commit()


def login():
    mode = input("login as admin or member: ")
    if mode=='member':

        username = input("Enter your username: ")
        password = input("Enter your password: ")

    # Check if the username and password match a record in the database
        cursor.execute("SELECT * FROM users WHERE username = %s and password = %s", (username, password))
        if cursor.fetchone():
            print("Login successful!")



            while True:
            

                print("1. Show workout")
                print("2. Enter day")
                print("3. Update info")
                print("4. Exit ")
                ch2 = int(input("Select option: "))
                if ch2 == 1:
                    print("""
                        +------------------------+
                        │      Workout Plan      │
                        +------------------------+
                        │  Mon: Chest day        │
                        │  Tue: Tricep & Abs     │
                        │  Wed: Bicep & Shoulder │
                        │  Thu: Leg day          │
                        │  Fri: Back day         │ 
                        │  Sat: Rest             │
                        │  Sun: Rest             │
                        +------------------------+

""")
                elif ch2 == 2:
                    d = input("Enter day: ")
                    lvl= input("Enter level (beginner, intermediate, pro): ")
                #monday chest day workouts (b,i,p)
                    if d == 'Mon' or d == 'mon' or d=='Monday' or d == 'monday':
                        print("Chest day")  
                    if lvl == 'beginner' or lvl=='Beginner':
                        print("Wokrouts kanikum(b)")
                    elif lvl == 'intermediate' or lvl == 'Intermediate':   
                        print("Wokrout(I)")
                    elif lvl =='Pro' or lvl=='pro':
                        print("Workout(P)")
                #Tuesday workout (b,i,p)        
                    elif d == 'Tue' or d == 'tue' or d=='tuesday' or d == 'Tuesday':
                        print("Tricep & Abs")  
                    if lvl == 'beginner' or lvl=='Beginner':
                        print("Wokrouts kanikum(b)")
                    elif lvl == 'intermediate' or lvl == 'Intermediate':   
                        print("Wokrout(I)")
                    elif lvl =='Pro' or lvl=='pro':
                        print("Workout(P)")
                #wednesday workout (b,i,p)    
                    elif d == 'Wed' or d == 'wed' or d=='Wednesday' or d == 'wednesday':
                        print("Bicep & shoulder")  
                    if lvl == 'beginner' or lvl=='Beginner':
                        print("Wokrouts kanikum(b)")
                    elif lvl == 'intermediate' or lvl == 'Intermediate':   
                        print("Wokrout(I)")
                    elif lvl =='Pro' or lvl=='pro':
                        print("Workout(P)")
                #thursday workout (b,i,p)        
                    elif d == 'Thu' or d == 'thu' or d=='Thursday' or d == 'thursday':
                        print("Leg day")  
                    if lvl == 'beginner' or lvl=='Beginner':
                        print("Wokrouts kanikum(b)")
                    elif lvl == 'intermediate' or lvl == 'Intermediate':   
                        print("Wokrout(I)")
                    elif lvl =='Pro' or lvl=='pro':
                        print("Workout(P)")
                #friday workout (b,i,p)        
                    elif d == 'Fri' or d == 'fri' or d=='Friday' or d == 'friday':
                        print("Back day")  
                    if lvl == 'beginner' or lvl=='Beginner':
                        print("Wokrouts kanikum(b)")
                    elif lvl == 'intermediate' or lvl == 'Intermediate':   
                        print("Wokrout(I)")
                    elif lvl =='Pro' or lvl=='pro':
                        print("Workout(P)")
                #rest day        
                    elif d == 'sat' or d == 'Sat' or d=='saturday' or d == 'Saturday':
                        print("Rest day")  
                        print("“If you get tired, learn to rest, not to quit.”")
                #rest day       
                    elif d == 'Sun' or d == 'sun' or d=='sunday' or d == 'Sunday':
                        print("Rest day")  
                        print("“Relax and recharge.")    
                    else:
                        print("please enter day(Mon,Tue,Wed...)")


                    
                elif ch2 == 3:
                    mid=int(input('Enter the member id of whose details you want to change :'))
                    o=input("enter the option you want to update (height,weight) :")
                    if o=="height":
                        new=int(input("enter new height :"))
                    elif o=="weight":
                        new=int(input("enter new weight :"))
                    else:
                        print("invalid choice, please enter given choices")
#                  new=input("enter new detail :")
                    cursor.execute("update members set {}={} where member_id='{}'".format(o,new,mid))
                    db.commit()
                    cursor.execute("select * from members")
                    a=cursor.fetchall()
                    print(a)
                    for i in a:
                        print(i[0],i[1],i[2],i[3],i[4])
                elif ch2 == 4:
                    print("STAY HARD SON!! KEEP GOING")
                    break
    elif mode == 'admin':
        print("Welcome to admin")





    else:
        print("Incorrect username or password. Please try again.")

# ...
if __name__ == "__main__":
    while True:
        print("1. Register")
        print("2. Login")
        print("3. Exit")
        choice = input("Choose an option (1/2/3): ")

        if choice == "1":
            register()
        elif choice == "2":
            login()
            break
        elif choice == "3":
            print("STAY HARD SON!! KEEP GOING")
            break
        else:
            print("Invalid choice. Please select 1, 2, or 3.")


# Close the database connection
db.close()
