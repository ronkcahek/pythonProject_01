import os, sys
from kivy.resources import resource_add_path, resource_find
from kivymd.app import MDApp
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager,Screen
from kivy.properties import ObjectProperty


try:
    import android
except ImportError:
    android = None

if not android:
    W = 335
    Window.size = 400,530#(W, W * 15.471074 / 9)

class Manager(ScreenManager):
    pass

Delimeter=":"

erorr_1="Вы не ввели время, повторите еще раз!"
erorr_2="Вы не правильно ввели время, повторите еще раз!"
erorr_3="Вы ввели неправильно топливо, повторите!"
erorr_4="Вы не ввели топливо, повторите еще раз!"

class Calc(Screen):
    textbox1 = ObjectProperty(None)
    textbox2 = ObjectProperty(None)
#############################   Очистка
    def super_clear(self):
        self.textbox2.text = ""
        self.toolbar.title = 'Начало работы:'
        self.bt.unbind(on_release=(self.work_finish))
        self.bt.unbind(on_release=(self.fuel_start))
        self.bt.unbind(on_release=(self.fuel_finish))
        self.bt.unbind(on_release=(self.fuel_finish_equip))
        self.bt.unbind(on_release=(self.hot_start_lq))
        self.bt.unbind(on_release=(self.hot_finish_lq))
        self.bt.unbind(on_release=(self.hot_start_loqo))
        self.bt.unbind(on_release=(self.hot_finish_loqo))
        self.bt.unbind(on_release=(self.hot_start_dinner))
        self.bt.unbind(on_release=(self.hot_finish_dinner))
        self.bt.unbind(on_release=(self.start_equip_time))
        self.bt.unbind(on_release=(self.finish_equip_time))
        self.bt.unbind(on_release=(self.start_to))
        self.bt.unbind(on_release=(self.finish_to))
        self.bt.unbind(on_release=(self.train_start))
        self.bt.unbind(on_release=(self.train_finish))
        self.bt.unbind(on_release=(self.trains_start))
        self.bt.unbind(on_release=(self.trains_finish))
        self.bt1.unbind(on_release=(self.skip_equip))
        self.bt1.unbind(on_release=(self.skip_hot_lq))
        self.bt1.unbind(on_release=(self.skip_hot_loqo))
        self.bt1.unbind(on_release=(self.hot_skip_dinner))
        self.bt1.unbind(on_release=(self.skip_equip_time))
        self.bt1.unbind(on_release=(self.skip_to))
        self.bt1.unbind(on_release=(self.skip_train))
        self.bt.bind(on_release=self.work_start)
        self.clear()

    def clear(self):
        self.textbox1.text = ""
        self.raw_data=""
#############################   Начало работы
    def work_start(self,infix):
        print("1",self.textbox1.text)
        work1 = self.textbox1.text
        self.textbox1.text = ""
        if work1=="":
            self.textbox2.text= erorr_1
            return self.clear()
        try:
            work_a, work_q = work1.split(Delimeter)
        except:
            self.textbox2.text=erorr_2
            self.clear()
        else:
            hour_work_start = int(work_a) * 60
            if hour_work_start > 1440:
                self.textbox2.text = erorr_2
                return self.clear()
            if int(work_q) > 60:
                self.textbox2.text = erorr_2
                return self.clear()
            self.tim_work_start = int(hour_work_start) + int(work_q)
            text="Начало работы"
            self.textbox2.text = "%s- %s"%(text,work1)
            self.bt.unbind(on_release=self.work_start)
            self.bt.bind(on_release=self.work_finish)
            self.toolbar.title = 'Окончание работы:'
            self.clear()
            
    def work_finish(self,infix):
        work2 = self.textbox1.text
        print("2",self.textbox1.text)
        self.textbox1.text = ""
        if work2=="":
            self.textbox2.text = erorr_1
            return self.clear()
        try:
            work_b, work_j = work2.split(Delimeter)
        except:
            self.textbox2.text=erorr_2
            self.clear()
        else:
            hour_work_finish = int(work_b) * 60
            if hour_work_finish > 1440:
                self.textbox2.text = erorr_2
                return self.clear()
            if int(work_j) > 60:
                self.textbox2.text = erorr_2
                return self.clear()
            tim_work_finish = int(hour_work_finish) + int(work_j)
            self.minutesw = 0
            self.minutesw = int()
            text = 'Окончание работы'
            self.textbox2.text = "%s- %s" % (text, work2)
            if self.tim_work_start>tim_work_finish:
                self.minutesw=1440-self.tim_work_start+tim_work_finish
                print(self.minutesw)
                self.bt.unbind(on_release=self.work_finish)
                self.bt.bind(on_release=self.fuel_start)
                self.toolbar.title = 'Топливо при приемке:'
                self.clear()
            else:
                self.minutesw=tim_work_finish-self.tim_work_start
                print(self.minutesw)
                self.bt.unbind(on_release=self.work_finish)
                self.bt.bind(on_release=self.fuel_start)
                self.toolbar.title = 'Топливо при приемке:'
                self.clear()
