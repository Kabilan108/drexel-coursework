"""
HWPlotGUI

Authors: Tony Okeke, Demetri Tsitsios
"""

# Imports
import numpy as np
import wx
from wx.lib import plot as wxplot


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
        self.SetSize((750, 450))
        self.panel = GUIPanel(self)


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
            field = wx.TextCtrl(parent, size=(60, 20), style=wx.TE_PROCESS_ENTER)
            field.name = label.GetLabelText()  # type: ignore
            field.SetFont(font)
            self.Add(field, 1)

            self.field = field
            self.label = label


    class ControlBox(wx.StaticBox):
        """
        Custom `StaticBox` for figure controls
        """

        def __init__(self, parent, label, inputs, **inputargs):

            assert isinstance(inputs, dict), 'inputs must be a dictionary'
            
            # Initialize the wx.StaticBox class
            super().__init__(parent, -1, label=label)

            # Create sizer
            self.sizer = wx.StaticBoxSizer(self, wx.VERTICAL)

            # Create text inputs
            self.input = dict()
            for label, arg in inputs.items():
                if arg == 'text':
                    # Create a text input
                    _label = f"{label.replace('_', ' ')}:"
                    self.input[label] = GUIPanel.TextInput(self, _label)
                    self.sizer.Add(self.input[label], 0, wx.EXPAND | wx.ALL, 5)
                    
                    # Bind events
                    self.input[label].field.Bind(
                        wx.EVT_TEXT_ENTER, self.GetParent().onEnter
                    )

                elif arg == 'selector':
                    # Check that appropriate arguments are provided
                    if 'choices' not in inputargs:
                        raise ValueError("Must provide choices for selector")
                    if 'value' not in inputargs:
                        raise ValueError("Must provide value for selector")

                    # Create a selector
                    self.dropdown = wx.ComboBox(self, -1, inputargs['value'],
                        choices=inputargs['choices'])
                    self.sizer.Add(self.dropdown, 0, wx.EXPAND | wx.TOP | wx.BOTTOM, 7)

                    # Bind events
                    self.dropdown.Bind(
                        wx.EVT_COMBOBOX, self.GetParent().onSelect
                    )

                else:
                    raise ValueError("Invalid input type")
            self.SetMinSize((200, -1))


    def __init__(self, parent):
        
        # Initialize the wx.Panel class
        super().__init__(parent)
        
        # Clear error state
        self.STATE = 0

        # Create sizers
        sizer = wx.BoxSizer(wx.VERTICAL)
        main_sizer = wx.BoxSizer(wx.HORIZONTAL)
        ctrl_sizer = wx.BoxSizer(wx.VERTICAL)

        # Create controls
        self.func_box = GUIPanel.ControlBox(
            parent=self,
            label='Function',
            inputs={'dropdown': 'selector'},    
            choices=['Gaussian', 'Decaying Oscillations'],
            value='Gaussian'
        )
        self.gauss_box = GUIPanel.ControlBox(
            parent=self, 
            label='Gaussian Parameters', 
            inputs=dict(mean='text', std_dev='text')
        )
        self.osc_box = GUIPanel.ControlBox(
            parent=self,
            label='Decaying Oscillation Parameters',
            inputs=dict(decay='text', freq='text')
        )

        # Set default values
        self.gauss_box.input['mean'].field.SetValue('5')
        self.gauss_box.input['std_dev'].field.SetValue('5')
        self.osc_box.input['decay'].field.SetValue('0.1')
        self.osc_box.input['freq'].field.SetValue('2.0')

        # Add controls to the layout
        ctrl_sizer.Add(self.func_box.sizer)
        ctrl_sizer.AddSpacer(15)
        ctrl_sizer.Add(self.gauss_box.sizer)
        ctrl_sizer.AddSpacer(15)
        ctrl_sizer.Add(self.osc_box.sizer)
        main_sizer.Add(ctrl_sizer)
        
        # Add figure canvas to the layout
        self.canvas = wxplot.PlotCanvas(self)
        self.enableGrid = True
        self.enablePointLabel = True
        main_sizer.Add(self.canvas, 1, wx.EXPAND | wx.ALL, 10)

        # Add layout to the panel
        sizer.Add(main_sizer, 1, wx.EXPAND | wx.TOP | wx.LEFT | wx.RIGHT, 10)

        # Add space for error messages
        font = wx.Font(10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, 
                       wx.FONTWEIGHT_BOLD)
        self.error = wx.StaticText(
            self, -1, '', (8,4), (-1,15), wx.ALIGN_CENTER | wx.ST_NO_AUTORESIZE
        )
        self.error.SetFont(font)
        self.error.SetForegroundColour('red')
        sizer.Add(self.error, 0, wx.EXPAND)

        # Set sizer
        self.SetSizer(sizer)

        # Trigger the event to set the visibility of the controls
        self.onSelect(None)

    
    def Error(self, msg):
        """Show an error message"""
        self.error.SetLabelText(msg)
        self.STATE = 1


    def ClearError(self):
        """Clear the error message"""
        self.error.SetLabelText('')
        self.STATE = 0


    def onSelect(self, event):
        """
        Callback for when the function dropdown is selected
        """

        # Get the selected function
        func = self.func_box.dropdown.GetValue()

        # Set the visibility of the controls
        if func == 'Gaussian':
            self.GetParent().Layout()
            self.gauss_box.Show()
            self.osc_box.Show(False)
            self.ClearError()
        elif func == 'Decaying Oscillations':
            self.GetParent().Layout()
            self.gauss_box.Show(False)
            self.osc_box.Show()
            self.ClearError()
        else:
            # Display error in the status bar
            self.Error('Invalid function selected');

        # Update the plot
        self.plotFunction(event)
 

    def onEnter(self, event):
        """
        This callback is triggered when the user presses the Enter key
        and will update the plot with the new values
        """

        # Get the selected function
        func = self.func_box.dropdown.GetValue()

        if func == 'Gaussian':
            inputs = dict(
                mean=self.gauss_box.input['mean'].field.GetValue(),
                std_dev=self.gauss_box.input['std_dev'].field.GetValue()
            )
        elif func == 'Decaying Oscillations':
            inputs = dict(
                decay=self.osc_box.input['decay'].field.GetValue(),
                freq=self.osc_box.input['freq'].field.GetValue()
            )
        else:
            raise ValueError("Invalid function selected")

        # Clear errors
        self.ClearError()

        # Check that the inputs are valid
        for key, value in inputs.items():
            # Check for numeric values
            try:
                float(value)
            except:
                self.Error('Invalid value for %s' % key)
                self.plotFunction(event)
                return

            # Check for negative values
            if key != 'mean' and '-' in value:
                self.Error('Negative values not allowed for %s' % key)

            # Standard devaiton must be non-zero
            if key == 'std_dev' and float(value) == 0:
                self.Error('Standard deviation must be non-zero')

            # No empty values
            if value == '':
                self.Error('Empty values not allowed for %s' % key)

        # Update the plot
        self.plotFunction(event)


    def plotFunction(self, event):
        """
        Plot the function
        """

        # Get the selected function
        func = self.func_box.dropdown.GetValue()

        # Show empty figure if in error state
        if self.STATE == 1:
            # Show empty figure
            X, Y = [], []
            line = wxplot.PolySpline(list(zip(X, Y)), colour='lightgray', width=0)
            graphics = wxplot.PlotGraphics([line])
            self.canvas.Draw(graphics)
            return

        if func == 'Gaussian':
            # Get the parameters
            mean = float(self.gauss_box.input['mean'].field.GetValue())
            std = float(self.gauss_box.input['std_dev'].field.GetValue())
            
            # Define the function values
            X = np.linspace(-10, 10, 100)
            Y = 1 / (std * np.sqrt(2 * np.pi)) * np.exp(-0.5 * ((X - mean) / std)**2)
        elif func == 'Decaying Oscillations':
            # Get the parameters
            decay = float(self.osc_box.input['decay'].field.GetValue())
            freq = float(self.osc_box.input['freq'].field.GetValue())
            
            # Define the function values
            X = np.linspace(0, 50, 100)
            Y = np.exp(-decay * X) * np.cos(freq * X)
        else:
            raise ValueError('Invalid function selected')

        # Update the plot
        line = wxplot.PolySpline(list(zip(X, Y)), colour='blue', width=2)
        graphics = wxplot.PlotGraphics([line])
        self.canvas.Draw(graphics, xAxis=(X.min(), X.max()), yAxis=(Y.min(), Y.max()))


if __name__ == '__main__':
    app = wx.App()
    frame = PlotGUI()
    frame.Show()
    app.MainLoop()
    del app
