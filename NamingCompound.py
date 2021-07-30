import DatabaseClass


def main():
    Naming_Class = NamingChemical();
    Testing_List_Molecular = ["As4O9","NBr3", "CO", "F4Br8", "H2O", "CO2", "SO2", "H2Br6", "SO3", "P4O10", "SiO2", "P4O7",
                              "Cl2O", "SiO2", "P2O5", "SCl6", "CS2", "OF2"]
    Testing_List_Ionic_Element = ["KCl","Li2S","NaBr","BeF2","CsCl","SrS","BaI2","PbSe","ZnTe","GaN","CoF3","SnBr4","V2O5","K3P"]

    Testing_List_Ionic_Compound_Element = ["K2SO3","AgC2H3O2","Cu2CO3","Mg(OH)2","Ca3(PO4)2","FeSO4","Cu(NO3)2","CoHPO3","NiCrO4","Ni(OH)3","Cr2(SO4)3","Mn(C2H3O2)3","Mn(ClO2)4","NH4ClO3","Hg(C2H3O2)2","CsClO4","NaClO","LiNO2","KMnO4","FeCrO4","(NH4)2S","NaHCO3","Ca(HSO4)2","NH4H2PO4","NH4Cl"];

    Testing_List_Molecular_Name = ["Carbon Monoxide","Dinitrogen Trioxide","Sulfur Dioxide","Sulfur Trioxide","Dinitrogen Monoxide","Dinitrogen Tetroxide","Dinitrogen Pentoxide","Phosphorus Trichloride","Sulfur Hexachloride","Diphosphorus Pentoxide","Silicon Dioxide","Phosphorus Tribromide"];

    Testing_List_Ionic_Compound_Name = ["Lithium Sulfide","Sodium Bromide","Potassium Sulfite","Rubidium Oxide","Caesium Chloride","Silver Acetate","Copper(I) Carbonate","Beryllium Fluoride","Magnesium Hydroxide","Calcium Phosphate","Iron(II) Sulfate","Copper(II) Nitrate","Cobalt(II) Hydrogen Phosphate","Calcium Phosphate","Lead(II) Selenide","Iron(III) Oxide",
                                        "Gallium Nitride","Nickel(III) Fluoride","Nickel(III) Hydroxide","Chromium(III) Sulfate","Manganese(III) Acetate","Tin(IV) Bromide","Calcium Hydrogen Sulfate","Ammonium Dihydrogen Phosphate","Potassium Permanganate"];

    #for name in Testing_List_Ionic_Compound_Name:
    '''for element in Testing_List_Molecular:
        print(Naming_Class.Naming_Compound_From_Symbol(element))
        #print(Naming_Class.get_molecular_key_as_element_value_as_charge_dictionary())'''


    '''for element in Testing_List_Ionic_Element:
        print(Naming_Class.Naming_Compound_From_Symbol(element))
        print(Naming_Class.get_ionic_dictionary_charge_list())'''


    '''for element in Testing_List_Ionic_Compound_Element:
        print(Naming_Class.Naming_Compound_From_Symbol(element));'''
        #print(Naming_Class.compound_symbol)
        #print(Naming_Class.chemical_name)
        #print(Naming_Class.Calculating_Molar_Mass_Chemical_Compound())

    '''for compound_name in Testing_List_Molecular_Name:
        print(Naming_Class.Naming_Symbol_From_Compound_Name(compound_name))
        print(Naming_Class.Calculating_Molar_Mass_Chemical_Compound())'''

    '''for compound_name in Testing_List_Ionic_Compound_Name:
        print(Naming_Class.Naming_Symbol_From_Compound_Name(compound_name))
        print(Naming_Class.Calculating_Molar_Mass_Chemical_Compound())'''

    #Naming_Class.Naming_Symbol_From_Compound_Name("Sodium Bromide");
    print(Naming_Class.Naming_Compound_From_Symbol(compound = "Na2O2"));
    print(Naming_Class.get_compound_type())
    #print(Naming_Class.get_ionic_dictionary_charge_list())
    #print(Naming_Class.get_molecular_key_as_element_value_as_charge_dictionary())
    #print(Naming_Class.Calculating_Molar_Mass_Chemical_Compound())
    #print(Naming_Class.Naming_Symbol_From_Compound_Name(compound_name = ""))