#############################   Топливо
    def fuel_start(self,infix):
        self.a = self.textbox1.text
        print(self.a)
        self.textbox1.text = ""
        if self.a=="":
            self.textbox2.text = erorr_4
            return self.clear()
        if len (self.a) > 4:
            self.textbox2.text = erorr_3
            return self.clear()
        else:
            text='Топливо при приемке'
            self.textbox2.text = "%s- %s"%(text,self.a)
            self.bt.unbind(on_release=self.fuel_start)
            self.bt.bind(on_release=self.fuel_finish)
            self.toolbar.title = 'Топливо при сдаче:'
            self.clear()
        
    def fuel_finish(self,infix):
        self.b = self.textbox1.text
        print(self.b)
        self.textbox1.text = ""
        if self.b=="":
            self.textbox2.text = erorr_4
            return self.clear()
        if len (self.b) > 4:
                self.textbox2.text = erorr_3
                return self.clear()
        else:
            self.bt.unbind(on_release=self.fuel_finish)
            text='Топливо при сдаче'
            self.textbox2.text = "%s- %s"%(text,self.b)
            if self.tim_work_start < 1080:
                self.bt1.bind(on_release=self.skip_equip)
                self.bt.bind(on_release=self.fuel_finish_equip)
                self.toolbar.title = 'Топливо при экипировке:'
                self.clear()
            else:
                self.skip_equip(infix)

    def skip_equip(self,infix):
        self.textbox1.text = str(0)
        self.raw_data=""
        self.bt.unbind(on_release=self.fuel_finish_equip)
        self.bt.bind(on_release=self.hot_start_lq)        
        self.fuel_finish_equip(infix)
    
    def fuel_finish_equip(self,infix):
        self.c = self.textbox1.text
        print(self.c)
        self.textbox1.text = ""
        if self.c == "":
            self.textbox2.text = erorr_4
            return self.clear()
        if int(self.c)==0:
            if self.a<self.b:
                self.textbox2.text = erorr_3
                self.bt.unbind(on_release=self.hot_start_lq)
                self.bt.bind(on_release=self.fuel_start)
                self.toolbar.title = 'Топливо при приемке:'
                return self.clear
        if int (self.c)>0:
            if len (str(self.c)) > 4:
                self.textbox2.text = erorr_3
                return self.clear()
            else:
                self.bt.unbind(on_release=self.fuel_finish_equip)
                self.bt.bind(on_release=self.hot_start_lq)
        self.toolbar.title = 'Начало приемки локомотива:'
        self.bt1.unbind(on_release=self.skip_equip)
        self.bt1.bind(on_release=self.skip_hot_lq)
        x = int(self.a) + int(self.c) - int(self.b)
        self.result=x
        text ="Расход топлива"
        self.textbox2.text = "%s- %s"%(text,self.result)
        print(self.result)
        self.total_message=0
        self.clear()
