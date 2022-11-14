"""
Curve Fitter
------------

This is an example of an wxPython GUI that uses matplotlib to interact
with plots and perfrom simple data analysis.

This app allows the user to fit a curve to a set of data points. Sliders
are used to adjust initial guesses for the parameters of the curve.

The data set used is taken from stress-relaxation data for articular
cartilege samples from the knee joints of adult chickens. The model used
is a streched exponential function based on a polydisperse polymer
reptation model.
"""

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import wx
from matplotlib.backends.backend_wx import NavigationToolbar2Wx
from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigureCanvas
from matplotlib.figure import Figure

# Activate matplotlib's wx backend.
mpl.use('WXAgg')


class CurveFitter(wx.Frame):
    """
    Frame for the application which displays a figure along with some
    controls.
    """

    def __init__(self, *args, **kwargs):
        """
        Initialize the frame with its components
        """

        super(CurveFitter, self).__init__(*args, **kwargs)

        # Create a panel
        panel = wx.Panel(self)

        # Create the layout (sizer)
        ## Create a sizer to hold buttons and controls
        control_sizer = wx.StaticBoxSizer(
            wx.VERTICAL, panel, "Buttons and controls"
        )
        ## Create sizer to hold the figure
        figure_sizer = wx.BoxSizer(wx.VERTICAL)
        ## Create a vertical sizer to hold the whole thing
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(control_sizer, 0, wx.ALL, 5)
        sizer.Add(figure_sizer, 1, wx.EXPAND)

        # Add buttons and controls
        draw_btn = wx.Button(panel, label="Click to draw")
        draw_btn.Bind(wx.EVT_BUTTON, self.onDraw)
        draw_btn.Bind(wx.EVT_ENTER_WINDOW, self.onMouseEnter)
        draw_btn.Bind(wx.EVT_LEAVE_WINDOW, self.onMouseExit)

        # Add event handler for mouse-move to change the text to bold
        control_sizer.Add(draw_btn, 0, wx.LEFT)
        self.draw_btn = draw_btn

        # Create the figure and add the matplotlib canvas and toolbar
        self.figure = Figure()
        self.axis = self.figure.add_subplot(111)
        self.canvas = FigureCanvas(panel, -1, self.figure)
        self.toolbar = NavigationToolbar2Wx(self.canvas)
        self.toolbar.Realize()
        figure_sizer.Add(self.toolbar, 0, wx.TOP)
        figure_sizer.Add(self.canvas, 1, wx.EXPAND)

        # Add a select box
        select = wx.ComboBox(panel, -1, style=wx.CB_READONLY, choices=[
            "Sine", "Cosine", "Tangent"
        ])
        select.SetSelection(0)
        select.Bind(wx.EVT_COMBOBOX, self.onSelect)
        control_sizer.Add(select, 0, wx.LEFT)
        self.select = select

        # Set the layout
        panel.SetSizer(sizer)

        # Add menu and status bars
        self.CreateMenuBar()
        self.CreateStatusBar()
        self.SetStatusText("Welcome to wxPython!")


    def CreateMenuBar(self):
        """
        Create a menu bar with a 'File' menu and a 'Help' menu
        """

        # Create the 'File' menu
        fileMenu = wx.Menu()
        saveItem = fileMenu.Append(wx.ID_SAVE, "&Save\tCtrl-S",
                                   "Save the figure")
        fileMenu.AppendSeparator()
        exitItem = fileMenu.Append(wx.ID_EXIT, "E&xit\tCtrl-Q",
                                   "Exit the application")

        # Create the 'Help' menu
        helpMenu = wx.Menu()
        aboutItem = helpMenu.Append(wx.ID_ABOUT, "&About\tCtrl-A")

        # Create the menu bar
        menuBar = wx.MenuBar()
        menuBar.Append(fileMenu, "&File")
        menuBar.Append(helpMenu, "&Help")
        self.SetMenuBar(menuBar)

        # Bind the menu events to handlers
        self.Bind(wx.EVT_MENU, self.onSave, saveItem)
        self.Bind(wx.EVT_MENU, self.onExit, exitItem)
        self.Bind(wx.EVT_MENU, self.onAbout, aboutItem)


    def onMouseEnter(self, event):
        """
        Change the button color to red when the mouse enters the button
        """

        self.draw_btn.SetBackgroundColour("#ffbdbd")
        event.Skip()


    def onMouseExit(self, event):
        """
        Change the button color to normal when the mouse exits the button
        """

        self.draw_btn.SetBackgroundColour(wx.NullColour)
        event.Skip()


    def onDraw(self, event):
        """
        Plot a the selected function in the figure
        """

        # Clear the figure
        self.axis.clear()

        # Get the selected function
        function = self.select.GetValue()

        # Plot the function
        x = np.linspace(0, 2 * np.pi, 100)
        if function == "Sine":
            y = np.sin(x)
        elif function == "Cosine":
            y = np.cos(x)
        elif function == "Tangent":
            y = np.tan(x)
        else:
            y = x
        sns.lineplot(x=x, y=y, ax=self.axis)

        # Redraw the figure
        self.axis.set_title(self.select.GetStringSelection(), fontsize=16)
        self.axis.grid()
        self.canvas.draw()


    def onSelect(self, event):
        """
        Change the figure based on the selection in the select box
        """

        return self.onDraw(event)


    def onSave(self, event):
        """Save the figure to a file"""

        print("Saving the figure")


    def onExit(self, event):
        """Exit the application"""

        self.Close()


    def onAbout(self, event):
        """Display the 'About' dialog"""

        wx.MessageBox(
            "This is a wxPython application which uses matplotlib",
            "About", 
            wx.OK | wx.ICON_INFORMATION
        )


def main():
    app = wx.App()
    frame = CurveFitter(None, title='Text and Button')
    frame.Show()
    frame.RequestUserAttention()
    app.MainLoop()
    del app


if __name__ == "__main__":
    
    app = wx.App()
    frame = CurveFitter(None, title="Figure Manipulation")
    frame.Show()
    app.MainLoop()
    del app
