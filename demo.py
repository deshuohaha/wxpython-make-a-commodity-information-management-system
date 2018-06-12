import wx 
import pymysql
import mainview

###################################################################
#主界面功能
###################################################################
class main_frame(mainview.main_frame): 
   #重写构造函数
   def __init__(self,parent):
   #引入模板的构造函数 
      mainview.main_frame.__init__(self,parent)  
		
   def goto_dengluframe(self,event):
      self.Destroy() 
      dengluframe = denglu_frame(None) 
      dengluframe.Show(True) 
     
   def goto_zhuceframe(self,event):
      self.Destroy()
      zhuceframe = zhuce_frame(None) 
      zhuceframe.Show(True) 

   def exitapp(self,event):
      self.Destroy()

###################################################################
#注册界面功能
###################################################################
class zhuce_frame(mainview.zhuce_frame):
    def __init__(self, parent):
        mainview.zhuce_frame.__init__(self,parent)
        self.check=False
        self.user=None
        self.password1=None
        self.password2=None


    def zhuce_ok(self,event):
        #获取用户输入
        self.user=self.zhuce_text_id.GetLineText(1)
        self.password1=self.zhuce_text_password1.GetLineText(1)
        self.password2=self.zhuce_text_password2.GetLineText(1)

        #检查用户名是否为空
        if not self.user:
            dialog = tanchuang1(None)
            dialog.ShowModal()
        #检查是否重名
        elif not self.check:
            dialog = tanchuang2(None)
            dialog.ShowModal()
        #检查密码是否为空
        elif not self.password1:
            dialog = tanchuang3(None)
            dialog.ShowModal()
        #确认密码输入一致
        elif self.password1 != self.password2:
            dialog = tanchuang4(None)
            dialog.ShowModal()
        #无错误信息，将用户信息录入数据库
        else:
        	self.zhuce_sqlInsert()
        	self.zhuce_sqlCreateTable()



    def zhuce_clear_text(self,event):
        self.zhuce_text_id.Clear()
        self.zhuce_text_password1.Clear()
        self.zhuce_text_password2.Clear()

    def zhuce_goback(self,event):
        self.Destroy()
        frame = main_frame(None) 
        frame.Show(True)

    def zhuce_sqlCheck(self,event):
        #数据库连接
        db = pymysql.connect("localhost", "root", "", "zhinengwuliu", charset='gb2312' )
        cursor = db.cursor()
        sql = "SELECT * FROM users WHERE user_id = '%s' "%self.user
        try:
            cursor.execute(sql)
            results = cursor.fetchall()
            for row in results:
                sql_user= row[0]
            if sql_user == user:
                dialog = tanchuang5(None)
                dialog.ShowModal()
            else:
                self.check = True
                dialog = tanchuang6(None)
                dialog.ShowModal()
        except:
            self.check = True
            dialog = tanchuang6(None)
            dialog.ShowModal()
        db.close()

    def zhuce_sqlInsert(self):
        #数据库连接
        db = pymysql.connect("localhost", "root", "", "zhinengwuliu", charset='gb2312' )
        cursor = db.cursor()
        sql = "INSERT INTO users(user_id,user_password)\
           VALUES ('%s','%s')"%(self.user,self.password1)
        try:
            # 执行sql语句
            cursor.execute(sql)
            # 提交到数据库执行
            db.commit()
            self.check=False
        except:
            # 如果发生错误则回滚
            db.rollback()
            # 关闭数据库连接
        db.close()

    def zhuce_sqlCreateTable(self):
        # 打开数据库连接
        db = pymysql.connect("localhost", "root", "", "zhinengwuliu", charset='gb2312' )
 
        # 使用 cursor() 方法创建一个游标对象 cursor
        cursor = db.cursor()
        # 使用预处理语句创建表
        sql = "CREATE TABLE `%s` (\
               `EAN13`  varchar(13) NOT NULL ,\
               `name`  varchar(255) NULL ,\
               `type`  varchar(255) NULL ,\
                PRIMARY KEY (`EAN13`))"%(self.user)
 
        cursor.execute(sql)
        dialog = tanchuang7(None)
        dialog.ShowModal()
        # 关闭数据库连接
        db.close()

