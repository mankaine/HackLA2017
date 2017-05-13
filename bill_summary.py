'''
Created on Apr 1, 2017
'''
import tkinter as tk 

UNIV_FONT   = ("Helvetica", 14)
HEADER_FONT = ("Helvetica", 20)
SUBHEADER_FONT = ("Helvetica", 16)
INITIAL_WIDTH   = 500
INITIAL_HEIGHT  = 500
CONSTANT_BKG    = "#FFFFFF"


class BillSummary: 
    def __init__(self, poltician, number):
        print(poltician)
        print(number)
        self._politician = poltician
        self._n = number 
        self._base_win = tk.Tk() 
        if number != -1: 
            self._base_win.title("Bill Summary") 
            self._show_summary(number) 
        else: 
            self._base_win.title("Error")
            self._show_error()
             
        
    def _show_summary(self, number):
        summary_text, title = self._politician.display_summary(number)
        summary_tk = tk.Message(master=self._base_win, text=title, justify=tk.LEFT, font=SUBHEADER_FONT, width=500)
        summary_tk.grid(row=0, column=0)

        summary_tk = tk.Message(master=self._base_win, text=title, justify=tk.LEFT, font=SUBHEADER_FONT, width=500)
        summary_tk.grid(row=0, column=0)
        
        if summary_text.strip() == "":
            summary_tk = tk.Message(master=self._base_win, text=summary_text, justify=tk.LEFT, font=UNIV_FONT, width=500)
            summary_tk.grid(row=1, column=0)
        else: 
            summary_tk = tk.Message(master=self._base_win, text=summary_text, justify=tk.LEFT, font=UNIV_FONT, width=500)
            summary_tk.grid(row=1, column=0)
        
    def _show_error(self):
        summary_tk = tk.Message(master=self._base_win, text="An error has occured :(", justify=tk.LEFT, font=SUBHEADER_FONT, width=500)
        summary_tk.grid(row=0, column=0)
        
        summary_tk = tk.Message(master=self._base_win, text="Please close this window to view another bill.", justify=tk.LEFT, font=UNIV_FONT, width=500)
        summary_tk.grid(row=1, column=0)

    
    
    def run(self):
        self._base_win.mainloop()
        
        