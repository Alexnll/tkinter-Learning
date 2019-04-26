import tkinter as tk
# 创建主窗口
window = tk.Tk()
window.title('ListBox')
window.geometry('200x200')
# 创建label用于显示
var1 = tk.StringVar()
var1.set('hello')
l = tk.Label(window,bg='yellow', width=4, textvariable=var1)
l.pack()
# 创建一个listbox和变量var2
var2 = tk.StringVar()
var2.set((11,22,33,44))

lb = tk.Listbox(window, listvariable=var2)
list_item = [1,2,3,4]
for item in list_item:
    lb.insert('end', item)
lb.insert('0', 'first')
lb.insert('2', 'second')
lb.delete(2)
lb.pack()
# mainloop
window.mainloop()