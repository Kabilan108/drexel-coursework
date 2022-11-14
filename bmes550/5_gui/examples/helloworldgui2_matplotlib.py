#!python
#Example taken/adapted  from: https://stackoverflow.com/questions/10737459/embedding-a-matplotlib-figure-inside-a-wxpython-panel


import matplotlib
import numpy as np
import wx
from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigureCanvas


class HelloFrame(wx.Frame):
    def __init__(self, *args, **kw):
        super(HelloFrame, self).__init__(*args, **kw, size=wx.Size(1000,600))

        panel = wx.Panel(self)


        vsizer = wx.BoxSizer(wx.VERTICAL)
        
        topsizer =  wx.StaticBoxSizer(wx.VERTICAL,panel,"Buttons and controls")
        bottomsizer =  wx.BoxSizer(wx.HORIZONTAL)

        vsizer.Add(topsizer);
        vsizer.Add(bottomsizer,flag=wx.EXPAND);

        btn = wx.Button(panel,label='Click to draw')
        btn.Bind(wx.EVT_BUTTON, self.onokbuttonclick)
        btn.Bind(wx.EVT_ENTER_WINDOW, self.onmouseenter)

        # add an event handler for mouse-move to change the text to bold
        topsizer.Add(btn,0,wx.LEFT)
        self.button = btn;


        combo = wx.ComboBox(panel, -1, style = wx.CB_READONLY)
        combo.Append('apple')
        combo.Append('orange')
        combo.Append('cherry')
        combo.SetSelection(1)
        combo.Bind(wx.EVT_COMBOBOX, self.onfruitselection)
        topsizer.Add(combo,0,wx.LEFT)
        self.fruitcombobox = combo

        fig = matplotlib.figure.Figure()
        # we need to store the axes and canvas variables in "self" so we can
        #  make use of them later in other functions.
        self.axes = fig.add_subplot(1,1,1) #1-by-1 matrix axes, select the first one.
        self.canvas = FigureCanvas(panel, -1, fig)
        bottomsizer.Add(self.canvas,1,flag=wx.EXPAND)


        panel.SetSizer(vsizer)
        #self.Fit()

    def onmouseenter(self,evt):
        font = self.button.GetFont(); font.PointSize += 10; font = font.Bold()
        self.button.SetSize(width=200, height=200)
        self.button.SetFont(font)
        self.button.SetLabel("apple")


    def onfruitselection(self,evt):
        dlg = wx.MessageDialog(None, "You selected: " + self.fruitcombobox.GetStringSelection())
        dlg.ShowModal()
        self.fruitcombobox.Hide()

    def onokbuttonclick(self,evt):
        x=np.linspace(-np.pi,np.pi,100)
        self.axes.plot(x,np.sin(x))
        self.axes.grid()
        self.canvas.draw()


def main():
    app = wx.App()
    frame=HelloFrame(None, title='Text and Button')
    frame.Show()
    frame.RequestUserAttention()
    app.MainLoop()
    del app

if __name__ == '__main__':
    main()
