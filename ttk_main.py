from tkinter import *
from tkinter.ttk import *
import subprocess
import os
import threading
from PIL import Image, ImageTk
from weibo import import_run


# 工作目录改为文件所在目录
os.chdir(os.path.dirname(os.path.abspath(__file__)))

def run_weibo():
    # subprocess.Popen("python weibo.py", shell=True)
    import_run()

def btn_start():
    with open("userinfo.ini", "w", encoding="utf-8") as f:
        content = f"uid={user_id_entry.get()}\n"
        content += f"cookie={cookie_entry.get()}\n"
        content += f"downloadDirRoot={path_entry.get().encode('utf-8').decode()}\n"
        f.write(content)
    subprocess_process = threading.Thread(target=run_weibo)
    subprocess_process.start()


def btn_exit():
    os._exit(0)

def open_question_window():
    top_window = Toplevel()
    # 创建一个toplevel显示图片，PhotoImage对象只能在一个线程下使用
    top_window.title("使用说明")
    # 打开图片
    image = Image.open("static/cookie.png")  # 替换为你的图片文件路径
    # 将图像转换为PhotoImage以便在Tkinter中使用
    photo = ImageTk.PhotoImage(image)

    # 创建一个标签以显示图像
    label = Label(top_window, image=photo)
    label.pack()
    top_window.mainloop()

# 读取配置文件，填充到文本框
def load_config_to_text_fields():
    try:
        with open("userinfo.ini", "r", encoding="utf-8") as f:
            lines = f.readlines()
            for line in lines:
                if line.startswith("uid="):
                    user_id_entry.delete(0, END)
                    user_id_entry.insert(0, line[len("uid="):].strip())
                elif line.startswith("cookie="):
                    cookie_entry.delete(0, END)
                    cookie_entry.insert(0, line[len("cookie="):].strip())
                elif line.startswith("downloadDirRoot="):
                    path_entry.delete(0, END)
                    path_entry.insert(0, line[len("downloadDirRoot="):].strip())
    except FileNotFoundError:
             with open("userinfo.ini", "a", encoding="utf-8") as f:
                pass

# ---------------------------------------------------------------------------------
class WinGUI(Tk):
    def __init__(self):
        super().__init__()
        self.__win()
        self.__ttk_style()
        self.__tk_lable_logo = self.__tk_lable_logo()
        self.__tk_lable_title = self.__tk_lable_title()
        self.__tk_lable_id = self.__tk_lable_id()
        self.__tk_entry_id = self.__tk_entry_id()
        self.__tk_lable_cookie = self.__tk_lable_cookie()
        self.__tk_entry_cookie = self.__tk_entry_cookie()
        self.__tk_lable_path = self.__tk_lable_path()
        self.__tk_entry_path = self.__tk_entry_path()
        self.__tk_button_start = self.__tk_button_start()
        self.__tk_button_exit = self.__tk_button_exit()
        self.__tk_button_question = self.__tk_button_question()
        self.__tk_lable_info = self.__tk_lable_info()

    def __ttk_style(self):
        style = Style()
        style.configure("Label", foreground="black", background="pink", font=("微软雅黑", 16, "bold"))
        style.configure("TLabel", foreground="black", background="pink", font=("微软雅黑", 10, "bold"))
        style.configure("TButton", foreground="black", font=("微软雅黑", 10))


    def __win(self):
        # 图标
        self.iconbitmap("static/weibo_icon.ico")
        # 标题
        self.title("微博图片批量下载器_v0.1 - By dhwark")
        # 设置窗口大小、居中
        width = 400
        height = 300
        screenwidth = self.winfo_screenwidth()
        screenheight = self.winfo_screenheight()
        geometry = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        self.geometry(geometry)
        
        self.resizable(width=False, height=False)
        self.config(bg="pink")
        # 透明度
        self.attributes("-alpha", 0.95)

    # 放一张图片在标题上
    def __tk_lable_logo(self):
        # 打开图片
        image = Image.open("static/weibo_icon.ico")  # 替换为你的图片文件路径
        image = image.resize((40, 40))
        # 将图像转换为PhotoImage以便在Tkinter中使用
        self.photo = ImageTk.PhotoImage(image)
        logo = Label(image=self.photo)
        logo.place(x=180, y=10)
        return logo


    def __tk_lable_title(self):
        # 标题
        title_text = Label(text="微博图片批量下载器", style="Label")
        title_text.place(x=100, y=50)
        return title_text

    def __tk_lable_id(self):
        user_id = Label(text="ID:", style="TLabel")
        label_width = user_id.winfo_reqwidth()  # 获取标签的宽度
        user_id.place(x=150 - label_width, y=90)
        return user_id

    def __tk_entry_id(self):
        global user_id_entry
        user_id_entry = Entry(width=20)
        user_id_entry.place(x=170, y=90)
        return user_id_entry

    def __tk_lable_cookie(self):
        cookie = Label(text="cookie:", style="TLabel")
        # 使用place方法设置标签的位置并实现右对齐
        label_width = cookie.winfo_reqwidth()  # 获取标签的宽度
        cookie.place(x=150 - label_width, y=140)
        return cookie

    def __tk_entry_cookie(self):
        global cookie_entry
        cookie_entry = Entry(width=25)
        cookie_entry.place(x=170, y=140)
        return cookie_entry

    def __tk_lable_path(self):
        path = Label(text="下载地址:", style="TLabel")
        label_width = path.winfo_reqwidth()  # 获取标签的宽度
        path.place(x=150 - label_width, y=190)
        return path

    def __tk_entry_path(self):
        global path_entry
        path_entry = Entry(width=20)
        path_entry.place(x=170, y=190)
        return path_entry

    def __tk_button_start(self):
        btn = Button(text="开始", style="TButton")
        btn.config(command=btn_start)
        btn.place(x=100, y=240,  width=50, height=30)
        return btn

    def __tk_button_exit(self):
        btn = Button(text="退出", style="TButton")
        btn.config(command=btn_exit)
        btn.place(x=250, y=240, width=50, height=30)
        return btn

    def __tk_button_question(self):
        # 添加一个问号图片按钮，调用打开一张本地图片
        # 打开并调整图片大小
        icon_image = Image.open("static/question_icon.png")  # 替换为你的图片文件路径
        icon_image = icon_image.resize((15, 15))  # 调整图片大小
        ###
        # 如果遇到图片不显示，可能是因为 ImagePhotoImage 对象被垃圾回收或没有被正确保存在引用中。
        # 确保 icon 是一个实例变量，而不仅仅是方法内的局部变量。如果你只在方法内创建 icon，它将在方法执行完毕后被销毁，导致图片不显示。
        ###
        self.icon = ImageTk.PhotoImage(icon_image)  # 将图像转换为PhotoImage
        btn = Button(image=self.icon, command=open_question_window)
        label_width = btn.winfo_reqwidth()  # 获取标签的宽度
        btn.place(x=350 + label_width, y=0)
        return btn

    def __tk_lable_info(self):
        info = Label(text="使用说明：", style="TLabel")
        info.place(x=305, y=0)
        return info

class Win(WinGUI):
    def __init__(self):
        super().__init__()
        self.__event_bind()

    def __event_bind(self):
        pass

# ---------------------------------------------------------------------------------
if __name__ == "__main__":
    # 先读取配置文件
    win = Win()
    load_config_to_text_fields()
    win.mainloop()