# Mau Apa OY
import base64, zlib, marshal, sys, os

def keluar():
    print '[!] Exit'
    os.sys.exit()


logo = '\x1b[1;33m\xe2\x95\x94\xe2\x95\x90\xe2\x95\x97\xe2\x94\x8c\xe2\x94\x90\xe2\x94\x8c\xe2\x94\x8c\xe2\x94\x80\xe2\x94\x90\xe2\x94\xac\xe2\x94\x80\xe2\x94\x90\xe2\x94\xac \xe2\x94\xac\xe2\x94\x8c\xe2\x94\x80\xe2\x94\x90\xe2\x94\x8c\xe2\x94\xac\xe2\x94\x90\x1b[0;36m<<<\x1b[0;34m\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x97\x1b[0m\n\x1b[1;37m\xe2\x95\x91\xe2\x95\xa3 \xe2\x94\x82\xe2\x94\x82\xe2\x94\x82\xe2\x94\x82  \xe2\x94\x9c\xe2\x94\xac\xe2\x94\x98\xe2\x94\x94\xe2\x94\xac\xe2\x94\x98\xe2\x94\x9c\xe2\x94\x80\xe2\x94\x98 \xe2\x94\x82        \x1b[41m             \x1b[0m\x1b[0;34m\xe2\x95\x91\x1b[0m\n\x1b[0;32m\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x9d\xe2\x94\x98\xe2\x94\x94\xe2\x94\x98\xe2\x94\x94\xe2\x94\x80\xe2\x94\x98\xe2\x94\xb4\xe2\x94\x94\xe2\x94\x80 \xe2\x94\xb4 \xe2\x94\xb4   \xe2\x94\xb4 \x1b[0;33mpython\x1b[0m \x1b[41m             \x1b[0m\x1b[0;34m\xe2\x95\x91\x1b[0m\n\x1b[0;32mAuthor \x1b[1;37m: \x1b[1;30mJengkolOnline      \x1b[47m             \x1b[0m\x1b[0;34m\xe2\x95\x91\x1b[0m\n\x1b[0;32mKontak \x1b[1;37m: \x1b[1;30m082372139631       \x1b[47m             \x1b[0m\x1b[0;34m\xe2\x95\x91\x1b[0m\n\x1b[0;32mCopyRing \x1b[1;37m: \x1b[1;30mSumarr-ID    \x1b[0;34m\xe2\x95\x91\x1b[0m\n\x1b[0;34m\xe2\x95\x91\x1b[1;35m-\xe2\x96\xba \x1b[0;31m{\x1b[1;37m01\x1b[0;31m}\x1b[0m Encrypt \x1b[1;30mBase16        \x1b[0;34m \xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x9d\x1b[0m\n\x1b[0;34m\xe2\x95\x91\x1b[1;35m-\xe2\x96\xba \x1b[0;31m{\x1b[1;37m02\x1b[0;31m}\x1b[0m Encrypt \x1b[1;30mBase32     \x1b[0;34m\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x97\x1b[0m\n\x1b[0;34m\xe2\x95\x91\x1b[1;35m-\xe2\x96\xba \x1b[0;31m{\x1b[1;37m03\x1b[0;31m}\x1b[0m Encrypt \x1b[1;30mBase64     \x1b[0;34m\xe2\x95\x91\x1b[0;30m\x1b[47mraz p5w\x1b[0m\x1b[0;34m\xe2\x95\x91\x1b[0;32m]\x1b[0;34m\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x97\x1b[0m\n\x1b[0;34m\xe2\x95\x91\x1b[1;35m-\xe2\x96\xba \x1b[0;31m{\x1b[1;37m04\x1b[0;31m}\x1b[0m Encrypt \x1b[1;30mMarshal   \x1b[0;34m \xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x9d    \xe2\x95\x91\x1b[0m\n\x1b[0;34m\xe2\x95\x91\x1b[1;35m-\xe2\x96\xba \x1b[0;31m{\x1b[1;37m05\x1b[0;31m}\x1b[0m Encrypt \x1b[1;30mZlib,Base16             \x1b[0;34m\xe2\x95\x91\x1b[0m\n\x1b[0;34m\xe2\x95\x91\x1b[1;35m-\xe2\x96\xba \x1b[0;31m{\x1b[1;37m06\x1b[0;31m}\x1b[0m Encrypt \x1b[1;30mZlib,Base32             \x1b[0;34m\xe2\x95\x91\x1b[0m\n\x1b[0;34m\xe2\x95\x91\x1b[1;35m-\xe2\x96\xba \x1b[0;31m{\x1b[1;37m07\x1b[0;31m}\x1b[0m Encrypt \x1b[1;30mZlib,Base64             \x1b[0;34m\xe2\x95\x91\x1b[0m\n\x1b[0;34m\xe2\x95\x91\x1b[1;35m-\xe2\x96\xba \x1b[0;31m{\x1b[1;37m08\x1b[0;31m}\x1b[0m Encrypt \x1b[1;30mMarshal,Zlib,Base16     \x1b[0;34m\xe2\x95\x91\x1b[0m\n\x1b[0;34m\xe2\x95\x91\x1b[1;35m-\xe2\x96\xba \x1b[0;31m{\x1b[1;37m09\x1b[0;31m}\x1b[0m Encrypt \x1b[1;30mMarshal,Zlib,Base32     \x1b[0;34m\xe2\x95\x91\x1b[0m\n\x1b[0;34m\xe2\x95\x91\x1b[1;35m-\xe2\x96\xba \x1b[0;31m{\x1b[1;37m10\x1b[0;31m}\x1b[0m Encrypt \x1b[1;30mMarshal,Zlib,Base64     \x1b[0;34m\xe2\x95\x91\x1b[0m\n\x1b[0;34m\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\x1b[0;32m[\x1b[0;35mEncrypt python\x1b[0;32m]\x1b[0;34m\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x9d\x1b[0m'

