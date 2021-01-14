import pymysql.cursors
from datetime import datetime

db = pymysql.connect(
host='localhost',
user='root',
password='',
db='blog',
charset='utf8mb4',
cursorclass=pymysql.cursors.DictCursor)

def login(email, password):
    login_query = db.cursor()
    sql = 'SELECT * FROM users WHERE user_mail = %s AND user_password = %s'
    login_query.execute(sql, [email, password])
    result = login_query.fetchall()
    if result:
        return True
    return False

def register(name, email, password):
    check_user_query = db.cursor()
    check_user_sql = 'SELECT * FROM users WHERE user_mail = %s OR user_name = %s'
    check_user_query.execute(check_user_sql , [email, name])
    check_user_result = check_user_query.fetchone()
    if check_user_result:
        print("Böyle bir üye mevcut!")
    else:
        sql = "INSERT INTO users (user_name, user_mail, user_password, user_date) VALUES (%s, %s, %s, %s)"
        register_query = db.cursor()
        current_datetime = datetime.now()
        register_query.execute(sql, [name, email, password, current_datetime])
        db.commit()
while True:
    komutlar = {
        "komut_1": {
            'komut_adi': 'giris',
            'komut_aciklama': 'Sisteme giriş yapın'
        },
        "komut_2": {
            'komut_adi': 'uyeler',
            'komut_aciklama': 'Üyeleri görün'
        },
        "komut_3": {
            'komut_adi': 'kayit',
            'komut_aciklama': 'Sisteme kayıt olun'
        }
    }
    print("Yapılabilecekler:\n")
    for komut in komutlar:
        print("{komut}: {aciklama}".format(komut = komutlar[komut].get('komut_adi'), aciklama = komutlar[komut].get('komut_aciklama')))
        #print(komutlar[komut].get('komut_adi'))
    komut = input("Ne yapmak istiyorsunuz? ")
    if komut == 'giris':
        giris_mail = input("Eposta girin: ")
        giris_pass = input("Şifre girin: ")
        check_login = login(giris_mail, giris_pass)
        if check_login:
            print("Başarıyla giriş yaptınız\n")
        else:
            print("Böyle bir üye bulunamadı!\n")
    
    if komut == 'uyeler':
        users_query = db.cursor()
        users_query.execute('SELECT * FROM users')
        users = users_query.fetchall()
        if users:
            for user in users:
                print("Kullanıcı adı: {name}".format(name = user['user_name']))
                print("Eposta adresi: {email}".format(email = user['user_mail']))
        else:
            print("Üye bulunamadı!\n")

    if komut == 'kayit':
        kayit_name = input("Kullanıcı adı girin: ")
        kayit_mail = input("E posta girin: ")
        kayit_pass = input("Şifre girin: ")
        register = register(kayit_name, kayit_mail, kayit_pass)