#############################  Приемка локомотива
    def hot_start_lq(self,infix):
        hot_start_acc = self.textbox1.text
        print(hot_start_acc)
        self.textbox1.text = ""
        if hot_start_acc=="":
            self.textbox2.text= erorr_1
            return self.clear()
        try:
            hot_start_acc_a, hot_start_acc_b = hot_start_acc.split(Delimeter)
        except:
            self.textbox2.text=erorr_2
            self.clear()
        else:
            hour_hot_start_acc = int(hot_start_acc_a) * 60
            if hour_hot_start_acc > 1440:
                self.textbox2.text = erorr_2
                return self.clear()
            if int(hot_start_acc_a) > 60:
                self.textbox2.text = erorr_2
                return self.clear()
            self.tim_hot_start_acc = int(hour_hot_start_acc) + int(hot_start_acc_b)
            text = 'Начало приемки локомотива'
            self.textbox2.text = "%s- %s"%(text,hot_start_acc)
            print(self.tim_hot_start_acc)
            self.bt.unbind(on_release=self.hot_start_lq)
            self.bt1.unbind(on_release=self.skip_hot_lq)
            self.bt.bind(on_release=self.hot_finish_lq)
            self.toolbar.title = 'Окончание приемки локомотива:'
            self.clear()
    
    def skip_hot_lq(self,infix):
        self.bt.unbind(on_release=self.hot_start_lq)
        self.bt1.unbind(on_release=self.skip_hot_lq)
        self.bt.bind(on_release=self.hot_start_loqo)
        self.bt1.bind(on_release=self.skip_hot_loqo)
        self.toolbar.title = 'Начало сдачи локомотива:'
        self.clear()
    
    def hot_finish_lq(self,infix):
        hot_finish_acc = self.textbox1.text
        print(hot_finish_acc )
        self.textbox1.text = ""
        if hot_finish_acc=="":
            self.textbox2.text= erorr_1
            return self.clear()
        try:
            hot_finish_acc_a, hot_finish_acc_b = hot_finish_acc.split(Delimeter)
        except:
            self.textbox2.text=erorr_2
            self.clear()
        else:
            hour_hot_finish_acc = int(hot_finish_acc_a) * 60
            if hour_hot_finish_acc > 1440:
                self.textbox2.text = erorr_2
                return self.clear()
            if int(hot_finish_acc_a) > 60:
                self.textbox2.text = erorr_2
                return self.clear()
            self.tim_hot_finish_acc = int(hour_hot_finish_acc) + int(hot_finish_acc_b)
            text = 'Окончание приемки локомотива'
            self.textbox2.text = "%s- %s"%(text,hot_finish_acc)
            self.bt.unbind(on_release=self.hot_finish_lq)                
            self.bt.bind(on_release=self.hot_start_loqo)
            self.bt1.bind(on_release=self.skip_hot_loqo)
            self.toolbar.title = 'Начало сдачи локомотива:'
            if self.tim_hot_start_acc > self.tim_hot_finish_acc:
                hot_x = 1440 - self.tim_hot_start_acc + self.tim_hot_finish_acc
                self.total_message+=hot_x
                print(self.total_message)
                self.clear()
            else:
                hot_x = self.tim_hot_finish_acc - self.tim_hot_start_acc
                self.total_message+=hot_x
                print(self.total_message)
                self.clear()
