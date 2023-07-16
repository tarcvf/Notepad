import tkinter as tk
from tkinter import ttk
from tkinter.filedialog import asksaveasfile, askopenfile,asksaveasfilename
from tkinter import messagebox as msg
import webbrowser
from requests import get as GetUrl
import qrcode
class main():
    def __init__(self) -> None:
        self.dir = None
        self.main()
    def saveas(self):
        print(self.texto.get("1.0","end-1c"))
        arquivo = asksaveasfile(mode= "w",title="salvar").name
        with open(arquivo,"w") as file:
            file.write(self.texto.get("1.0","end-1c")) 
            self.janela.title(arquivo)
            self.dir  = arquivo
    def openarq(self):
        arquivo = askopenfile("r",title="abrir").name
        with open(arquivo) as file:
            self.texto.delete("1.0","end")
            self.texto.insert("1.0",file.read())
            self.janela.title(arquivo)
            self.dir = arquivo
    def novo(self):
        self.janela.title("NotepadClone - Novo")
        self.texto.delete("1.0","end")
        self.dir = None
    def salvar(self):
        if self.dir == None:
            self.saveas()
            return
        with open(self.dir,"w") as file:
            file.write(self.texto.get("1.0","end-1c"))
    def autor(self):
        webbrowser.open("https://www.linkedin.com/in/fabr%C3%ADcio-reinaldo-8a1a2024b/")
            
    def licensa(self):
        
        self.janela.title("Carregando licensa...")
        try:
            dados = GetUrl("https://www.gnu.org/licenses/gpl-3.0.txt")
            self.texto.delete("1.0","end")
            self.texto.insert("1.0",dados.text)
            self.janela.title("Licensa Geral GNU")
        except Exception as e:
            msg.showerror("erro","Não foi possivel carregar a licensa\n{}".format(e))
            self.janela.title("NotepadClone - Novo")
            self.dir = None
    def darkyellow(self):
        self.texto.config(foreground="#ffff00",background="#000000",insertbackground="#0000ff")
        self.menubar.config(foreground="#ffff00",background="#000000")
        self.janela.config(background="#000000")
    def lightpadr(self):
        self.texto.config(foreground="#000000",background="#ffffff",insertbackground="#000000")
        self.menubar.config(foreground="#000000",background="#cccccc")
        self.janela.config(background="#000000")
    def darkblue(self):
        self.texto.config(foreground="#0000cc",background="#000000",insertbackground="#ffff00")
        self.menubar.config(foreground="#0000cc",background="#000000")
        self.janela.config(background="#000000")
    def darkwhite(self):
        self.texto.config(foreground="#ffffff",background="#000000",insertbackground="#ffffff")
        self.menubar.config(foreground="#ffffff",background="#000000")
        self.janela.config(background="#000000")
    def ExpQrcode(self):
        try:
            nomearq = asksaveasfilename(defaultextension=".png")
            qr = qrcode.QRCode(version=40)
            qr.add_data(self.texto.get("1.0","end"))
            qr.make(fit=True)
            img = qr.make_image()
            img.save(nomearq)
        except Exception as e:
            msg.showerror("erro","Não foi possivel exportar o arquivo\n{}".format(e))







        
        
    
    def main(self):
        print("começando...")
        
        self.janela = tk.Tk()
        self.janela.title("NotepadClone - Novo")
        self.texto = tk.Text(self.janela)
        #self.janela.geometry("400x400")
        self.menubar = tk.Menu(master=self.janela)
        menu = tk.Menu(self.menubar,tearoff=False)
        sobre = tk.Menu(self.menubar,tearoff=False)
        Linguagem = tk.Menu(self.menubar,tearoff=False)
        editar = tk.Menu(self.menubar,tearoff=False)
        tema = tk.Menu(editar,tearoff=False)
        
        menu.add_command(label="Abrir",command=self.openarq)
        menu.add_command(label="Novo",command=self.novo)
        menu.add_command(label="salvar",command=self.salvar)
        menu.add_command(label="Salvar como...",command=self.saveas)
        self.menubar.add_cascade(label="arquivo",menu=menu)
        self.menubar.add_cascade(label="Editar",menu=editar)
        self.menubar.add_cascade(label="Sobre",menu=sobre)
        sobre.add_command(label="autor(Linkedin)",command=self.autor)
        sobre.add_command(label="Licença",command=self.licensa)
        editar.add_cascade(label="tema",menu=tema)
        tema.add_radiobutton(label="Dark yellow",command=self.darkyellow)
        tema.add_radiobutton(label="Dark blue",command= self.darkblue)
        tema.add_radiobutton(label="Dark white",command=self.darkwhite)
        tema.add_radiobutton(label="Light padrão",command=self.lightpadr,state="active")
        editar.add_command(label="Exportar QR Code",command=self.ExpQrcode)
        
        self.janela.config(menu=self.menubar)
        self.texto.pack(side="left",fill="both",expand=True)
        scr = ttk.Scrollbar(self.janela,command=self.texto.yview).pack(side="right",fill="y")
        self.janela.mainloop()

if __name__ == "__main__":
    main()
