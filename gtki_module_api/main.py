""" Модуль API для Gravity Tkinter Interface """
from gravity_core_api.main import GCSE

class GTKIAPI(GCSE):
    def __init__(self, myip, myport, core, debug=None, sqlshell=None, *args, **kwargs):
        super().__init__(myip, myport, sqlshell, core, debug=debug, sqlshell=sqlshell)

