import pymysql.cursors

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
while True:
    print("Yapılabilecekler:\ngiris: Giriş yapmak için girin\nuyeler: Üyeleri görmek için girin\n")
    komut = input("Ne yapmak istiyorsunuz? ")
    if komut == 'giris':
        input_mail = input("Eposta girin: ")
        input_pass = input("Şifre girin: ")
        check_login = login(input_mail, input_pass)
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
