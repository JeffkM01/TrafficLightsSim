from tkinter import *

class TrafficLights:
    def __init__(self):
        window = Tk()
        window.title("Traffic Lights")
        self.canvas = Canvas(window, width = "300", height = "400", bg = "white")
        self.buttonframe = Frame(window)
        self.canvas.pack()
        self.red_c = None
        self.yellow_c = None
        self.green_c = None

        red_b = Radiobutton(self.buttonframe, text = "Red", command=self.color_red)
        yellow_b = Radiobutton(self.buttonframe, text="Yellow", command=self.color_yellow)
        green_b = Radiobutton(self.buttonframe, text="Green", command=self.color_green)
        self.buttonframe.pack()
        self.create_shapes()
        red_b.grid(row=0, column=0, padx=10)
        yellow_b.grid(row=0, column=1, padx=10)
        green_b.grid(row=0, column=2, padx=10)

        window.geometry("700x500")
        window.mainloop()


    def create_shapes(self):
        self.canvas.create_rectangle(205, 365, 65, 10)
        self.red_c = self.canvas.create_oval(80, 15, 190, 120) #red
        self.yellow_c = self.canvas.create_oval(80, 130, 190, 240)  #yellow
        self.green_c = self.canvas.create_oval(80, 250, 190, 360)  #green

    def turn_off_lights(self):
        self.canvas.itemconfig(self.yellow_c, fill="white")
        self.canvas.itemconfig(self.green_c, fill="white")
        self.canvas.itemconfig(self.red_c, fill="white")

    def color_red(self):
        self.turn_off_lights()
        self.canvas.itemconfig(self.red_c, fill="red")

    def color_green(self):
        self.turn_off_lights()
        self.canvas.itemconfig(self.green_c, fill="green")

    def color_yellow(self):
        self.turn_off_lights()
        self.canvas.itemconfig(self.yellow_c, fill="yellow")

TrafficLights()
