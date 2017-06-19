# Get the GUI stuff
import wx

# We're going to be handling files and directories
import os, datetime

# Set up some button numbers for the menu
# ID_ABOUT=101
# ID_OPEN=102
# ID_SAVE=103
ID_BUTTON1=300
# ID_EXIT=200

class MainWindow(wx.Frame):
    def __init__(self,parent,title):
        # based on a frame, so set up the frame
        wx.Frame.__init__(self,parent,wx.ID_ANY, title, pos=(300, 200), size=(600, 400))

        # Add a text editor and a status bar
        # Each of these is within the current instance
        # so that we can refer to them later.
        self.control = wx.TextCtrl(self, 1, style=wx.TE_MULTILINE)
        self.status_bar_frame = self.CreateStatusBar() # A Statusbar in the bottom of the window
  
        # Set up a series of buttons arranged horizontally
        self.sizer2 = wx.BoxSizer(wx.HORIZONTAL)
		
        self.saveButton = wx.Button(self, ID_BUTTON1, "Save")
        self.saveButton.Bind(wx.EVT_BUTTON, self.OnSave)
        self.sizer2.Add(self.saveButton,1,wx.EXPAND)
        # Set up the overall frame verically - text edit window above buttons
        # We want to arrange the buttons vertically below the text edit window
        self.sizer=wx.BoxSizer(wx.VERTICAL)
        self.sizer.Add(self.control,1,wx.EXPAND)
        self.sizer.Add(self.sizer2,0,wx.EXPAND)

        # Tell it which sizer is to be used for main frame
        # It may lay out automatically and be altered to fit window
        self.SetSizer(self.sizer)
        self.SetAutoLayout(1)
        #self.sizer.Fit(self)

        # Show it !!!
        self.Show(1)

        # Define widgets early even if they're not going to be seen
        # so that they can come up FAST when someone clicks for them!
        self.doiexit = wx.MessageDialog( self, " Exit - R U Sure? \n",
                        "GOING away ...", wx.YES_NO)

        # dirname is an APPLICATION variable that we're choosing to store
        # in with the frame - it's the parent directory for any file we
        # choose to edit in this frame
        self.dirname = 'D:\desktop\Case Logs(total)'

    def OnExit(self,e):
        # A modal with an "are you sure" check - we don't want to exit
        # unless the user confirms the selection in this case ;-)
        igot = self.doiexit.ShowModal() # Shows it
        if igot == wx.ID_YES:
            self.Close(True)  # Closes out this simple application

    def OnSave(self,e):
        # Save away the edited text
        # Open the file, do an RU sure check for an overwrite!
        time = datetime.datetime.now()
        daytime = time.strftime('%Y-%m-%d_')
        # self.filename = daytime
        itcontains = self.control.GetValue()
        i = 1
        email_line = itcontains.split('\n', 10)[i]
        while True:
            if "Email Address" not in email_line and ("电子邮件地址" not in email_line):
                i += 1
                email_line = itcontains.split('\n', 10)[i]
                continue
            else:
                break
        self.filename = daytime + email_line + '.txt'
        self.filepath = os.path.join(self.dirname, self.filename)
        # print(self.filepath)
        # check if file already exists
        count = 1
        while os.path.isfile(self.filepath) and os.path.getsize(self.filepath):
            count += 1
            self.filename = daytime + email_line + '(' + str(count) + ')' + '.txt'
            self.filepath = os.path.join(self.dirname, self.filename)
            # self.status_bar_frame.SetStatusText("Save Successfully!")     
        
        filehandle=open(self.filepath,'w')
        filehandle.write(itcontains)
        filehandle.close()

        if os.path.isfile(self.filepath) and os.path.getsize(self.filepath):
            self.status_bar_frame.SetStatusText("Save Successfully!")     
        else:
            self.status_bar_frame.SetStatusText("Save Failed!")

# Set up a window based app, and create a main window in it
app = wx.App()
view = MainWindow(None, "Chat Saver")
# Enter event loop
app.MainLoop()
