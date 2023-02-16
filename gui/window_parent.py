import sys
sys.path.insert(0,'/Users/ernestmoney/ohmystock/tool')
import wx
import matplotlib.pyplot as plt
# from dao.fiscal_dao import Fiscal_Dao
# from component.custom_plot_1_axes import Custom_Plot_1_Axes
# from window_downloader import Downloader_Window
from tool.report import Report

class Window_Parent(wx.Frame):
    def __init__(self, parent, title = "Am I Expensive?",  size = (800,550)):
        super(Window_Parent, self).__init__(parent, title = title,  size = size)
        self.BG_COLOUR = (48,56,65) #(10,52,64)
        self.FR_COLOUR = (91,162,164)
        self.FR_COLOUR_WARNING = "brown"
        self.FR_COLOUR_OKAY = "MEDIUM AQUAMARINE"
        self.SetBackgroundColour(self.BG_COLOUR)
        self.Centre()
        # self.createMenu()
        
        self.HEAD = wx.Font(50, wx.SWISS, wx.NORMAL, wx.NORMAL)
        self.HEAD_HIGHTLIGHT = wx.SystemSettings.GetFont(wx.SYS_SYSTEM_FONT)
        self.HEAD_HIGHTLIGHT.SetPointSize(17)
        self.HEAD_HIGHTLIGHT_1 = wx.SystemSettings.GetFont(wx.SYS_SYSTEM_FONT)
        self.HEAD_HIGHTLIGHT_1.SetPointSize(20)
        self.BODY = wx.SystemSettings.GetFont(wx.SYS_SYSTEM_FONT)
        self.BODY.SetPointSize(14)

        self.report = Report()
        
    def createMenu(self):
        menubar = wx.MenuBar()
        actionMenu = wx.Menu() 
        d = wx.MenuItem(actionMenu, wx.ID_ANY,text = "Open Download Window",kind = wx.ITEM_NORMAL)
        self.Bind(wx.EVT_MENU, self.show_download_window_handler, d) 
        actionMenu.Append(d) 
        actionMenu.AppendSeparator()

        q = wx.MenuItem(actionMenu, wx.ID_ANY, text = '&Quit\tCtrl+Q',kind = wx.ITEM_NORMAL) 
        self.Bind(wx.EVT_MENU, self.onExit, q) 
        actionMenu.Append(q) 
        menubar.Append(actionMenu, '&Action')        

        self.SetMenuBar(menubar)

    def show_download_window_handler(self, event): 
        frame = Downloader_Window()
        frame.Show()

    def onExit(self, event):
        plt.close()
        self.Close(True)

if __name__ == '__main__':
    app = wx.App()
    s1 = Stock('M')
    s2 = Stock('ABG')
    window= Window_Stock_Eps(None, stock=s1, stocks=[s1,s2])
    window.Show()
    app.MainLoop()          