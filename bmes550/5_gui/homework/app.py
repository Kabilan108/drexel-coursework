"""
HWPlotGUI

Authors: Tony Okeke, Demetri Tsitsios
"""

# Imports
import matplotlib.pyplot as plt
import matplotlib as mpl
import seaborn as sns

import numpy as np
import wx

from wx.lib.plot import PolyLine, PlotCanvas, PlotGraphics


class PlotGUI(wx.Frame):
    """
    This class serves as the main body for our GUI
    """

    def __init__(self, *args, **kwargs):
        
        # Initialize the wx.Frame class
        super().__init__(
            parent=None,
            title='hwplotgui by Tony Okeke and Demetri Tsitsios',
            *args, **kwargs
        )

        # Window settings
        self.SetSize((1000, 700))
        self.panel = GUIPanel(self)

        # self.panel.onSelect(None)


class GUIPanel(wx.Panel):
    """
    This class serves as the panel for our GUI
    """

    class TextInput(wx.BoxSizer):
        """
        Custom text input with label
        """

        def __init__(self, parent, label):
            
            # Initialize the wx.BoxSizer class
            super().__init__(wx.HORIZONTAL)

            # Define font
            font = wx.Font(10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, 
                           wx.FONTWEIGHT_NORMAL)

            # Create label
            label = wx.StaticText(parent, label=label)
            label.SetFont(font)
            self.Add(label, 1, wx.RIGHT)

            # Create text input
            field = wx.TextCtrl(parent, size=(60, 20))
            field.SetFont(font)
            self.Add(field, 1)

            self.field = field
            self.label = label


    def __init__(self, parent):
        
        # Initialize the wx.Panel class
        super().__init__(parent)

        # Creaete sizers
        main_sizer = wx.BoxSizer(wx.HORIZONTAL)
        ctrl_sizer = wx.BoxSizer(wx.VERTICAL)

        # Controls: Function Selection
        func_box = wx.StaticBoxSizer(wx.VERTICAL, self, "Function")
        dropdown = wx.ComboBox(self, -1, 'Gaussian',
            choices=['Gaussian', 'Decaying Oscillations']
        )
        dropdown.Bind(wx.EVT_COMBOBOX, self.onSelect)
        self.dropdown = dropdown
        func_box.Add(dropdown, 0, wx.CENTER|25)
        func_box.SetMinSize((200, -1))

        # Controls: Plot Settings (Gaussian)
        gauss_box = wx.StaticBoxSizer(wx.VERTICAL, self, "Gaussian Parameters")
        self.mean = GUIPanel.TextInput(self, "mean:")
        self.std = GUIPanel.TextInput(self, "std dev:")
        gauss_box.Add(self.mean, 0, wx.CENTER|25)
        gauss_box.Add(self.std, 0, wx.CENTER|25)
        gauss_box.SetMinSize((200, 50))
        self.gauss_box = gauss_box

        # Controls: Plot Settings (Decaying Oscillations)
        osc_box = wx.StaticBoxSizer(wx.VERTICAL, self, "Decaying Oscillations Parameters")
        self.decay = GUIPanel.TextInput(self, "decay:")
        self.freq = GUIPanel.TextInput(self, "frequency:")
        osc_box.Add(self.decay, 0, wx.CENTER|25)
        osc_box.Add(self.freq, 0, wx.CENTER|25)
        osc_box.SetMinSize((200, 50))
        self.osc_box = osc_box

        # Add controls to the layout
        ctrl_sizer.Add(func_box)
        ctrl_sizer.AddSpacer(15)
        ctrl_sizer.Add(gauss_box)
        ctrl_sizer.AddSpacer(15)
        ctrl_sizer.Add(osc_box)
        main_sizer.Add(ctrl_sizer)
        
        # Add figure canvas to the layout
        # self.figure = Figure()
        # self.axis = self.figure.add_subplot(111)
        # self.canvas = FigureCanvas(self, -1, self.figure)
        # main_sizer.Add(self.canvas, 1, wx.EXPAND)

        self.canvas = PlotCanvas(self)
        self.canvas.SetEnableGrid(True)
        self.canvas.SetEnablePointLabel(True)

        main_sizer.Add(self.canvas, 1, wx.EXPAND | wx.ALL, 10)

        
        self.SetSizer(main_sizer)

        # Trigger the event to set the visibility of the controls
        self.osc_box.ShowItems(False)


    def onSelect(self, event):
        """
        
        """

        # Get the selected function
        func = self.dropdown.GetValue()

        # Set the visibility of the controls
        if func == 'Gaussian':
            print('Gauss')
            self.gauss_box.ShowItems(True)
            self.osc_box.ShowItems(False)
            # self.gauss_box.Layout()
            # self.osc_box.Hide()
        elif func == 'Decaying Oscillations':
            print('Osc')
            self.osc_box.ShowItems(True)
            self.gauss_box.ShowItems(False)
            # self.gauss_box.Hide()
            # self.osc_box.Layout()
        else:
            print('None')
            self.gauss_box.ShowItems(False)
            self.osc_box.ShowItems(False)
            # self.gauss_box.Hide(True)
            # self.osc_box.Hide(True)
        

if __name__ == '__main__':
    app = wx.App()
    frame = PlotGUI()
    frame.Show()
    app.MainLoop()
    del app