def menu():
    os.system('clear')
    print logo
    print
    masuk = raw_input('\x1b[0;31m[\x1b[1;33m+\x1b[0;31m] \x1b[0;34mChoice \x1b[1;37m\xe2\x9e\xa4\x1b[0m ')
    if masuk == '':
        print '[!] Wrong input'
        keluar()
    elif masuk == '1':
        satu()
    elif masuk == '2':
        dua()
    elif masuk == '3':
        tiga()
    elif masuk == '4':
        empat()
    elif masuk == '5':
        lima()
    elif masuk == '6':
        enam()
    elif masuk == '7':
        tujuh()
    elif masuk == '8':
        delapan()
    elif masuk == '9':
        sembilan()
    elif masuk == '10':
        sepuluh()
    elif masuk == '0':
        keluar()
    else:
        print '[!] Wrong input'
        keluar()


def satu():
    try:
        file = raw_input('\x1b[0;36m[\x1b[0;31m!\x1b[0;36m] \x1b[1;37mFile \x1b[0;31m-\xe2\x96\xba\x1b[0m ')
        fileopen = open(file).read()
        a = base64.b16encode(fileopen)
        b = "#Encrypt by Sumarr ID\n#Gitlab : Https://gitlab.com/\nimport base64\nexec(base64.b16decode('" + a + "'))"
        c = file.replace('.py', '-enc.py')
        d = open(c, 'w')
        d.write(b)
        d.close()
        print '\x1b[0;31m[\x1b[0;34m+\x1b[0;31m] \x1b[0;32mHasil \x1b[1;37m:\x1b[0m ', c
        print '\x1b[0;31m[\x1b[1;33m+\x1b[0;31m] \x1b[0;31m[\x1b[0;32mTekan enter untuk kembali\x1b[0;31m]\x1b[0;34m\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x97'
        print '\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x9d'
        raw_input('\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\x1b[0;31m[\x1b[1;37mBack\x1b[0;31m]\x1b[0m')
        menu()
    except:
        print '[?] File tidak ada'
        print '\x1b[0;31m[\x1b[1;33m+\x1b[0;31m] \x1b[0;31m[\x1b[0;32mTekan enter untuk kembali\x1b[0;31m]\x1b[0;34m\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x97'
        print '\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x9d'
        raw_input('\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\x1b[0;31m[\x1b[1;37mBack\x1b[0;31m]\x1b[0m')
        menu()


