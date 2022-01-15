# Module securegui.py
import tkinter as tk
import tkinter.messagebox as mb



i=0
s1 = 0
# SecureGUI is a Tk Window that hides itself until a required authorization is complete:
#    the authorization requires a username & password
# A separate (Toplevel) window_login is created and used for signing in

class SecureGUI(tk.Tk):

  # authorization info
  usernames = [ ]
  passwords = [ ]
  authorized = True

  # login window
  window_login = None


  # save username and password
  def add_authorization(self, user="", pw=""):
   self.usernames.append(user)
   self.passwords.append(pw)
    

  # create an instance of this class and display the gui
  def __init__(self):
    tk.Tk.__init__(self)
    self.authorized = False
    self.window_login = tk.Toplevel(self) # create login window
    self.display_login()


  def display_login(self):
    if self.authorized == False:
      self.withdraw() # hide the main window
      self.window_login.deiconify() # show the login window
      self.display_authorization()
    else:
      self.window_login.withdraw() # hide the login window
      self.deiconify() # show the root window

  
  def display_authorization(self):
    # create authorization frame and place widgets in it
    self.frame_login = tk.Frame(self.window_login)
    self.window_login.title("Authorize")
    self.frame_login.grid(row=0, column=0, sticky="news")

    self.lbl_username = tk.Label(self.frame_login,text="Username")
    self.lbl_username.pack(pady=5)
    self.ent_username = tk.Entry(self.frame_login, bd=3)
    self.ent_username.pack(pady=5)

    self.lbl_passwd = tk.Label(self.frame_login,text="Password")
    self.lbl_passwd.pack(pady=5)
    self.ent_password = tk.Entry(self.frame_login, show="*", bd=3)
    self.ent_password.pack(pady=5)

    self.btn_login = tk.Button(self.frame_login, text="LOG IN", command=self.check_authorization)
    self.btn_login.pack(padx=175, pady=20)


  def check_authorization(self):
    user = self.ent_username.get()
    pw = self.ent_password.get()
    
    if user in self.usernames  and  pw in self.passwords :
      self.authorized = True
      self.display_login()
    else:
      mb.showinfo("Login failed","Invalid username and/or password")

