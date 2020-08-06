"""
this class helps us to visualize a new song
It helps the user see it in a popup window
"""

import tkinter as tkinter
WINDOWSIZE=800

class SongVisual():
    def __init__(self, lines):
        self.lines=lines
        canvas=self.make_canvas(WINDOWSIZE,'Song Inspiration')
        self.draw_background(canvas)
        self.show_song(canvas)
        canvas.mainloop()


    def make_canvas(self, size, name=None):
        top = tkinter.Tk()
        top.minsize(width=2*size + 10, height=size + 10)
        if name:
            top.title(name)
        canvas = tkinter.Canvas(top, width=2*size + 1, height=size + 1)
        canvas.pack()
        canvas.xview_scroll(8, 'units')  # This is so (0, 0) works correctly,
        canvas.yview_scroll(8, 'units')  # otherwise it's clipped off
        self.top=top
        return canvas

    def draw_background(self,canvas):
        width=WINDOWSIZE*2
        height=WINDOWSIZE
        color='magenta'
        canvas.create_rectangle(8,8, WINDOWSIZE*2, WINDOWSIZE, fill=color)

    def show_song(self, canvas):
        x=30
        y=30
        for line in self.lines:
            print(line)
            text_instance=canvas.create_text(x,y, anchor="w", font=("Times", 13), text=line)
            x+= 3
            y += 25
        canvas.mainloop()

        print(self.lines)

    #def add_song(self, lines):