def dua():
    try:
        file = raw_input('\x1b[0;36m[\x1b[0;31m!\x1b[0;36m] \x1b[1;37mFile \x1b[0;31m-\xe2\x96\xba\x1b[0m ')
        fileopen = open(file).read()
        a = base64.b32encode(fileopen)
        b = "#Encrypt by Sumarr ID\n#Gitlab : Https://gitlab.com/\nimport base64\nexec(base64.b32decode('" + a + "'))"
        c = file.replace('.py', '-enc.py')
        d = open(c, 'w')
        d.write(b)
        d.close()
        print '\x1b[0;31m[\x1b[0;34m+\x1b[0;31m] \x1b[0;32mHasil \x1b[1;37m:\x1b[0m ', c
        print '\x1b[0;31m[\x1b[1;33m+\x1b[0;31m] \x1b[0;31m[\x1b[0;32mTekan enter untuk kembali\x1b[0;31m]\x1b[0;34m\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x97'
        print '\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x9d'
        raw_input('\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\x1b[0;31m[\x1b[1;37mBack\x1b[0;31m]\x1b[0m')
        menu()
    except:
        print '[?] File tidak ada'
        print '\x1b[0;31m[\x1b[1;33m+\x1b[0;31m] \x1b[0;31m[\x1b[0;32mTekan enter untuk kembali\x1b[0;31m]\x1b[0;34m\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x97'
        print '\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x9d'
        raw_input('\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\x1b[0;31m[\x1b[1;37mBack\x1b[0;31m]\x1b[0m')
        menu()


def tiga():
    try:
        file = raw_input('\x1b[0;36m[\x1b[0;31m!\x1b[0;36m] \x1b[1;37mFile \x1b[0;31m-\xe2\x96\xba\x1b[0m ')
        fileopen = open(file).read()
        a = base64.b64encode(fileopen)
        b = "#Encrypt by Sumarr ID\n#Gitlab : Https://gitlab.com/\nimport base64\nexec(base64.b64decode('" + a + "'))"
        c = file.replace('.py', '-enc.py')
        d = open(c, 'w')
        d.write(b)
        d.close()
        print '\x1b[0;31m[\x1b[0;34m+\x1b[0;31m] \x1b[0;32mHasil \x1b[1;37m:\x1b[0m ', c
        print '\x1b[0;31m[\x1b[1;33m+\x1b[0;31m] \x1b[0;31m[\x1b[0;32mTekan enter untuk kembali\x1b[0;31m]\x1b[0;34m\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x97'
        print '\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x9d'
        raw_input('\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\x1b[0;31m[\x1b[1;37mBack\x1b[0;31m]\x1b[0m')
        menu()
    except:
        print '[?] File tidak ada'
        print '\x1b[0;31m[\x1b[1;33m+\x1b[0;31m] \x1b[0;31m[\x1b[0;32mTekan enter untuk kembali\x1b[0;31m]\x1b[0;34m\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x97'
        print '\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x9d'
        raw_input('\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\x1b[0;31m[\x1b[1;37mBack\x1b[0;31m]\x1b[0m')
        menu()


