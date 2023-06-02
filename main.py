import mysql.connector as mc
conn = mc.connect(host='localhost', user='root', password='1967')
c = conn.cursor()

def read_data():
    c.execute('Show Databases; ')
    databases = c.fetchall()
    for show in databases:
        print(show)

def main():
    read_data()

if __name__ == "__main__":
    main()