###################################################################
#登陆功能
###################################################################
class denglu_frame(mainview.denglu_frame):
    def __init__(self, parent):
        mainview.denglu_frame.__init__(self,parent)
        self.usercheck=False
        self.passwordcheck=False
        self.user=None
        self.password=None

    def denglu_ok(self,event):
    	#获取用户输入
        self.user=self.denglu_text_id.GetLineText(1)
        self.password=self.denglu_text_password.GetLineText(1)

        #判断用户是否注册与密码是否正确
        self.denglu_sqlCheck()
        #检查用户名是否为空
        if not self.user:
            dialog = tanchuang1(None)
            dialog.ShowModal()
        #用户是否注册
        elif not self.usercheck:
            dialog = tanchuang8(None)
            dialog.ShowModal()
        #检查密码是否为空
        elif not self.password:
            dialog = tanchuang3(None)
            dialog.ShowModal()
        #检查密码是否正确
        elif not self.passwordcheck:
            dialog = tanchuang9(None)
            dialog.ShowModal()
        else:
            self.Destroy()
            dialog = tanchuang10(None,user=self.user)
            dialog.ShowModal()
        
        self.usercheck=False
        self.passwordcheck=False

    def denglu_clear_text(self,event):
        self.denglu_text_id.Clear()
        self.denglu_text_password.Clear()

    def denglu_goback(self,event):
        self.Destroy()
        frame = main_frame(None) 
        frame.Show(True)

    def denglu_sqlCheck(self):
    	#数据库连接
        db = pymysql.connect("localhost", "root", "", "zhinengwuliu", charset='gb2312' )
        cursor = db.cursor()
        sql = "SELECT * FROM users WHERE user_id = '%s' "%self.user
        try:
            cursor.execute(sql)
            results = cursor.fetchall()
            for row in results:
                sql_user= row[0]
                sql_password = row[1]
            if sql_user == self.user:
                self.usercheck=True
            if sql_password == self.password:
                self.passwordcheck=True
        except:
        	pass
        db.close()


###################################################################
#操作选择界面
###################################################################
class caozuo_frame(mainview.caozuo_frame):
    def __init__(self, parent,user):
        mainview.caozuo_frame.__init__(self,parent)
        self.user=user
        self.caozuo_text_user.SetLabel("欢迎你："+self.user)

    def goto_tianjiaframe(self,event):
    	self.Destroy()
    	frame=tianjia_frame(None,user=self.user)
    	frame.Show(True)

    def goto_chaxunframe(self,event):
        self.Destroy()
        frame=chaxun_frame(None,user=self.user)
        frame.Show(True)

    def goto_xiugaiframe(self,event):
        self.Destroy()
        frame=xiugai_frame(None,user=self.user)
        frame.Show(True)

    def goto_shanchuframe(self,event):
        self.Destroy()
        frame=shanchu_frame(None,user=self.user)
        frame.Show(True)
    	


    def caozuo_back(self,event):
      self.Destroy()
      frame=main_frame(None)
      frame.Show(True)

