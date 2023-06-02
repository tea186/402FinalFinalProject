import mysql.connector as mc
conn = mc.connect(host='localhost', user='root', password='1967', db='menagerie')
c = conn.cursor()


def show_name_birth():
    c.execute('SELECT name, birth FROM pet')
    fields = c.fetchall()
    for field in fields:
        print(field)


def main():
    show_name_birth()


if __name__ == '__main__':
    main()