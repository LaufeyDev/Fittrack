import mysql.connector

# Connect to MySQL database
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="sebs",
    database="gym_database"
)

cursor = db.cursor()
cursor.execute("""
    CREATE TABLE IF NOT EXISTS Members (
        member_id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(255) NOT NULL,
        height DECIMAL(5, 2),
        weight DECIMAL(5, 2),
        level VARCHAR(50),
        password VARCHAR(50)
    )
""")
cursor.execute("CREATE TABLE IF NOT EXISTS users (id INT AUTO_INCREMENT PRIMARY KEY, username VARCHAR(255), password VARCHAR(255))")

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


def login():
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    # Check if the username and password match a record in the database
    cursor.execute("SELECT * FROM users WHERE username = %s and password = %s", (username, password))
    if cursor.fetchone():
        print("Login successful!")

        # Add member information
        mid = int(input("Enter member id: "))
        name = input("Enter name: ")
        ht = int(input("Enter height in cm: "))
        wt = int(input("Enter weight in kg: "))
        lvl = input("Enter level (beginner, intermediate, pro): ")

        # Insert member data into the Members table
        cursor.execute("INSERT INTO Members (member_id, name, height, weight, level) VALUES (%s, %s, %s, %s, %s)",
                       (mid, name, ht, wt, lvl))
        db.commit()

        while True:

            print("1. Show workout")
            print("2. Enter day")
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
                if d == 'Mon' or d == 'mon' or d=='Monday' or d == 'monday':
                    print("Chest day")  
                    print("Wokrouts kanikum")
                elif d == 'Tue' or d == 'tue' or d=='tuesday' or d == 'Tuesday':
                    print("Tricep & Abs")  
                    print("Wokrouts kanikum")
                elif d == 'Wed' or d == 'wed' or d=='Wednesday' or d == 'wednesday':
                    print("Bicep & shoulder")  
                    print("Wokrouts kanikum")
                elif d == 'Thu' or d == 'thu' or d=='Thursday' or d == 'thursday':
                    print("Leg day")  
                    print("Wokrouts kanikum")
                elif d == 'Fri' or d == 'fri' or d=='Friday' or d == 'friday':
                    print("Back day")  
                    print("Wokrouts kanikum")
                elif d == 'sat' or d == 'Sat' or d=='saturday' or d == 'Saturday':
                    print("Rest day")  
                    print("Wokrouts kanikum")
                elif d == 'Sun' or d == 'sun' or d=='sunday' or d == 'Sunday':
                    print("Rest day")  
                    print("Wokrouts kanikum")    
                else:
                    print("please enter day(Mon,Tue,Wed...)")                




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
            break
        else:
            print("Invalid choice. Please select 1, 2, or 3.")


# Close the database connection
db.close()


print("""
      +------------------------+
      │      Workout Plan      │
      +------------------------+
      │  Mon:                  │
      │  Tue:                  │
      │  Wed:                  │
      │  Thu:                  │
      │  Fri:                  │ 
      │  Sat:                  │
      │  Sun:                  │
      +------------------------+

""")
