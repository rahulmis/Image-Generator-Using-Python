def choose_color():
    color_code = colorchooser.askcolor()
    colorentrybox.delete(0, END)
    colorentrybox.insert(END, "{},{},{}".format(int(color_code[0][0]), int(color_code[0][1]), int(color_code[0][2])))

def createimage():
    color = colorentrybox.get()
    extension = extensionentrybox.get()
    name = imagenameentrybox.get()
    imagenumber = imagenumberentrybox.get()
    width = int(widthentrybox.get())
    height = int(heightentrybox.get())
    url = filedialog.askdirectory()
    convertstatuslabel.configure(text="{} - Creating Image ----------".format(imagenumber))
    col = color.split(',')
    colorname = []
    try:
        for i in col:
            colorname.append(int(i))
        colorname = tuple(colorname)
    except:
        colorname = col[0]
    for i in range(int(imagenumber)):
        path = url + '/{}{}{}'.format(name, i+1, extension)
        im = Image.new("RGB", (width, height), color=colorname)
        im.save(path)
    convertstatuslabel.configure(text="{} - Images Created Sucessfully ------".format(imagenumber))


from tkinter import *
from tkinter import colorchooser, filedialog
from PIL import Image

root = Tk()
root.title("Blank Image Generator")
root.iconbitmap('logo.ico')
root.resizable(False, False)
root.geometry('712x508+300+100')
root.configure(bg='green yellow')


############################################################# Labels

colorlabel = Label(root, text='Color        : ', font=('arial', 20, ' bold'), bg='green yellow')
colorlabel.place(x=50, y=10)

extensionlabel = Label(root, text='Extension : ', font=('arial', 20, ' bold'), bg='green yellow')
extensionlabel.place(x=50, y=80)

widthlabel = Label(root, text='Width        : ', font=('arial', 20, ' bold'), bg='green yellow')
widthlabel.place(x=50, y=150)

heightlabel = Label(root, text='Height       : ', font=('arial', 20, ' bold'), bg='green yellow')
heightlabel.place(x=50, y=220)

numberlabel = Label(root, text='Images No: ', font=('arial', 20, ' bold'), bg='green yellow')
numberlabel.place(x=50, y=290)

imagenamelabel = Label(root, text='Name        : ', font=('arial', 20, ' bold'), bg='green yellow')
imagenamelabel.place(x=50, y=360)

convertstatuslabel = Label(root, text='', font=('arial', 20, ' bold'), bg='green yellow', width=40)
convertstatuslabel.place(x=10, y=465)

######################################################################  Entry Box
colorentrybox = Entry(root, font=('arial', 14, 'italic bold'),
                      bg='blue', relief=RIDGE, bd=5, justify='center', selectbackground='white',
                      selectforeground='black', fg='yellow')
colorentrybox.insert(END, "255,0,0")
colorentrybox.place(x=230, y=10, height=45, width=350)

extensionentrybox = Entry(root, font=('arial', 20, 'italic bold'), width=30, bg='blue', relief=RIDGE, bd=5,
                          justify='center', selectbackground='white', selectforeground='black', fg='yellow')
extensionentrybox.insert(END, ".png")
extensionentrybox.place(x=230, y=80)

widthentrybox = Entry(root, font=('arial', 14, 'italic bold'), bg='blue', relief=RIDGE, bd=5,
                      justify='center', selectbackground='white', selectforeground='black', fg='yellow')
widthentrybox.insert(END, "800")
widthentrybox.place(x=230, y=150, height=45, width=460)

heightentrybox = Entry(root, font=('arial', 14, 'italic bold'), bg='blue', relief=RIDGE, bd=5,
                       justify='center', selectbackground='white', selectforeground='black', fg='yellow')
heightentrybox.insert(END, "800")
heightentrybox.place(x=230, y=220, height=45, width=460)

imagenumberentrybox = Entry(root, font=('arial', 14, 'italic bold'), bg='blue', relief=RIDGE, bd=5,
                            justify='center', selectbackground='white', selectforeground='black', fg='yellow')
imagenumberentrybox.insert(END, "5")
imagenumberentrybox.place(x=230, y=290, height=45, width=460)

imagenameentrybox = Entry(root, font=('arial', 14, 'italic bold'), bg='blue', relief=RIDGE, bd=5,
                          justify='center', selectbackground='white', selectforeground='black', fg='yellow')
imagenameentrybox.insert(END, "RedImages")
imagenameentrybox.place(x=230, y=360, height=45, width=460)

################################################################################## Buttons


button = Button(root, text="Select color", font=('arial', 10, ' bold'), width=52, bd=5, relief=RIDGE,
                bg='red', activebackground='blue', activeforeground='white', command=choose_color)
button.place(x=590, y=10, height=45, width=100)

Convertsinglebtn = Button(root, text='Create Coloured Images', font=('arial', 15, ' bold'), width=52, bd=5,
                          relief=RIDGE, bg='red', activebackground='blue', activeforeground='white',
                          command=createimage)
Convertsinglebtn.place(x=50, y=410, height=45)

root.mainloop()
