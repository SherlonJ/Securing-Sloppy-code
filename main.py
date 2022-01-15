 # a213_multi_factor.py
import securegui as sg
import tkinter as tk


# create an app that has restricted access
my_app = sg.SecureGUI()


# set logins
logins_file = open("userpass.txt")
for line in logins_file:
  start_index = line.find("[")
  colon_index = line.find(":")
  end_index = line.find("]")
  username = line[ start_index+1 : colon_index ].strip()
  password = line[ colon_index+1 : end_index ].strip()
  my_app.add_authorization(user=username, pw=password)
logins_file.close()


# User Adding Account
def add_account():
 
  s1 = [None]*49
  a = ent_username.get()
  b = ent_password.get()

  i = 0
  for c in a:
    s1[i] = c
    i += 1 
  s1[25] = ":"
  i = 26
  for c in b:
    s1[i] = c
    i += 1

  s2 = "["
  for c in s1:
    if c == None:
      s2 = s2 + " "
    else:
      s2 = s2 + c
  s2 = s2 + "]\n"
  print("s1 value:" + str(s1))
  print(" \n s2 value:" + str(s2))
  print("")
  if s1 > 8 and i <=24: 
   logins_file = open("userpass.txt", "a")
   logins_file.write(s2)
   logins_file.close()
   
   ent_username.delete('0', 'end')
   ent_password.delete('0', 'end')



# create the app
my_app.title("My App")
my_frame = tk.Frame(my_app, bg="sienna2")
my_frame.grid(row=0, column=0, sticky="news")

welcome = "Welcome to the restricted application."
lbl_welcome = tk.Label(my_frame, text=welcome, bg="sienna2")
lbl_welcome.config( font=("Arial", 18) )
lbl_welcome.pack(pady=10)

message = "_The_Secret_Recipe_\nSpread peanut butter on slice of bread.\nSpread jelly on another slice.\nPut the slices together to form a sandwich."
lbl_message = tk.Label(my_frame, text=message, bg="sienna2")
lbl_message.pack(pady=10)

btn_account = tk.Button(my_frame, text="Add a Login:", command=add_account)
btn_account.pack()
ent_username = tk.Entry(my_frame, bd=3)
ent_username.pack(pady=5)
ent_password = tk.Entry(my_frame, bd=3)
ent_password.pack(pady=5)

btn_quit = tk.Button(my_frame, text="Quit", command=my_app.quit)
btn_quit.pack(pady=10)




# UI Bindings
ent_username.insert(0, "username") # hint
ent_username.bind("<FocusIn>", lambda args: ent_username.delete('0', 'end'))
ent_password.insert(0, "password") #hint
ent_password.bind("<FocusIn>", lambda args: ent_password.delete('0', 'end'))


# Allow the user to interact with the app
my_app.mainloop()
