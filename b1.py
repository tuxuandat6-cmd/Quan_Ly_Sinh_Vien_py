# import thư viện tkinter
import tkinter as tk
root = tk.Tk()   # tạo cửa sở chính, Tk() tạo cửa sổ gốc, root bién đại diện cho toàn cửa sổ
 # Creating a label widget
myLabel = tk.Label(root, text='Hello World')   #hiện thị chữm root là có label nằm trong
 # shovingit onto the screen
myLabel.pack(expand = True)  #pack() quanr lý bố cục, nếu kh có thif sex kh hiển thị, expand = True cho phép widget mở rộng
root.mainloop()  #chạy vòng lặp giao diện, nếu kh có thì chương trình chạy xong sẽ tắt luôn