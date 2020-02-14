
import tkinter as tk

# main window
root = tk.Tk()
root.wm_geometry("200x150")
root.title("authorization")

# create empty frame

frame_login = tk.Frame(root)
frame_login.grid()

#TODO: Add a label to frame_auth

#username insert
lbl_username = tk.Label(frame_login, text='Username:')
lbl_username.pack()
ent_username = tk.Entry(frame_login, bd=3)
ent_username.pack(pady=5)

#password insert
lbl_password = tk.Label(frame_login, text='Password:')
lbl_password.pack()
ent_password = tk.Entry(frame_login, bd=3)
ent_password.pack(pady=5)

#button testing

def test_btn():
 print("clicked")
 frame_auth.tkraise()
#TODO: Use get method of ent_password when the button is pressed, and store result
 password = ent_password.get()
 print("password")
#TODO: Configure the label in frame_auth to display the password
 lbl_show_password.config(text = password)


btn_login = tk.Frame(root)
btn_login= tk.Label(btn_login)
btn_login.pack()
clk_btn = tk.Button(frame_login, bd=10,text="Login", command=test_btn)
clk_btn.pack(pady=5)

frame_auth= tk.Frame(root)
frame_auth.grid(row=0,column=0, sticky="news")

lbl_show_password=tk.Label(frame_auth, text = "text")
lbl_show_password.pack()

frame_login.tkraise()
root.mainloop()