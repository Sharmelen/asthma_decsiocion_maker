from xpxchain import models
from xpxchain import client
import wx
import mysql.connector
import hashlib
import sys
import os
from green_result import *
from yellow_result import *
from red_result import *
app = wx.App()
win = wx.Frame(None, title="Asthma Descision Maker", size=(410, 350))
win.SetBackgroundColour('white')

vbox = wx.BoxSizer(wx.VERTICAL)
font = wx.SystemSettings.GetFont(wx.SYS_SYSTEM_FONT)
font.SetPointSize(9)

f = open("result_1.txt","w")
f.close()
f = open("result_2.txt","w")
f.close()
f = open("result_3.txt","w")
f.close()
f = open("result_4.txt","w")
f.close()

def onChecked_1(event):
	
	
	cb = event.GetEventObject()
	
	result = cb.GetLabel()
	state = cb.GetValue()
	
	f = open("result_1.txt","a")
	f.write(str(result)+"-"+str(state)+"\n")
	f.close()
		
def onChecked_2(event):
	
	
	cb = event.GetEventObject()
	
	result = cb.GetLabel()
	state = cb.GetValue()
	
	f = open("result_2.txt","a")
	f.write(str(result)+"-"+str(state)+"\n")
	f.close()

def onChecked_3(event):

	cb = event.GetEventObject()
	
	result = cb.GetLabel()
	state = cb.GetValue()
	
	f = open("result_3.txt","a")
	f.write(str(result)+"-"+str(state)+"\n")
	f.close()
	
def onChecked_4(event):

	cb = event.GetEventObject()
	
	result = cb.GetLabel()
	state = cb.GetValue()
	
	f = open("result_4.txt","a")
	f.write(str(result)+"-"+str(state)+"\n")

	
def submit_button(event):
	final_yes = []
	final_no = []
	
	file_array = ["result_1.txt","result_2.txt","result_3.txt","result_4.txt"]
	
	for x in range(len(file_array)):
	
		f = open(str(file_array[x]),"r")
		array = f.readlines()
		#print(array)
		
		yes_1 = []
		no_1 = []
		
		
		for i in range (len(array)):
			if "Yes" in array[i]:
				yes_1.append(array[i])
			elif "No" in array[i]:
				no_1.append(array[i])
		try:
		
			if len(yes_1) < 1 and len(no_1) >=1:
				if "False" in no_1[-1]:
					#print("Please Pick Something")
					print()
				if "True" in no_1[-1]:
					final_no.append("No")
					
			if len(no_1) <1 and len(yes_1)>=1:
				if "False" in yes_1[-1]:
					#print("Please Pick Something")
					print()
				if "True" in yes_1[-1]:
					final_yes.append("Yes")

			if "False" in yes_1[-1] and "False" in no_1[-1]:
				#print("You did not pick anything")
				print()
			if "True" in yes_1[-1] and "False" in no_1[-1]:
				#print("The Ans is Yes")
				final_yes.append("Yes")
			if "False" in yes_1[-1] and "True" in no_1[-1]:
				#print("The Ans is No")
				final_no.append("No")
			if "True" in yes_1[-1] and "True" in no_1[-1]:
				#print("Please Pick Only One")
				print()
		
		except:
			print()
		no_1.clear()
		yes_1.clear()
	total = len(final_yes)+len(final_no)
	
	if total == 4:
	
		if len(final_yes)>=3:
			#print("Shit thats 3 or more")
			alert_result()
		elif len(final_yes) == 2 or len(final_yes) == 1:
			#print("Ok cool only 2 or less")
			worse_result()
		else:
			#print("You're cool")
			good_result()
	else:
		wx.MessageBox('Please Pick One of The Required Answers', 'ERROR',wx.OK | wx.ICON_ERROR)
		sys.exit(0)

#######################################################################################################################

hbox1 = wx.BoxSizer(wx.HORIZONTAL)
st1 = wx.StaticText(win, label = "Please Tick The Relevant Boxes")

st1.SetFont(font)
hbox1.Add(st1, flag = wx.RIGHT, border = 8)
vbox.Add(hbox1, flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, border=10)
######################################################################################################################

hbox2 = wx.BoxSizer(wx.HORIZONTAL)
st2 = wx.StaticText(win, label = "In the past Four Weeks Does The Patient Had?")

st2.SetFont(font)
hbox2.Add(st2, flag = wx.RIGHT, border = 8)
vbox.Add(hbox2, flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, border=10)


######################################################################################################################

