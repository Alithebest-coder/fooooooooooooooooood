import tkinter as tk
from tkinter import ttk,messagebox

class rms:
    def __init__(self,root):
        self.root=root
        self.root.title("Restaurent Management App")   
        self.menu_items={
            "tiny meal":25,
            "main meal":36,
            "drinks":10
        }
                
        frame=ttk.Frame(root)
        frame.place(relx=0.5,rely=0.5,anchor="center")        
        ttk.Label(frame, text="Restaurent order menu").grid(row=0,columnspan=3,padx=10,pady=10)
        
        self.menu_label={}        
        self.menu_quantities={}
        for i,(item,price) in enumerate(self.menu_items.items()):
            label=ttk.Label(frame,text=item)
            label.grid(row=i,column=0,padx=10,pady=10)
            self.menu_label[item]=label
            
            quantity_entry=ttk.Entry(frame,width=5)
            quantity_entry.grid(row=i,column=1,padx=10,pady=10)
            self.menu_label[item]=quantity_entry
            
            order_btn=ttk.Button(frame,text="place order",command=self.place_order)
            order_btn.grid(row=len(self.menu_items)+2,columnspan=3,padx=10,pady=10)
    def place_order(self):
        pass
if __name__=="__main__":
    root=tk.Tk()
    app=rms(root)
    root.geometry("800x600")
    root.mainloop()