###################################################################
#添加商品界面
###################################################################
class tianjia_frame(mainview.tianjia_frame):
    def __init__(self, parent,user):
        mainview.tianjia_frame.__init__(self,parent)
        self.user=user
        self.tianjia_text_user.SetLabel("欢迎你："+self.user)
        self.name=None
        self.guojia=None
        self.changshang=None
        self.shangpin=None
        self.shangpintype=None
        self.EAN13=None
        self.check = False

    def tianjia_ok(self,event):
        self.name=self.tianjia_text_name.GetLineText(1)
        self.guojia=self.tianjia_text_guojia.GetLineText(1)
        self.changshang=self.tianjia_text_changshang.GetLineText(1)
        self.shangpin=self.tianjia_text_shangpin.GetLineText(1)
        self.shangpintype=self.tianjia_choicetype.GetStringSelection()

        self.checkcode()
        self.EAN13=self.get_EAN13()
        self.tianjia_sqlCheck()
        if self.check:
            self.tianjia_sqlInsert()

    def tianjia_clear(self,event):
        self.tianjia_text_name.Clear()
        self.tianjia_text_guojia.Clear()
        self.tianjia_text_changshang.Clear()
        self.tianjia_text_shangpin.Clear()

    def tianjia_back(self,event):
        self.Destroy()
        frame=caozuo_frame(None,user=self.user)
        frame.Show(True)

    def checkcode(self):
        if not self.name and len(self.guojia)<3 and len(self.changshang)<4 and len(self.shangpin)<5:
            self.tianjia_text_guojia.Clear()
            self.tianjia_text_changshang.Clear()
            self.tianjia_text_shangpin.Clear()
            dialog=tanchuang11(None)
            dialog.Show(True)

    def get_EAN13(self):
        code=self.guojia+self.changshang+self.shangpin
        c1=0
        c2=0
        for index in code[::2]:
            c1+=int(index)
        for index in code[1::2]:
            c2+=int(index)
        c3=c2*3
        cc=(c1+c3)%10
        c=10-cc
        if c==10:
           c=0

        code=self.guojia+self.changshang+self.shangpin+str(c)
        return code


    def tianjia_sqlCheck(self):
        #数据库连接
        db = pymysql.connect("localhost", "root", "", "zhinengwuliu", charset='gb2312' )
        cursor = db.cursor()
        sql = "SELECT * FROM `%s` WHERE EAN13 = '%s' "%(self.user,self.EAN13)
        try:
            cursor.execute(sql)
            results = cursor.fetchall()
            for row in results:
                sql_EAN13= row[0]
            if sql_EAN13 ==self.EAN13:
                dialog = tanchuang12(None)
                dialog.ShowModal()
            else:
                self.check = True
        except:
            self.check = True
        db.close()

    def tianjia_sqlInsert(self):
    	#数据库连接
        db = pymysql.connect("localhost", "root", "", "zhinengwuliu", charset='gb2312' )
        cursor = db.cursor()
        sql = "INSERT INTO `%s`(EAN13,name,type)\
           VALUES ('%s','%s','%s')"%(self.user,self.EAN13,self.name,self.shangpintype)
        try:
            # 执行sql语句
            cursor.execute(sql)
            # 提交到数据库执行
            db.commit()
            self.check=False
            dialog=tanchuang13(None)
            dialog.Show(True)
        except:
            # 如果发生错误则回滚
            db.rollback()
            # 关闭数据库连接
        db.close()
###################################################################
#查询商品界面
###################################################################
class chaxun_frame(mainview.chaxun_frame):
    def __init__(self, parent,user):
        mainview.chaxun_frame.__init__(self,parent)
        self.user=user
        self.tianjia_text_user.SetLabel("欢迎你："+self.user)
        self.code=None
        self.name=None
        self.shangpintype=None
        
        self.chaxun_sqlGetvalue()

    def chaxun_sqlGetvalue(self):
    	#数据库连接
        db = pymysql.connect("localhost", "root", "", "zhinengwuliu", charset='gb2312' )
        cursor = db.cursor()
        sql = "SELECT * FROM `%s`"%(self.user)
        try:
            cursor.execute(sql)
            results = cursor.fetchall()
            code=[]
            name=[]
            stype=[]
            for row in results:
                code.append(row[0])
                name.append(row[1])
                stype.append(row[2])

            self.info_text11.SetLabel(code[0])
            self.info_text12.SetLabel(name[0])
            self.info_text13.SetLabel(stype[0])
            self.info_text21.SetLabel(code[1])
            self.info_text22.SetLabel(name[1])
            self.info_text23.SetLabel(stype[1])
            self.info_text31.SetLabel(code[2])
            self.info_text32.SetLabel(name[2])
            self.info_text33.SetLabel(stype[2])
            self.info_text41.SetLabel(code[3])
            self.info_text42.SetLabel(name[3])
            self.info_text43.SetLabel(stype[3])
            self.info_text51.SetLabel(code[4])
            self.info_text52.SetLabel(name[4])
            self.info_text53.SetLabel(stype[4])
        except:
            # 如果发生错误则回滚
            db.rollback()
            # 关闭数据库连接
        db.close()


    def chaxun_back(self,event):
        self.Destroy()
        frame=caozuo_frame(None,user=self.user)
        frame.Show(True)
