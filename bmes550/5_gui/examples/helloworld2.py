"""
Hello World, but with more meat.
Here, we'll put a little more flesh on the bones of our program.
"""

import wx


class HelloFrame(wx.Frame):
    """
    A frame that says Hello World
    """

    def __init__(self, *args, **kwargs):
        # Ensure the parent's __init__ is called
        super(HelloFrame, self).__init__(*args, **kwargs)

        # Create a panel in the frame
        panel = wx.Panel(self)

        # Put some text with a larger bold font on it
        text = wx.StaticText(panel, label="Hello World!")
        font = text.GetFont()
        font.PointSize += 10
        font = font.Bold()
        text.SetFont(font)

        # Create a sizer to manage the layout of the child widgets
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(text, wx.SizerFlags().Border(wx.TOP | wx.LEFT, 25))
        panel.SetSizer(sizer)

        # Create a menu bar
        self.makeMenuBar()

        # Add a status bar
        self.CreateStatusBar()
        self.SetStatusText("This is the status bar.")


    def makeMenuBar(self):
        """
        A menu bar is composed of menus, which are composed of menu
        items. The method builds a set of menus and binds handlers to
        be called when the menu item is selected.
        """

        # Create a file menu with Hello and Exit items
        fileMenu = wx.Menu()
        # The '\t...' syntax defines an accelerator key that also
        # triggers the same event
        helloItem = fileMenu.Append(-1, "&Hello...\tCtrl-H", 
            "Help string shown in status bar for this menu item")
        fileMenu.AppendSeparator()
        # When using a stock ID we don't need to specify the menu item's
        # label
        exitItem = fileMenu.Append(wx.ID_EXIT)

        # Now a help menu for the about item
        helpMenu = wx.Menu()
        aboutItem = helpMenu.Append(wx.ID_ABOUT)

        # Make the menu bar and add the two menus to it. The '&' defines
        # that the next letter is the 'mnemonic' for the menu item. On
        # the platforms that support it those letters are underlined and
        # can be triggered from the keyboard.
        menuBar = wx.MenuBar()
        menuBar.Append(fileMenu, "&File")
        menuBar.Append(helpMenu, "&Help")

        # Give the menu bar to the frame
        self.SetMenuBar(menuBar)

        # Finally, associate a handler function with the EVT_MENU event
        # for each of the menu items. That means that when that menu
        # item is activated, then the associated handler function will
        # be called.
        self.Bind(wx.EVT_MENU, self.onHello, helloItem)
        self.Bind(wx.EVT_MENU, self.onExit,  exitItem)
        self.Bind(wx.EVT_MENU, self.onAbout, aboutItem)


    def onExit(self, event):
        """
        Close the frame, terminating the application.
        """
        self.Close(True)


    def onHello(self, event):
        """
        Say hello to the user.
        """
        wx.MessageBox("Hello again from wxPython")

    
    def onAbout(self, event):
        """
        Display an About Dialog
        """
        wx.MessageBox(
            "This is a wxPython Hello World sample",
            "About Hello World 2",
            wx.OK | wx.ICON_INFORMATION
        )


if __name__ == '__main__':
    """
    When this module is run (not imported), then create the app, the
    frame, show it, and start the event loop.
    """

    app = wx.App()
    frame = HelloFrame(None, title="Hello World")
    frame.Show()
    app.MainLoop()
