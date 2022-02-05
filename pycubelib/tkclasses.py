import tkinter as tk

tkfont = 'Consolas 12'


def tkwindow(title, window=(20, 20, 500, 300), bg='gray75'):
    tkw = tk.Tk()
    tkw.title(title)
    x0, y0, ax, ay = window
    tkw.geometry(f'{ax}x{ay}+{x0}+{y0}')
    tkw.iconbitmap('pycubelib\hcube.ico')
    tkw.config(bg=bg)
    return tkw


def tkframe(tkw, window=(10, 10, 100, 100), bg='gray85'):
    x, y, w, h = window
    tkf = tk.Frame(tkw, bg=bg, width=w, height=h, relief=tk.RAISED)
    tkf.place(x=x, y=y)
    return tkf


class CmdButton:
    def __init__(self, frame, xyw, text='button', off_color='orange', on_color='yellow'):
        x, y, w = xyw
        self.button = tk.Button(frame, text=text, bg=off_color, width=w, font=tkfont)
        self.button.place(x=x, y=y)
        self.off_color = off_color
        self.on_color = on_color

    def command(self, command):
        self.button.config(command=command)

    def on(self):
        self.button['bg'] = self.on_color

    def off(self):
        self.button['bg'] = self.off_color

    def is_on(self):
        return self.button['bg'] == self.on_color

    def switch(self):
        if self.is_on():
            self.off()
        else:
            self.on()

    def color(self, color):
        self.button['bg'] = color


class ParamEntry:
    def __init__(self, frame, xyw, label='entry', val=0, bg='white'):
        x, y, w = xyw
        self.entry = tk.Entry(frame, font=tkfont, justify=tk.CENTER)
        self.entry['width'] = w
        self.entry['bg'] = bg
        self.entry.place(x=x, y=y)
        self.set_entry(val)
        self.lbl = tk.Label(frame, text=label, font=tkfont, bg=frame['bg'])
        self.lbl.place(x=x+w, y=y)
        frame.update_idletasks()
        lw = self.lbl.winfo_width()
        self.lbl.place(x=x-lw-5, y=y)

    def set_entry(self, val):
        self.entry.delete(0, tk.END)
        self.entry.insert(0, val)
        self.entry.xview_moveto(1.)

    def get_val(self, typ=int):
        try:
            val = typ(self.entry.get())
        except ValueError:
            if typ == str:
                val = ''
            else:
                val = 0
        return val

    def right(self):
        self.entry.config(justify=tk.RIGHT)

    def get_list_val(self, typ=int):
        aa = self.entry.get()
        bb = aa.split(',')
        cc = [typ(b) for b in bb]
        return cc


class ProgressBar:
    def __init__(self, frame, xyw, bxw, label='progress', val=0):
        import tkinter.ttk as ttk
        x, y, w = xyw
        bx, bw = bxw
        self.entry = ParamEntry(frame, xyw=xyw, label=label, val=0, bg='gray85')
        self.prog = ttk.Progressbar(frame)
        self.prog.place(x=bx, y=y+30, width=bw, height=15)

        self.setval(val)
        frame.update_idletasks()

    def setval(self, val):
        self.prog['value'] = val
        self.entry.set_entry(val)
        self.prog.update_idletasks()

    def getval(self):
        val = self.prog['value']
        return val


class ScaleBar():
    def __init__(self, frame, xyw, vminmax=(0, 100), label='scalebar'):
        x, y, w = xyw
        vmin, vmax = vminmax
        self.slilder = tk.Scale(frame, orient=tk.HORIZONTAL, font=tkfont, bg='gray85')
        self.slilder.place(x=x, y=y)
        self.slilder['length'] = w
        self.slilder['from_'] = vmin
        self.slilder['to'] = vmax
        self.lbl = tk.Label(frame, text=label, font=tkfont, bg=frame['bg'])
        # self.lbl.place(x=x-30, y=y)
        self.lbl.place(x=x+w, y=y)
        frame.update_idletasks()
        lw = self.lbl.winfo_width()
        self.lbl.place(x=x-lw-5, y=y)


    # def set_max(self, vmax):
    #     self.slilder['to'] = vmax
    #     tick = vmax - 1
    #     self.slilder['tickinterval'] = tick

    # def get_max(self):
    #     return self.slilder['to']

    def set_val(self, value):
        self.slilder.set(value)

    def get_val(self):
        return self.slilder.get()

    # def command(self, comm):
    #     self.slilder.config(command=comm)



class TextBox:
    def __init__(self, frame, xywh, label='textbox'):
        x, y, w, h = xywh
        self.txtbox = tk.Text(frame)
        self.txtbox.place(x=x, y=y, width=w, height=h)
        self.label = tk.Label(frame, text=label, bg=frame['bg'])
        self.label.place(x=x, y=y-20)

    def update(self, text):
        self.txtbox.delete('1.0', tk.END)
        self.txtbox.insert('1.0', text)


if __name__ == '__main__':
    tkw = tkwindow(title='fp')

    btn1 = CmdButton(tkw, xyw=(100, 50, 10))
    ent1 = ParamEntry(tkw, xyw=(100, 100, 30))
    aaa = [11, 22, 33, 44, 55]
    ent1.set_entry(aaa)
    c = ent1.get_list_val()
    print(f'c = {c}')
    prog = ProgressBar(tkw, xyw=(100, 150, 100))
    prog.setval(75)
    txtbox = TextBox(tkw, xywh=(100, 200, 300, 50))
    txtbox.update('Simple is better than complex. \nComplex is better than complicated.')

    tk.mainloop()