def empat():
    try:
        file = raw_input('\x1b[0;36m[\x1b[0;31m!\x1b[0;36m] \x1b[1;37mFile \x1b[0;31m-\xe2\x96\xba\x1b[0m ')
        fileopen = open(file).read()
        a = compile(fileopen, 'Sumarr ID', 'exec')
        m = marshal.dumps(a)
        s = repr(m)
        b = '#Encrypt by Sumarr ID\n#Gitlab : Https://gitlab.com/\nimport marshal\nexec(marshal.loads(' + s + '))'
        c = file.replace('.py', '-enc.py')
        d = open(c, 'w')
        d.write(b)
        d.close()
        print '\x1b[0;31m[\x1b[0;34m+\x1b[0;31m] \x1b[0;32mHasil \x1b[1;37m:\x1b[0m ', c
        print '\x1b[0;31m[\x1b[1;33m+\x1b[0;31m] \x1b[0;31m[\x1b[0;32mTekan enter untuk kembali\x1b[0;31m]\x1b[0;34m\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x97'
        print '\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x9d'
        raw_input('\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\x1b[0;31m[\x1b[1;37mBack\x1b[0;31m]\x1b[0m')
        main()
    except:
        print '[?] File tidak ada'
        print '\x1b[0;31m[\x1b[1;33m+\x1b[0;31m] \x1b[0;31m[\x1b[0;32mTekan enter untuk kembali\x1b[0;31m]\x1b[0;34m\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x97'
        print '\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x9d'
        raw_input('\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\x1b[0;31m[\x1b[1;37mBack\x1b[0;31m]\x1b[0m')
        main()


def lima():
    try:
        file = raw_input('\x1b[0;36m[\x1b[0;31m!\x1b[0;36m] \x1b[1;37mFile \x1b[0;31m-\xe2\x96\xba\x1b[0m ')
        fileopen = open(file).read()
        c = zlib.compress(fileopen)
        d = base64.b16encode(c)
        e = '#Encrypt by Sumarr ID\n#Gitlab : Https://gitlab.com/\nimport marshal,zlib,base64\nexec(zlib.decompress(base64.b16decode("' + d + '")))'
        f = file.replace('.py', '-enc.py')
        g = open(f, 'w')
        g.write(e)
        g.close()
        print '\x1b[0;31m[\x1b[0;34m+\x1b[0;31m] \x1b[0;32mHasil \x1b[1;37m:\x1b[0m ', f
        print '\x1b[0;31m[\x1b[1;33m+\x1b[0;31m] \x1b[0;31m[\x1b[0;32mTekan enter untuk kembali\x1b[0;31m]\x1b[0;34m\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x97'
        print '\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x9d'
        raw_input('\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\x1b[0;31m[\x1b[1;37mBack\x1b[0;31m]\x1b[0m')
        menu()
    except:
        print '[?] File tidak ada'
        print '\x1b[0;31m[\x1b[1;33m+\x1b[0;31m] \x1b[0;31m[\x1b[0;32mTekan enter untuk kembali\x1b[0;31m]\x1b[0;34m\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x97'
        print '\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x9d'
        raw_input('\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\x1b[0;31m[\x1b[1;37mBack\x1b[0;31m]\x1b[0m')
        menu()


def enam():
    try:
        file = raw_input('\x1b[0;36m[\x1b[0;31m!\x1b[0;36m] \x1b[1;37mFile \x1b[0;31m-\xe2\x96\xba\x1b[0m ')
        fileopen = open(file).read()
        c = zlib.compress(fileopen)
        d = base64.b32encode(c)
        e = '#Encrypt by Sumarr ID\n#Gitlab : Https://gitlab.com/\nimport marshal,zlib,base64\nexec(zlib.decompress(base64.b32decode("' + d + '")))'
        f = file.replace('.py', '-enc.py')
        g = open(f, 'w')
        g.write(e)
        g.close()
        print '\x1b[0;31m[\x1b[0;34m+\x1b[0;31m] \x1b[0;32mHasil \x1b[1;37m:\x1b[0m ', f
        print '\x1b[0;31m[\x1b[1;33m+\x1b[0;31m] \x1b[0;31m[\x1b[0;32mTekan enter untuk kembali\x1b[0;31m]\x1b[0;34m\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x97'
        print '\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x9d'
        raw_input('\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\x1b[0;31m[\x1b[1;37mBack\x1b[0;31m]\x1b[0m')
        menu()
    except:
        print '[?] File tidak ada'
        print '\x1b[0;31m[\x1b[1;33m+\x1b[0;31m] \x1b[0;31m[\x1b[0;32mTekan enter untuk kembali\x1b[0;31m]\x1b[0;34m\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x97'
        print '\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x9d'
        raw_input('\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\x1b[0;31m[\x1b[1;37mBack\x1b[0;31m]\x1b[0m')
        menu()


