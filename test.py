import tkinter as tk
import tkinter.messagebox as mbox


# 定义MainUI类表示应用/窗口，继承Frame类
class MainUI(tk.Frame):
    # Application构造函数，master为窗口的父控件
    def __init__(self, master=None):
        # 初始化Application的Frame部分
        tk.Frame.__init__(self, master)
        # 显示窗口，并使用grid布局
        self.grid()
        # 创建控件
        self.createWidgets()

    # 创建控件
    def createWidgets(self):
        # 创建一个标签，输出要显示的内容
        self.firstLabel = tk.Label(
            self, text="--------------Created by Al--------------")
        # 设定使用grid布局
        self.firstLabel.grid()
        # 创建一个按钮，用来触发answer方法
        self.clickButton = tk.Button(self, text="Click it!", command=self.answer)
        # 设定使用grid布局
        self.clickButton.grid()

    def answer(self):
        # 我们通过messagebox来显示一个提示框
        mbox.showinfo("Al_Test", '''My QQ:2575442820''')


# 创建一个MainUI对象
app = MainUI()
# 设置窗口标题
app.master.title('Al_Test')
# 设置窗体的大小
app.master.geometry('400x100')
# 主循环开始
app.mainloop()