############################    Сдача локомотива
    def hot_start_loqo(self,infix):
        hot_start_loqo = self.textbox1.text
        print(hot_start_loqo)
        self.textbox1.text = ""
        if hot_start_loqo=="":
            self.textbox2.text= erorr_1
            return self.clear()
        try:
            hot_start_loqo_a, hot_start_loqo_b = hot_start_loqo.split(Delimeter)
        except:
            self.textbox2.text=erorr_2
            self.clear()
        else:
            hour_hot_start_loqo = int(hot_start_loqo_a) * 60
            if hour_hot_start_loqo > 1440:
                self.textbox2.text = erorr_2
                return self.clear()
            if int(hot_start_loqo_a) > 60:
                self.textbox2.text = erorr_2
                return self.clear()
            self.tim_hot_start_loqo = int(hour_hot_start_loqo) + int(hot_start_loqo_b)
            text = 'Начало сдачи локомотива'
            self.textbox2.text = "%s- %s"%(text,hot_start_loqo)
            print(self.tim_hot_start_loqo)
            self.bt.unbind(on_release=self.hot_start_loqo)
            self.bt1.unbind(on_release=self.skip_hot_loqo)
            self.bt.bind(on_release=self.hot_finish_loqo)
            self.toolbar.title = 'Окончания сдачи локомотива:'
            self.clear()
            
    def skip_hot_loqo(self,infix):
        self.bt.unbind(on_release=self.hot_start_loqo)
        self.bt1.unbind(on_release=self.skip_hot_loqo)
        self.bt.bind(on_release=self.hot_start_dinner)
        self.bt1.bind(on_release=self.hot_skip_dinner)
        self.toolbar.title = 'Начало обеда:'
        self.clear()
        
    def hot_finish_loqo(self,infix):
        hot_finish_loqo = self.textbox1.text
        print(hot_finish_loqo)
        self.textbox1.text = ""
        if hot_finish_loqo=="":
            self.textbox2.text= erorr_1
            return self.clear()
        try:
            hot_finish_loqo_a, hot_finish_loqo_b = hot_finish_loqo.split(Delimeter)
        except:
            self.textbox2.text=erorr_2
            self.clear()
        else:
            hour_hot_finish_loqo = int(hot_finish_loqo_a) * 60
            if hour_hot_finish_loqo > 1440:
                self.textbox2.text = erorr_2
                return self.clear()
            if int(hot_finish_loqo_a) > 60:
                self.textbox2.text = erorr_2
                return self.clear()
            self.tim_hot_finish_loqo = int(hour_hot_finish_loqo) + int(hot_finish_loqo_b)
            text = 'Окончания сдачи локомотива'
            self.textbox2.text = "%s- %s"%(text,hot_finish_loqo)
            self.bt.unbind(on_release=self.hot_finish_loqo)
            self.bt.bind(on_release=self.hot_start_dinner)
            self.bt1.bind(on_release=self.hot_skip_dinner)
            self.toolbar.title = 'Начало обеда:'
            if self.tim_hot_start_loqo > self.tim_hot_finish_loqo:
                hot_x = 1440 - self.tim_hot_start_loqo + self.tim_hot_finish_loqo
                self.total_message+=hot_x
                print(self.total_message)
                self.clear()
            else:
                hot_x = self.tim_hot_finish_loqo - self.tim_hot_start_loqo
                self.total_message+=hot_x
                print(self.total_message)
                self.clear()
