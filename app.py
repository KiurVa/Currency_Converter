from controllers.Controller import Controller
from models.CurrencyConverter import CurrencyConverter
from views.View import View

if __name__ == '__main__':
    model = CurrencyConverter()
    view = View(model)
    Controller = Controller(model, view)
    view.mainloop()