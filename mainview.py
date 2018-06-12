# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class main_frame
###########################################################################

class main_frame ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"deshuohaha", pos = wx.DefaultPosition, size = wx.Size( 1078,679 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		self.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWFRAME ) )
		self.SetBackgroundColour( wx.Colour( 204, 232, 207 ) )
		
		bSizer1 = wx.BoxSizer( wx.VERTICAL )
		
		self.MainTitle = wx.StaticText( self, wx.ID_ANY, u"欢迎使用商品信息管理系统", wx.Point( 1000,1000 ), wx.Size( 1500,100 ), wx.ALIGN_CENTRE )
		self.MainTitle.Wrap( -1 )
		self.MainTitle.SetFont( wx.Font( 50, 70, 90, 90, False, wx.EmptyString ) )
		self.MainTitle.SetForegroundColour( wx.Colour( 255, 0, 128 ) )
		self.MainTitle.SetBackgroundColour( wx.Colour( 146, 215, 252 ) )
		
		bSizer1.Add( self.MainTitle, 0, wx.ALL, 5 )
		
		self.denglu_button = wx.Button( self, wx.ID_ANY, u"登陆", wx.Point( -1,-1 ), wx.Size( 500,100 ), 0 )
		self.denglu_button.SetFont( wx.Font( 20, 70, 90, 92, False, wx.EmptyString ) )
		self.denglu_button.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHT ) )
		self.denglu_button.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
		
		bSizer1.Add( self.denglu_button, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )
		
		self.zhuce_button = wx.Button( self, wx.ID_ANY, u"注册", wx.DefaultPosition, wx.Size( 500,100 ), 0 )
		self.zhuce_button.SetFont( wx.Font( 20, 70, 90, 92, False, wx.EmptyString ) )
		self.zhuce_button.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHT ) )
		self.zhuce_button.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
		
		bSizer1.Add( self.zhuce_button, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.zhuce_button1 = wx.Button( self, wx.ID_ANY, u"退出", wx.DefaultPosition, wx.Size( 500,100 ), 0 )
		self.zhuce_button1.SetFont( wx.Font( 20, 70, 90, 92, False, wx.EmptyString ) )
		self.zhuce_button1.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHT ) )
		self.zhuce_button1.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
		
		bSizer1.Add( self.zhuce_button1, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		self.SetSizer( bSizer1 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.Bind( wx.EVT_ERASE_BACKGROUND, self.set_bgimg )
		self.denglu_button.Bind( wx.EVT_BUTTON, self.goto_dengluframe )
		self.zhuce_button.Bind( wx.EVT_BUTTON, self.goto_zhuceframe )
		self.zhuce_button1.Bind( wx.EVT_BUTTON, self.exitapp )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def set_bgimg( self, event ):
		event.Skip()
	
	def goto_dengluframe( self, event ):
		event.Skip()
	
	def goto_zhuceframe( self, event ):
		event.Skip()
	
	def exitapp( self, event ):
		event.Skip()
	

###########################################################################
## Class zhuce_frame
###########################################################################

class zhuce_frame ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"注册", pos = wx.DefaultPosition, size = wx.Size( 774,340 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.Colour( 204, 232, 207 ) )
		
		bSizer2 = wx.BoxSizer( wx.VERTICAL )
		
		self.MainTitle = wx.StaticText( self, wx.ID_ANY, u"注册", wx.Point( 1000,1000 ), wx.Size( 1500,100 ), wx.ALIGN_CENTRE )
		self.MainTitle.Wrap( -1 )
		self.MainTitle.SetFont( wx.Font( 50, 70, 90, 90, False, wx.EmptyString ) )
		self.MainTitle.SetForegroundColour( wx.Colour( 255, 0, 128 ) )
		self.MainTitle.SetBackgroundColour( wx.Colour( 146, 215, 252 ) )
		
		bSizer2.Add( self.MainTitle, 0, wx.ALL, 5 )
		
		bSizer6 = wx.BoxSizer( wx.VERTICAL )
		
		gSizer1 = wx.GridSizer( 0, 2, 0, 0 )
		
		bSizer3 = wx.BoxSizer( wx.VERTICAL )
		
		self.zhuce_id = wx.StaticText( self, wx.ID_ANY, u"用户名：", wx.DefaultPosition, wx.Size( 150,30 ), wx.ALIGN_RIGHT )
		self.zhuce_id.Wrap( -1 )
		self.zhuce_id.SetFont( wx.Font( 20, 71, 90, 92, False, wx.EmptyString ) )
		
		bSizer3.Add( self.zhuce_id, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )
		
		self.zhuce_password1 = wx.StaticText( self, wx.ID_ANY, u"密码：", wx.DefaultPosition, wx.Size( 150,30 ), wx.ALIGN_RIGHT )
		self.zhuce_password1.Wrap( -1 )
		self.zhuce_password1.SetFont( wx.Font( 20, 71, 90, 92, False, wx.EmptyString ) )
		
		bSizer3.Add( self.zhuce_password1, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )
		
		self.zhuce_password2 = wx.StaticText( self, wx.ID_ANY, u"确认密码：", wx.DefaultPosition, wx.Size( 200,30 ), wx.ALIGN_RIGHT )
		self.zhuce_password2.Wrap( -1 )
		self.zhuce_password2.SetFont( wx.Font( 20, 71, 90, 92, False, wx.EmptyString ) )
		
		bSizer3.Add( self.zhuce_password2, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )
		
		
		gSizer1.Add( bSizer3, 1, wx.EXPAND, 5 )
		
		gSizer3 = wx.GridSizer( 0, 2, 0, 0 )
		
		bSizer4 = wx.BoxSizer( wx.VERTICAL )
		
		self.zhuce_text_id = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 250,30 ), 0 )
		self.zhuce_text_id.SetMaxLength( 20 ) 
		bSizer4.Add( self.zhuce_text_id, 0, wx.ALL, 5 )
		
		self.zhuce_text_password1 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 250,30 ), wx.TE_PASSWORD )
		self.zhuce_text_password1.SetMaxLength( 20 ) 
		bSizer4.Add( self.zhuce_text_password1, 0, wx.ALL, 5 )
		
		self.zhuce_text_password2 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 250,30 ), wx.TE_PASSWORD )
		self.zhuce_text_password2.SetMaxLength( 20 ) 
		bSizer4.Add( self.zhuce_text_password2, 0, wx.ALL, 5 )
		
		
		gSizer3.Add( bSizer4, 1, wx.EXPAND, 5 )
		
		self.zhuce_check_button = wx.Button( self, wx.ID_ANY, u"检查用户名", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer3.Add( self.zhuce_check_button, 0, wx.ALL, 5 )
		
		
		gSizer1.Add( gSizer3, 1, wx.EXPAND, 5 )
		
		
		bSizer6.Add( gSizer1, 1, wx.EXPAND, 5 )
		
		gSizer2 = wx.GridSizer( 1, 3, 0, 0 )
		
		self.zhuce_button_ok = wx.Button( self, wx.ID_ANY, u"确定", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer2.Add( self.zhuce_button_ok, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )
		
		self.zhuce_button_clear = wx.Button( self, wx.ID_ANY, u"清除", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer2.Add( self.zhuce_button_clear, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.zhuce_button_back = wx.Button( self, wx.ID_ANY, u"返回", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer2.Add( self.zhuce_button_back, 0, wx.TOP|wx.BOTTOM|wx.RIGHT, 5 )
		
		
		bSizer6.Add( gSizer2, 1, wx.EXPAND, 1 )
		
		
		bSizer2.Add( bSizer6, 1, wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer2 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.zhuce_check_button.Bind( wx.EVT_BUTTON, self.zhuce_sqlCheck )
		self.zhuce_button_ok.Bind( wx.EVT_BUTTON, self.zhuce_ok )
		self.zhuce_button_clear.Bind( wx.EVT_BUTTON, self.zhuce_clear_text )
		self.zhuce_button_back.Bind( wx.EVT_BUTTON, self.zhuce_goback )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def zhuce_sqlCheck( self, event ):
		event.Skip()
	
	def zhuce_ok( self, event ):
		event.Skip()
	
	def zhuce_clear_text( self, event ):
		event.Skip()
	
	def zhuce_goback( self, event ):
		event.Skip()
	

###########################################################################
## Class denglu_frame
###########################################################################

class denglu_frame ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"登陆", pos = wx.DefaultPosition, size = wx.Size( 774,340 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.Colour( 204, 232, 207 ) )
		
		bSizer2 = wx.BoxSizer( wx.VERTICAL )
		
		self.dengluTitle = wx.StaticText( self, wx.ID_ANY, u"登陆", wx.Point( 1000,1000 ), wx.Size( 1500,100 ), wx.ALIGN_CENTRE )
		self.dengluTitle.Wrap( -1 )
		self.dengluTitle.SetFont( wx.Font( 50, 70, 90, 90, False, wx.EmptyString ) )
		self.dengluTitle.SetForegroundColour( wx.Colour( 255, 0, 128 ) )
		self.dengluTitle.SetBackgroundColour( wx.Colour( 146, 215, 252 ) )
		
		bSizer2.Add( self.dengluTitle, 0, wx.ALL, 5 )
		
		bSizer6 = wx.BoxSizer( wx.VERTICAL )
		
		gSizer1 = wx.GridSizer( 0, 2, 0, 0 )
		
		bSizer3 = wx.BoxSizer( wx.VERTICAL )
		
		self.denglu_id = wx.StaticText( self, wx.ID_ANY, u"用户名：", wx.DefaultPosition, wx.Size( 150,30 ), wx.ALIGN_RIGHT )
		self.denglu_id.Wrap( -1 )
		self.denglu_id.SetFont( wx.Font( 20, 71, 90, 92, False, wx.EmptyString ) )
		
		bSizer3.Add( self.denglu_id, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )
		
		self.denglu_password = wx.StaticText( self, wx.ID_ANY, u"  密码：", wx.DefaultPosition, wx.Size( 150,30 ), wx.ALIGN_RIGHT )
		self.denglu_password.Wrap( -1 )
		self.denglu_password.SetFont( wx.Font( 20, 71, 90, 92, False, wx.EmptyString ) )
		
		bSizer3.Add( self.denglu_password, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )
		
		
		gSizer1.Add( bSizer3, 1, wx.EXPAND, 5 )
		
		bSizer4 = wx.BoxSizer( wx.VERTICAL )
		
		self.denglu_text_id = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 250,30 ), 0 )
		self.denglu_text_id.SetMaxLength( 20 ) 
		bSizer4.Add( self.denglu_text_id, 0, wx.ALL, 5 )
		
		self.denglu_text_password = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 250,30 ), wx.TE_PASSWORD )
		self.denglu_text_password.SetMaxLength( 20 ) 
		bSizer4.Add( self.denglu_text_password, 0, wx.ALL, 5 )
		
		
		gSizer1.Add( bSizer4, 1, wx.EXPAND, 5 )
		
		
		bSizer6.Add( gSizer1, 1, wx.EXPAND, 5 )
		
		gSizer2 = wx.GridSizer( 1, 3, 0, 0 )
		
		self.denglu_button_ok = wx.Button( self, wx.ID_ANY, u"确定", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer2.Add( self.denglu_button_ok, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )
		
		self.denglu_button_clear = wx.Button( self, wx.ID_ANY, u"清除", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer2.Add( self.denglu_button_clear, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.denglu_button_back = wx.Button( self, wx.ID_ANY, u"返回", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer2.Add( self.denglu_button_back, 0, wx.TOP|wx.BOTTOM|wx.RIGHT, 5 )
		
		
		bSizer6.Add( gSizer2, 1, wx.EXPAND, 1 )
		
		
		bSizer2.Add( bSizer6, 1, wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer2 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.denglu_button_ok.Bind( wx.EVT_BUTTON, self.denglu_ok )
		self.denglu_button_clear.Bind( wx.EVT_BUTTON, self.denglu_clear_text )
		self.denglu_button_back.Bind( wx.EVT_BUTTON, self.denglu_goback )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def denglu_ok( self, event ):
		event.Skip()
	
	def denglu_clear_text( self, event ):
		event.Skip()
	
	def denglu_goback( self, event ):
		event.Skip()
	

###########################################################################
## Class caozuo_frame
###########################################################################

class caozuo_frame ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"deshuohaha", pos = wx.DefaultPosition, size = wx.Size( 1078,720 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		self.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWFRAME ) )
		self.SetBackgroundColour( wx.Colour( 204, 232, 207 ) )
		
		bSizer1 = wx.BoxSizer( wx.VERTICAL )
		
		self.caozuoTitle = wx.StaticText( self, wx.ID_ANY, u"选择操作", wx.Point( 1000,1000 ), wx.Size( 1500,100 ), wx.ALIGN_CENTRE )
		self.caozuoTitle.Wrap( -1 )
		self.caozuoTitle.SetFont( wx.Font( 50, 70, 90, 90, False, wx.EmptyString ) )
		self.caozuoTitle.SetForegroundColour( wx.Colour( 255, 0, 128 ) )
		self.caozuoTitle.SetBackgroundColour( wx.Colour( 146, 215, 252 ) )
		
		bSizer1.Add( self.caozuoTitle, 0, wx.ALL, 5 )
		
		self.caozuo_text_user = wx.StaticText( self, wx.ID_ANY, u"欢迎你：", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.caozuo_text_user.Wrap( -1 )
		self.caozuo_text_user.SetFont( wx.Font( 15, 70, 90, 92, False, wx.EmptyString ) )
		
		bSizer1.Add( self.caozuo_text_user, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.tianjia_button = wx.Button( self, wx.ID_ANY, u"添加商品", wx.Point( -1,-1 ), wx.Size( 500,100 ), 0 )
		self.tianjia_button.SetFont( wx.Font( 20, 70, 90, 92, False, wx.EmptyString ) )
		self.tianjia_button.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHT ) )
		self.tianjia_button.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
		
		bSizer1.Add( self.tianjia_button, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )
		
		self.chaxun_button = wx.Button( self, wx.ID_ANY, u"查询商品", wx.DefaultPosition, wx.Size( 500,100 ), 0 )
		self.chaxun_button.SetFont( wx.Font( 20, 70, 90, 92, False, wx.EmptyString ) )
		self.chaxun_button.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHT ) )
		self.chaxun_button.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
		
		bSizer1.Add( self.chaxun_button, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.xiugai_button = wx.Button( self, wx.ID_ANY, u"修改商品", wx.Point( -1,-1 ), wx.Size( 500,100 ), 0 )
		self.xiugai_button.SetFont( wx.Font( 20, 70, 90, 92, False, wx.EmptyString ) )
		self.xiugai_button.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHT ) )
		self.xiugai_button.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
		
		bSizer1.Add( self.xiugai_button, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.shanchu_button = wx.Button( self, wx.ID_ANY, u"删除商品", wx.Point( -1,-1 ), wx.Size( 500,100 ), 0 )
		self.shanchu_button.SetFont( wx.Font( 20, 70, 90, 92, False, wx.EmptyString ) )
		self.shanchu_button.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHT ) )
		self.shanchu_button.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
		
		bSizer1.Add( self.shanchu_button, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.caozuo_button_back = wx.Button( self, wx.ID_ANY, u"退出登陆", wx.DefaultPosition, wx.Size( 500,100 ), 0 )
		self.caozuo_button_back.SetFont( wx.Font( 20, 70, 90, 92, False, wx.EmptyString ) )
		self.caozuo_button_back.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHT ) )
		self.caozuo_button_back.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
		
		bSizer1.Add( self.caozuo_button_back, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		self.SetSizer( bSizer1 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.Bind( wx.EVT_ERASE_BACKGROUND, self.set_bgimg )
		self.tianjia_button.Bind( wx.EVT_BUTTON, self.goto_tianjiaframe )
		self.chaxun_button.Bind( wx.EVT_BUTTON, self.goto_chaxunframe )
		self.xiugai_button.Bind( wx.EVT_BUTTON, self.goto_xiugaiframe )
		self.shanchu_button.Bind( wx.EVT_BUTTON, self.goto_shanchuframe )
		self.caozuo_button_back.Bind( wx.EVT_BUTTON, self.caozuo_back )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def set_bgimg( self, event ):
		event.Skip()
	
	def goto_tianjiaframe( self, event ):
		event.Skip()
	
	def goto_chaxunframe( self, event ):
		event.Skip()
	
	def goto_xiugaiframe( self, event ):
		event.Skip()
	
	def goto_shanchuframe( self, event ):
		event.Skip()
	
	def caozuo_back( self, event ):
		event.Skip()
	

###########################################################################
## Class tianjia_frame
###########################################################################

class tianjia_frame ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"deshuohaha", pos = wx.DefaultPosition, size = wx.Size( 1098,536 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		self.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWFRAME ) )
		self.SetBackgroundColour( wx.Colour( 204, 232, 207 ) )
		
		bSizer1 = wx.BoxSizer( wx.VERTICAL )
		
		self.caozuoTitle = wx.StaticText( self, wx.ID_ANY, u"添加商品", wx.Point( 1000,1000 ), wx.Size( 1500,100 ), wx.ALIGN_CENTRE )
		self.caozuoTitle.Wrap( -1 )
		self.caozuoTitle.SetFont( wx.Font( 50, 70, 90, 90, False, wx.EmptyString ) )
		self.caozuoTitle.SetForegroundColour( wx.Colour( 255, 0, 128 ) )
		self.caozuoTitle.SetBackgroundColour( wx.Colour( 146, 215, 252 ) )
		
		bSizer1.Add( self.caozuoTitle, 0, wx.ALL, 5 )
		
		self.tianjia_text_user = wx.StaticText( self, wx.ID_ANY, u"欢迎你：", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.tianjia_text_user.Wrap( -1 )
		self.tianjia_text_user.SetFont( wx.Font( 15, 70, 90, 92, False, wx.EmptyString ) )
		
		bSizer1.Add( self.tianjia_text_user, 0, wx.ALL|wx.EXPAND, 5 )
		
		gSizer8 = wx.GridSizer( 0, 2, 0, 0 )
		
		bSizer30 = wx.BoxSizer( wx.VERTICAL )
		
		self.tianjia_name = wx.StaticText( self, wx.ID_ANY, u"商品名称：", wx.DefaultPosition, wx.Size( 200,30 ), wx.ALIGN_RIGHT )
		self.tianjia_name.Wrap( -1 )
		self.tianjia_name.SetFont( wx.Font( 20, 71, 90, 92, False, wx.EmptyString ) )
		
		bSizer30.Add( self.tianjia_name, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )
		
		self.tianjia_guojia = wx.StaticText( self, wx.ID_ANY, u"国家代码（3位）：", wx.DefaultPosition, wx.Size( 250,30 ), wx.ALIGN_RIGHT )
		self.tianjia_guojia.Wrap( -1 )
		self.tianjia_guojia.SetFont( wx.Font( 20, 71, 90, 92, False, wx.EmptyString ) )
		
		bSizer30.Add( self.tianjia_guojia, 0, wx.ALL|wx.ALIGN_RIGHT|wx.EXPAND, 5 )
		
		self.tianjia_changshang = wx.StaticText( self, wx.ID_ANY, u"厂商代码（4位）：", wx.DefaultPosition, wx.Size( 250,30 ), wx.ALIGN_RIGHT )
		self.tianjia_changshang.Wrap( -1 )
		self.tianjia_changshang.SetFont( wx.Font( 20, 71, 90, 92, False, wx.EmptyString ) )
		
		bSizer30.Add( self.tianjia_changshang, 0, wx.ALL|wx.ALIGN_RIGHT|wx.EXPAND, 5 )
		
		self.tianjia_shangpin = wx.StaticText( self, wx.ID_ANY, u"商品代码（5位）：", wx.DefaultPosition, wx.Size( 200,30 ), wx.ALIGN_RIGHT )
		self.tianjia_shangpin.Wrap( -1 )
		self.tianjia_shangpin.SetFont( wx.Font( 20, 71, 90, 92, False, wx.EmptyString ) )
		
		bSizer30.Add( self.tianjia_shangpin, 0, wx.ALL|wx.ALIGN_RIGHT|wx.EXPAND, 5 )
		
		self.tianjia_type = wx.StaticText( self, wx.ID_ANY, u"类型：", wx.DefaultPosition, wx.Size( 150,30 ), wx.ALIGN_RIGHT )
		self.tianjia_type.Wrap( -1 )
		self.tianjia_type.SetFont( wx.Font( 20, 71, 90, 92, False, wx.EmptyString ) )
		
		bSizer30.Add( self.tianjia_type, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )
		
		
		gSizer8.Add( bSizer30, 1, wx.EXPAND, 5 )
		
		bSizer32 = wx.BoxSizer( wx.VERTICAL )
		
		self.tianjia_text_name = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 250,30 ), 0 )
		self.tianjia_text_name.SetMaxLength( 20 ) 
		bSizer32.Add( self.tianjia_text_name, 0, wx.ALL, 5 )
		
		self.tianjia_text_guojia = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 250,30 ), 0 )
		self.tianjia_text_guojia.SetMaxLength( 3 ) 
		bSizer32.Add( self.tianjia_text_guojia, 0, wx.ALL, 5 )
		
		self.tianjia_text_changshang = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 250,30 ), 0 )
		self.tianjia_text_changshang.SetMaxLength( 4 ) 
		bSizer32.Add( self.tianjia_text_changshang, 0, wx.ALL, 5 )
		
		self.tianjia_text_shangpin = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 250,30 ), 0 )
		self.tianjia_text_shangpin.SetMaxLength( 5 ) 
		bSizer32.Add( self.tianjia_text_shangpin, 0, wx.ALL, 5 )
		
		tianjia_choicetypeChoices = [ u"饮料", u"食品", u"日用品" ]
		self.tianjia_choicetype = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, tianjia_choicetypeChoices, 0 )
		self.tianjia_choicetype.SetSelection( 2 )
		bSizer32.Add( self.tianjia_choicetype, 0, wx.ALL, 5 )
		
		
		gSizer8.Add( bSizer32, 1, wx.EXPAND, 5 )
		
		
		bSizer1.Add( gSizer8, 1, wx.EXPAND, 5 )
		
		bSizer36 = wx.BoxSizer( wx.HORIZONTAL )
		
		gSizer10 = wx.GridSizer( 0, 3, 0, 0 )
		
		self.tianjia_button_ok = wx.Button( self, wx.ID_ANY, u"确定", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer10.Add( self.tianjia_button_ok, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )
		
		self.tianjia_button_clear = wx.Button( self, wx.ID_ANY, u"清除", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer10.Add( self.tianjia_button_clear, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.tianjia_button_close = wx.Button( self, wx.ID_ANY, u"返回", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer10.Add( self.tianjia_button_close, 0, wx.ALL, 5 )
		
		
		bSizer36.Add( gSizer10, 1, wx.EXPAND, 5 )
		
		
		bSizer1.Add( bSizer36, 1, wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer1 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.Bind( wx.EVT_ERASE_BACKGROUND, self.set_bgimg )
		self.tianjia_button_ok.Bind( wx.EVT_BUTTON, self.tianjia_ok )
		self.tianjia_button_clear.Bind( wx.EVT_BUTTON, self.tianjia_clear )
		self.tianjia_button_close.Bind( wx.EVT_BUTTON, self.tianjia_back )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def set_bgimg( self, event ):
		event.Skip()
	
	def tianjia_ok( self, event ):
		event.Skip()
	
	def tianjia_clear( self, event ):
		event.Skip()
	
	def tianjia_back( self, event ):
		event.Skip()
	

###########################################################################
## Class chaxun_frame
###########################################################################

class chaxun_frame ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"deshuohaha", pos = wx.DefaultPosition, size = wx.Size( 1078,679 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		self.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWFRAME ) )
		self.SetBackgroundColour( wx.Colour( 204, 232, 207 ) )
		
		bSizer1 = wx.BoxSizer( wx.VERTICAL )
		
		self.chaxunTitle = wx.StaticText( self, wx.ID_ANY, u"查询商品", wx.Point( 1000,1000 ), wx.Size( 1500,100 ), wx.ALIGN_CENTRE )
		self.chaxunTitle.Wrap( -1 )
		self.chaxunTitle.SetFont( wx.Font( 50, 70, 90, 90, False, wx.EmptyString ) )
		self.chaxunTitle.SetForegroundColour( wx.Colour( 255, 0, 128 ) )
		self.chaxunTitle.SetBackgroundColour( wx.Colour( 146, 215, 252 ) )
		
		bSizer1.Add( self.chaxunTitle, 0, wx.ALL, 5 )
		
		self.tianjia_text_user = wx.StaticText( self, wx.ID_ANY, u"欢迎你：", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.tianjia_text_user.Wrap( -1 )
		self.tianjia_text_user.SetFont( wx.Font( 15, 70, 90, 92, False, wx.EmptyString ) )
		
		bSizer1.Add( self.tianjia_text_user, 0, wx.ALL|wx.EXPAND, 5 )
		
		fgSizer1 = wx.FlexGridSizer( 7, 3, 0, 0 )
		fgSizer1.SetFlexibleDirection( wx.BOTH )
		fgSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.text_code = wx.StaticText( self, wx.ID_ANY, u"商品代码", wx.DefaultPosition, wx.Size( 300,-1 ), wx.ALIGN_CENTRE )
		self.text_code.Wrap( -1 )
		self.text_code.SetFont( wx.Font( 25, 70, 90, 92, False, wx.EmptyString ) )
		
		fgSizer1.Add( self.text_code, 0, wx.ALL, 5 )
		
		self.text_name = wx.StaticText( self, wx.ID_ANY, u"商品名称", wx.DefaultPosition, wx.Size( 300,-1 ), wx.ALIGN_CENTRE )
		self.text_name.Wrap( -1 )
		self.text_name.SetFont( wx.Font( 25, 70, 90, 92, False, wx.EmptyString ) )
		
		fgSizer1.Add( self.text_name, 0, wx.ALL, 5 )
		
		self.text_type = wx.StaticText( self, wx.ID_ANY, u"商品类型", wx.DefaultPosition, wx.Size( 300,-1 ), wx.ALIGN_CENTRE )
		self.text_type.Wrap( -1 )
		self.text_type.SetFont( wx.Font( 25, 70, 90, 92, False, wx.EmptyString ) )
		
		fgSizer1.Add( self.text_type, 0, wx.ALL, 5 )
		
		self.info_text11 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 300,-1 ), wx.ALIGN_CENTRE )
		self.info_text11.Wrap( -1 )
		self.info_text11.SetFont( wx.Font( 15, 70, 90, 90, False, wx.EmptyString ) )
		
		fgSizer1.Add( self.info_text11, 0, wx.ALL, 5 )
		
		self.info_text12 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 300,-1 ), wx.ALIGN_CENTRE )
		self.info_text12.Wrap( -1 )
		self.info_text12.SetFont( wx.Font( 15, 70, 90, 90, False, wx.EmptyString ) )
		
		fgSizer1.Add( self.info_text12, 0, wx.ALL, 5 )
		
		self.info_text13 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 300,-1 ), wx.ALIGN_CENTRE )
		self.info_text13.Wrap( -1 )
		self.info_text13.SetFont( wx.Font( 15, 70, 90, 90, False, wx.EmptyString ) )
		
		fgSizer1.Add( self.info_text13, 0, wx.ALL, 5 )
		
		self.info_text21 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 300,-1 ), wx.ALIGN_CENTRE )
		self.info_text21.Wrap( -1 )
		self.info_text21.SetFont( wx.Font( 15, 70, 90, 90, False, wx.EmptyString ) )
		
		fgSizer1.Add( self.info_text21, 0, wx.ALL, 5 )
		
		self.info_text22 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 300,-1 ), wx.ALIGN_CENTRE )
		self.info_text22.Wrap( -1 )
		self.info_text22.SetFont( wx.Font( 15, 70, 90, 90, False, wx.EmptyString ) )
		
		fgSizer1.Add( self.info_text22, 0, wx.ALL, 5 )
		
		self.info_text23 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 300,-1 ), wx.ALIGN_CENTRE )
		self.info_text23.Wrap( -1 )
		self.info_text23.SetFont( wx.Font( 15, 70, 90, 90, False, wx.EmptyString ) )
		
		fgSizer1.Add( self.info_text23, 0, wx.ALL, 5 )
		
		self.info_text31 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 300,-1 ), wx.ALIGN_CENTRE )
		self.info_text31.Wrap( -1 )
		self.info_text31.SetFont( wx.Font( 15, 70, 90, 90, False, wx.EmptyString ) )
		
		fgSizer1.Add( self.info_text31, 0, wx.ALL, 5 )
		
		self.info_text32 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 300,-1 ), wx.ALIGN_CENTRE )
		self.info_text32.Wrap( -1 )
		self.info_text32.SetFont( wx.Font( 15, 70, 90, 90, False, wx.EmptyString ) )
		
		fgSizer1.Add( self.info_text32, 0, wx.ALL, 5 )
		
		self.info_text33 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 300,-1 ), wx.ALIGN_CENTRE )
		self.info_text33.Wrap( -1 )
		self.info_text33.SetFont( wx.Font( 15, 70, 90, 90, False, wx.EmptyString ) )
		
		fgSizer1.Add( self.info_text33, 0, wx.ALL, 5 )
		
		self.info_text41 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 300,-1 ), wx.ALIGN_CENTRE )
		self.info_text41.Wrap( -1 )
		self.info_text41.SetFont( wx.Font( 15, 70, 90, 90, False, wx.EmptyString ) )
		
		fgSizer1.Add( self.info_text41, 0, wx.ALL, 5 )
		
		self.info_text42 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 300,-1 ), wx.ALIGN_CENTRE )
		self.info_text42.Wrap( -1 )
		self.info_text42.SetFont( wx.Font( 15, 70, 90, 90, False, wx.EmptyString ) )
		
		fgSizer1.Add( self.info_text42, 0, wx.ALL, 5 )
		
		self.info_text43 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 300,-1 ), wx.ALIGN_CENTRE )
		self.info_text43.Wrap( -1 )
		self.info_text43.SetFont( wx.Font( 15, 70, 90, 90, False, wx.EmptyString ) )
		
		fgSizer1.Add( self.info_text43, 0, wx.ALL, 5 )
		
		self.info_text51 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 300,-1 ), wx.ALIGN_CENTRE )
		self.info_text51.Wrap( -1 )
		self.info_text51.SetFont( wx.Font( 15, 70, 90, 90, False, wx.EmptyString ) )
		
		fgSizer1.Add( self.info_text51, 0, wx.ALL, 5 )
		
		self.info_text52 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 300,-1 ), wx.ALIGN_CENTRE )
		self.info_text52.Wrap( -1 )
		self.info_text52.SetFont( wx.Font( 15, 70, 90, 90, False, wx.EmptyString ) )
		
		fgSizer1.Add( self.info_text52, 0, wx.ALL, 5 )
		
		self.info_text53 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 300,-1 ), wx.ALIGN_CENTRE )
		self.info_text53.Wrap( -1 )
		self.info_text53.SetFont( wx.Font( 15, 70, 90, 90, False, wx.EmptyString ) )
		
		fgSizer1.Add( self.info_text53, 0, wx.ALL, 5 )
		
		self.m_button42 = wx.Button( self, wx.ID_ANY, u"返回", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer1.Add( self.m_button42, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		bSizer1.Add( fgSizer1, 1, wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer1 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.Bind( wx.EVT_ERASE_BACKGROUND, self.set_bgimg )
		self.m_button42.Bind( wx.EVT_BUTTON, self.chaxun_back )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def set_bgimg( self, event ):
		event.Skip()
	
	def chaxun_back( self, event ):
		event.Skip()
	

###########################################################################
## Class xiugai_frame
###########################################################################

class xiugai_frame ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"deshuohaha", pos = wx.DefaultPosition, size = wx.Size( 1078,493 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		self.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWFRAME ) )
		self.SetBackgroundColour( wx.Colour( 204, 232, 207 ) )
		
		bSizer1 = wx.BoxSizer( wx.VERTICAL )
		
		self.chaxunTitle = wx.StaticText( self, wx.ID_ANY, u"修改商品", wx.Point( 1000,1000 ), wx.Size( 1500,100 ), wx.ALIGN_CENTRE )
		self.chaxunTitle.Wrap( -1 )
		self.chaxunTitle.SetFont( wx.Font( 50, 70, 90, 90, False, wx.EmptyString ) )
		self.chaxunTitle.SetForegroundColour( wx.Colour( 255, 0, 128 ) )
		self.chaxunTitle.SetBackgroundColour( wx.Colour( 146, 215, 252 ) )
		
		bSizer1.Add( self.chaxunTitle, 0, wx.ALL, 5 )
		
		self.tianjia_text_user = wx.StaticText( self, wx.ID_ANY, u"欢迎你：", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.tianjia_text_user.Wrap( -1 )
		self.tianjia_text_user.SetFont( wx.Font( 15, 70, 90, 92, False, wx.EmptyString ) )
		
		bSizer1.Add( self.tianjia_text_user, 0, wx.ALL|wx.EXPAND, 5 )
		
		gSizer8 = wx.GridSizer( 0, 2, 0, 0 )
		
		bSizer30 = wx.BoxSizer( wx.VERTICAL )
		
		self.xiugai_code = wx.StaticText( self, wx.ID_ANY, u"商品代码：", wx.DefaultPosition, wx.Size( 200,30 ), wx.ALIGN_RIGHT )
		self.xiugai_code.Wrap( -1 )
		self.xiugai_code.SetFont( wx.Font( 20, 71, 90, 92, False, wx.EmptyString ) )
		
		bSizer30.Add( self.xiugai_code, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )
		
		
		gSizer8.Add( bSizer30, 1, wx.EXPAND, 5 )
		
		bSizer32 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.xiugai_text_code = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 250,30 ), 0 )
		self.xiugai_text_code.SetMaxLength( 13 ) 
		bSizer32.Add( self.xiugai_text_code, 0, wx.ALL, 5 )
		
		self.xiugai_button_chaxun = wx.Button( self, wx.ID_ANY, u"查询", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer32.Add( self.xiugai_button_chaxun, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )
		
		self.xiugai_button_clear = wx.Button( self, wx.ID_ANY, u"清除", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer32.Add( self.xiugai_button_clear, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		gSizer8.Add( bSizer32, 1, wx.EXPAND, 5 )
		
		
		bSizer1.Add( gSizer8, 0, wx.EXPAND, 5 )
		
		bSizer45 = wx.BoxSizer( wx.VERTICAL )
		
		gSizer12 = wx.GridSizer( 0, 2, 0, 0 )
		
		bSizer43 = wx.BoxSizer( wx.VERTICAL )
		
		self.info_name = wx.StaticText( self, wx.ID_ANY, u"商品名称：", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_RIGHT )
		self.info_name.Wrap( -1 )
		self.info_name.SetFont( wx.Font( 20, 70, 90, 92, False, wx.EmptyString ) )
		
		bSizer43.Add( self.info_name, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )
		
		self.info_type = wx.StaticText( self, wx.ID_ANY, u"商品类型：", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_RIGHT )
		self.info_type.Wrap( -1 )
		self.info_type.SetFont( wx.Font( 20, 70, 90, 92, False, wx.EmptyString ) )
		
		bSizer43.Add( self.info_type, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )
		
		
		gSizer12.Add( bSizer43, 1, wx.EXPAND, 5 )
		
		bSizer44 = wx.BoxSizer( wx.VERTICAL )
		
		self.result_name = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer44.Add( self.result_name, 0, wx.ALL, 5 )
		
		xiugai_choicetypeChoices = [ u"饮料", u"食品", u"日用品" ]
		self.xiugai_choicetype = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, xiugai_choicetypeChoices, 0 )
		self.xiugai_choicetype.SetSelection( 2 )
		bSizer44.Add( self.xiugai_choicetype, 0, wx.ALL, 5 )
		
		
		gSizer12.Add( bSizer44, 1, wx.EXPAND, 5 )
		
		
		bSizer45.Add( gSizer12, 0, wx.EXPAND, 5 )
		
		bSizer36 = wx.BoxSizer( wx.HORIZONTAL )
		
		gSizer10 = wx.GridSizer( 0, 2, 0, 0 )
		
		self.xiugai_button_ok = wx.Button( self, wx.ID_ANY, u"确定", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer10.Add( self.xiugai_button_ok, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )
		
		self.xiugai_button_close = wx.Button( self, wx.ID_ANY, u"返回", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer10.Add( self.xiugai_button_close, 0, wx.ALL, 5 )
		
		
		bSizer36.Add( gSizer10, 1, wx.EXPAND, 5 )
		
		
		bSizer45.Add( bSizer36, 0, wx.EXPAND, 5 )
		
		
		bSizer1.Add( bSizer45, 1, wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer1 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.Bind( wx.EVT_ERASE_BACKGROUND, self.set_bgimg )
		self.xiugai_button_chaxun.Bind( wx.EVT_BUTTON, self.xiugai_chaxun )
		self.xiugai_button_clear.Bind( wx.EVT_BUTTON, self.xiugai_clear )
		self.xiugai_button_ok.Bind( wx.EVT_BUTTON, self.xiugai_ok )
		self.xiugai_button_close.Bind( wx.EVT_BUTTON, self.xiugai_back )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def set_bgimg( self, event ):
		event.Skip()
	
	def xiugai_chaxun( self, event ):
		event.Skip()
	
	def xiugai_clear( self, event ):
		event.Skip()
	
	def xiugai_ok( self, event ):
		event.Skip()
	
	def xiugai_back( self, event ):
		event.Skip()
	

###########################################################################
## Class shanchu_frame
###########################################################################

class shanchu_frame ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"deshuohaha", pos = wx.DefaultPosition, size = wx.Size( 1078,493 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		self.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWFRAME ) )
		self.SetBackgroundColour( wx.Colour( 204, 232, 207 ) )
		
		bSizer1 = wx.BoxSizer( wx.VERTICAL )
		
		self.shanchuTitle = wx.StaticText( self, wx.ID_ANY, u"删除商品", wx.Point( 1000,1000 ), wx.Size( 1500,100 ), wx.ALIGN_CENTRE )
		self.shanchuTitle.Wrap( -1 )
		self.shanchuTitle.SetFont( wx.Font( 50, 70, 90, 90, False, wx.EmptyString ) )
		self.shanchuTitle.SetForegroundColour( wx.Colour( 255, 0, 128 ) )
		self.shanchuTitle.SetBackgroundColour( wx.Colour( 146, 215, 252 ) )
		
		bSizer1.Add( self.shanchuTitle, 0, wx.ALL, 5 )
		
		self.tianjia_text_user = wx.StaticText( self, wx.ID_ANY, u"欢迎你：", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.tianjia_text_user.Wrap( -1 )
		self.tianjia_text_user.SetFont( wx.Font( 15, 70, 90, 92, False, wx.EmptyString ) )
		
		bSizer1.Add( self.tianjia_text_user, 0, wx.ALL|wx.EXPAND, 5 )
		
		gSizer8 = wx.GridSizer( 0, 2, 0, 0 )
		
		bSizer30 = wx.BoxSizer( wx.VERTICAL )
		
		self.shanchu_code = wx.StaticText( self, wx.ID_ANY, u"商品代码：", wx.DefaultPosition, wx.Size( 200,30 ), wx.ALIGN_RIGHT )
		self.shanchu_code.Wrap( -1 )
		self.shanchu_code.SetFont( wx.Font( 20, 71, 90, 92, False, wx.EmptyString ) )
		
		bSizer30.Add( self.shanchu_code, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )
		
		
		gSizer8.Add( bSizer30, 1, wx.EXPAND, 5 )
		
		bSizer32 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.shanchu_text_code = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 250,30 ), 0 )
		self.shanchu_text_code.SetMaxLength( 13 ) 
		bSizer32.Add( self.shanchu_text_code, 0, wx.ALL, 5 )
		
		self.shanchu_button_chaxun = wx.Button( self, wx.ID_ANY, u"查询", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer32.Add( self.shanchu_button_chaxun, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )
		
		self.shanchu_button_clear = wx.Button( self, wx.ID_ANY, u"清除", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer32.Add( self.shanchu_button_clear, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		gSizer8.Add( bSizer32, 1, wx.EXPAND, 5 )
		
		
		bSizer1.Add( gSizer8, 0, wx.EXPAND, 5 )
		
		bSizer45 = wx.BoxSizer( wx.VERTICAL )
		
		gSizer12 = wx.GridSizer( 0, 2, 0, 0 )
		
		bSizer43 = wx.BoxSizer( wx.VERTICAL )
		
		self.info_name = wx.StaticText( self, wx.ID_ANY, u"商品名称：", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_RIGHT )
		self.info_name.Wrap( -1 )
		self.info_name.SetFont( wx.Font( 20, 70, 90, 92, False, wx.EmptyString ) )
		
		bSizer43.Add( self.info_name, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )
		
		self.info_type = wx.StaticText( self, wx.ID_ANY, u"商品类型：", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_RIGHT )
		self.info_type.Wrap( -1 )
		self.info_type.SetFont( wx.Font( 20, 70, 90, 92, False, wx.EmptyString ) )
		
		bSizer43.Add( self.info_type, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )
		
		
		gSizer12.Add( bSizer43, 1, wx.EXPAND, 5 )
		
		bSizer44 = wx.BoxSizer( wx.VERTICAL )
		
		self.result_name = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_RIGHT )
		self.result_name.Wrap( -1 )
		self.result_name.SetFont( wx.Font( 20, 70, 90, 92, False, wx.EmptyString ) )
		
		bSizer44.Add( self.result_name, 0, wx.ALL, 5 )
		
		self.result_shangpintype = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_RIGHT )
		self.result_shangpintype.Wrap( -1 )
		self.result_shangpintype.SetFont( wx.Font( 20, 70, 90, 92, False, wx.EmptyString ) )
		
		bSizer44.Add( self.result_shangpintype, 0, wx.ALL, 5 )
		
		
		gSizer12.Add( bSizer44, 1, wx.EXPAND, 5 )
		
		
		bSizer45.Add( gSizer12, 0, wx.EXPAND, 5 )
		
		bSizer36 = wx.BoxSizer( wx.HORIZONTAL )
		
		gSizer10 = wx.GridSizer( 0, 2, 0, 0 )
		
		self.shanchu_button_ok = wx.Button( self, wx.ID_ANY, u"确定", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer10.Add( self.shanchu_button_ok, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )
		
		self.shanchu_button_close = wx.Button( self, wx.ID_ANY, u"返回", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer10.Add( self.shanchu_button_close, 0, wx.ALL, 5 )
		
		
		bSizer36.Add( gSizer10, 1, wx.EXPAND, 5 )
		
		
		bSizer45.Add( bSizer36, 0, wx.EXPAND, 5 )
		
		
		bSizer1.Add( bSizer45, 1, wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer1 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.Bind( wx.EVT_ERASE_BACKGROUND, self.set_bgimg )
		self.shanchu_button_chaxun.Bind( wx.EVT_BUTTON, self.shanchu_chaxun )
		self.shanchu_button_clear.Bind( wx.EVT_BUTTON, self.shanchu_clear )
		self.shanchu_button_ok.Bind( wx.EVT_BUTTON, self.shanchu_ok )
		self.shanchu_button_close.Bind( wx.EVT_BUTTON, self.shanchu_back )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def set_bgimg( self, event ):
		event.Skip()
	
	def shanchu_chaxun( self, event ):
		event.Skip()
	
	def shanchu_clear( self, event ):
		event.Skip()
	
	def shanchu_ok( self, event ):
		event.Skip()
	
	def shanchu_back( self, event ):
		event.Skip()
	

###########################################################################
## Class tanchuang1
###########################################################################

class tanchuang1 ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"错误", pos = wx.DefaultPosition, size = wx.Size( 400,159 ), style = wx.DEFAULT_DIALOG_STYLE|wx.STAY_ON_TOP )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer7 = wx.BoxSizer( wx.VERTICAL )
		
		self.error_text1 = wx.StaticText( self, wx.ID_ANY, u"用户名不能为空！", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTRE )
		self.error_text1.Wrap( -1 )
		self.error_text1.SetFont( wx.Font( 25, 70, 90, 90, False, wx.EmptyString ) )
		self.error_text1.SetMinSize( wx.Size( 500,50 ) )
		
		bSizer7.Add( self.error_text1, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.error_button1 = wx.Button( self, wx.ID_ANY, u"确定", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer7.Add( self.error_button1, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		self.SetSizer( bSizer7 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.error_button1.Bind( wx.EVT_BUTTON, self.dialog_close )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def dialog_close( self, event ):
		event.Skip()
	

###########################################################################
## Class tanchuang2
###########################################################################

class tanchuang2 ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"错误", pos = wx.DefaultPosition, size = wx.Size( 346,159 ), style = wx.DEFAULT_DIALOG_STYLE|wx.STAY_ON_TOP )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer7 = wx.BoxSizer( wx.VERTICAL )
		
		self.error_text2 = wx.StaticText( self, wx.ID_ANY, u"请检查用户名！", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTRE )
		self.error_text2.Wrap( -1 )
		self.error_text2.SetFont( wx.Font( 25, 70, 90, 90, False, wx.EmptyString ) )
		self.error_text2.SetMinSize( wx.Size( 500,50 ) )
		
		bSizer7.Add( self.error_text2, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.error_button2 = wx.Button( self, wx.ID_ANY, u"确定", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer7.Add( self.error_button2, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		self.SetSizer( bSizer7 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.error_button2.Bind( wx.EVT_BUTTON, self.dialog_close )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def dialog_close( self, event ):
		event.Skip()
	

###########################################################################
## Class tanchuang3
###########################################################################

class tanchuang3 ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"错误", pos = wx.DefaultPosition, size = wx.Size( 346,159 ), style = wx.DEFAULT_DIALOG_STYLE|wx.STAY_ON_TOP )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer7 = wx.BoxSizer( wx.VERTICAL )
		
		self.error_text3 = wx.StaticText( self, wx.ID_ANY, u"密码不能为空！", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTRE )
		self.error_text3.Wrap( -1 )
		self.error_text3.SetFont( wx.Font( 25, 70, 90, 90, False, wx.EmptyString ) )
		self.error_text3.SetMinSize( wx.Size( 500,50 ) )
		
		bSizer7.Add( self.error_text3, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.error_button3 = wx.Button( self, wx.ID_ANY, u"确定", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer7.Add( self.error_button3, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		self.SetSizer( bSizer7 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.error_button3.Bind( wx.EVT_BUTTON, self.dialog_close )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def dialog_close( self, event ):
		event.Skip()
	

###########################################################################
## Class tanchuang4
###########################################################################

class tanchuang4 ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"错误", pos = wx.DefaultPosition, size = wx.Size( 346,159 ), style = wx.DEFAULT_DIALOG_STYLE|wx.STAY_ON_TOP )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer7 = wx.BoxSizer( wx.VERTICAL )
		
		self.error_text4 = wx.StaticText( self, wx.ID_ANY, u"密码不一致！", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTRE )
		self.error_text4.Wrap( -1 )
		self.error_text4.SetFont( wx.Font( 25, 70, 90, 90, False, wx.EmptyString ) )
		self.error_text4.SetMinSize( wx.Size( 500,50 ) )
		
		bSizer7.Add( self.error_text4, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.error_button4 = wx.Button( self, wx.ID_ANY, u"确定", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer7.Add( self.error_button4, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		self.SetSizer( bSizer7 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.error_button4.Bind( wx.EVT_BUTTON, self.dialog_close )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def dialog_close( self, event ):
		event.Skip()
	

###########################################################################
## Class tanchuang5
###########################################################################

class tanchuang5 ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"错误", pos = wx.DefaultPosition, size = wx.Size( 346,159 ), style = wx.DEFAULT_DIALOG_STYLE|wx.STAY_ON_TOP )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer7 = wx.BoxSizer( wx.VERTICAL )
		
		self.error_text5 = wx.StaticText( self, wx.ID_ANY, u"用户名已存在！", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTRE )
		self.error_text5.Wrap( -1 )
		self.error_text5.SetFont( wx.Font( 25, 70, 90, 90, False, wx.EmptyString ) )
		self.error_text5.SetMinSize( wx.Size( 500,50 ) )
		
		bSizer7.Add( self.error_text5, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.error_button5 = wx.Button( self, wx.ID_ANY, u"确定", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer7.Add( self.error_button5, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		self.SetSizer( bSizer7 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.error_button5.Bind( wx.EVT_BUTTON, self.dialog_close )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def dialog_close( self, event ):
		event.Skip()
	

###########################################################################
## Class tanchuang6
###########################################################################

class tanchuang6 ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"ok", pos = wx.DefaultPosition, size = wx.Size( 346,159 ), style = wx.DEFAULT_DIALOG_STYLE|wx.STAY_ON_TOP )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer7 = wx.BoxSizer( wx.VERTICAL )
		
		self.error_text6 = wx.StaticText( self, wx.ID_ANY, u"用户名可使用！", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTRE )
		self.error_text6.Wrap( -1 )
		self.error_text6.SetFont( wx.Font( 25, 70, 90, 90, False, wx.EmptyString ) )
		self.error_text6.SetMinSize( wx.Size( 500,50 ) )
		
		bSizer7.Add( self.error_text6, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.error_button6 = wx.Button( self, wx.ID_ANY, u"确定", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer7.Add( self.error_button6, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		self.SetSizer( bSizer7 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.error_button6.Bind( wx.EVT_BUTTON, self.dialog_close )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def dialog_close( self, event ):
		event.Skip()
	

###########################################################################
## Class tanchuang7
###########################################################################

class tanchuang7 ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"ok", pos = wx.DefaultPosition, size = wx.Size( 346,159 ), style = wx.DEFAULT_DIALOG_STYLE|wx.STAY_ON_TOP )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer7 = wx.BoxSizer( wx.VERTICAL )
		
		self.error_text7 = wx.StaticText( self, wx.ID_ANY, u"注册成功！", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTRE )
		self.error_text7.Wrap( -1 )
		self.error_text7.SetFont( wx.Font( 25, 70, 90, 90, False, wx.EmptyString ) )
		self.error_text7.SetMinSize( wx.Size( 500,50 ) )
		
		bSizer7.Add( self.error_text7, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.error_button7 = wx.Button( self, wx.ID_ANY, u"确定", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer7.Add( self.error_button7, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		self.SetSizer( bSizer7 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.error_button7.Bind( wx.EVT_BUTTON, self.dialog_close )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def dialog_close( self, event ):
		event.Skip()
	

###########################################################################
## Class tanchuang8
###########################################################################

class tanchuang8 ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"错误", pos = wx.DefaultPosition, size = wx.Size( 346,159 ), style = wx.DEFAULT_DIALOG_STYLE|wx.STAY_ON_TOP )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer7 = wx.BoxSizer( wx.VERTICAL )
		
		self.error_text8 = wx.StaticText( self, wx.ID_ANY, u"用户尚未注册！", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTRE )
		self.error_text8.Wrap( -1 )
		self.error_text8.SetFont( wx.Font( 25, 70, 90, 90, False, wx.EmptyString ) )
		self.error_text8.SetMinSize( wx.Size( 500,50 ) )
		
		bSizer7.Add( self.error_text8, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.error_button8 = wx.Button( self, wx.ID_ANY, u"确定", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer7.Add( self.error_button8, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		self.SetSizer( bSizer7 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.error_button8.Bind( wx.EVT_BUTTON, self.dialog_close )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def dialog_close( self, event ):
		event.Skip()
	

###########################################################################
## Class tanchuang9
###########################################################################

class tanchuang9 ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"错误", pos = wx.DefaultPosition, size = wx.Size( 346,159 ), style = wx.DEFAULT_DIALOG_STYLE|wx.STAY_ON_TOP )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer7 = wx.BoxSizer( wx.VERTICAL )
		
		self.error_text9 = wx.StaticText( self, wx.ID_ANY, u"密码错误！", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTRE )
		self.error_text9.Wrap( -1 )
		self.error_text9.SetFont( wx.Font( 25, 70, 90, 90, False, wx.EmptyString ) )
		self.error_text9.SetMinSize( wx.Size( 500,50 ) )
		
		bSizer7.Add( self.error_text9, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.error_button9 = wx.Button( self, wx.ID_ANY, u"确定", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer7.Add( self.error_button9, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		self.SetSizer( bSizer7 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.error_button9.Bind( wx.EVT_BUTTON, self.dialog_close )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def dialog_close( self, event ):
		event.Skip()
	

###########################################################################
## Class tanchuang10
###########################################################################

class tanchuang10 ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"错误", pos = wx.DefaultPosition, size = wx.Size( 346,159 ), style = wx.DEFAULT_DIALOG_STYLE|wx.STAY_ON_TOP )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer7 = wx.BoxSizer( wx.VERTICAL )
		
		self.error_text10 = wx.StaticText( self, wx.ID_ANY, u"登陆成功！", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTRE )
		self.error_text10.Wrap( -1 )
		self.error_text10.SetFont( wx.Font( 25, 70, 90, 90, False, wx.EmptyString ) )
		self.error_text10.SetMinSize( wx.Size( 500,50 ) )
		
		bSizer7.Add( self.error_text10, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.error_button10 = wx.Button( self, wx.ID_ANY, u"确定", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer7.Add( self.error_button10, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		self.SetSizer( bSizer7 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.error_button10.Bind( wx.EVT_BUTTON, self.dialog_close )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def dialog_close( self, event ):
		event.Skip()
	

###########################################################################
## Class tanchuang11
###########################################################################

class tanchuang11 ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"错误", pos = wx.DefaultPosition, size = wx.Size( 346,159 ), style = wx.DEFAULT_DIALOG_STYLE|wx.STAY_ON_TOP )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer7 = wx.BoxSizer( wx.VERTICAL )
		
		self.error_text11 = wx.StaticText( self, wx.ID_ANY, u"输入错误！", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTRE )
		self.error_text11.Wrap( -1 )
		self.error_text11.SetFont( wx.Font( 25, 70, 90, 90, False, wx.EmptyString ) )
		self.error_text11.SetMinSize( wx.Size( 500,50 ) )
		
		bSizer7.Add( self.error_text11, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.error_button11 = wx.Button( self, wx.ID_ANY, u"确定", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer7.Add( self.error_button11, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		self.SetSizer( bSizer7 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.error_button11.Bind( wx.EVT_BUTTON, self.dialog_close )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def dialog_close( self, event ):
		event.Skip()
	

###########################################################################
## Class tanchuang12
###########################################################################

class tanchuang12 ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"错误", pos = wx.DefaultPosition, size = wx.Size( 346,159 ), style = wx.DEFAULT_DIALOG_STYLE|wx.STAY_ON_TOP )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer7 = wx.BoxSizer( wx.VERTICAL )
		
		self.error_text12 = wx.StaticText( self, wx.ID_ANY, u"商品已存在！", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTRE )
		self.error_text12.Wrap( -1 )
		self.error_text12.SetFont( wx.Font( 25, 70, 90, 90, False, wx.EmptyString ) )
		self.error_text12.SetMinSize( wx.Size( 500,50 ) )
		
		bSizer7.Add( self.error_text12, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.error_button12 = wx.Button( self, wx.ID_ANY, u"确定", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer7.Add( self.error_button12, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		self.SetSizer( bSizer7 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.error_button12.Bind( wx.EVT_BUTTON, self.dialog_close )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def dialog_close( self, event ):
		event.Skip()
	

###########################################################################
## Class tanchuang13
###########################################################################

class tanchuang13 ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"OK", pos = wx.DefaultPosition, size = wx.Size( 346,159 ), style = wx.DEFAULT_DIALOG_STYLE|wx.STAY_ON_TOP )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer7 = wx.BoxSizer( wx.VERTICAL )
		
		self.error_text13 = wx.StaticText( self, wx.ID_ANY, u"修改成功！", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTRE )
		self.error_text13.Wrap( -1 )
		self.error_text13.SetFont( wx.Font( 25, 70, 90, 90, False, wx.EmptyString ) )
		self.error_text13.SetMinSize( wx.Size( 500,50 ) )
		
		bSizer7.Add( self.error_text13, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.error_button13 = wx.Button( self, wx.ID_ANY, u"确定", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer7.Add( self.error_button13, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		self.SetSizer( bSizer7 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.error_button13.Bind( wx.EVT_BUTTON, self.dialog_close )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def dialog_close( self, event ):
		event.Skip()
	

###########################################################################
## Class tanchuang14
###########################################################################

class tanchuang14 ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"错误", pos = wx.DefaultPosition, size = wx.Size( 346,159 ), style = wx.DEFAULT_DIALOG_STYLE|wx.STAY_ON_TOP )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer7 = wx.BoxSizer( wx.VERTICAL )
		
		self.error_text14 = wx.StaticText( self, wx.ID_ANY, u"商品不存在！", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTRE )
		self.error_text14.Wrap( -1 )
		self.error_text14.SetFont( wx.Font( 25, 70, 90, 90, False, wx.EmptyString ) )
		self.error_text14.SetMinSize( wx.Size( 500,50 ) )
		
		bSizer7.Add( self.error_text14, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.error_button14 = wx.Button( self, wx.ID_ANY, u"确定", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer7.Add( self.error_button14, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		self.SetSizer( bSizer7 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.error_button14.Bind( wx.EVT_BUTTON, self.dialog_close )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def dialog_close( self, event ):
		event.Skip()
	

###########################################################################
## Class tanchuang15
###########################################################################

class tanchuang15 ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"OK", pos = wx.DefaultPosition, size = wx.Size( 346,159 ), style = wx.DEFAULT_DIALOG_STYLE|wx.STAY_ON_TOP )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer7 = wx.BoxSizer( wx.VERTICAL )
		
		self.error_text13 = wx.StaticText( self, wx.ID_ANY, u"删除成功！", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTRE )
		self.error_text13.Wrap( -1 )
		self.error_text13.SetFont( wx.Font( 25, 70, 90, 90, False, wx.EmptyString ) )
		self.error_text13.SetMinSize( wx.Size( 500,50 ) )
		
		bSizer7.Add( self.error_text13, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.error_button13 = wx.Button( self, wx.ID_ANY, u"确定", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer7.Add( self.error_button13, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		self.SetSizer( bSizer7 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.error_button13.Bind( wx.EVT_BUTTON, self.dialog_close )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def dialog_close( self, event ):
		event.Skip()
	

