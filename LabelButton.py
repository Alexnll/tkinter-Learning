import tkinter as tk
# 主体框架
window = tk.Tk()
window.title("my window")
window.geometry("1000x1000")
var = tk.StringVar()      # 文字变量存储器 
# 点击命令设置
on_hit = False
def hit_me():
    global on_hit
    if on_hit == False:
        on_hit = True
        var.set('you hit me')
    else:
        on_hit = False
        var.set(" ")
# 窗口内容
l = tk.Label(window,
            textvariable=var,        # 标签文字
            bg='green',         # 背景颜色
            font=('Arial, 12'), # 字体
            width=30, height=10  # 标签长宽
            )
l.pack()   # 固定窗口位置
# 按钮
b = tk.Button(window,
            text='hit me',
            width=15, height=20,
            command=hit_me)
b.pack()

window.mainloop()