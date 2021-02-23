import wx
from main import MainFrame

if __name__ == '__main__':
    app = wx.App()
    frm = MainFrame(None, title='百度AI语音识别助手')
    frm.Show()
    app.MainLoop()