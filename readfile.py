import wx
import os


class SiteLog(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, title='SiteLog', size=(640, 480))
        self.SelBtn = wx.Button(self, label='>>', pos=(305, 5), size=(80, 25))
        self.SelBtn.Bind(wx.EVT_BUTTON, self.OnOpenFile)
        self.OkBtn = wx.Button(self, label='OK', pos=(405, 5), size=(80, 25))
        self.OkBtn.Bind(wx.EVT_BUTTON, self.ReadFile)
        self.FileName = wx.TextCtrl(self, pos=(5, 5), size=(230, 25))
        self.FileContent = wx.TextCtrl(self, pos=(5, 35), size=(620, 480), style=(wx.TE_MULTILINE))

    def OnOpenFile(self, event):
        wildcard = 'All files(*.*)|*.*'
        dialog = wx.FileDialog(None, 'select', os.getcwd(), '', wildcard, wx.FD_OPEN)
        if dialog.ShowModal() == wx.ID_OK:
            self.FileName.SetValue(dialog.GetPath())
            dialog.Destroy

    def ReadFile(self, event):
        file = open(self.FileName.GetValue())
        self.FileContent.SetValue(file.read())
        file.close()


if __name__ == '__main__':
    app = wx.App()
    SiteLog().Show()
    app.MainLoop()