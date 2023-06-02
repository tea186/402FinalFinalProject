import mysql.connector as mc
conn = mc.connect(host='localhost', user='root', password='1967', db='menagerie')
c = conn.cursor()


def birth_month():
    c.execute('SELECT name, birth, MONTH(birth) FROM pet')
    months = c.fetchall()
    for month in months:
        print(month)


def main():
    birth_month()


if __name__ == '__main__':
    main()