##############################  Обед
    def hot_start_dinner(self,infix):
        hot_start_dinner = self.textbox1.text
        print(hot_start_dinner)
        self.textbox1.text = ""
        if hot_start_dinner=="":
            self.textbox2.text= erorr_1
            return self.clear()
        try:
            hot_start_dinner_a, hot_start_dinner_b = hot_start_dinner.split(Delimeter)
        except:
            self.textbox2.text=erorr_2
            self.clear()
        else:
            hour_hot_start_dinner = int(hot_start_dinner_a) * 60
            if hour_hot_start_dinner > 1440:
                self.textbox2.text = erorr_2
                return self.clear()
            if int(hot_start_dinner_a) > 60:
                self.textbox2.text = erorr_2
                return self.clear()
            self.tim_hot_start_dinner = int(hour_hot_start_dinner) + int(hot_start_dinner_b)
            text = 'Начало обеда'
            self.textbox2.text = "%s- %s"%(text,hot_start_dinner)
            print(self.tim_hot_start_dinner)
            self.bt.unbind(on_release=self.hot_start_dinner)
            self.bt1.unbind(on_release=self.hot_skip_dinner)
            self.bt.bind(on_release=self.hot_finish_dinner)
            self.toolbar.title = 'Окончание обеда:'
            self.clear()
    
    def hot_skip_dinner(self,infix):
        self.bt.unbind(on_release=self.hot_start_dinner)
        self.bt1.unbind(on_release=self.hot_skip_dinner)
        if self.tim_work_start < 1080:
            if int(self.c)>0:
                self.toolbar.title = 'Начало экипировки:'
                self.bt.bind(on_release=self.start_equip_time)
                self.bt1.bind(on_release=self.skip_equip_time)
            if int(self.c)==0:
                self.bt.bind(on_release=self.start_to)
                self.bt1.bind(on_release=self.skip_to)
                self.minutesf=0
                self.toolbar.title = 'Начало ТО:'
        if self.tim_work_start >= 1080:
            self.bt.bind(on_release=self.train_start)
            self.bt1.bind(on_release=self.skip_train)
            self.toolbar.title = 'Отпр. ст.Промышленная:'
            self.total_train=0
            self.total_trains=0
            self.minutesf =0
            self.minutesto=0
        self.clear()
    
    def hot_finish_dinner(self,infix):
        hot_finish_dinner = self.textbox1.text
        print(hot_finish_dinner)
        self.textbox1.text = ""
        if hot_finish_dinner=="":
            self.textbox2.text= erorr_1
            return self.clear()
        try:
            hot_finish_dinner_a, hot_finish_dinner_b = hot_finish_dinner.split(Delimeter)
        except:
            self.textbox2.text=erorr_2
            self.clear()
        else:
            hour_hot_finish_dinner = int(hot_finish_dinner_a) * 60
            if hour_hot_finish_dinner > 1440:
                self.textbox2.text = erorr_2
                return self.clear()
            if int(hot_finish_dinner_a) > 60:
                self.textbox2.text = erorr_2
                return self.clear()
            self.tim_hot_finish_dinner = int(hour_hot_finish_dinner) + int(hot_finish_dinner_b)
            text = 'Окончание обеда'
            self.textbox2.text = "%s- %s"%(text,hot_finish_dinner)
            self.bt.unbind(on_release=self.hot_finish_dinner)
            self.bt1.unbind(on_release=self.hot_skip_dinner)
            if self.tim_work_start < 1080:
                if int(self.c)>0:
                    self.bt.bind(on_release=self.start_equip_time)
                    self.bt1.bind(on_release=self.skip_equip_time)
                    self.toolbar.title = 'Начало экипировки:'
                if int(self.c)==0:
                    self.bt.bind(on_release=self.start_to)
                    self.bt1.bind(on_release=self.skip_to)
                    self.minutesf=0
                    self.toolbar.title = 'Начало ТО:'
            if self.tim_work_start >= 1080:
                self.bt.bind(on_release=self.train_start)
                self.bt1.bind(on_release=self.skip_train)
                self.toolbar.title = 'Отпр. ст.Промышленная:'
                self.total_train=0
                self.total_trains=0
                self.minutesf =0
                self.minutesto=0
            if self.tim_hot_start_dinner > self.tim_hot_finish_dinner:
                hot_x = 1440 - self.tim_hot_start_dinner + self.tim_hot_finish_dinner
                self.total_message+=hot_x
                print(hot_x)
                print(self.total_message)
                self.clear()
            else:
                hot_x = self.tim_hot_finish_dinner - self.tim_hot_start_dinner
                self.total_message+=hot_x
                print(hot_x)
                print(self.total_message)
                self.clear()
