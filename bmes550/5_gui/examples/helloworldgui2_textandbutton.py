#!python
#Example taken/adapted  from: http://zetcode.com/wxpython/layout/


import wx


class HelloFrame(wx.Frame):
    def __init__(self, *args, **kw):
        super(HelloFrame, self).__init__(*args, **kw)

        panel = wx.Panel(self)

        font = wx.SystemSettings.GetFont(wx.SYS_SYSTEM_FONT)
        font.SetPointSize(30); font=font.Bold();


        vsizer = wx.BoxSizer(wx.VERTICAL)        


        hbox1 = wx.BoxSizer(wx.HORIZONTAL)
        st1 = wx.StaticText(panel, label='Enter a number: ')
        st1.SetFont(font)
        hbox1.Add(st1, flag=wx.RIGHT, border=8)
        
        tc = wx.TextCtrl(panel)
        tc.SetFont(font)
        hbox1.Add(tc, proportion=1)
        self.inputbox=tc;
        
        btn1 = wx.Button(panel, label='Ok', size=(70, 30))
        hbox1.Add(btn1)
        btn1.Bind(wx.EVT_BUTTON, self.onokbuttonclick)
        self.inputbox.Bind(wx.EVT_KEY_UP, self.onokbuttonclick)
        
        
        
        vsizer.Add(hbox1, flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, border=10)


        st1 = wx.StaticText(panel, label='Result will be shown here...')
        st1.SetFont(font)
        vsizer.Add(st1, flag=wx.RIGHT, border=8,proportion=1)
        self.resultbox=st1;


        panel.SetSizer(vsizer)


    def onokbuttonclick(self,evt):
        self.resultbox.SetLabel("You entered: "+self.inputbox.GetValue())
        evt.Skip()



if __name__ == '__main__':
    # When this module is run (not imported) then create the app, the
    # frame, show it, and start the event loop.
    app = wx.App()
    frm = HelloFrame(None, title='Text and Button')
    frm.Show()
    app.MainLoop()
    del app
