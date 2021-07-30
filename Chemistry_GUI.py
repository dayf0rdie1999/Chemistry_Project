from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.bottomnavigation import MDBottomNavigation, MDBottomNavigationItem
from kivymd.uix.gridlayout import MDGridLayout
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.datatables import MDDataTable
from kivy.metrics import dp
from kivymd.uix.dialog import MDDialog
from kivymd.uix.dropdownitem import MDDropDownItem
import NamingCompound
import ChemistryBalancer
import DatabaseClass
from kivymd.uix.menu import MDDropdownMenu


class root(MDBottomNavigation):
    pass

class MainApp(MDApp):
    Naming_Compound_Class = NamingCompound.NamingChemical();
    Chemistry_Balancer_Class = ChemistryBalancer.ChemistryBalancer();
    Database = DatabaseClass.Using_Database();

    def build(self):
        self.theme_cls.primary_palette = "Blue"
        self.theme_cls.primary_hue = "500"

        return Builder.load_file("main.kv")

    def on_start(self):
        menu_items = [{"text": "Name"},{"text": "Symbol"}]

        self.menu = MDDropdownMenu(
            caller = self.root.ids.drop_item, items = menu_items, width_mult = 4,
            callback = self.set_item
        )

        self.Periodic_data_tables = MDDataTable(
            size_hint=(0.7, 0.6),
            # name column, width column
            use_pagination=True,
            pagination_menu_pos = "auto",
            column_data=[
                ("Atom", dp(30)),
                ("Name", dp(30)),
                ("Symbol", dp(30)),
                ("Molar Mass", dp(30)),
                ("Charge", dp(30)),
                ("Type", dp(30)),
            ],
            row_data=self.Database.get_everything_From_element_except_Suffix_Periodic(),
        )

        self.Polyatomic_data_tables = MDDataTable(
            size_hint=(0.7, 0.6),
            # name column, width column
            use_pagination=True,
            pagination_menu_pos="auto",
            column_data=[
                ("Name", dp(30)),
                ("Symbol", dp(30)),
                ("Molar Mass", dp(30)),
                ("Charge", dp(30)),
                ("Type", dp(30)),
            ],
            row_data=self.Database.get_everything_From_element_except_Suffix_Polyatomic(),
        )


    def set_item(self, instance):
        self.root.ids.drop_item.set_item(instance.text)
        self.root.ids.search.hint_text = "Enter " + instance.text
        self.menu.dismiss()

    def create_table_Periodic(self, row_data_info):
        print(row_data_info)
        self.Found_data_tables = MDDataTable(
            size_hint=(0.7, 0.6),
            # name column, width column
            use_pagination=True,
            pagination_menu_pos="auto",
            column_data=[
                ("Atom", dp(30)),
                ("Name", dp(30)),
                ("Symbol", dp(30)),
                ("Molar Mass", dp(30)),
                ("Charge", dp(30)),
                ("Type", dp(30)),
            ],
            row_data= row_data_info,
        )

    def create_table_Polyatomic(self, row_data_info):
        print(row_data_info)
        self.Found_data_tables = MDDataTable(
            size_hint=(0.7, 0.6),
            # name column, width column
            use_pagination=True,
            pagination_menu_pos="auto",
            column_data=[
                ("Name", dp(30)),
                ("Symbol", dp(30)),
                ("Molar Mass", dp(30)),
                ("Type", dp(30)),
                ("Charge", dp(30)),
            ],
            row_data=row_data_info,
        )

    def search_element(self):
        if self.root.ids.drop_item.current_item == "":
            self.alert_dialog("Select The Type For Searching")
        elif self.root.ids.drop_item.current_item == "Name":
            if self.Database.get_everything_element_Periodic_From_Name(self.root.ids.search.text) is not None:
                print(self.Database.get_everything_element_Periodic_From_Name(self.root.ids.search.text))
                self.create_table_Periodic(row_data_info=self.Database.get_everything_element_Periodic_From_Name(self.root.ids.search.text));
                return self.Found_data_tables.open()
            elif self.Database.get_everything_element_Periodic_From_Name(self.root.ids.search.text) is None:
                pass

            if self.Database.get_everything_element_Polyatomic_From_Name(self.root.ids.search.text) is not None:
                self.create_table_Polyatomic(row_data_info=self.Database.get_everything_element_Polyatomic_From_Name(self.root.ids.search.text))
                return self.Found_data_tables.open()
            elif self.Database.get_everything_element_Polyatomic_From_Name(self.root.ids.search.text) is None:
                self.alert_dialog("The Compound Or Element Doesn't Exist in Database")

        elif self.root.ids.drop_item.current_item == "Symbol":
            if self.Database.get_everything_element_Periodic_From_Symbol(self.root.ids.search.text) is not None:
                self.create_table_Periodic(
                    row_data_info=self.Database.get_everything_element_Periodic_From_Symbol(self.root.ids.search.text));
                return self.Found_data_tables.open()
            elif self.Database.get_everything_element_Periodic_From_Symbol(self.root.ids.search.text) is None:
                pass

            if self.Database.get_everything_element_Polyatomic_From_Symbol(self.root.ids.search.text) is not None:
                self.create_table_Polyatomic(row_data_info=self.Database.get_everything_element_Polyatomic_From_Symbol(self.root.ids.search.text))
                return self.Found_data_tables.open()
            elif self.Database.get_everything_element_Polyatomic_From_Symbol(self.root.ids.search.text) is None:
                self.alert_dialog("The Compound Or Element Doesn't Exist in Database")

    def open_table_Periodic(self):
        self.Periodic_data_tables.open()

    def open_table_Polyatomic(self):
        self.Polyatomic_data_tables.open()

    def open_table(self):
        try:
            self.data_tables.open();
        except:
            self.alert_dialog(Message = "Need Chemistry Equation to Format the Tables")

    def Naming_Compound(self):
        if self.root.ids.Compound_Symbol.text != "" and self.root.ids.Compound_Name.text == "":
            try:
                self.root.ids.Compound_Name.text = self.Naming_Compound_Class.Naming_Compound_From_Symbol(self.root.ids.Compound_Symbol.text);
                self.root.ids.Molar_Mass.text = str(self.Naming_Compound_Class.Calculating_Molar_Mass_Chemical_Compound());
                self.root.ids.Type.text = str(self.Naming_Compound_Class.get_compound_type());
            except:
                self.alert_dialog(Message = "Incorrect Chemical Compound")

        elif self.root.ids.Compound_Name.text != "" and self.root.ids.Compound_Symbol.text == "":
            try:
                self.root.ids.Compound_Symbol.text = self.Naming_Compound_Class.Naming_Symbol_From_Compound_Name(self.root.ids.Compound_Name.text)
                self.root.ids.Molar_Mass.text = str(self.Naming_Compound_Class.Calculating_Molar_Mass_Chemical_Compound());
                self.root.ids.Type.text = str(self.Naming_Compound_Class.get_compound_type());
            except:
                self.alert_dialog(Message = "Incorrect Chemical Name")

        else:
            self.alert_dialog(Message = "Enter only either Name or Symbol")


    def Delete_Everything(self):
        self.root.ids.Compound_Symbol.text = ""
        self.root.ids.Compound_Name.text = ""
        self.root.ids.Molar_Mass.text = ""
        self.root.ids.Type.text = ""

    # Alerting the user something that they are missing
    def alert_dialog(self, Message):
        self.dialog = MDDialog(
            title="Warning",
            text=Message
        )
        self.dialog.open();

    def Balancing_Equation(self):

        try:
            self.root.ids.answer.text = self.Chemistry_Balancer_Class.Balance_Chemistry_Equation(self.root.ids.equation.text)
        except:
            self.alert_dialog("Please Input Spaces Bewteen Chemical Component and Input the correct Chemical Equation")

        row_data = self.Chemistry_Balancer_Class.Compound_key_Information_Dictionary;
        row_data_list = [];
        for key, information_dictionary in row_data.items():
            row_list = [key];
            for items_key, value in information_dictionary.items():
                if items_key != "Selected":
                    row_list.append(value);
                else:
                    pass
            row_list = tuple(row_list);
            row_data_list.append(row_list)


        self.data_tables = MDDataTable(
            size_hint=(0.9, 0.6),
            # name column, width column
            column_data=[
                ("Symbol", dp(30)),
                ("Coefficient", dp(30)),
                ("Name", dp(30)),
                ("Molar Mass", dp(30)),
            ],
            row_data = row_data_list,
        )

    def Calculating_Mass_Moles(self):
        if self.root.ids.Symbol.text != "" and self.root.ids.Mass.text != "" and self.root.ids.Moles.text == "":
            row_data = self.Chemistry_Balancer_Class.Calculating_The_Moles_Number_And_Weight_Each_Compound_In_Equation(symbol = self.root.ids.Symbol.text, Mass = float(self.root.ids.Mass.text));
            row_data_list = [];
            for key, information_dictionary in row_data.items():
                row_list = [key];
                for items_key, value in information_dictionary.items():
                    if items_key != "Selected":
                        row_list.append(value);
                    else:
                        pass
                row_list = tuple(row_list);
                row_data_list.append(row_list)

            self.data_tables = MDDataTable(
                size_hint=(0.9, 0.6),
                # name column, width column
                column_data=[
                    ("Symbol", dp(30)),
                    ("Coefficient", dp(30)),
                    ("Name", dp(30)),
                    ("Molar Mass", dp(30)),
                    ("Moles", dp(30)),
                    ("Mass", dp(30)),
                ],
                row_data=row_data_list,
            )

        elif self.root.ids.Symbol.text != "" and self.root.ids.Mass.text == "" and self.root.ids.Moles.text != "":
            row_data = self.Chemistry_Balancer_Class.Calculating_The_Moles_Number_And_Weight_Each_Compound_In_Equation(symbol = self.root.ids.Symbol.text, Moles = float(self.root.ids.Moles.text));
            row_data_list = [];
            for key, information_dictionary in row_data.items():
                row_list = [key];
                for items_key, value in information_dictionary.items():
                    if items_key != "Selected":
                        row_list.append(value);
                    else:
                        pass
                row_list = tuple(row_list);
                row_data_list.append(row_list)


            self.data_tables = MDDataTable(
                size_hint=(0.9, 0.6),
                # name column, width column
                column_data=[
                    ("Symbol", dp(30)),
                    ("Coefficient", dp(30)),
                    ("Name", dp(30)),
                    ("Molar Mass", dp(30)),
                    ("Moles", dp(30)),
                    ("Mass", dp(30)),
                ],
                row_data=row_data_list,
            )

        else:
            self.alert_dialog(Message = "Missing symbol or The original symbol or Inputing both Mass and Moles at the same time")

    def Clear_Balancer(self):
        self.root.ids.answer.text = "Result Appear Here"
        self.root.ids.equation.text = ""
        self.root.ids.Symbol.text = ""
        self.root.ids.Mass.text = ""
        self.root.ids.Moles.text = ""

if __name__ == "__main__":
    MainApp().run()