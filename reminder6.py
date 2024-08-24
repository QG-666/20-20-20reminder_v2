import tkinter as tk
import pystray
from pystray import MenuItem as Item
from PIL import Image, ImageTk
import threading


def show_reminder():
    global reminder_window
    reminder_window = tk.Toplevel()
    reminder_window.title("Reminder")

    # 设置自定义图标
    icon = Image.open("icon2.png")
    message_icon = ImageTk.PhotoImage(icon)
    reminder_window.iconphoto(False, message_icon)

    # 创建一个标签并添加到提醒窗口
    label = tk.Label(reminder_window, text="Take a 20-second break and look at something 20 feet away!")
    label.pack(pady=20, padx=20)

    # 更新窗口大小以适应内容
    reminder_window.update_idletasks()
    reminder_window.geometry(f"{reminder_window.winfo_width()}x{reminder_window.winfo_height()}")

    root.after(1200, show_reminder)  # 20分钟 = 1200000毫秒


def quit_app(icon, _):
    icon.stop()
    if reminder_window:
        reminder_window.destroy()
    root.quit()


def setup_tray():
    tray_icon = pystray.Icon("20-20-20 Reminder")
    tray_icon.icon = Image.open("icon2.png")  # 使用现成的图标文件
    tray_icon.menu = pystray.Menu(Item('Quit', quit_app))
    tray_icon.run()


# 创建主窗口
root = tk.Tk()
root.withdraw()  # 隐藏主窗口

# 初始化提醒窗口变量
reminder_window = None

# 设置第一个20分钟的提醒
root.after(1200, show_reminder)  # 20分钟 = 1200000毫秒

# 启动系统托盘图标线程
threading.Thread(target=setup_tray).start()

# 运行Tkinter主循环
root.mainloop()