hbox2 = wx.BoxSizer(wx.HORIZONTAL)
st2 = wx.StaticText(win, label = "\nDaytime Asthma Symptoms More Than Twice A Weeks?")

st2.SetFont(font)
hbox2.Add(st2, flag = wx.RIGHT, border = 8)
vbox.Add(hbox2, flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, border=10)

######################################################################################################################

hbox3 = wx.BoxSizer(wx.HORIZONTAL)

check_1 = wx.CheckBox(win, label="Yes")
check_1.Bind(wx.EVT_CHECKBOX, onChecked_1) 
check_1.SetFont(font)
hbox3.Add(check_1, flag = wx.EXPAND|wx.LEFT, border = 8)

check_2 = wx.CheckBox(win, label="No")
check_2.Bind(wx.EVT_CHECKBOX, onChecked_1) 
check_2.SetFont(font)
hbox3.Add(check_2, flag = wx.EXPAND|wx.RIGHT, border = 100)

vbox.Add(hbox3, flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, border=10)



######################################################################################################################

hbox4 = wx.BoxSizer(wx.HORIZONTAL)
st3 = wx.StaticText(win, label = "\nAny Night Waking Due To Asthma?")

st3.SetFont(font)
hbox4.Add(st3, flag = wx.RIGHT, border = 8)
vbox.Add(hbox4, flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, border=10)

######################################################################################################################

hbox5 = wx.BoxSizer(wx.HORIZONTAL)

check_3 = wx.CheckBox(win, label="Yes")
check_3.Bind(wx.EVT_CHECKBOX, onChecked_2) 
check_3.SetFont(font)
hbox5.Add(check_3, flag = wx.EXPAND|wx.LEFT, border = 8)

check_4 = wx.CheckBox(win, label="No")
check_4.Bind(wx.EVT_CHECKBOX, onChecked_2) 
check_4.SetFont(font)
hbox5.Add(check_4, flag = wx.EXPAND|wx.RIGHT, border = 100)

vbox.Add(hbox5, flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, border=10)

######################################################################################################################


hbox6 = wx.BoxSizer(wx.HORIZONTAL)
st4 = wx.StaticText(win, label = "\nReliever Needed More Than Twice/Week?")

st4.SetFont(font)
hbox6.Add(st4, flag = wx.RIGHT, border = 8)
vbox.Add(hbox6, flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, border=10)

######################################################################################################################

hbox7 = wx.BoxSizer(wx.HORIZONTAL)

check_5 = wx.CheckBox(win, label="Yes")
check_5.Bind(wx.EVT_CHECKBOX, onChecked_3) 
check_5.SetFont(font)
hbox7.Add(check_5, flag = wx.EXPAND|wx.LEFT, border = 8)

check_6 = wx.CheckBox(win, label="No")
check_6.Bind(wx.EVT_CHECKBOX, onChecked_3) 
check_6.SetFont(font)
hbox7.Add(check_6, flag = wx.EXPAND|wx.RIGHT, border = 100)

vbox.Add(hbox7, flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, border=10)

######################################################################################################################

hbox8 = wx.BoxSizer(wx.HORIZONTAL)
st5 = wx.StaticText(win, label = "\nAny Activity Limitations Due To Asthma?")

st5.SetFont(font)
hbox8.Add(st5, flag = wx.RIGHT, border = 8)
vbox.Add(hbox8, flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, border=10)

######################################################################################################################

hbox9 = wx.BoxSizer(wx.HORIZONTAL)

check_6 = wx.CheckBox(win, label="Yes")
check_6.Bind(wx.EVT_CHECKBOX, onChecked_4) 
check_6.SetFont(font)
hbox9.Add(check_6, flag = wx.EXPAND|wx.LEFT, border = 8)

check_7 = wx.CheckBox(win, label="No")
check_7.Bind(wx.EVT_CHECKBOX, onChecked_4) 
check_7.SetFont(font)
hbox9.Add(check_7, flag = wx.EXPAND|wx.RIGHT, border = 100)

vbox.Add(hbox9, flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, border=10)

######################################################################################################################

vbox.Add((-1,20))

hbox5 = wx.BoxSizer(wx.HORIZONTAL)

acc_info = wx.Button(win, label = 'Submit', size = (150,30))
hbox5.Add(acc_info)
acc_info.Bind(wx.EVT_BUTTON, submit_button)
vbox.Add(hbox5, flag = wx.CENTER)

win.SetSizer(vbox)

win.SetSizerAndFit(vbox)
win.Show()
app.MainLoop()
win.SetSizer(vbox)

