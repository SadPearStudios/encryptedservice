import os
import time
from cryptography.fernet import Fernet
from datetime import datetime
from pathlib import Path

k = os.environ.get('FERNET')
fernet = Fernet(k)


def cs():
  os.system("ls")
  os.system('clear')


def e(m):
  em = fernet.encrypt(m.encode())
  return em


def d(m):
  dm = fernet.decrypt(m).decode()
  return dm


def fp(u, p):
  d = False
  with open(str(u) + '/' + str(u) + "password.bin", "r") as f:
    z = f.read()
    while d is False:
      if p != fernet.decrypt(z).decode():
        p = input("Incorrect password! : ")
      else:
        d = True
    print("Loading...")
    time.sleep(1)
    cs()
    li(u)


def li(u):
  print("Welcome, " + str(u))
  fi(u)


def fi(u):
  with open(str(u) + '/' + str(u) + 'inbox.bin', 'r') as f:
    c = f.read()
    print(fernet.decrypt(c).decode())
  sm(u)


def sm(u):
  dt = datetime.now()

  t = input("TO: ")
  s = input("SUBJECT: ")
  m = input("MESSAGE: ")

  i = Path(str(t) + '/' + str(t) + 'inbox.bin').read_bytes()
  d = "\nTIME:" + str(dt) + "\nFROM:" + str(u) + '\nSUBJ:' + s + '\n' + m + "\n\n"
  Path(str(t)+'/'+str(t)+'inbox.bin').write_bytes(e(fernet.decrypt(i).decode()+d))

  time.sleep(1)
  print("MESSAGE SENT.")


print("Don't have a user ID or forgot your password? Enter 'signup'. ")
u = input("Enter your ID: ")

if u == "signup":
  print("Account setup:")
  o = input("Enter new user ID: ")

  try:
    os.mkdir(str(o))
    q = input("Enter new user password: ")

    Path(str(o) + '/' + str(o) + 'inbox.bin').write_bytes(e("INBOX"))
    Path(str(o) + '/' + str(o) + 'password.bin').write_bytes(e(q))
    print("Please restart the program. Thanks for using this service!")

  except OSError:
    print("Account already existing")

    with open(str(o) + '/' + str(o) + 'password.bin', 'r') as z:
      c = z.read()
      if fernet.decrypt(c).decode() == "pass":
        print("Incomplete user setup, select a password: ")
        q = input("Enter new user password: ")

        Path(str(o) + '/' + str(o) + 'inbox.bin').write_bytes(e("INBOX"))
        Path(str(o) + '/' + str(o) + 'password.bin').write_bytes(e(q))
else:
  p = input("Enter password: ")
  fp(u, p)
