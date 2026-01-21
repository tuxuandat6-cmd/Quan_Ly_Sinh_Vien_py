#import thư viện và gọi thư viện của file data
from tkinter import *
from dataQLSV import *

# hàm xử lí của các chức năng
#hàm hiển thị danh sách
def show():
    listbox.delete(0, END)  #xóa toàn bộ dữ liệu đang có trong listbox
    sv = read()   #đọc dữ liệu
    for i in sv:    #duyệt từng sinh viên và hiển thị lên listbox
        listbox.insert(END, i)
#hàm thêm sinh viên vào listbox
def add():
    if student_id.get() == "" or name.get() == "" or year.get() == "":  #kiểm tra nếu chưa nhập đủ thông tin thì kh làm gì cả
        return

    line = f"{student_id.get()} - {name.get()} - {year.get()}"  #ghép dữ liệu vào 1 dòng text
    save(line)  #gọi hàm save để lưu xuống file
    show()  #cập nhật listbox
    #xóa trắng ô sau khi nhập
    student_id.set("")
    name.set("")
    year.set("")

def delete():
    selected = listbox.curselection()   #lấy vị trí dòng được chọn
    if not selected:  #nếu chưa chọn dòng nào thì kh xóa
        return

    value = listbox.get(selected[0]) #lấy nội dung được chọn
    delete_by_value(value)  #xóa sv khỏi file
    show()

def sort_sv():
    sv = read()
    sv.sort(key=lambda x: x.split(" - ")[2])  # sắp xếp theo năm sinh

    listbox.delete(0, END) #xóa list cũ
    for i in sv:
        listbox.insert(END, i)

#giao diện của chương trình
root = Tk()  #tạo cửa sổ GUI

student_id = StringVar() #biến liên kết với entry
name = StringVar()
year = StringVar()
#đặt tiêu đề và setting size
root.title("Quản Lý Sinh Viên")
root.minsize(500, 500)

root.grid_rowconfigure(1, weight=1)
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)

Label(
    root,
    text="ỨNG DỤNG QUẢN LÝ SINH VIÊN",
    fg="red",
    font=("Cambria", 16),
    width=25
).grid(row=0, column=0, columnspan=2, pady=10)

listbox = Listbox(root)
listbox.grid(row=1, column=0, columnspan=2, sticky="nsew", padx=10)

Label(root, text='Mã Sinh Viên:').grid(row=2, column=0, sticky=E, padx=5)
Entry(root, textvariable=student_id,width=28).grid(row=2, column=1, sticky="ew", padx=5)

Label(root, text='Tên Sinh Viên:').grid(row=3, column=0, sticky=E, padx=5)
Entry(root, textvariable=name,width=28).grid(row=3, column=1, sticky="ew", padx=5)

Label(root, text='Năm Sinh:').grid(row=4, column=0, sticky=E, padx=5)
Entry(root, textvariable=year,width=28).grid(row=4, column=1, sticky="ew", padx=5)

btn = Frame(root)
btn.grid(row=5, column=1, sticky="w", pady=10)

Button(btn, text="Thêm", command=add).pack(side=LEFT)
Button(btn, text="Xóa", command=delete).pack(side=LEFT)
Button(btn, text="Sắp xếp", command=sort_sv).pack(side=LEFT)
Button(btn, text="Thoát", command=root.quit).pack(side=LEFT)

show()
root.mainloop()