###################################################################
#修改商品界面
###################################################################
class xiugai_frame(mainview.xiugai_frame):
    def __init__(self, parent,user):
        mainview.xiugai_frame.__init__(self,parent)
        self.user=user
        self.tianjia_text_user.SetLabel("欢迎你："+self.user)
        self.name=None
        self.shangpintype=None
        self.code=None
        self.check = False
    
    def xiugai_chaxun(self,event):
        self.code=self.xiugai_text_code.GetLineText(1)

        if len(self.code)<13:
            self.xiugai_text_code.Clear()
            dialog=tanchuang11(None)
            dialog.Show(True)
        else:
        	self.xiugai_sqlCheck()

        if self.check:
            self.xiugai_sqlGetvalue()
            self.result_name.SetLabel(self.name)

    def xiugai_ok(self,event):
        self.name = self.result_name.GetLineText(1)

        if not self.name or not self.code:
            dialog=tanchuang11(None)
            dialog.Show(True)
        elif self.check:
            self.xiugai_sqlUpdate()
        else:
            dialog=tanchuang11(None)
            dialog.Show(True)
        

    def xiugai_clear(self,event):
        self.xiugai_text_code.Clear()
        self.code=None

    def xiugai_back(self,event):
        self.Destroy()
        frame=caozuo_frame(None,user=self.user)
        frame.Show(True)

    def xiugai_sqlCheck(self):
        #数据库连接
        db = pymysql.connect("localhost", "root", "", "zhinengwuliu", charset='gb2312' )
        cursor = db.cursor()
        sql = "SELECT * FROM `%s` WHERE EAN13 = '%s' "%(self.user,self.code)
        cursor.execute(sql)
        results = cursor.fetchall()
        try:
            for row in results:
                sql_code = row[0]
            if sql_code == self.code:
                self.check=True
            else:
                dialog = tanchuang14(None)
                dialog.ShowModal()
        except:
            dialog = tanchuang14(None)
            dialog.ShowModal()
        
        db.close()

    def xiugai_sqlGetvalue(self):
    	#数据库连接
        db = pymysql.connect("localhost", "root", "", "zhinengwuliu", charset='gb2312' )
        cursor = db.cursor()
        sql = "SELECT * FROM `%s` WHERE EAN13 = '%s' "%(self.user,self.code)
        try:
            cursor.execute(sql)
            results = cursor.fetchall()
            for row in results:
                self.name = row[1]
        except:
            # 如果发生错误则回滚
            db.rollback()
            # 关闭数据库连接
        db.close()


    def xiugai_sqlUpdate(self):
    	#数据库连接
        db = pymysql.connect("localhost", "root", "", "zhinengwuliu", charset='gb2312' )
        cursor = db.cursor()
        sql = ("UPDATE `%s` SET name = '%s' WHERE EAN13 = '%s'")%(self.user,self.name,self.code)
        try:
            # 执行sql语句
            cursor.execute(sql)
            # 提交到数据库执行
            db.commit()
            self.check=False
            dialog=tanchuang13(None)
            dialog.Show(True)
        except:
            # 如果发生错误则回滚
            db.rollback()
            # 关闭数据库连接
        db.close()
###################################################################
#删除商品界面
###################################################################
class shanchu_frame(mainview.shanchu_frame):
    def __init__(self, parent,user):
        mainview.shanchu_frame.__init__(self,parent)
        self.user=user
        self.tianjia_text_user.SetLabel("欢迎你："+self.user)
        self.name=None
        self.shangpintype=None
        self.code=None
        self.check = False
    
    def shanchu_chaxun(self,event):
        self.code=self.shanchu_text_code.GetLineText(1)

        if len(self.code)<13:
            self.shanchu_text_code.Clear()
            dialog=tanchuang11(None)
            dialog.Show(True)
        else:
        	self.shanchu_sqlCheck()

        if self.check:
            self.shanchu_sqlGetvalue()
            self.result_name.SetLabel(self.name)
            self.result_shangpintype.SetLabel(self.shangpintype)

    def shanchu_ok(self,event):
        if self.check:
            self.shanchu_sqlDelete()
        else:
            dialog=tanchuang11(None)
            dialog.Show(True)
        

    def shanchu_clear(self,event):
        self.shanchu_text_code.Clear()
        self.code=None

    def shanchu_back(self,event):
        self.Destroy()
        frame=caozuo_frame(None,user=self.user)
        frame.Show(True)

    def shanchu_sqlCheck(self):
        #数据库连接
        db = pymysql.connect("localhost", "root", "", "zhinengwuliu", charset='gb2312' )
        cursor = db.cursor()
        sql = "SELECT * FROM `%s` WHERE EAN13 = '%s' "%(self.user,self.code)
        cursor.execute(sql)
        results = cursor.fetchall()
        try:
            for row in results:
                sql_code = row[0]
            if sql_code == self.code:
                self.check=True
            else:
                dialog = tanchuang14(None)
                dialog.ShowModal()
        except:
            dialog = tanchuang14(None)
            dialog.ShowModal()
        
        db.close()

    def shanchu_sqlGetvalue(self):
    	#数据库连接
        db = pymysql.connect("localhost", "root", "", "zhinengwuliu", charset='gb2312' )
        cursor = db.cursor()
        sql = "SELECT * FROM `%s` WHERE EAN13 = '%s' "%(self.user,self.code)
        try:
            cursor.execute(sql)
            results = cursor.fetchall()
            for row in results:
                self.name = row[1]
                self.shangpintype=row[2]
        except:
            # 如果发生错误则回滚
            db.rollback()
            # 关闭数据库连接
        db.close()


    def shanchu_sqlDelete(self):
    	#数据库连接
        db = pymysql.connect("localhost", "root", "", "zhinengwuliu", charset='gb2312' )
        cursor = db.cursor()
        sql = ("DELETE FROM `%s` WHERE EAN13='%s'")%(self.user,self.code)
        try:
            # 执行sql语句
            cursor.execute(sql)
            # 提交到数据库执行
            db.commit()
            self.check=False
            dialog=tanchuang15(None)
            dialog.Show(True)
        except:
            # 如果发生错误则回滚
            db.rollback()
            # 关闭数据库连接
        db.close()
