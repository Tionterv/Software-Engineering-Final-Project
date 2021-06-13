from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.image import Image
from kivy.uix.rst import RstDocument
from kivy.uix.textinput import TextInput
from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.uix.label import Label
from kivy.app import App
from kivy.uix.tabbedpanel import TabbedPanel, TabbedPanelHeader, TabbedPanelItem
from kivy.lang import Builder
from kivy.config import Config
Config.set('input', 'mouse', 'mouse,multitouch_on_demand')

class Location:
    def __init__(self, aisle, bay, capacity):
        self.aisle = aisle
        self.bay = bay
        self.capacity = capacity
        self.available = capacity
        self.categories = 0
        self.item = {}  # to store all

    def add_item(self, ident, quant):
        if quant > self.available:  # cannot add
            return False
        else:
            self.available -= quant
            if ident not in self.item:  # no pre-exist item found
                self.item[ident] = quant
                self.categories += 1
            else:
                self.item[ident] += quant
            return True

    def remove_item(self, ident, quant):
        if ident not in self.item:
            return False
        else:
            if quant > self.item[ident]:
                return False
            else:
                if quant == self.item[ident]:
                    #remove listing
                    self.item.pop(ident)
                else:
                    self.item[ident] -= quant
                    self.available += quant
                return True

    def search_item(self, ident):
        if ident in self.item:
            return 1
        return -1

    def selfprint(self):
        # print(self.idx, self.capacity, self.available, self.item)
        print(1, 2, 3, 4, 5)