def tujuh():
    try:
        file = raw_input('\x1b[0;36m[\x1b[0;31m!\x1b[0;36m] \x1b[1;37mFile \x1b[0;31m-\xe2\x96\xba\x1b[0m ')
        fileopen = open(file).read()
        c = zlib.compress(fileopen)
        d = base64.b64encode(c)
        e = '#Encrypt by Sumarr ID\n#Gitlab : Https://gitlab.com/\nimport marshal,zlib,base64\nexec(zlib.decompress(base64.b64decode("' + d + '")))'
        f = file.replace('.py', '-enc.py')
        g = open(f, 'w')
        g.write(e)
        g.close()
        print '\x1b[0;31m[\x1b[0;34m+\x1b[0;31m] \x1b[0;32mHasil \x1b[1;37m:\x1b[0m ', f
        print '\x1b[0;31m[\x1b[1;33m+\x1b[0;31m] \x1b[0;31m[\x1b[0;32mTekan enter untuk kembali\x1b[0;31m]\x1b[0;34m\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x97'
        print '\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x9d'
        raw_input('\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\x1b[0;31m[\x1b[1;37mBack\x1b[0;31m]\x1b[0m')
        menu()
    except:
        print '[?] File tidak ada'
        print '\x1b[0;31m[\x1b[1;33m+\x1b[0;31m] \x1b[0;31m[\x1b[0;32mTekan enter untuk kembali\x1b[0;31m]\x1b[0;34m\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x97'
        print '\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x9d'
        raw_input('\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\x1b[0;31m[\x1b[1;37mBack\x1b[0;31m]\x1b[0m')
        menu()


def delapan():
    try:
        file = raw_input('\x1b[0;36m[\x1b[0;31m!\x1b[0;36m] \x1b[1;37mFile \x1b[0;31m-\xe2\x96\xba\x1b[0m ')
        fileopen = open(file).read()
        sa = compile(fileopen, 'Sumarr ID', 'exec')
        sb = marshal.dumps(sa)
        c = zlib.compress(sb)
        d = base64.b16encode(c)
        e = '#Encrypt by Sumarr ID\n#Gitlab : Https://gitlab.com/\nimport marshal,zlib,base64\nexec(marshal.loads(zlib.decompress(base64.b16decode("' + str(d) + '"))))'
        f = file.replace('.py', '-enc.py')
        g = open(f, 'w')
        g.write(e)
        g.close()
        print '\x1b[0;31m[\x1b[0;34m+\x1b[0;31m] \x1b[0;32mHasil \x1b[1;37m:\x1b[0m ', f
        print '\x1b[0;31m[\x1b[1;33m+\x1b[0;31m] \x1b[0;31m[\x1b[0;32mTekan enter untuk kembali\x1b[0;31m]\x1b[0;34m\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x97'
        print '\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x9d'
        raw_input('\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\x1b[0;31m[\x1b[1;37mBack\x1b[0;31m]\x1b[0m')
        menu()
    except:
        print '[?] File tidak ada'
        print '[+] [Tekan enter untuk kembali]\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x97'
        print '\x1b[0;31m[\x1b[1;33m+\x1b[0;31m] \x1b[0;31m[\x1b[0;32mTekan enter untuk kembali\x1b[0;31m]\x1b[0;34m\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x97'
        print '\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x9d'
        raw_input('\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\x1b[0;31m[\x1b[1;37mBack\x1b[0;31m]\x1b[0m')
        menu()