class NamingChemical():
    def __init__(self):
        self.database = DatabaseClass.Using_Database();
        self.element_and_compound = [];
        self.element_name_list = [];
        self.compound_name_list = [];
        self.type_list = [];
        self.charge_list = [];
        self.compound_type = None;
        self.compound_symbol = None;
        self.element_in_chemical_name_list = []
        self.element_list = [];
        self.compound_list = [];
        self.vowels = "AaEeIiOoUuYy"
        self.chemical_name = ''
        self.exception_element_prefix_list = ["Iodine", "Fluorine", "Chlorine", "Bromine", "Sulfur","Phosphorus","Selenium","Tellurium","Nitrogen","Hydrogen"];
        self.ionic_dictionary_list = [];
        self.exception_compound_list = ["CH3COO","C2H3O2","Cr2O7","CrO4","MnO4","ClO","ClO2","ClO3","ClO4","H2PO4","OH"]
        self.Latin_Number = {'1': 'I', '2': 'II', '3': 'III', '4': 'IV', '5': 'V', '6': 'VI', '7': 'VII', '8': 'VIII',
                             '9': 'IX', '10': 'X'};

        self.prefix_dictionary = {"Mono": '1',"Di": '2',"Tri":'3',"Tetra":'4', "Tetro":'4',"Penta":'5',"Pento":'5',"Hexa":'6',"Hepta":'7',"Octo":'8',"Nona":'9',"Deca":'10'};
        self.chemical_compound = "";
        self.Element_and_Compound_Key_To_Atomic_Number_Dictionary = {};
        self.Molar_mass = 0;
        self.checking_input = 0;
        self.molecular_key_as_element_value_as_charge = {}

    # Determining the molecular dictionary charge list
    def determning_the_molecular_dictionary_charge(self, digit, symbol, order):
        if order == 0:
            charge = "+" + str(digit)
        elif order == 1:
            charge = "-" + str(digit)
        elif order is None:
            charge = str(digit)
        self.molecular_key_as_element_value_as_charge[symbol] = charge

    def get_molecular_key_as_element_value_as_charge_dictionary(self):
        return self.molecular_key_as_element_value_as_charge

    # Getting the ionic dictionary charge list
    def get_ionic_dictionary_charge_list(self):
        temporary_key_as_name_value_as_charge = {};
        self.element_and_compound.reverse();

        for dictionary_value_index in range(0, len(self.ionic_dictionary_list)):
            for key,value in self.ionic_dictionary_list[dictionary_value_index].items():
                if key == "charge":
                    temporary_key_as_name_value_as_charge[self.element_and_compound[dictionary_value_index]] = value
                else:
                    pass

        return temporary_key_as_name_value_as_charge

    # getting compound type
    def get_compound_type(self):
        return self.compound_type;

    # Calculating the molar mass of the entire chemical compound
    def Calculating_Molar_Mass_Chemical_Compound(self):
        list_temporary = []
        #print(self.Element_and_Compound_Key_To_Atomic_Number_Dictionary)
        for key,value in self.Element_and_Compound_Key_To_Atomic_Number_Dictionary.items():
            if self.database.get_molar_mass_periodicTable(symbol = key) is None:
                value = float(self.database.get_molar_mass_polyatomicTable(symbol = key)) * int(value);
                value = round(value,3)
                list_temporary.append(value);

            elif self.database.get_molar_mass_periodicTable(symbol = key) is not None:
                value = float(self.database.get_molar_mass_periodicTable(symbol=key)) * int(value);
                value = round(value, 3)
                list_temporary.append(value);

        for element_mass in list_temporary:
            self.Molar_mass += element_mass;

        self.Molar_mass = round(self.Molar_mass, 3)

        return self.Molar_mass

    # Getting the key from the dictionary
    def get_key(self, val):
        for key,value in self.Latin_Number.items():
            if val == value:
                return key

        return "key doesn't exist"

    def create_key_value(self,key,value,dictionary):
        dictionary[key] = value;



    # Reading the input compound in symbol
    def Naming_Compound_From_Symbol(self, compound):
        self.element_list.clear();
        self.compound_list.clear();
        self.chemical_name = "";
        self.element_and_compound.clear();
        # Clearing the self.name_list every time
        self.element_name_list.clear()
        self.element_in_chemical_name_list.clear()
        self.ionic_dictionary_list.clear();
        self.charge_list.clear();
        self.compound_name_list.clear();
        self.type_list.clear();
        self.chemical_compound = "";
        self.compound_type = None;
        self.Element_and_Compound_Key_To_Atomic_Number_Dictionary = {};
        self.Molar_mass = 0;
        self.compound_symbol = compound
        self.checking_input = 0;
        self.molecular_key_as_element_value_as_charge = {}

        # getting the name of the element from the database
        ''' Separating the input compound into element_and_compound with atomic numbers'''
        while len(compound) > 0:
            self.checking_input += 1;
            if self.checking_input > 10:
                return None;
            else:
                pass
            # Trying to test if there is two polyatomic compound in the compound name:
            if len(compound) == len(self.compound_symbol):
                for checking_index in range(0, len(compound)):
                    if len(compound) - checking_index == 1:
                        break;
                    elif compound[checking_index].isdigit() and not compound[checking_index + 1].isdigit():
                        compound_split_check_1 = compound[:checking_index + 1];
                        if compound_split_check_1 == "NH4":
                            self.element_and_compound.append(compound_split_check_1);
                            compound = compound[checking_index + 1:]
                            break;
                        break;
                    else:
                        pass
            # Adding special case to the naming list
            for compound_exception in self.exception_compound_list:
                if compound == compound_exception:
                    self.element_and_compound.append(compound);
                    compound = compound[len(compound):]
                    break;
                else:
                    pass

            if len(compound) != 0:
                for index in range(0, 1):
                    # Setting if condition statement to separate all the element in the compound symbol
                    if compound[index].isupper() and len(compound) == 1:
                        self.element_and_compound.append(compound[index])
                        compound = []
                    elif compound[index].isupper() and len(compound) == 2:
                        if compound[index + 1].isupper():
                            self.element_and_compound.append(compound[index])
                            compound = compound[index + 1:]
                        elif compound[index + 1].isdigit():
                            self.element_and_compound.append(compound[:index + 2])
                            compound = compound[index + 2:]
                        elif compound[index + 1].islower():
                            self.element_and_compound.append(compound[:index + 2])
                            compound = compound[index + 2:]

                    elif compound[index].isupper() and compound[index + 1].isupper() and len(self.compound_symbol) != len(
                            compound):
                        if compound[index + 1].isupper() and compound[index + 2].isdigit():
                            self.element_and_compound.append(compound[:index + 3]);
                            compound = compound[index + 3:]
                        elif compound[index + 1].isupper() and compound[index + 2].isupper() and compound[
                            index + 3].isdigit():
                            self.element_and_compound.append(compound[:index + 4]);
                            compound = compound[index + 4:]
                        elif compound[index + 1].isupper() and compound[index + 2].isupper():
                            self.element_and_compound.append(compound[:index + 3]);
                            compound = compound[index + 3:]

                    elif compound[index] == "(":
                        for i in range(0, len(compound)):
                            if compound[i].isdigit() and compound[i - 1] == ")":
                                self.element_and_compound.append(compound[:i + 1])
                                compound = compound[i + 1:]
                                break;

                    elif compound[index].isupper():
                        if compound[index + 1].islower() and not compound[index + 2].isdigit():
                            self.element_and_compound.append(compound[:index + 2]);
                            compound = compound[index + 2:];
                        elif compound[index + 1].isupper():
                            self.element_and_compound.append(compound[index])
                            compound = compound[index + 1:]
                        elif compound[index + 1].islower() and compound[index + 2].isdigit():
                            self.element_and_compound.append(compound[:index + 3]);
                            compound = compound[index + 3:];
                        elif compound[index + 1].isdigit():
                            self.element_and_compound.append(compound[:index + 2])
                            compound = compound[index + 2:]

                    elif len(compound) == 1 and compound[index].isdigit():
                        compound = self.element_and_compound.pop() + compound[index]
                        self.element_and_compound.append(compound)
                        compound = []


        #print(self.element_and_compound)

        '''Assigning compound to compound_list, element to element_list without atomic numbers'''
        for index in range(0, len(self.element_and_compound)):
            if len(self.element_and_compound[index]) > 3:
                for element_index in range(0, len(self.element_and_compound[index])):
                    if self.element_and_compound[index][element_index] == "(":
                        for element_index in range(0, len(self.element_and_compound[index])):
                            if self.element_and_compound[index][element_index] == ")":
                                self.compound_list.append(self.element_and_compound[index][1:element_index])
                                self.create_key_value(key = self.element_and_compound[index][1:element_index], value = int(self.element_and_compound[index][element_index + 1:]),dictionary = self.Element_and_Compound_Key_To_Atomic_Number_Dictionary);
                                compound_order = index
                                break;
                            else:
                                pass
                        break;
                    elif self.element_and_compound[index][element_index + 1].islower() and \
                            self.element_and_compound[index][element_index + 2].isdigit() and \
                            self.element_and_compound[index][element_index + 3].isdigit():
                        self.element_list.append(self.element_and_compound[index][:element_index + 2])
                        self.create_key_value(key=self.element_and_compound[index][:element_index + 2],
                                              value= int(self.element_and_compound[index][element_index + 2:]),
                                              dictionary=self.Element_and_Compound_Key_To_Atomic_Number_Dictionary);
                        element_order = index
                        break;
                    else:
                        self.compound_list.append(self.element_and_compound[index][element_index:])
                        self.create_key_value(key=self.element_and_compound[index][element_index:],
                                              value= 1,
                                              dictionary=self.Element_and_Compound_Key_To_Atomic_Number_Dictionary);
                        compound_order = index
                        break;

            elif 0 < len(self.element_and_compound[index]) <= 3:
                for element_index in range(0, len(self.element_and_compound[index])):
                    if self.element_and_compound[index][element_index].isupper() and len(
                            self.element_and_compound[index]) == 1:
                        self.element_list.append(self.element_and_compound[index][element_index])
                        self.create_key_value(key=self.element_and_compound[index][element_index],
                                              value=1,
                                              dictionary=self.Element_and_Compound_Key_To_Atomic_Number_Dictionary);
                        element_order = index
                        break;

                    elif self.element_and_compound[index][element_index + 1].isupper() and len(self.element_and_compound[index]) == 2:
                        self.compound_list.append(self.element_and_compound[index][:element_index + 2])
                        self.create_key_value(key=self.element_and_compound[index][:element_index + 2],
                                              value=1,
                                              dictionary=self.Element_and_Compound_Key_To_Atomic_Number_Dictionary);
                        compound_order = index
                        break;

                    elif self.element_and_compound[index][element_index + 1].isdigit() and len(self.element_and_compound[index]) == 2:
                        self.element_list.append(self.element_and_compound[index][:element_index + 1])
                        self.create_key_value(key=self.element_and_compound[index][:element_index + 1],
                                              value= int(self.element_and_compound[index][element_index + 1]),
                                              dictionary=self.Element_and_Compound_Key_To_Atomic_Number_Dictionary);
                        element_order = index
                        break;


                    elif self.element_and_compound[index][element_index + 1].islower() and len(self.element_and_compound[index]) == 2:
                        self.element_list.append(self.element_and_compound[index][:element_index + 2]);
                        self.create_key_value(key= self.element_and_compound[index][:element_index + 2],
                                              value= 1,
                                              dictionary= self.Element_and_Compound_Key_To_Atomic_Number_Dictionary);
                        element_order = index
                        break;

                    elif self.element_and_compound[index][element_index + 1].isdigit() and self.element_and_compound[index][element_index + 2].isdigit() and len(self.element_and_compound[index]) == 3:
                        self.element_list.append(self.element_and_compound[index][:element_index + 1])
                        self.create_key_value(key=self.element_and_compound[index][:element_index + 1],
                                              value= int(self.element_and_compound[index][element_index + 1:]),
                                              dictionary=self.Element_and_Compound_Key_To_Atomic_Number_Dictionary);
                        element_order = index
                        break;

                    elif self.element_and_compound[index][element_index + 1].islower() and self.element_and_compound[index][element_index + 2].isdigit() and len(self.element_and_compound[index]) == 3:
                        self.element_list.append(self.element_and_compound[index][:element_index + 2])
                        self.create_key_value(key=self.element_and_compound[index][:element_index + 2],
                                              value= int(self.element_and_compound[index][element_index + 2]),
                                              dictionary=self.Element_and_Compound_Key_To_Atomic_Number_Dictionary);
                        element_order = index
                        break;

                    elif self.element_and_compound[index][element_index + 1].isupper() and self.element_and_compound[index][element_index + 2].isdigit() and len(self.element_and_compound[index]) == 3:
                        self.compound_list.append(self.element_and_compound[index]);
                        self.create_key_value(key=self.element_and_compound[index],
                                              value= 1,
                                              dictionary=self.Element_and_Compound_Key_To_Atomic_Number_Dictionary);
                        compound_order = index
                        break;

                    elif self.element_and_compound[index][element_index + 1].islower() and self.element_and_compound[index][element_index + 2].isupper() and len(self.element_and_compound[index]) == 3:
                        self.compound_list.append(self.element_and_compound[index]);
                        self.create_key_value(key=self.element_and_compound[index],
                                              value= 1,
                                              dictionary=self.Element_and_Compound_Key_To_Atomic_Number_Dictionary);
                        compound_order = index
                        break;

        #print(self.element_list, self.compound_list, self.Element_and_Compound_Key_To_Atomic_Number_Dictionary);

        '''Assigning the type for element and compound'''
        # Reading compound type
        if len(self.compound_list) == 0:
            for element in self.element_list:
                self.type_list.append(self.database.get_type_sym_element(element))
        elif len(self.element_list) == 0:
            for compound in self.compound_list:
                self.type_list.append("Polyatomic Ion");
        elif len(self.element_list) != 0 and len(self.compound_list) != 0:
            # Adding type of element in self.type_list
            if element_order > compound_order:
                # Adding the polyatomic
                self.type_list.append("Polyatomic Ion")
                for element in self.element_list:
                    self.type_list.append(self.database.get_type_sym_element(element))
            else:
                for element in self.element_list:
                    self.type_list.append(self.database.get_type_sym_element(element))
                self.type_list.append("Polyatomic Ion")



        ''' Determining the chemical type'''
        for index in range(0, len(self.type_list)):
            if self.type_list[index] == "Metals":
                self.compound_type = "Ionic Compound";
                break;
            elif self.type_list[index] == "Polyatomic Ion":
                self.compound_type = "Ionic Compound";
                break;
            else:
                self.compound_type = "Molecular Compound";

        #print(self.compound_type)

        '''Using the prefix function to determine the molecular name'''
        # Naming the compound
        if self.compound_type == "Molecular Compound":
            # Getting name from all the elements in the list
            for element in self.element_list:
                self.element_name_list.append(self.database.get_name_sym_element(element));

            if len(self.element_and_compound) == 1:
                #print(self.element_and_compound)
                if len(self.element_and_compound[0]) == 1:
                    self.element_in_chemical_name_list.append(
                        self.determine_molecular_prefix(digit= 1, name=self.element_name_list[0], order=0));
                    self.determning_the_molecular_dictionary_charge(digit= 0, symbol=self.element_and_compound[0], order=None);

                elif len(self.element_and_compound[0]) == 2 and self.element_and_compound[0][1].islower():
                    self.element_in_chemical_name_list.append(
                        self.determine_molecular_prefix(digit = 1, name=self.element_name_list[0], order=0));
                    self.determning_the_molecular_dictionary_charge(digit=0, symbol=self.element_and_compound[0],
                                                                    order= None);

                elif len(self.element_and_compound[0]) == 2 and self.element_and_compound[0][1].isdigit():
                    self.element_in_chemical_name_list.append(
                        self.determine_molecular_prefix(digit=int(self.element_and_compound[0][1]),
                                                        name=self.element_name_list[0], order= 0));
                    self.determning_the_molecular_dictionary_charge(digit= 0, symbol=self.element_and_compound[0],
                                                                    order=None);

                elif len(self.element_and_compound[0]) == 3 and self.element_and_compound[0][1].islower() and \
                        self.element_and_compound[0][2].isdigit():
                    self.element_in_chemical_name_list.append(
                        self.determine_molecular_prefix(digit=int(self.element_and_compound[0][2]),
                                                        name=self.element_name_list[0], order=0));

                    self.determning_the_molecular_dictionary_charge(digit=0,
                                                                    symbol=self.element_and_compound[0],
                                                                    order= None);
            else:
                # Accessing to the element and compound list to determine the prefix name ot the element
                for index in range(0, len(self.element_and_compound)):
                    if len(self.element_and_compound[index]) == 1:
                        self.element_in_chemical_name_list.append(
                            self.determine_molecular_prefix(digit=1, name=self.element_name_list[index], order=index));
                        self.determning_the_molecular_dictionary_charge(digit=1, symbol=self.element_and_compound[index], order=index);

                    elif len(self.element_and_compound[index]) == 2 and self.element_and_compound[index][1].islower():
                        self.element_in_chemical_name_list.append(
                            self.determine_molecular_prefix(digit = 1, name=self.element_name_list[index], order=index));
                        self.determning_the_molecular_dictionary_charge(digit=1, symbol=self.element_and_compound[index],
                                                                        order=index);

                    elif len(self.element_and_compound[index]) == 2 and self.element_and_compound[index][1].isdigit():
                        self.element_in_chemical_name_list.append(
                            self.determine_molecular_prefix(digit=int(self.element_and_compound[index][1]),
                                                            name=self.element_name_list[index], order=index));
                        self.determning_the_molecular_dictionary_charge(digit=int(self.element_and_compound[index][1]), symbol=self.element_and_compound[index],
                                                                        order=index);
                    elif len(self.element_and_compound[index]) == 3 and self.element_and_compound[index][1].islower() and \
                            self.element_and_compound[index][2].isdigit():
                        self.element_in_chemical_name_list.append(
                            self.determine_molecular_prefix(digit=int(self.element_and_compound[index][2]),
                                                            name=self.element_name_list[index], order=index));

                        self.determning_the_molecular_dictionary_charge(digit=int(self.element_and_compound[index][2]),
                                                                        symbol=self.element_and_compound[index],
                                                                        order=index);

                    elif len(self.element_and_compound[index]) == 3 and self.element_and_compound[index][1].isdigit() and \
                            self.element_and_compound[index][2].isdigit():
                        digit = self.element_and_compound[index][1] + self.element_and_compound[index][2]
                        self.element_in_chemical_name_list.append(
                            self.determine_molecular_prefix(digit=int(digit), name=self.element_name_list[index],
                                                            order=index));
                        self.determning_the_molecular_dictionary_charge(digit=int(digit),
                                                                        symbol=self.element_and_compound[index],
                                                                        order=index);
                    elif len(self.element_and_compound[index]) == 4 and self.element_and_compound[index][1].islower() and \
                            self.element_and_compound[index][2].isdigit() and self.element_and_compound[index][3].isdigit():
                        digit = self.element_and_compound[index][2] + self.element_and_compound[index][3]
                        self.element_in_chemical_name_list.append(
                            self.determine_molecular_prefix(digit=int(digit), name=self.element_name_list[index],
                                                            order=index));
                        self.determning_the_molecular_dictionary_charge(digit=int(digit),
                                                                        symbol=self.element_and_compound[index],
                                                                        order=index);
            #print(self.charge_list,self.element_list)
            # Combining individual name together
            for element_in_compound_name in self.element_in_chemical_name_list:
                self.chemical_name += element_in_compound_name + " "

            #print(self.chemical_name)
            return self.chemical_name

        # Using the prefix function to determine the ionic compound name
        elif self.compound_type == "Ionic Compound":
            if len(self.element_list) != 0 and len(self.compound_list) == 0:
                # Getting the name of the element or compound and store to the name_list
                for element in self.element_list:
                    self.element_name_list.append(self.database.get_name_sym_element(element))
                    # Getting the charge of the element or compound and store it to the charge_list
                    self.charge_list.append(self.database.get_charge_sym_element(element))
            elif len(self.element_list) == 0 and len(self.compound_list) != 0:
                for compound_symbol in self.compound_list:
                    self.compound_name_list.append(self.database.get_name_sym_polyatomic(compound_symbol));

                    self.charge_list.append(self.database.get_charge_sym_polyatomic(compound_symbol));

            elif len(self.element_list) != 0 and len(self.compound_list) != 0:
                if element_order < compound_order:
                    for element in self.element_list:
                        self.element_name_list.append(self.database.get_name_sym_element(element))
                        # Getting the charge of the element or compound and store it to the charge_list
                        self.charge_list.append(self.database.get_charge_sym_element(element))
                    for compound in self.compound_list:
                        self.compound_name_list.append(self.database.get_name_sym_polyatomic(compound));

                        self.charge_list.append(self.database.get_charge_sym_polyatomic(compound));
                elif element_order > compound_order:
                    for compound in self.compound_list:
                        self.compound_name_list.append(self.database.get_name_sym_polyatomic(compound));

                        self.charge_list.append(self.database.get_charge_sym_polyatomic(compound));
                    for element in self.element_list:
                        self.element_name_list.append(self.database.get_name_sym_element(element))
                        # Getting the charge of the element or compound and store it to the charge_list
                        self.charge_list.append(self.database.get_charge_sym_element(element))
                else:
                    print("Something is wrong")


            # Reverse the charge list
            self.charge_list.reverse()
            #print(self.element_list)
            # Determining the atomic mass of the element and compound
            symbol_atomic_number = 0;
            # Separating the digit from the element_and_compound list
            # If there is no Polyatomic compound in the Compound name
            if len(self.compound_list) == 0:
                #print(self.element_and_compound)
                for element_compound_index in range(0, len(self.element_and_compound)):
                    if len(self.element_list) == 1:
                        if len(self.charge_list[0]) == 1:
                            self.ionic_dictionary_list.append(
                                dict(name=self.element_name_list[0], charge= str(0), length=
                                len(self.charge_list[0]), type= self.type_list[0]));
                            break;
                        else:
                            for charge in self.charge_list[0]:
                                if charge[0] == "+":
                                    self.ionic_dictionary_list.append(
                                        dict(name=self.element_name_list[0], charge= str(0), length=
                                        len(self.charge_list[0]), type=self.type_list[0]));
                                    break;
                                else:
                                    pass
                        break;
                    else:
                        pass
                    #print("The name of the element is " + self.element_and_compound[element_compound_index])
                    for index in range(0, len(self.element_and_compound[index])):
                        # Setting condition through certain senario to let the computer knows what to do with each element and its atomic numbers
                        if len(self.element_and_compound[element_compound_index]) == 1 and element_compound_index != 0:
                            # Determining its corresponding charges
                            for charge in self.charge_list[element_compound_index]:
                                if charge[0] == "+" and int(charge[1]) == 1:
                                    self.ionic_dictionary_list.append(
                                        dict(name=self.element_name_list[element_compound_index - 1], charge=charge,
                                             length=len(self.charge_list[element_compound_index]), type = self.type_list[element_index - 1]));
                                    charge_reduction_signal = False;
                                    break;
                                else:
                                    charge_reduction_signal = True;

                            if charge_reduction_signal == True:
                                for charge_larger in self.charge_list[element_compound_index]:
                                    for charge_lower in self.charge_list[element_compound_index - 1]:
                                        if charge_larger[0] == "+" and charge_lower[0] == "-" and charge_larger[1] == charge_lower[1]:
                                            self.ionic_dictionary_list.append(
                                                dict(name=self.element_name_list[element_compound_index - 1],
                                                     charge=charge,
                                                     length=len(self.charge_list[element_compound_index]),
                                                     type=self.type_list[element_index - 1]));
                                            break;
                                        else:
                                            pass
                            else:
                                pass

                            break;

                        elif len(self.element_and_compound[element_compound_index]) == 1 and element_compound_index == 0:
                            # Determining its corresponding charges
                            for charge in self.charge_list[element_compound_index]:
                                if charge[0] == "-" and int(charge[1]) == 1:
                                    self.ionic_dictionary_list.append(
                                        dict(name=self.element_name_list[element_compound_index + 1], charge=charge,
                                             length=len(self.charge_list[element_compound_index]),
                                             type=self.type_list[element_index + 1]));
                                    charge_reduction_signal = False;
                                    break;
                                else:
                                    charge_reduction_signal = True;

                            if charge_reduction_signal == True:
                                for charge_larger in self.charge_list[element_compound_index]:
                                    for charge_lower in self.charge_list[element_compound_index - 1]:
                                        if charge_larger[0] == "-" and charge_lower[0] == "+" and charge_larger[1] == \
                                                charge_lower[1]:
                                            self.ionic_dictionary_list.append(
                                                dict(name=self.element_name_list[element_compound_index + 1],
                                                     charge=charge,
                                                     length=len(self.charge_list[element_compound_index]),
                                                     type=self.type_list[element_index + 1]));
                                            break;
                                        else:
                                            pass
                            else:
                                pass

                            break;

                        elif self.element_and_compound[element_compound_index][index].isupper() and \
                                self.element_and_compound[element_compound_index][
                                    index + 1].islower() and element_compound_index != 0 and len(
                                self.element_and_compound[element_compound_index]) == 2:
                            # Determining its corresponding charges
                            for charge in self.charge_list[element_compound_index]:
                                if charge[0] == "+" and int(charge[1]) == 1:
                                    self.ionic_dictionary_list.append(
                                        dict(name=self.element_name_list[element_compound_index - 1], charge=charge,
                                             length=len(self.charge_list[element_compound_index]), type = self.type_list[element_index - 1]));

                                    charge_reduction_signal = False;
                                    break;
                                else:
                                    charge_reduction_signal = True;
                                    pass

                            if charge_reduction_signal == True:
                                for charge_larger in self.charge_list[element_compound_index]:
                                    for charge_lower in self.charge_list[element_compound_index - 1]:
                                        if charge_larger[0] == "+" and charge_lower[0] == "-" and charge_larger[1] == charge_lower[1]:
                                            self.ionic_dictionary_list.append(
                                                dict(name=self.element_name_list[element_compound_index - 1],
                                                     charge=charge,
                                                     length=len(self.charge_list[element_compound_index]),
                                                     type=self.type_list[element_index - 1]));
                                            break;
                                        else:
                                            pass
                            else:
                                pass
                            break;

                        elif self.element_and_compound[element_compound_index][index].isupper() and \
                                self.element_and_compound[element_compound_index][
                                    index + 1].isdigit() and element_compound_index != 0 and len(
                                self.element_and_compound[element_compound_index]) == 2:
                            # Determining its corresponding charges
                            for charge in self.charge_list[element_compound_index]:
                                if charge[0] == "+" and int(charge[1]) == int(
                                        self.element_and_compound[element_compound_index][index + 1]):
                                    self.ionic_dictionary_list.append(
                                        dict(name=self.element_name_list[element_compound_index - 1], charge=charge,
                                             length=len(self.charge_list[element_compound_index]), type = self.type_list[element_index - 1]));
                                    charge_reduction_signal = False;
                                    break;
                                else:
                                    charge_reduction_signal = True;

                            if charge_reduction_signal == True:
                                for charge_larger in self.charge_list[element_compound_index]:
                                    for charge_lower in self.charge_list[element_compound_index - 1]:
                                        if charge_larger[0] == "+" and charge_lower[0] == "-" and charge_larger[1] == charge_lower[1]:
                                            self.ionic_dictionary_list.append(
                                                dict(name=self.element_name_list[element_compound_index - 1],
                                                     charge=charge,
                                                     length=len(self.charge_list[element_compound_index]),
                                                     type=self.type_list[element_index - 1]));
                                            break;
                                        else:
                                            pass
                            else:
                                pass

                            break;

                        elif self.element_and_compound[element_compound_index][index].isupper() and \
                                self.element_and_compound[element_compound_index][
                                    index + 1].islower() and element_compound_index == 0 and len(
                                self.element_and_compound[element_compound_index]) == 2:
                            # Determining its corresponding charges
                            for charge in self.charge_list[element_compound_index]:
                                if charge[0] == "-" and int(charge[1]) == 1:
                                    self.ionic_dictionary_list.append(
                                        dict(name=self.element_name_list[element_compound_index + 1], charge=charge,
                                             length=len(self.charge_list[element_compound_index]), type = self.type_list[element_index + 1]));
                                    charge_reduction_signal = False;
                                    break;
                                else:
                                    charge_reduction_signal = True;

                            if charge_reduction_signal == True:
                                for charge_larger in self.charge_list[element_compound_index]:
                                    for charge_lower in self.charge_list[element_compound_index + 1]:
                                        if charge_larger[0] == "-" and charge_lower[0] == "+" and charge_larger[1] == charge_lower[1]:
                                            self.ionic_dictionary_list.append(
                                                dict(name=self.element_name_list[element_compound_index + 1],
                                                     charge=charge,
                                                     length=len(self.charge_list[element_compound_index]),
                                                     type=self.type_list[element_index + 1]));
                                            break;
                                        else:
                                            pass
                            else:
                                pass
                            break;
                        elif self.element_and_compound[element_compound_index][index].isupper() and \
                                self.element_and_compound[element_compound_index][
                                    index + 1].isdigit() and element_compound_index == 0 and len(
                                self.element_and_compound[element_compound_index]) == 2:
                            # Determining its corresponding charges
                            for charge in self.charge_list[element_compound_index]:
                                if charge[0] == "-" and int(charge[1]) == int(
                                        self.element_and_compound[element_compound_index][index + 1]):
                                    self.ionic_dictionary_list.append(
                                        dict(name=self.element_name_list[element_compound_index + 1], charge=charge,
                                             length=len(self.charge_list[element_compound_index]), type = self.type_list[element_index + 1]));
                                    charge_reduction_signal = False;
                                    break;
                                else:
                                    charge_reduction_signal = True;
                            if charge_reduction_signal == True:
                                for charge_larger in self.charge_list[element_compound_index]:
                                    for charge_lower in self.charge_list[element_compound_index + 1]:
                                        if charge_larger[0] == "-" and charge_lower[0] == "+" and charge_larger[1] == charge_lower[1]:
                                            self.ionic_dictionary_list.append(
                                                dict(name=self.element_name_list[element_compound_index + 1],
                                                     charge=charge,
                                                     length=len(self.charge_list[element_compound_index]),
                                                     type=self.type_list[element_index + 1]));
                                            break;
                                        else:
                                            pass
                            else:
                                pass
                            break;

                        elif self.element_and_compound[element_compound_index][index].isupper() and \
                                self.element_and_compound[element_compound_index][index + 1].islower() and \
                                self.element_and_compound[element_compound_index][
                                    index + 2].isdigit() and element_compound_index != 0:
                            # Determining its corresponding charges
                            for charge in self.charge_list[element_compound_index]:
                                if charge[0] == "+" and int(charge[1]) == int(
                                        self.element_and_compound[element_compound_index][index + 2]):
                                    self.ionic_dictionary_list.append(
                                        dict(name=self.element_name_list[element_compound_index - 1], charge=charge,
                                             length=len(self.charge_list[element_compound_index]), type = self.type_list[element_index - 1]));
                                    charge_reduction_signal = False;
                                    break;
                                else:
                                    charge_reduction_signal = True;

                            if charge_reduction_signal == True:
                                for charge_larger in self.charge_list[element_compound_index]:
                                    for charge_lower in self.charge_list[element_compound_index - 1]:
                                        if charge_larger[0] == "+" and charge_lower[0] == "-" and charge_larger[1] == charge_lower[1]:
                                            self.ionic_dictionary_list.append(
                                                dict(name=self.element_name_list[element_compound_index - 1],
                                                     charge=charge,
                                                     length=len(self.charge_list[element_compound_index]),
                                                     type=self.type_list[element_index - 1]));
                                            break;
                                        else:
                                            pass
                            else:
                                pass

                            break;

                        elif self.element_and_compound[element_compound_index][index].isupper() and \
                                self.element_and_compound[element_compound_index][index + 1].islower() and \
                                self.element_and_compound[element_compound_index][
                                    index + 2].isdigit() and element_compound_index == 0:
                            for charge in self.charge_list[element_compound_index]:
                                if charge[0] == "-" and int(charge[1]) == int(
                                        self.element_and_compound[element_compound_index][index + 2]):
                                    self.ionic_dictionary_list.append(
                                        dict(name=self.element_name_list[element_compound_index + 1], charge=charge,
                                             length=len(self.charge_list[element_compound_index]), type = self.type_list[element_index + 1]));
                                    charge_reduction_signal = False;
                                    break;
                                else:
                                    charge_reduction_signal = True;
                                    pass

                            if charge_reduction_signal == True:
                                for charge_larger in self.charge_list[element_compound_index]:
                                    for charge_lower in self.charge_list[element_compound_index + 1]:
                                        if charge_larger[0] == "-" and charge_lower[0] == "+" and charge_larger[1] == charge_lower[1]:
                                            self.ionic_dictionary_list.append(
                                                dict(name=self.element_name_list[element_compound_index + 1],
                                                     charge=charge,
                                                     length=len(self.charge_list[element_compound_index]),
                                                     type=self.type_list[element_index + 1]));
                                            break;
                                        else:
                                            pass
                            else:
                                pass

                            break;

            # If there is no element in element_list
            elif len(self.element_list) == 0 and len(self.compound_list ) != 0:
                for element_index in range(0, len(self.element_and_compound)):
                    if len(self.compound_list) == 1:
                        if len(self.charge_list) == 1:
                            self.ionic_dictionary_list.append(
                                dict(name=self.compound_name_list[0], charge=self.charge_list[0][0], length=
                                len(self.charge_list[0]), type="Polyatomic Ion"));
                        else:
                            for charge[0] in self.charge_list:
                                if charge[0] == "+" and charge[1] == 1:
                                    self.ionic_dictionary_list.append(
                                        dict(name=self.compound_name_list[0], charge= charge, length=
                                        len(self.charge_list[0]), type="Polyatomic Ion"));
                                    break;
                                else:
                                    pass
                        break;
                    else:
                        pass
                    for compound in self.compound_list:
                        if self.element_and_compound[element_index] == compound and element_index == 0:
                            for charge in self.charge_list[element_index]:
                                if charge[0] == "-" and int(charge[1]) == 1:
                                    self.ionic_dictionary_list.append(
                                        dict(name=self.compound_name_list[element_index + 1], charge=charge, length=
                                        len(self.charge_list[element_index + 1]), type="Polyatomic Ion"));
                                    charge_reduction_signal = False;
                                    break;
                                else:
                                    charge_reduction_signal = True;

                            if charge_reduction_signal == True:
                                for charge_larger in self.charge_list[element_index]:
                                    for charge_lower in self.charge_list[element_index + 1]:
                                        if charge_larger[0] == "-" and charge_lower[0] == "+" and charge_larger[1] == \
                                                charge_lower[1]:
                                            self.ionic_dictionary_list.append(
                                                dict(name=self.compound_name_list[element_index + 1],
                                                     charge=charge,
                                                     length=len(self.charge_list[element_index + 1 ]),
                                                     type="Polyatomic Ion"));
                                            break;
                                        else:
                                            pass
                            else:
                                pass

                        elif self.element_and_compound[element_index] != compound and element_index == 0 and self.element_and_compound[0] == "(":
                            for compound_index_to_digit in range(0, len(self.element_and_compound[element_index])):
                                if self.element_and_compound[element_index][compound_index_to_digit] == ")":
                                    compound_polyatomic_atom_number = int(self.element_and_compound[element_index][compound_index_to_digit + 1]);
                                    break;
                                else:
                                    pass
                            for charge in self.charge_list[element_index]:
                                if charge[0] == "-" and  int(charge[1]) == compound_polyatomic_atom_number:
                                    self.ionic_dictionary_list.append(dict(name =self.compound_name_list[element_index + 1], charge = charge, length = len(self.charge_list[element_index]), type = self.type_list[element_index -1]));
                                    break;
                                else:
                                    pass

                        elif self.element_and_compound[element_index] != compound and element_index != 0 and self.element_and_compound[0] == "(":
                            for compound_index_to_digit in range(0, len(self.element_and_compound[element_index])):
                                if self.element_and_compound[element_index][compound_index_to_digit] == ")":
                                    compound_polyatomic_atom_number = int(self.element_and_compound[element_index][compound_index_to_digit + 1]);
                                    break;
                                else:
                                    pass
                            for charge in self.charge_list[element_index]:
                                if charge[0] == "+" and  int(charge[1]) == compound_polyatomic_atom_number:
                                    self.ionic_dictionary_list.append(dict(name =self.compound_name_list[element_index - 1], charge = charge, length = len(self.charge_list[element_index]), type = self.type_list[element_index - 1]));
                                    break;
                                else:
                                    pass

                        elif self.element_and_compound[element_index] == compound and element_index != 0:
                            for charge in self.charge_list[element_index]:
                                if charge[0] == "+" and int(charge[1]) == 1:
                                    self.ionic_dictionary_list.append(
                                        dict(name=self.compound_name_list[element_index - 1], charge=charge, length=
                                        len(self.charge_list[element_index - 1]), type="Polyatomic Ion"));
                                    charge_reduction_signal = False;
                                    break;
                                else:
                                    charge_reduction_signal = True;

                            if charge_reduction_signal == True:
                                for charge_larger in self.charge_list[element_index]:
                                    for charge_lower in self.charge_list[element_index - 1]:
                                        if charge_larger[0] == "+" and charge_lower[0] == "-" and charge_larger[1] == \
                                                charge_lower[1]:
                                            self.ionic_dictionary_list.append(
                                                dict(name=self.compound_name_list[element_index - 1],
                                                     charge=charge,
                                                     length=len(self.charge_list[element_index - 1 ]),
                                                     type="Polyatomic Ion"));
                                            break;
                                        else:
                                            pass
                            else:
                                pass

            # If there is a polyatomic in the chemical symbol
            elif len(self.element_list) != 0 and len(self.compound_list) != 0:
                for element_index in range(0, len(self.element_and_compound)):
                    ''' Finding the compound in element_and_compound '''
                    for compound in self.compound_list:
                        #print("The element name is " + self.element_and_compound[element_index])
                        if self.element_and_compound[element_index] == compound and element_index != 0:
                            for charge in self.charge_list[element_index]:
                                if charge[0] == "+" and int(charge[1]) == 1:
                                    self.ionic_dictionary_list.append(dict(name = self.element_name_list[element_index - 1], charge = charge, length = len(self.charge_list[element_index]), type = self.type_list[element_index]));
                                    charge_reduction_signal = False;
                                    break;
                                else:
                                    charge_reduction_signal = True;
                                    pass
                            if charge_reduction_signal == True:
                                for charge_larger in self.charge_list[element_index]:
                                    for charge_lower in self.charge_list[element_index - 1]:
                                        if charge_larger[0] == "+" and charge_lower[0] == "-" and charge_larger[1] == charge_lower[1]:
                                            self.ionic_dictionary_list.append(
                                                dict(name=self.element_name_list[element_index - 1],
                                                     charge=charge,
                                                     length=len(self.charge_list[element_index]),
                                                     type=self.type_list[element_index - 1]));
                                            break;
                                        else:
                                            pass
                            else:
                                pass

                        elif self.element_and_compound[element_index] == compound and element_index == 0:
                            for charge in self.charge_list[element_index]:
                                if charge[0] == "-" and int(charge[1]) == 1:
                                    self.ionic_dictionary_list.append(dict(name = self.element_name_list[element_index],charge = charge,
                                          length = len(self.charge_list[element_index + 1]), type = self.type_list[element_index]));
                                    charge_reduction_signal = False;
                                    break;
                                else:
                                    charge_reduction_signal = True;
                                    pass

                            if charge_reduction_signal == True:
                                for charge_larger in self.charge_list[element_index]:
                                    for charge_lower in self.charge_list[element_index + 1]:
                                        if charge_larger[0] == "-" and charge_lower[0] == "+" and charge_larger[1] == charge_lower[1]:
                                            self.ionic_dictionary_list.append(
                                                dict(name=self.element_name_list[element_index],
                                                     charge=charge,
                                                     length=len(self.charge_list[element_index]),
                                                     type=self.type_list[element_index]));
                                            break;
                                        else:
                                            pass
                            else:
                                pass

                        elif self.element_and_compound[element_index] != compound and element_index == 0 and self.type_list[element_index] == "Polyatomic Ion":
                            for compound_index_to_digit in range(0, len(self.element_and_compound[element_index])):
                                if self.element_and_compound[element_index][compound_index_to_digit] == ")":
                                    compound_polyatomic_atom_number = int(self.element_and_compound[element_index][compound_index_to_digit + 1]);
                                    break;
                                else:
                                    pass

                            for charge in self.charge_list[element_index]:
                                if charge[0] == "-" and  int(charge[1]) == compound_polyatomic_atom_number:
                                    self.ionic_dictionary_list.append(dict(name =self.element_name_list[element_index], charge = charge, length = len(self.charge_list[element_index]), type = self.type_list[element_index + 1]));
                                    charge_reduction_signal = False;
                                    break;
                                else:
                                    charge_reduction_signal = True;
                                    pass

                            if charge_reduction_signal == True:
                                for charge_larger in self.charge_list[element_index]:
                                    for charge_lower in self.charge_list[element_index + 1]:
                                        if charge_larger[0] == "-" and charge_lower[0] == "+" and charge_larger[1] == charge_lower[1]:
                                            self.ionic_dictionary_list.append(
                                                dict(name=self.element_name_list[element_index],
                                                     charge=charge,
                                                     length=len(self.charge_list[element_index]),
                                                     type=self.type_list[element_index]));
                                            break;
                                        else:
                                            pass
                            else:
                                pass

                        elif self.element_and_compound[element_index] != compound and element_index != 0:
                            try:
                                for compound_index_to_digit in range(0, len(self.element_and_compound[element_index])):
                                    if self.element_and_compound[element_index][compound_index_to_digit] == ")":
                                        compound_polyatomic_atom_number = int(self.element_and_compound[element_index][compound_index_to_digit + 1]);
                                        break;
                                    else:
                                        pass
                                for charge in self.charge_list[element_index]:
                                    if charge[0] == "+" and  int(charge[1]) == compound_polyatomic_atom_number:
                                        self.ionic_dictionary_list.append(dict(name =self.element_name_list[element_index - 1], charge = charge, length = len(self.charge_list[element_index]), type = self.type_list[element_index -1]));
                                        charge_reduction_signal = False;
                                        break;
                                    else:
                                        charge_reduction_signal = True;
                                        pass

                                if charge_reduction_signal == True:
                                    for charge_larger in self.charge_list[element_index]:
                                        for charge_lower in self.charge_list[element_index - 1]:
                                            if charge_larger[0] == "+" and charge_lower[0] == "-" and charge_larger[1] == charge_lower[1]:
                                                self.ionic_dictionary_list.append(
                                                    dict(name=self.element_name_list[element_index - 1],
                                                         charge=charge,
                                                         length=len(self.charge_list[element_index]),
                                                         type=self.type_list[element_index - 1]));
                                                break;
                                            else:
                                                pass
                                else:
                                    pass
                            except:
                                pass

                    for element in self.element_list:
                        if self.element_and_compound[element_index] == element and element_index == 0:
                            for charge in self.charge_list[element_index]:
                                if charge[0] == "-" and int(charge[1]) == 1:
                                    self.ionic_dictionary_list.append(dict(name = self.compound_name_list[element_index], charge = charge, length =
                                          len(self.charge_list[element_index]),type = "Polyatomic Ion"));
                                    charge_reduction_signal = False;
                                    break;
                                else:
                                    charge_reduction_signal = True;

                            if charge_reduction_signal == True:
                                for charge_larger in self.charge_list[element_index]:
                                    for charge_lower in self.charge_list[element_index + 1]:
                                        if charge_larger[0] == "-" and charge_lower[0] == "+" and charge_larger[1] == charge_lower[1]:
                                            self.ionic_dictionary_list.append(
                                                dict(name=self.compound_name_list[element_index],
                                                     charge=charge,
                                                     length=len(self.charge_list[element_index]),
                                                     type= "Polyatomic Ion"));
                                            break;
                                        else:
                                            pass
                            else:
                                pass

                        elif self.element_and_compound[element_index] == element and element_index != 0:
                            for charge in self.charge_list[element_index]:
                                if charge[0] == "+" and int(charge[1]) == 1:
                                    self.ionic_dictionary_list.append(
                                        dict(name=self.compound_name_list[element_index - 1], charge=charge, length=
                                        len(self.charge_list[element_index]), type="Polyatomic Ion"));
                                    charge_reduction_signal = False;
                                    break;
                                else:
                                    charge_reduction_signal = True;

                            if charge_reduction_signal == True:
                                for charge_larger in self.charge_list[element_index]:
                                    for charge_lower in self.charge_list[element_index - 1]:
                                        if charge_larger[0] == "+" and charge_lower[0] == "-" and charge_larger[1] == \
                                                charge_lower[1]:
                                            self.ionic_dictionary_list.append(
                                                dict(name=self.compound_name_list[element_index],
                                                     charge=charge,
                                                     length=len(self.charge_list[element_index]),
                                                     type="Polyatomic Ion"));
                                            break;
                                        else:
                                            pass
                            else:
                                pass

                        elif self.element_and_compound[element_index] != element and element_index == 0:
                            if len(self.element_and_compound[element_index]) - len(element) == 1 and self.database.get_type_name_element(self.element_and_compound[element_index]) is not None:
                                for charge in self.charge_list[element_index]:
                                    if charge[0] == "-" and int(charge[1]) == int(self.element_and_compound[element_index][len(self.element_and_compound[element_index])- 1]):
                                        self.ionic_dictionary_list.append(dict(name = self.compound_name_list[element_index],
                                              charge =charge,
                                              length = len(self.charge_list[element_index]),type = "Polyatomic Ion"));
                                        charge_reduction_signal = False;
                                        break;
                                    else:
                                        charge_reduction_signal= True;
                                        pass

                                if charge_reduction_signal == True:
                                    for charge_larger in self.charge_list[element_index]:
                                        for charge_lower in self.charge_list[element_index + 1]:
                                            if charge_larger[0] == "-" and charge_lower[0] == "+" and charge_larger[1] == charge_lower[1]:
                                                self.ionic_dictionary_list.append(
                                                    dict(name=self.compound_name_list[element_index],
                                                         charge=charge,
                                                         length=len(self.charge_list[element_index]),
                                                         type="Polyatomic Ion"));
                                                break;
                                            else:
                                                pass
                                else:
                                    pass

                            elif len(self.element_and_compound[element_index]) - len(element) == 2:
                                element_atomic_number = int(self.element_and_compound[element_index][len(self.element_and_compound[element_index])-2:]);
                                for charge in self.charge_list[element_index]:
                                    if charge[0] == "-" and int(charge[1]) == element_atomic_number:
                                        self.ionic_dictionary_list.append(dict(name = self.compound_name_list[element_index],
                                              charge =charge,
                                              length =len(self.charge_list[element_index]), type = "Polyatomic Ion"));
                                        break;
                                    else:
                                        pass

            #(self.element_and_compound)
            #print(self.ionic_dictionary_list)
            for dictionary_item in self.ionic_dictionary_list:
                self.element_in_chemical_name_list.append(self.determine_ionic_prefix(dictionary=dictionary_item));
            # Creating a function to assign name or each element or compound correctly
            #print(self.element_in_chemical_name_list)
            self.element_in_chemical_name_list.reverse();
            if len(self.element_in_chemical_name_list) != len(self.element_and_compound):
                return None;
            else:
                for element_in_compound_name in self.element_in_chemical_name_list:
                    self.chemical_name += element_in_compound_name + " "

                #print(self.chemical_name)
                return self.chemical_name

    # Determining the ionic compound prefix and suffix
    def determine_ionic_prefix(self, dictionary):
        index_list = [];
        name = dictionary['name'];
        charge = dictionary['charge'];
        if charge[0] == "-" and dictionary['type'] != "Polyatomic Ion":
            for name_index in range(0, len(dictionary['name'])):
                for vowels in self.vowels:
                    if name[name_index] == vowels and name_index != 0:
                        index_list.append(name_index);
                    else:
                        pass

            if len(index_list) != 0 and name == self.exception_element_prefix_list[0]:
                name = name[:index_list[1]];
                name = name + "ide";
            elif len(index_list) != 0 and name == self.exception_element_prefix_list[1]:
                name = name[:index_list[2]];
                name = name + "ide";
            elif len(index_list) != 0 and name == self.exception_element_prefix_list[2]:
                name = name[:index_list[1]];
                name = name + "ide";
            elif len(index_list) != 0 and name == self.exception_element_prefix_list[3]:
                name = name[:index_list[1]];
                name = name + "ide";
            elif len(index_list) != 0 and name == self.exception_element_prefix_list[4]:
                name = name[:index_list[1]];
                name = name + "ide";
            elif len(index_list) != 0 and name == self.exception_element_prefix_list[5]:
                name = name[:index_list[1]];
                name = name + "ide";
            elif len(index_list) != 0 and name == self.exception_element_prefix_list[6]:
                name = name[:index_list[2]];
                name = name + "ide";
            elif len(index_list) != 0 and name == self.exception_element_prefix_list[7]:
                name = name[:index_list[2]];
                name = name + "ide";
            elif len(index_list) != 0 and name == self.exception_element_prefix_list[8]:
                name = name[:index_list[1]];
                name = name + "ide";
            elif len(index_list) != 0 and name == self.exception_element_prefix_list[9]:
                name = name[:index_list[1]];
                name = name + "ide";
            elif len(index_list) != 0:
                name = name[:index_list[0]];
                name = name + "ide";

            return name;
        else:
            if dictionary['length'] == 1 or len(self.element_and_compound) == 1:
                return name;
            elif dictionary['length'] != 1 and len(self.element_and_compound) != 1:
                for number in self.Latin_Number.keys():
                    if charge[1] == number:
                        name = name + "({})".format(self.Latin_Number.get(number));
                        return name;
                    else:
                        pass

    # Determining the molecular compound prefix and suffix
    def determine_molecular_prefix(self, digit=1, name=None, order=0):
        index_list = []
        for name_index in range(0, len(name)):
            for vowels in self.vowels:
                if name[name_index] == vowels and order != 0 and name_index != 0:
                    index_list.append(name_index);
                else:
                    pass

        if len(index_list) != 0 and name == self.exception_element_prefix_list[0]:
            name = name[:index_list[2]];
            name = name + "ide";
        elif len(index_list) != 0 and name == self.exception_element_prefix_list[1]:
            name = name[:index_list[2]];
            name = name + "ide";
        elif len(index_list) != 0 and name == self.exception_element_prefix_list[2]:
            name = name[:index_list[1]];
            name = name + "ide";
        elif len(index_list) != 0 and name == self.exception_element_prefix_list[3]:
            name = name[:index_list[1]];
            name = name + "ide";
        elif len(index_list) != 0 and name == self.exception_element_prefix_list[4]:
            name = name[:index_list[1]];
            name = name + "ide";
        elif len(index_list) != 0 and name == self.exception_element_prefix_list[5]:
            name = name[:index_list[1]];
            name = name + "ide";
        elif len(index_list) != 0 and name == self.exception_element_prefix_list[6]:
            name = name[:index_list[2]];
            name = name + "ide";
        elif len(index_list) != 0 and name == self.exception_element_prefix_list[7]:
            name = name[:index_list[2]];
            name = name + "ide";
        elif len(index_list) != 0 and name == self.exception_element_prefix_list[8]:
            name = name[:index_list[1]];
            name = name + "ide";
        elif len(index_list) != 0 and name == self.exception_element_prefix_list[9]:
            name = name[:index_list[1]];
            name = name + "ide";
        elif len(index_list) != 0:
            name = name[:index_list[0]];
            name = name + "ide";

        if digit == 1 and order == 0:
            pass
        elif digit == 1:
            name = "Mono" + name.lower();
        elif digit == 2:
            name = "Di" + name.lower();
        elif digit == 3:
            name = "Tri" + name.lower();
        elif digit == 4:
            name = "Tetra" + name.lower();
        elif digit == 5:
            name = "Penta" + name.lower();
        elif digit == 6:
            name = "Hexa" + name.lower();
        elif digit == 7:
            name = "Hepta" + name.lower();
        elif digit == 8:
            name = "Octa" + name.lower();
        elif digit == 9:
            name = "Nona" + name.lower();
        elif digit == 10:
            name = "Deca" + name.lower();

        for name_index in range(0, len(name)):
            if name[name_index] == "a" and name[name_index + 1] == name[name_index]:
                name = name.replace("a", "", 1);
                break;
            elif name[name_index] == "a" and name[name_index + 1] == "o":
                name = name.replace("a", "", 1);
                break;
            elif name[name_index] == "o" and name[name_index + 1] == name[name_index]:
                name = name[:name_index] + name[name_index + 1:]
                break;

        return name

    # Naming symbol from compound
    def Naming_Symbol_From_Compound_Name(self, compound_name):
        self.element_list.clear();
        self.compound_list.clear();
        self.chemical_name = "";
        self.element_and_compound.clear();
        # Clearing the self.name_list every time
        self.element_name_list.clear()
        self.element_in_chemical_name_list.clear()
        self.ionic_dictionary_list.clear();
        self.charge_list.clear();
        self.compound_name_list.clear();
        self.type_list.clear();
        self.chemical_compound = "";
        self.compound_type = None
        self.Element_and_Compound_Key_To_Atomic_Number_Dictionary = {}
        self.Molar_mass = 0;

        #print(compound_name)

        # Checking if there is two letter in the string
        for character_index in range(0, len(compound_name)):
            if character_index == 0 and compound_name[character_index].isspace():
                return None;
                break;
            elif character_index != 0 and compound_name[character_index].isspace():
                compound_name = compound_name.split(" ");
                if len(compound_name) == 3:
                    compound_name[1] = compound_name[1] + " " + compound_name[2]
                    compound_name.pop(2)
                else:
                    pass
                break;
            elif len(compound_name) - 1 == character_index:
                return None;
            else:
                pass

        # Checking what type of the compound
        for element in compound_name:
            if self.database.get_type_name_element(element) == "Metals" or self.database.get_type_name_polyatomic(element) == "Polyatomic Ion":
                self.compound_type = "Ionic Compound";
                break;
            elif self.compound_type == "Ionic Compound":
                break;
            elif self.database.get_type_name_element(element) == "Nonmetals" and compound_name.index(element) == 1:
                self.compound_type = "Molecular Compound";
            elif self.database.get_type_name_element(element) == None:
                for character_index in range(0, len(element)):
                    if element[character_index] == "(":
                        self.compound_type = "Ionic Compound";
                        break;
                    else:
                        self.compound_type = "Molecular Compound";

        #print(self.compound_type);


        '''Getting the symbol of the compound'''
        # If the compound type is molecular compound
        if self.compound_type == "Molecular Compound":
            for element in compound_name:
                if compound_name.index(element) == 0:
                    self.element_list.append(self.Determining_Symbol_Atomic_Number_Molecular(name = element, order = 0));

                elif compound_name.index(element) != 0:
                    self.element_list.append(self.Determining_Symbol_Atomic_Number_Molecular(name = element, order = 1));

            #print(self.element_list)
            for symbol in self.element_list:
                if symbol == None:
                    return None;
                else:
                    self.chemical_compound += symbol;

            #print(self.chemical_compound)
        # If the compound type is molecular compound
        elif self.compound_type == "Ionic Compound":
            # Getting the symbol and the charge of the ionic compound
            for element in compound_name:
                if compound_name.index(element) == 0:
                    self.Determinging_Symbol_Charges_Ionic(name = element, order = 0);

                elif compound_name.index(element) != 0:
                    self.Determinging_Symbol_Charges_Ionic(name = element, order = 1);

            # If the first element is non POlyatomic Ion
            #print(self.element_and_compound, self.charge_list,self.type_list);
            if self.charge_list[0][0][0] == "+" and self.type_list[0] != "Polyatomic Ion":
                for charge in self.charge_list[1]:
                    if charge[0] == "-" and charge[1] == self.charge_list[0][0][1]:
                        self.chemical_compound = self.element_and_compound[0] + self.element_and_compound[1];
                        self.create_key_value(key = self.element_and_compound[0], value = 1, dictionary = self.Element_and_Compound_Key_To_Atomic_Number_Dictionary);
                        self.create_key_value(key=self.element_and_compound[1], value=1,
                                              dictionary=self.Element_and_Compound_Key_To_Atomic_Number_Dictionary);

                    elif charge[0] == "-" and charge[1] != self.charge_list[0][0][1] and int(self.charge_list[0][0][1]) == 1:
                        self.chemical_compound = self.element_and_compound[0] + charge[1] + self.element_and_compound[1]
                        self.create_key_value(key=self.element_and_compound[0], value= int(charge[1]),
                                              dictionary=self.Element_and_Compound_Key_To_Atomic_Number_Dictionary);

                        self.create_key_value(key=self.element_and_compound[1], value=1,
                                              dictionary=self.Element_and_Compound_Key_To_Atomic_Number_Dictionary);

                    elif charge[0] == "-" and charge[1] != self.charge_list[0][0][1] and int(charge[1]) == 1 and self.type_list[1] != "Polyatomic Ion":
                        self.chemical_compound = self.element_and_compound[0] + self.element_and_compound[1] + self.charge_list[0][0][1]

                        self.create_key_value(key=self.element_and_compound[0], value= 1,
                                              dictionary=self.Element_and_Compound_Key_To_Atomic_Number_Dictionary);

                        self.create_key_value(key=self.element_and_compound[1], value= int(self.charge_list[0][0][1]),
                                              dictionary=self.Element_and_Compound_Key_To_Atomic_Number_Dictionary);

                    elif charge[0] == "-" and charge[1] != self.charge_list[0][0][1] and int(charge[1]) == 1 and \
                            self.type_list[1] == "Polyatomic Ion":
                        self.chemical_compound = self.element_and_compound[0] + "(" + self.element_and_compound[1] + ")" + self.charge_list[0][0][1];

                        self.create_key_value(key=self.element_and_compound[0], value= 1,
                                              dictionary=self.Element_and_Compound_Key_To_Atomic_Number_Dictionary);

                        self.create_key_value(key=self.element_and_compound[1], value= int(self.charge_list[0][0][1]),
                                              dictionary=self.Element_and_Compound_Key_To_Atomic_Number_Dictionary);

                    elif charge[0] == "-" and charge[1] != self.charge_list[0][0][1] and self.type_list[1] != "Polyatomic Ion":
                        self.chemical_compound = self.element_and_compound[0] + charge[1] + self.element_and_compound[1] + self.charge_list[0][0][1];

                        self.create_key_value(key=self.element_and_compound[0], value= int(charge[1]),
                                              dictionary=self.Element_and_Compound_Key_To_Atomic_Number_Dictionary);

                        self.create_key_value(key=self.element_and_compound[1], value= int(self.charge_list[0][0][1]),
                                              dictionary=self.Element_and_Compound_Key_To_Atomic_Number_Dictionary);

                    elif charge[0] == "-" and charge[1] != self.charge_list[0][0][1] and self.type_list[1] == "Polyatomic Ion":
                        self.chemical_compound = self.element_and_compound[0] + charge[1] + "(" + self.element_and_compound[1] + ")" + self.charge_list[0][0][1];

                        self.create_key_value(key=self.element_and_compound[0], value= int(charge[1]),
                                              dictionary=self.Element_and_Compound_Key_To_Atomic_Number_Dictionary);

                        self.create_key_value(key=self.element_and_compound[1], value= int(self.charge_list[0][0][1]),
                                              dictionary=self.Element_and_Compound_Key_To_Atomic_Number_Dictionary);

            # If the first element is Polyatomic Ion
            elif self.charge_list[0][0][0] == "+" and self.type_list[0] == "Polyatomic Ion":
                for charge in self.charge_list[1]:
                    if charge[0] == "-" and charge[1] == self.charge_list[0][0][1]:
                        self.chemical_compound = self.element_and_compound[0] + self.element_and_compound[1];

                        self.create_key_value(key=self.element_and_compound[0], value= 1,
                                              dictionary=self.Element_and_Compound_Key_To_Atomic_Number_Dictionary);

                        self.create_key_value(key=self.element_and_compound[1], value= 1,
                                              dictionary=self.Element_and_Compound_Key_To_Atomic_Number_Dictionary);

                    elif charge[0] == "-" and charge[1] != self.charge_list[0][0][1] and int(self.charge_list[0][0][1]) == 1:
                        self.chemical_compound = "(" + self.element_and_compound[0] + ")" + charge[1] + self.element_and_compound[1]

                        self.create_key_value(key=self.element_and_compound[0], value= int(charge[1]),
                                              dictionary=self.Element_and_Compound_Key_To_Atomic_Number_Dictionary);

                        self.create_key_value(key=self.element_and_compound[1], value= 1,
                                              dictionary=self.Element_and_Compound_Key_To_Atomic_Number_Dictionary);

                    elif charge[0] == "-" and charge[1] != self.charge_list[0][0][1] and int(charge[1]) == 1 and \
                            self.type_list[1] != "Polyatomic Ion":
                        self.chemical_compound = self.element_and_compound[0] + self.element_and_compound[1] + \
                                                 self.charge_list[0][0][1]

                        self.create_key_value(key=self.element_and_compound[0], value= 1,
                                              dictionary=self.Element_and_Compound_Key_To_Atomic_Number_Dictionary);

                        self.create_key_value(key=self.element_and_compound[1], value= int(self.charge_list[0][0][1]),
                                              dictionary=self.Element_and_Compound_Key_To_Atomic_Number_Dictionary);

                    elif charge[0] == "-" and charge[1] != self.charge_list[0][0][1] and int(charge[1]) == 1 and \
                            self.type_list[1] == "Polyatomic Ion":
                        self.chemical_compound = self.element_and_compound[0] + "(" + self.element_and_compound[
                            1] + ")" + self.charge_list[0][0][1];

                        self.create_key_value(key=self.element_and_compound[0], value=1,
                                              dictionary=self.Element_and_Compound_Key_To_Atomic_Number_Dictionary);

                        self.create_key_value(key=self.element_and_compound[1], value=int(self.charge_list[0][0][1]),
                                              dictionary=self.Element_and_Compound_Key_To_Atomic_Number_Dictionary);



                    elif charge[0] == "-" and charge[1] != self.charge_list[0][0][1] and self.type_list[
                        1] != "Polyatomic Ion":
                        self.chemical_compound = "(" + self.element_and_compound[0] + ")" + charge[1] + self.element_and_compound[
                            1] + self.charge_list[0][0][1];

                        self.create_key_value(key=self.element_and_compound[0], value=int(charge[1]),
                                              dictionary=self.Element_and_Compound_Key_To_Atomic_Number_Dictionary);

                        self.create_key_value(key=self.element_and_compound[1], value=int(self.charge_list[0][0][1]),
                                              dictionary=self.Element_and_Compound_Key_To_Atomic_Number_Dictionary);

                    elif charge[0] == "-" and charge[1] != self.charge_list[0][0][1] and self.type_list[
                        1] == "Polyatomic Ion":
                        self.chemical_compound = "(" + self.element_and_compound[0] + ")" + charge[1] + "(" + \
                                                 self.element_and_compound[1] + ")" + self.charge_list[0][0][1];

                        self.create_key_value(key=self.element_and_compound[0], value= int(charge[1]),
                                              dictionary=self.Element_and_Compound_Key_To_Atomic_Number_Dictionary);

                        self.create_key_value(key=self.element_and_compound[1], value=int(self.charge_list[0][0][1]),
                                              dictionary=self.Element_and_Compound_Key_To_Atomic_Number_Dictionary);
        return self.chemical_compound

    def Determinging_Symbol_Charges_Ionic(self,name,order):
        if order == 0:
            if self.database.get_symbol_name_PeriodicTable(name) is not None:
                self.element_and_compound.append(self.database.get_symbol_name_PeriodicTable(name));
                self.charge_list.append(self.database.get_charge_sym_element(self.database.get_symbol_name_PeriodicTable(name)));
                self.type_list.append(self.database.get_type_name_element(name))

            elif self.database.get_symbol_name_PeriodicTable(name) is None:
                for character_index in range(0, len(name)):
                    if name[character_index] == "(":
                        for inner_character_index in range(0, len(name)):
                            if name[inner_character_index] == ")":
                                Latin_Number_Temp = name[character_index + 1:inner_character_index];
                                charge = ["+" + str(self.get_key(Latin_Number_Temp))];
                                self.charge_list.append(charge);
                            else:
                                pass
                        name = name[:character_index];
                        self.element_and_compound.append(self.database.get_symbol_name_PeriodicTable(name));
                        self.type_list.append(self.database.get_type_name_element(name));
                        break;
                    elif len(name) - 1 == character_index:
                        self.element_and_compound.append(self.database.get_sym_name_polyatomic(name));
                        self.charge_list.append(self.database.get_charge_name_polyatomic(name));
                        self.type_list.append(self.database.get_type_name_polyatomic(name));


        elif order != 0:
            if self.database.get_symbol_suffix_PeriodicTable(name) is not None:
                self.element_and_compound.append(self.database.get_symbol_suffix_PeriodicTable(name));
                self.charge_list.append(self.database.get_charge_suffix_PeriodicTable(name));
                self.type_list.append(self.database.get_type_suffix_element(name));

            elif self.database.get_symbol_suffix_PeriodicTable(name) is None:
                self.element_and_compound.append(self.database.get_sym_name_polyatomic(name));
                self.charge_list.append(self.database.get_charge_name_polyatomic(name));
                self.type_list.append(self.database.get_type_name_polyatomic(name));

    def Determining_Symbol_Atomic_Number_Molecular(self, name, order):
        if order == 0:
            if self.database.get_symbol_name_PeriodicTable(name) is not None:
                self.create_key_value(
                    key=self.database.get_symbol_name_PeriodicTable(name),
                    value= 1,
                    dictionary=self.Element_and_Compound_Key_To_Atomic_Number_Dictionary);
                return self.database.get_symbol_name_PeriodicTable(name)
            elif self.database.get_symbol_name_PeriodicTable(name) is None:
                for prefix in self.prefix_dictionary.keys():
                    if name[:len(prefix)] == prefix:
                        nonconfirmed_element = name[len(prefix):].capitalize();
                        if self.database.get_symbol_name_PeriodicTable(nonconfirmed_element) is not None:
                            confirmed_element_symbol = self.database.get_symbol_name_PeriodicTable(nonconfirmed_element) + self.prefix_dictionary.get(prefix);
                            self.create_key_value(
                                key=self.database.get_symbol_name_PeriodicTable(nonconfirmed_element),
                                value= int(self.prefix_dictionary.get(prefix)),
                                dictionary=self.Element_and_Compound_Key_To_Atomic_Number_Dictionary);

                            return confirmed_element_symbol;
                        elif self.database.get_symbol_name_PeriodicTable(nonconfirmed_element) is None:
                            nonconfirmed_element = name[len(prefix) - 1:].capitalize();
                            confirmed_element_symbol = self.database.get_symbol_name_PeriodicTable(nonconfirmed_element) + self.prefix_dictionary.get(prefix);
                            self.create_key_value(
                                key=self.database.get_symbol_name_PeriodicTable(nonconfirmed_element),
                                value= int(self.prefix_dictionary.get(prefix)),
                                dictionary=self.Element_and_Compound_Key_To_Atomic_Number_Dictionary);
                            return confirmed_element_symbol;

        elif order != 0:
            for prefix in self.prefix_dictionary.keys():
                if name[:len(prefix)] == prefix:
                    nonconfirmed_element = name[len(prefix):].capitalize();
                    if self.database.get_symbol_suffix_PeriodicTable(nonconfirmed_element) is not None:
                        if prefix == "Mono":
                            confirmed_element_symbol = self.database.get_symbol_suffix_PeriodicTable(
                                nonconfirmed_element)
                            self.create_key_value(
                                key=self.database.get_symbol_suffix_PeriodicTable(nonconfirmed_element),
                                value= 1,
                                dictionary=self.Element_and_Compound_Key_To_Atomic_Number_Dictionary);
                        else:
                            confirmed_element_symbol = self.database.get_symbol_suffix_PeriodicTable(nonconfirmed_element) + self.prefix_dictionary.get(prefix);
                            self.create_key_value(
                                key=self.database.get_symbol_suffix_PeriodicTable(nonconfirmed_element),
                                value= int(self.prefix_dictionary.get(prefix)),
                                dictionary=self.Element_and_Compound_Key_To_Atomic_Number_Dictionary);

                        return confirmed_element_symbol;

                    elif self.database.get_symbol_suffix_PeriodicTable(nonconfirmed_element) is None:
                        nonconfirmed_element = name[len(prefix) - 1:].capitalize();
                        if prefix == "Mono":
                            confirmed_element_symbol = self.database.get_symbol_suffix_PeriodicTable(nonconfirmed_element)
                            self.create_key_value(
                                key=self.database.get_symbol_suffix_PeriodicTable(nonconfirmed_element),
                                value= 1,
                                dictionary=self.Element_and_Compound_Key_To_Atomic_Number_Dictionary);
                        else:
                            confirmed_element_symbol = self.database.get_symbol_suffix_PeriodicTable(nonconfirmed_element) + self.prefix_dictionary.get(prefix)
                            self.create_key_value(
                                key= self.database.get_symbol_suffix_PeriodicTable(nonconfirmed_element),
                                value= int(self.prefix_dictionary.get(prefix)),
                                dictionary=self.Element_and_Compound_Key_To_Atomic_Number_Dictionary);

                        return confirmed_element_symbol



if __name__ == "__main__":
    main();