###################    Экипировка
    def start_equip_time(self,infix):
        start_equip_time = self.textbox1.text
        print(start_equip_time)
        self.textbox1.text = ""
        if start_equip_time=="":
            self.textbox2.text= erorr_1
            return self.clear()
        try:
            start_equip_time_a, start_equip_time_b = start_equip_time.split(Delimeter)
        except:
            self.textbox2.text=erorr_2
            self.clear()
        else:
            hour_start_equip_time = int(start_equip_time_a) * 60
            if hour_start_equip_time > 1440:
                self.textbox2.text = erorr_2
                return self.clear()
            if int(start_equip_time_a) > 60:
                self.textbox2.text = erorr_2
                return self.clear()
            self.tim_start_equip_time = int(hour_start_equip_time) + int(start_equip_time_b)
            text = 'Начало экипировки'
            self.textbox2.text = "%s- %s"%(text,start_equip_time)
            print(self.tim_start_equip_time)
            self.bt.unbind(on_release=self.start_equip_time)
            self.bt1.unbind(on_release=self.skip_equip_time)
            self.bt.bind(on_release=self.finish_equip_time)
            self.toolbar.title = 'Окончание экипировки:'
            self.clear()

    def skip_equip_time(self, infix):
        self.bt.unbind(on_release=self.start_equip_time)
        self.bt1.unbind(on_release=self.skip_equip_time)
        self.bt.bind(on_release=self.start_to)
        self.bt1.bind(on_release=self.skip_to)
        self.toolbar.title = 'Начало ТО:'
        self.minutesf=0
        self.clear()
        
    def finish_equip_time(self,infix):
        finish_equip_time = self.textbox1.text
        print(finish_equip_time)
        self.textbox1.text = ""
        if finish_equip_time=="":
            self.textbox2.text= erorr_1
            return self.clear()
        try:
            finish_equip_time_a, finish_equip_time_b = finish_equip_time.split(Delimeter)
        except:
            self.textbox2.text=erorr_2
            self.clear()
        else:
            hour_finish_equip_time = int(finish_equip_time_a) * 60
            if hour_finish_equip_time > 1440:
                self.textbox2.text = erorr_2
                return self.clear()
            if int(finish_equip_time_a) > 60:
                self.textbox2.text = erorr_2
                return self.clear()
            self.tim_finish_equip_time = int(hour_finish_equip_time) + int(finish_equip_time_b)
            text ='Окончание экипировки'
            self.textbox2.text = "%s- %s"%(text,finish_equip_time)
            self.bt.unbind(on_release=self.finish_equip_time)
            self.bt.bind(on_release=self.start_to)
            self.bt1.bind(on_release=self.skip_to)
            self.toolbar.title = 'Начало ТО:'
            if self.tim_start_equip_time > self.tim_finish_equip_time:
                self.minutesf = 1440 - self.tim_start_equip_time + self.tim_finish_equip_time
                print(self.minutesf)
                self.clear()
            else:
                self.minutesf = self.tim_finish_equip_time - self.tim_start_equip_time
                print(self.minutesf)
                self.clear()
##################    ТО
    def start_to(self,infix):
        start_to = self.textbox1.text
        print(start_to)
        self.textbox1.text = ""
        if start_to=="":
            self.textbox2.text= erorr_1
            return self.clear()
        try:
            start_to_a, start_to_b = start_to.split(Delimeter)
        except:
            self.textbox2.text=erorr_2
        else:
            hour_start_to = int(start_to_a) * 60
            if hour_start_to > 1440:
                self.textbox2.text = erorr_2
                return self.clear()
            if int(start_to_a) > 60:
                self.textbox2.text = erorr_2
                return self.clear()
            self.tim_start_to = int(hour_start_to) + int(start_to_b)
            text = 'Начало ТО'
            self.textbox2.text = "%s- %s"%(text,start_to)
            print(self.tim_start_to)
            self.bt.unbind(on_release=self.start_to)
            self.bt1.unbind(on_release=self.skip_to)
            self.bt.bind(on_release=self.finish_to)
            self.toolbar.title = 'Окончание ТО:'
            self.clear()

    def skip_to(self, infix):
        self.bt.unbind(on_release=self.start_to)
        self.bt1.unbind(on_release=self.skip_to)
        self.bt.bind(on_release=self.train_start)
        self.bt1.bind(on_release=self.skip_train)
        self.total_train=0
        self.total_trains=0
        self.toolbar.title = 'Отпр. ст.Промышленная:'
        self.minutesto=0
        self.clear()
        
    def finish_to(self,infix):
        finish_to = self.textbox1.text
        print(finish_to)
        self.textbox1.text = ""
        if finish_to=="":
            self.textbox2.text= erorr_1
            return self.clear()
        try:
            finish_to_a, finish_to_b = finish_to.split(Delimeter)
        except:
            self.textbox2.text=erorr_2
            self.clear()
        else:
            hour_finish_to = int(finish_to_a) * 60
            if hour_finish_to > 1440:
                self.textbox2.text = erorr_2
                return self.clear()
            if int(finish_to_a) > 60:
                self.textbox2.text = erorr_2
                return self.clear()
            self.tim_finish_to = int(hour_finish_to) + int(finish_to_b)
            text = 'Окончание ТО'
            self.textbox2.text = "%s- %s"%(text,finish_to)
            self.bt.unbind(on_release=self.finish_to)
            self.bt.bind(on_release=self.train_start)
            self.bt1.bind(on_release=self.skip_train)
            self.total_train=0
            self.total_trains = 0
            self.toolbar.title = 'Отпр. ст.Промышленная:'
            if self.tim_start_to > self.tim_finish_to:
                self.minutesto = 1440 - self.tim_start_to + self.tim_finish_to
                print(self.minutesto)
                self.clear()
            else:
                self.minutesto = self.tim_finish_to - self.tim_start_to
                print(self.minutesto)
                self.clear()