def sembilan():
    try:
        file = raw_input('\x1b[0;36m[\x1b[0;31m!\x1b[0;36m] \x1b[1;37mFile \x1b[0;31m-\xe2\x96\xba\x1b[0m ')
        fileopen = open(file).read()
        sa = compile(fileopen, 'Sumarr ID', 'exec')
        sb = marshal.dumps(sa)
        c = zlib.compress(sb)
        d = base64.b32encode(c)
        e = '#Encrypt by Sumarr ID\n#Gitlab : Https://gitlab.com/\nimport marshal,zlib,base64\nexec(marshal.loads(zlib.decompress(base64.b32decode("' + str(d) + '"))))'
        f = file.replace('.py', '-enc.py')
        g = open(f, 'w')
        g.write(e)
        g.close()
        print '\x1b[0;31m[\x1b[0;34m+\x1b[0;31m] \x1b[0;32mHasil \x1b[1;37m:\x1b[0m ', f
        print '\x1b[0;31m[\x1b[1;33m+\x1b[0;31m] \x1b[0;31m[\x1b[0;32mTekan enter untuk kembali\x1b[0;31m]\x1b[0;34m\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x97'
        print '\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x9d'
        raw_input('\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\x1b[0;31m[\x1b[1;37mBack\x1b[0;31m]\x1b[0m')
        menu()
    except:
        print '[?] File tidak ada'
        print '[+] [Tekan enter untuk kembali]\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x97'
        print '\x1b[0;31m[\x1b[1;33m+\x1b[0;31m] \x1b[0;31m[\x1b[0;32mTekan enter untuk kembali\x1b[0;31m]\x1b[0;34m\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x97'
        print '\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x9d'
        raw_input('\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\x1b[0;31m[\x1b[1;37mBack\x1b[0;31m]\x1b[0m')
        menu()


def sepuluh():
    try:
        file = raw_input('\x1b[0;36m[\x1b[0;31m!\x1b[0;36m] \x1b[1;37mFile \x1b[0;31m-\xe2\x96\xba\x1b[0m ')
        fileopen = open(file).read()
        sa = compile(fileopen, 'Sumarr ID', 'exec')
        sb = marshal.dumps(sa)
        c = zlib.compress(sb)
        d = base64.b64encode(c)
        e = '#Encrypt by Sumarr ID\n#Gitlab : Https://gitlab.com/\nimport marshal,zlib,base64\nexec(marshal.loads(zlib.decompress(base64.b64decode("' + str(d) + '"))))'
        f = file.replace('.py', '-enc.py')
        g = open(f, 'w')
        g.write(e)
        g.close()
        print '\x1b[0;31m[\x1b[0;34m+\x1b[0;31m] \x1b[0;32mHasil \x1b[1;37m:\x1b[0m ', f
        print '\x1b[0;31m[\x1b[1;33m+\x1b[0;31m] \x1b[0;31m[\x1b[0;32mTekan enter untuk kembali\x1b[0;31m]\x1b[0;34m\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x97'
        print '\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x9d'
        raw_input('\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\x1b[0;31m[\x1b[1;37mBack\x1b[0;31m]\x1b[0m')
        menu()
    except:
        print '[?] File tidak ada'
        print '\x1b[0;31m[\x1b[1;33m+\x1b[0;31m] \x1b[0;31m[\x1b[0;32mTekan enter untuk kembali\x1b[0;31m]\x1b[0;34m\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x97'
        print '\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x9d'
        raw_input('\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\x1b[0;31m[\x1b[1;37mBack\x1b[0;31m]\x1b[0m')
        menu()


if __name__ == '__main__':
    menu()
