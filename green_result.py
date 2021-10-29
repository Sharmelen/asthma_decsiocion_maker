from xpxchain import models
from xpxchain import client
import wx
import mysql.connector
import hashlib
import sys
import os

def good_result():

	def submit_button(event):
		wx.MessageBox('Thank You', 'INOFRMATION',wx.OK | wx.ICON_INFORMATION)
		sys.exit(0)
	
	
	
	app = wx.App()
	win = wx.Frame(None, title="Result", size=(410, 350))
	win.SetBackgroundColour('green')

	vbox = wx.BoxSizer(wx.VERTICAL)
	font = wx.SystemSettings.GetFont(wx.SYS_SYSTEM_FONT)
	font.SetPointSize(9)

	hbox1 = wx.BoxSizer(wx.HORIZONTAL)
	st1 = wx.StaticText(win, label = "You're Doing Well")
	st1.SetFont(font)
	hbox1.Add(st1, flag = wx.CENTER, border = 8)
	vbox.Add(hbox1, flag=wx.CENTER, border=10)

	hbox2 = wx.BoxSizer(wx.HORIZONTAL)
	st2 = wx.StaticText(win, label = "You Should Be:")
	st2.SetFont(font)
	hbox2.Add(st2, flag = wx.RIGHT, border = 8)
	vbox.Add(hbox2, flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, border=10)
	
	hbox3 = wx.BoxSizer(wx.HORIZONTAL)
	st3 = wx.StaticText(win, label = "  - No Cough, Wheeze, Chest Tightness or Shortness of Breath")
	st3.SetFont(font)
	hbox3.Add(st3, flag = wx.RIGHT, border = 8)
	vbox.Add(hbox3, flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, border=10)
	
	hbox4 = wx.BoxSizer(wx.HORIZONTAL)
	st4 = wx.StaticText(win, label = "  - Can Sleep Well At Day and Night")
	st4.SetFont(font)
	hbox4.Add(st4, flag = wx.RIGHT, border = 8)
	vbox.Add(hbox4, flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, border=10)
	
	hbox5 = wx.BoxSizer(wx.HORIZONTAL)
	st5 = wx.StaticText(win, label = "  - Can Do Casual Activities")
	st5.SetFont(font)
	hbox5.Add(st5, flag = wx.RIGHT, border = 8)
	vbox.Add(hbox5, flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, border=10)
	
	vbox.Add((-1,20))

	hbox5 = wx.BoxSizer(wx.HORIZONTAL)

	acc_info = wx.Button(win, label = 'OK', size = (150,30))
	hbox5.Add(acc_info)
	acc_info.Bind(wx.EVT_BUTTON, submit_button)
	vbox.Add(hbox5, flag = wx.CENTER)

	win.SetSizer(vbox)

	win.SetSizerAndFit(vbox)
	win.Show()
	app.MainLoop()
	win.SetSizer(vbox)