###################
    def train_start(self,infix):
        train_start = self.textbox1.text
        print(train_start)
        self.textbox1.text = ""
        if train_start=="":
            self.textbox2.text= erorr_1
            return self.clear()
        try:
            train_start_a, train_start_b = train_start.split(Delimeter)
        except:
            self.textbox2.text=erorr_2
            self.clear()
        else:
            hour_train_start = int(train_start_a) * 60
            if hour_train_start > 1440:
                self.textbox2.text = erorr_2
                return self.clear()
            if int(train_start_a) > 60:
                self.textbox2.text = erorr_2
                return self.clear()
            self.tim_train_start = int(hour_train_start) + int(train_start_b)
            text = 'Отпр. ст.Промышленная'
            self.textbox2.text = "%s- %s"%(text,train_start)
            print(self.tim_train_start)
            self.bt.unbind(on_release=self.train_start)
            self.bt1.unbind(on_release=self.skip_train)
            self.bt.bind(on_release=self.train_finish)
            self.toolbar.title = 'Приб. ст.Сургут:'
            self.clear()

    def skip_train(self,infix):
        self.bt.unbind(on_release=self.train_start)
        self.bt1.unbind(on_release=self.skip_train)
        self.bt.bind(on_release=self.trains_start)
        self.bt1.bind(on_release=self.skip_trains)
        self.toolbar.title = 'Отпр. ст.Сургут:'
        self.clear()
        
    def train_finish(self,infix):
        train_finish = self.textbox1.text
        print(train_finish)
        self.textbox1.text = ""
        if train_finish=="":
            self.textbox2.text= erorr_1
            return self.clear()
        try:
            train_finish_a, train_finish_b = train_finish.split(Delimeter)
        except:
            self.textbox2.text=erorr_2
            self.clear()
        else:
            hour_train_finish = int(train_finish_a) * 60
            if hour_train_finish > 1440:
                self.textbox2.text = erorr_2
                return self.clear()
            if int(train_finish_a) > 60:
                self.textbox2.text = erorr_2
                return self.clear()
            self.tim_train_finish = int(hour_train_finish) + int(train_finish_b)
            text = 'Приб. ст.Сургут'
            self.textbox2.text = "%s- %s"%(text,train_finish)
            self.bt.unbind(on_release=self.train_finish)
            self.bt.bind(on_release=self.train_start)
            self.bt1.bind(on_release=self.skip_train)
            self.toolbar.title = 'Отпр. ст.Промышленная:'
            if self.tim_train_start > self.tim_train_finish:
                train_x = 1440 - self.tim_train_start + self.tim_train_finish
                self.total_train+=train_x
                print(self.total_train)
                self.clear()
            else:
                train_x = self.tim_train_finish - self.tim_train_start
                self.total_train+=train_x
                print(self.total_train)
                self.clear()