class Test(TabbedPanel):
    def __init__(self, **kwargs):
        super(Test, self).__init__(**kwargs)
        self.size_hint = (0.9, 0.9)
        self.pos_hint = {'center_x': .5, 'center_y': .5}
        tab1 = TabbedPanelItem(text="Home")
        wimg = Image(source='Overhead-CEO-Logo4.jpg')  # image background
        tab1.add_widget(wimg)
        self.add_widget(tab1)
        self.default_tab = tab1
        tab2 = TabbedPanelItem(text="Add")
        layout1_1 = GridLayout()
        layout1_1.cols = 1
        layout1_2 = GridLayout()
        layout1_2.cols = 2
        layout1_2.add_widget(Label(text="Product ID"))
        self.addid = TextInput(multiline=False, cursor_color = [0,0,0,1])
        layout1_2.add_widget(self.addid)
        layout1_2.add_widget(Label(text="Quantity"))
        self.addquant = TextInput(multiline=False, cursor_color = [0,0,0,1])
        layout1_2.add_widget(self.addquant)
        layout1_2.add_widget(Label(text="Aisle"))
        self.addaisle = TextInput(multiline=False, cursor_color = [0,0,0,1])
        layout1_2.add_widget(self.addaisle)
        layout1_2.add_widget(Label(text="Bay"))
        self.addbay = TextInput(multiline=False, cursor_color = [0,0,0,1])
        layout1_2.add_widget(self.addbay)
        layout1_1.add_widget(layout1_2)
        self.button1 = Button(text="Add")
        self.button1.bind(on_press=self.add_press1)
        layout1_1.add_widget(self.button1)
        layout1_3 = GridLayout()
        layout1_3.cols = 2
        layout1_3.add_widget(Label(text="Log Info"))
        self.addinfo = TextInput(text="", readonly = True, cursor_blink = False, cursor_color = [0,0,0,1])
        layout1_3.add_widget(self.addinfo)
        layout1_1.add_widget(layout1_3)
        tab2.add_widget(layout1_1)
        self.add_widget(tab2)
        tab3 = TabbedPanelItem(text="Remove")
        # label2 = Label(text="HELLO", text_size=self.size, valign="top", halign="left")
        layout2_1 = GridLayout()
        layout2_1.cols = 1
        layout2_2 = GridLayout()
        layout2_2.cols = 2
        layout2_2.add_widget(Label(text="Product ID"))
        self.removeid = TextInput(multiline=False, cursor_color = [0,0,0,1])
        layout2_2.add_widget(self.removeid)
        layout2_2.add_widget(Label(text="Quantity"))
        self.removequant = TextInput(multiline=False, cursor_color = [0,0,0,1])
        layout2_2.add_widget(self.removequant)
        layout2_2.add_widget(Label(text="Aisle"))
        self.removeaisle = TextInput(multiline=False, cursor_color = [0,0,0,1])
        layout2_2.add_widget(self.removeaisle)
        layout2_2.add_widget(Label(text="Bay"))
        self.removebay = TextInput(multiline=False, cursor_color = [0,0,0,1])
        layout2_2.add_widget(self.removebay)
        layout2_1.add_widget(layout2_2)
        self.button2 = Button(text="Remove")
        self.button2.bind(on_press=self.add_press2)
        layout2_1.add_widget(self.button2)
        layout2_3 = GridLayout()
        layout2_3.cols = 2
        layout2_3.add_widget(Label(text="Log Info"))
        self.removeinfo = TextInput(text="", readonly = True, cursor_blink = False, cursor_color = [0,0,0,1])
        layout2_3.add_widget(self.removeinfo)
        layout2_1.add_widget(layout2_3)
        tab3.add_widget(layout2_1)
        self.add_widget(tab3)
        tab4 = TabbedPanelItem(text="Search")
        layout3_1 = GridLayout()
        layout3_1.cols = 1
        layout3_2 = GridLayout()
        layout3_2.cols = 2
        layout3_2.add_widget(Label(text="Product ID"))
        self.searchid = TextInput(multiline=False, cursor_color = [0,0,0,1])
        layout3_2.add_widget(self.searchid)
        layout3_1.add_widget(layout3_2)
        self.button3 = Button(text="Search")
        self.button3.bind(on_press=self.add_press3)
        layout3_1.add_widget(self.button3)
        layout3_3 = GridLayout()
        layout3_3.cols = 2
        layout3_3.add_widget(Label(text="Result"))
        self.searchinfo = TextInput(text="", readonly = True, cursor_blink = False, cursor_color = [0,0,0,1])
        layout3_3.add_widget(self.searchinfo)
        layout3_1.add_widget(layout3_3)
        tab4.add_widget(layout3_1)
        self.add_widget(tab4)
        tab5 = TabbedPanelItem(text="Inventory")
        label4 = self.inventoryinfo = TextInput(text="", readonly = True, cursor_blink = False, cursor_color = [0,0,0,1], font_size = 20)
        tab5.add_widget(label4)
        self.add_widget(tab5)
        loca1 = Location(1, 2, 50)
        loca2 = Location(2, 3, 50)
        loca3 = Location(1, 4, 80)
        loca4 = Location(4, 7, 120)
        self.loc_list = [loca1, loca2, loca3, loca4]

    def add_press1(self, instance):
        """print(int(self.addid.text), int(self.addquant.text), int(self.addaisle.text), int(self.addbay.text))
        print("type of input text: {}".format(type(int(self.addid.text))))
        self.addinfo.text = "Success\""""

        self.addinfo.text = ""
        self.addinfo.font_size = 20
        self.addinfo.valign = 'middle'
        self.addinfo.halign = 'center'
        self.addinfo.cursor_color = [0,0,0,1]

        try:
            addid = int(self.addid.text)
            addquant = int(self.addquant.text)
            addaisle = int(self.addaisle.text)
            addbay = int(self.addbay.text)
        except BaseException as error:
            self.addinfo.font_size = 30
            self.addinfo.valign = 'middle'
            self.addinfo.halign = 'center'
            self.addinfo.cursor_color = [255,255,255,1]
            self.addinfo.text = "--- Input Error ---"
            self.addinfo.text = "--- Input Error ---\n\n---Integers Only---\n---All Fields Required---"
            return

        
        for i in range(len(self.loc_list)):
            if self.loc_list[i].aisle == addaisle and self.loc_list[i].bay == addbay:
                if self.loc_list[i].add_item(addid, addquant):
                    self.addinfo.text = "Success Add {} Product ID: {} to Aisle-Bay {}-{}".format(addquant, addid, addaisle, addbay)
                else:
                    self.addinfo.text = "Space not enough to fill the given quantity"
                    
                #Inventory Update
                self.inventoryinfo.text = ""
                self.inventoryinfo.text = "---Inventory---\n"

                for i in range(len(self.loc_list)):
                    self.inventoryinfo.text = self.inventoryinfo.text + "\nLocation {}-{}:\n".format(self.loc_list[i].aisle, self.loc_list[i].bay)
                    for productid in self.loc_list[i].item: 
                        self.inventoryinfo.text = self.inventoryinfo.text + "\tProduct ID: {} - Quantity: {}\n".format(productid,self.loc_list[i].item[productid])
                #
                return
        self.addinfo.text = "No such location found"
        return

    def add_press2(self, instance):
       
        self.removeinfo.text = ""
        self.removeinfo.font_size = 20
        self.removeinfo.valign = 'middle'
        self.removeinfo.halign = 'center'
        self.removeinfo.cursor_color = [0,0,0,1]
        try:
            removeid = int(self.removeid.text)
            removequant = int(self.removequant.text)
            removeaisle = int(self.removeaisle.text)
            removebay = int(self.removebay.text)
        except BaseException as error:
            self.removeinfo.font_size = 30
            self.removeinfo.valign = 'middle'
            self.removeinfo.halign = 'center'
            self.removeinfo.cursor_color = [255,255,255,1]
            self.removeinfo.text = "--- Input Error ---\n\n---Integers Only---\n---All Fields Required---"
            return
           

        for i in range(len(self.loc_list)):
            if self.loc_list[i].aisle == removeaisle and self.loc_list[i].bay == removebay:
                if self.loc_list[i].remove_item(removeid, removequant):
                    self.removeinfo.text = "Success Remove {} Product ID: {} to Aisle-Bay {}-{}".format(removequant, removeid,removeaisle, removebay)
                else:
                    self.removeinfo.text = "Failure Remove: remove more than available"
                #Inventory Update
                self.inventoryinfo.text = ""
                self.inventoryinfo.text = "---Inventory---\n"
                for i in range(len(self.loc_list)):
                    self.inventoryinfo.text = self.inventoryinfo.text + "\nLocation {}-{}:\n".format(self.loc_list[i].aisle, self.loc_list[i].bay)
                    for productid in self.loc_list[i].item: 
                        self.inventoryinfo.text = self.inventoryinfo.text + "\tProduct ID: {} - Quantity: {}\n".format(productid,self.loc_list[i].item[productid])
                #
                return
        self.removeinfo.text = "No such location found"
        return

    def add_press3(self,instance):
        self.searchinfo.text = ""
        self.searchinfo.font_size = 20
        self.searchinfo.valign = 'middle'
        self.searchinfo.halign = 'center'
        self.searchinfo.cursor_color = [0,0,0,1]
        try:
            searchid = int(self.searchid.text)
        except BaseException as error:
            self.searchinfo.font_size = 30
            self.searchinfo.valign = 'middle'
            self.searchinfo.halign = 'center'
            self.searchinfo.cursor_color = [255,255,255,1]
            self.searchinfo.text = "--- Input Error ---\n\n---Integers Only---\n---All Fields Required---"
            return

        flag = 0
        self.searchinfo.text = ""
        for i in range(len(self.loc_list)):
                if searchid in self.loc_list[i].item: 
                    flag = 1
                    self.searchinfo.text = self.searchinfo.text + "\nInfo found\nProduct ID: {}\nQuantity: {}\nLocation: {}-{}\n".format(searchid,self.loc_list[i].item[searchid], self.loc_list[i].aisle, self.loc_list[i].bay)
                    
        if flag == 0:
            self.searchinfo.text = "No Product ID: {}".format(searchid)

        return


   

class Overhead_CEO(App):
    def build(self):
        Window.clearcolor = (255 / 255.0, 153 / 255.0, 51 / 255.0, 1)
        return Test()

Overhead_CEO().run()
# TestApp().run()
