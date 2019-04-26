import tkinter as tk
# 窗口声明
window = tk.Tk()
window.title('my window')
# 窗口p尺寸
window.geometry('200x200')
# 窗口内容-控件
# 定义触发按钮的函数
def insert_point():
    var = e.get()
    t.insert('insert',var)

def insert_end():
    var = e.get()
    t.insert('end',var)
# 按钮
b1 = tk.Button(window, text='insert point',
                width=15, 
                height=2, 
                command=insert_point)
b1.pack()

b2 = tk.Button(window,
                text='insert end',
                width=15, 
                height=2, 
                command=insert_end)
b2.pack()
# 创建输入框entry
e = tk.Entry(window, show='*')
e.pack()
# 创建文本框
t = tk.Text(window, height=2)
t.pack()

# 显示
window.mainloop()