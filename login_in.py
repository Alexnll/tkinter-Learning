# 登录窗口
import tkinter as tk
from tkinter import messagebox
import pickle
# welcome image
# 创建窗口
window = tk.Tk()
window.title("Welcome!")
window.geometry('600x400')

# 创建画布
canvas = tk.Canvas(window,width=500, height=200)
image_file = tk.PhotoImage(file='welcome.gif') # 加载图片
image = canvas.create_image(0, 0, anchor='nw', image=image_file)
canvas.place(x=50, y=50)

# 填入用户信息
tk.Label(window, text='User name: ').place(x=10, y=250)
tk.Label(window, text='User password: ').place(x=10, y=290)

var_name = tk.StringVar()
var_password = tk.StringVar()
entry_name = tk.Entry(window, textvariable=var_name)
entry_name.place(x=200,y=250)
entry_password = tk.Entry(window, textvariable=var_password)
entry_password.place(x=200,y=290)

# 创建登入和新建按钮
def login_in():
    pass
def sign_in():
    pass
but_login = tk.Button(window, text='Login in', command=login_in)
but_login.place(x=170, y=330)
but_sign = tk.Button(window, text='Sign up', command=sign_in)
but_sign.place(x=270, y=330)

# 创建sign up界面
window_sign_up = tk.Toplevel(window)
window_sign_up>geometry('350x200')
window_sign_up.title('Sign up here.')


## 触发usr_login功能
user_name = var_name.get()
user_password = var_password.get()

## 设置异常捕获
try:
    with open('user_info.pickle', 'rb') as user_file:
        user_info = pickle.load(user_file)
except FileNotFoundError:
## 若没有读取到user_file文件，则创建，并将管理员的用户和密码
## 写入，即用户名为“admin”, 密码为“admin”
    with open('user_info.pickle', 'wb') as user_file:
        user_info = {'admin': 'admin'}
        pickle.dump(user_info, user_file)

# 匹配
if user_name in user_info:
    if user_password == user_info[user_name]:
        tk.messagebox.showinfo(title='Successful Login in!', message='How are you? '+user_name)
    else:
        tk.messagebox.showerror(title='Error!', message='Your information is wrong, try again.')
else:
    is_sign_up = tk.messagebox.askyesno('Welcome, you have not sign up yet. Sign up today?')
    if is_sign_up:
        user_sign_up()

# 运行
window.mainloop()