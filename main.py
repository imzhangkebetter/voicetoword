#!/usr/bin/env python
"""
Hello World, but with more meat.
"""
import wx, os
from tool import to_pcm_by_command, get_file_name
from api.get_words import get_words


# 创建窗口类
class MainFrame(wx.Frame):
    def __init__(self, *args, **kw):
        super(MainFrame, self).__init__(*args, **kw)
        self.Title = '百度AI语音识别助手'
        self.Center()
        self.SetSize(500, 400)
        self.MakeTop()
        self.MakeFunc()
        self.Show()

    def OnExit(self, event):
        self.Close(True)

    def MakeTop(self):
        self.filecontent = wx.TextCtrl(self)
        self.filecontent.SetSize(500, 200)

    def OnOpenFile(self, event):
        wildcard = 'All files(*.*)|*.*'
        dialog = wx.FileDialog(None, 'select', os.getcwd(), '', wildcard, wx.FD_OPEN)
        if dialog.ShowModal() == wx.ID_OK:
            self.FileName.SetValue(dialog.GetPath())
            com_line = to_pcm_by_command(self.FileName.GetValue())
            if com_line == 0:
                file_name = get_file_name(self.FileName.GetValue())
                words = get_words(os.getcwd()+'/tmp/'+file_name+'.pcm')
                self.filecontent.SetValue(words)
                os.remove(os.getcwd()+'/tmp/'+file_name+'.pcm')
                dialog.Destroy

    def MakeFunc(self):
        self.FileName = wx.TextCtrl(self, pos=(5, 210), size=(230, 25))
        self.findBtn = wx.Button(self, label='浏览', pos=(250, 210), size=(80, 25))
        self.findBtn.Bind(wx.EVT_BUTTON, self.OnOpenFile)


if __name__ == '__main__':
    app = wx.App()
    frm = MainFrame(None)
    app.MainLoop()
