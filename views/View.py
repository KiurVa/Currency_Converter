from tkinter import *
from tkinter import font
from tkinter.ttk import Combobox


class View(Tk):
    def __init__(self, model):
        super().__init__()
        self.model = model

        #Põhiaken
        self.__width = 500
        self.__height = 260
        self.title("Valuuta konverter")
        self.center(self.__width, self.__height)

        # Kirjastiilid
        self.__default = font.Font(family='Arial', size=10)
        self.__header = font.Font(family='Arial', size=10, weight='bold')

        #Kogu vormi stiil
        self.option_add('*Font', self.__default) #Määrab fondiks default

        #Ettemääratud valuutad
        self.__currencies = ['EUR', 'USD', 'GPD', 'JPY']

        #loome frame-id
        self.__frame_top, self.__frame_middle = self.create_frames()

        #Loome label-id
        self.__lbl_result = self.create_labels()

        #Loome nupu
        self.__btn_convert = self.create_button()

        #Loome sisestuskasti
        self.__num_input = self.create_entry()

        #Loome comboboxid
        self.__cmb_cfrom, self.__cmb_cto = self.create_combobox()




    def center(self, w, h): #Paigutab akna ekraani keskele
        x = int((self.winfo_screenwidth() / 2) - (w / 2))
        y = int((self.winfo_screenheight() / 2) - (h / 2))
        self.geometry(f'{w}x{h}+{x}+{y}')

    def create_frames(self):
        top = Frame(self, background="light blue")
        middle = Frame(self, background="light yellow")

        #Paigtab põhiaknale
        top.pack(fill=BOTH, expand=True)
        middle.pack(fill=BOTH)
        return top, middle

    def create_labels(self):
        Label(self.__frame_top, text='Konverteeritav summa', font=self.__header).grid(row=0, column=0,
                                                                                      padx=10, pady=5, sticky=EW)
        Label(self.__frame_top, text='Alus valuuta', font=self.__header).grid(row=1, column=0, padx=10, pady=5, sticky=EW)
        Label(self.__frame_top, text='Siht valuuta', font=self.__header).grid(row=2, column=0, padx=10, pady=5, sticky=EW)
        Label(self.__frame_top, text='Tulemus', font=self.__header).grid(row=4, column=0, padx=10, pady=5, sticky=EW)
        result = Label(self.__frame_top, text='0.00')
        result.grid(row=4, column=1, padx=10, pady=5, sticky=EW)

        return result

    def create_button(self):
        convert = Button(self.__frame_top, text='Konverteeri', font=self.__header)
        convert.grid(row=3, column=0, padx=10, pady=5, columnspan=2, sticky=EW)
        return convert

    def create_entry(self):
        num = Entry(self.__frame_top)
        num.focus()
        num.grid(row=0, column=1, padx=10, pady=5, sticky=EW)
        return num

    def create_combobox(self):
        cfrom = Combobox(self.__frame_top, state='readonly')
        cto = Combobox(self.__frame_top, state='readonly')
        cfrom['values'] = self.__currencies
        cto['values'] = self.__currencies
        cfrom.current(0)
        cto.current(1)
        cfrom.grid(row=1, column=1, padx=10, pady=5, sticky=EW)
        cto.grid(row=2, column=1, padx=10, pady=5, sticky=EW)
        return cfrom, cto



