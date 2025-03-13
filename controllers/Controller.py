class Controller:
    def __init__(self, model, view):
        self.model = model
        self.view = view

        #Nupu callback
        self.btn_convert_callback()

        #Enter klahviga toimib konventeeri nupp
        self.view.bind('<Return>', lambda event: self.btn_convert_click())

    def btn_convert_callback(self):
        self.view.set_btn_convert_callback(self.btn_convert_click)

    def btn_convert_click(self):
        self.model.get_user_input(self.view.num_input.get().strip().replace(',', '.'))
        self.model.convert_currency(self.view.cmb_cfrom.get(), self.view.cmb_cto.get())
        self.view.lbl_result.config(text=f'{self.model.result:.2f} {self.view.cmb_cto.get()}')