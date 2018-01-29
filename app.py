import tkinter as tk
from analyser import ContmanAnalyser


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master.minsize(width=300, height=500)
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.winfo_toplevel().title("Keyword analyser")
        self.uri = tk.Entry(self, width=40)
        self.uri.insert(0, "https://www.w3schools.com/tags/tag_meta.asp")
        self.uri.pack(side="top")

        self.analyse = tk.Button(self, text="Analyse", command=self.analyse)
        self.analyse.pack(side="top")

        self.infoList = tk.Listbox()
        self.infoList.pack(side="left", fill=tk.BOTH, expand=1)
        self.scroll = tk.Scrollbar()
        self.scroll.pack(side="right", fill=tk.Y)
        self.infoList.config(yscrollcommand=self.scroll.set)
        self.scroll.config(command=self.infoList.yview)

    def analyse(self):
        uri = self.uri.get()
        self.infoList.delete(0, tk.END)
        try:
            anlzr = ContmanAnalyser(uri)
        except ValueError:
            self.infoList.insert(tk.END, "Wrong URI format")

        counted_words = anlzr.count_words()
        if len(counted_words) == 0:
            self.infoList.insert(tk.END, "No keywords found in meta tags")
        for entry in counted_words:
            self.infoList.insert(tk.END, entry + ": " +str(counted_words[entry]))
        print(anlzr.count_words())


root = tk.Tk()
app = Application(master=root)
app.mainloop()