###################
    def trains_start(self,infix):
        trains_start = self.textbox1.text
        print(trains_start)
        self.textbox1.text = ""
        if trains_start=="":
            self.textbox2.text= erorr_1
            return self.clear()
        try:
            trains_start_a, trains_start_b = trains_start.split(Delimeter)
        except:
            self.textbox2.text=erorr_2
            self.clear()
        else:
            hour_trains_start = int(trains_start_a) * 60
            if hour_trains_start > 1440:
                self.textbox2.text = erorr_2
                return self.clear()
            if int(trains_start_a) > 60:
                self.textbox2.text = erorr_2
                return self.clear()
            self.tim_trains_start = int(hour_trains_start) + int(trains_start_b)
            text = 'Отпр. ст.Сургут'
            self.textbox2.text = "%s- %s"%(text,trains_start)
            print(self.tim_trains_start)
            self.bt.unbind(on_release=self.trains_start)
            self.bt1.unbind(on_release=self.skip_trains)
            self.bt.bind(on_release=self.trains_finish)
            self.toolbar.title = 'Приб. ст.Промышленная:'
            self.clear()

    def trains_finish(self,infix):
        trains_finish = self.textbox1.text
        print(trains_finish)
        self.textbox1.text = ""
        if trains_finish=="":
            self.textbox2.text= erorr_1
            return self.clear()
        try:
            trains_finish_a, trains_finish_b = trains_finish.split(Delimeter)
        except:
            self.textbox2.text=erorr_2
            self.clear()
        else:
            hour_trains_finish = int(trains_finish_a) * 60
            if hour_trains_finish > 1440:
                self.textbox2.text = erorr_2
                return self.clear()
            if int(trains_finish_a) > 60:
                self.textbox2.text = erorr_2
                return self.clear()
            self.tim_trains_finish = int(hour_trains_finish) + int(trains_finish_b)
            text = 'Приб. ст.Промышленная'
            self.textbox2.text = "%s- %s"%(text,trains_finish)
            self.bt.unbind(on_release=self.trains_finish)
            self.bt.bind(on_release=self.trains_start)
            self.bt1.bind(on_release=self.skip_trains)
            self.toolbar.title = 'Отпр. ст.Сургут:'
            if self.tim_trains_start > self.tim_trains_finish:
                trains_x = 1440 - self.tim_trains_start + self.tim_trains_finish
                self.total_trains+=trains_x
                print(self.total_trains)
                self.clear()
            else:
                trains_x = self.tim_trains_finish - self.tim_trains_start
                self.total_trains+=trains_x
                print(self.total_trains)
                self.clear()
###################
    def skip_trains(self,infix):
        self.bt.unbind(on_release=self.trains_start)
        self.bt1.unbind(on_release=self.skip_trains)
        self.toolbar.title = 'Результат:'
        #self.textbox2.text=""
        workm = int(self.minutesw) - int(self.total_message) - int(self.minutesf) - int(self.minutesto) - int(self.total_train) - int(self.total_trains)
        normf = float((self.total_message / 60) * 9) + float((workm / 60) * 32.550) + float((self.total_train / 60) * 108) + float((self.total_trains / 60) * 73.820) + float((self.minutesto / 60) * 0) + float((self.minutesf / 60) * 0)
        result = normf - self.result
        ga = abs(result)
        economy= "Экономия"
        text= "кг"
        overspending= "Перерасход"
        zero="Вы сожгли топлива по норме"
        if result >0:
            self.textbox2.text= "%s- %s,%s"%(economy,result,text)

        if result <0:
            self.textbox2.text= "%s- %s,%s"%(overspending,ga,text)
        if result ==0:
            self.textbox2.text= "%s"%(zero)
        self.clear()
###################
class CalculatorApp(MDApp):
    def build(self):
        #Window.size = 400,530
        self.theme_cls.theme_style='Dark'
        sc = ScreenManager()
        cl = Calc()
        sc.add_widget(cl)
        return sc
if __name__ == '__main__':
    if hasattr(sys, '_MEIPASS'):
        resource_add_path(os.path.join(sys._MEIPASS))
    CalculatorApp().run()