###################################################################
#Dialog弹窗
###################################################################   		
class tanchuang1(mainview.tanchuang1):
    def __init__(self, parent):
        mainview.tanchuang1.__init__(self,parent)

    def dialog_close(self,event):
    	self.Destroy()

class tanchuang2(mainview.tanchuang2):
    def __init__(self, parent):
        mainview.tanchuang2.__init__(self,parent)

    def dialog_close(self,event):
    	self.Destroy()

class tanchuang3(mainview.tanchuang3):
    def __init__(self, parent):
        mainview.tanchuang3.__init__(self,parent)

    def dialog_close(self,event):
    	self.Destroy()

class tanchuang4(mainview.tanchuang4):
    def __init__(self, parent):
        mainview.tanchuang4.__init__(self,parent)

    def dialog_close(self,event):
    	self.Destroy()

class tanchuang5(mainview.tanchuang5):
    def __init__(self, parent):
        mainview.tanchuang5.__init__(self,parent)

    def dialog_close(self,event):
    	self.Destroy()

class tanchuang6(mainview.tanchuang6):
    def __init__(self, parent):
        mainview.tanchuang6.__init__(self,parent)

    def dialog_close(self,event):
    	self.Destroy()

class tanchuang7(mainview.tanchuang7):
    def __init__(self, parent):
        mainview.tanchuang7.__init__(self,parent)

    def dialog_close(self,event):
    	self.Destroy()

class tanchuang8(mainview.tanchuang8):
    def __init__(self, parent):
        mainview.tanchuang8.__init__(self,parent)

    def dialog_close(self,event):
    	self.Destroy()

class tanchuang9(mainview.tanchuang9):
    def __init__(self, parent):
        mainview.tanchuang9.__init__(self,parent)

    def dialog_close(self,event):
    	self.Destroy()

class tanchuang10(mainview.tanchuang10):
    def __init__(self, parent, user):
        mainview.tanchuang10.__init__(self,parent)
        self.user=user

    def dialog_close(self,event):
    	self.Destroy()
    	frame=caozuo_frame(None,user=self.user)
    	frame.Show(True)

class tanchuang11(mainview.tanchuang11):
    def __init__(self, parent):
        mainview.tanchuang11.__init__(self,parent)

    def dialog_close(self,event):
    	self.Destroy()

class tanchuang12(mainview.tanchuang12):
    def __init__(self, parent):
        mainview.tanchuang12.__init__(self,parent)

    def dialog_close(self,event):
    	self.Destroy()

class tanchuang13(mainview.tanchuang13):
    def __init__(self, parent):
        mainview.tanchuang13.__init__(self,parent)

    def dialog_close(self,event):
    	self.Destroy()

class tanchuang14(mainview.tanchuang14):
    def __init__(self, parent):
        mainview.tanchuang14.__init__(self,parent)

    def dialog_close(self,event):
    	self.Destroy()

class tanchuang15(mainview.tanchuang15):
    def __init__(self, parent):
        mainview.tanchuang15.__init__(self,parent)

    def dialog_close(self,event):
    	self.Destroy()

###################################################################
#主函数运行
###################################################################
def main():
    app = wx.App(False) 
    frame = main_frame(None) 
    frame.Show(True) 
    #start the applications 
    app.MainLoop()

if __name__ == '__main__':
    main()

