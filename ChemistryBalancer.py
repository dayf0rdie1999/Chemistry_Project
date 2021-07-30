import sympy as sp
import DatabaseClass
import NamingCompound


def main():
    print("Let's get this show go on")
    Calculator = ChemistryBalancer();
    list_Chemistry_Equation = ['NaBr + Cl2 = NaCl + Br2', 'C3H8 + O2 = CO2 + H2O', 'C + O2 = CO2',
                               'LiCl + Mg(NO3)2 = LiNO3 + MgCl2', 'Al + Cu(NO3)2 = Cu + Al(NO3)3', 'Mg + Cl2 = MgCl2',
                               'Al2(SO4)3 + Ca(OH)2 = Al(OH)3 + CaSO4', 'NaOH + CO2 = Na2CO3 + H2O','Mg + HF = MgF2 + H2','PCl3 + Cl2 = PCl5','Mg + AlCl3 = MgCl2 + Al','K + H2O = KOH + H2']

    #for element in list_Chemistry_Equation:
        #print(Calculator.Balance_Chemistry_Equation(element));
    #print(Calculator.Balance_Chemistry_Equation('NaBr + Cl2 = NaCl + Br2'))
    print(Calculator.Balance_Chemistry_Equation('C + O2 = CO2'))
    #print(Calculator.Balance_Chemistry_Equation('Al2(SO4)3 + Ca(OH)2 = Al(OH)3 + CaSO4'))
    #print(Calculator.Compound_key_Information_Dictionary)
    #print(Calculator.Calculating_The_Moles_Number_And_Weight_Each_Compound_In_Equation('NaBr', Mass = 15.0 ));

class ChemistryBalancer():
    def __init__(self):
        self.NameCompound = NamingCompound.NamingChemical();
        self.database = DatabaseClass.Using_Database();
        self.product = ""
        self.reactant = ""
        self.product_list = None
        self.reactant_list = None
        self.Chemistry_Equation = None
        self.element_list_dictionary = {};
        self.System_Equation_Preparation_Dictionary = {};
        self.System_Equation_Dictionary = {};
        self.Coefficient_List = [];
        self.order_letter = None
        self.alphabet = 'a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z';
        self.element_list = []
        self.System_Equation = []
        self.System_Equation_Temporary = []
        self.number_order_to_letter = {};
        self.answer = {};
        self.temporary_answer = {};
        self.Compound_list = [];
        self.Compound_Key_To_Coefficient_Dictionary = {};
        self.Compound_symbol = [];
        self.Compound_key_Information_Dictionary = {};
        self.check_number = 0;
        self.reactant_element_list = []
        self.product_element_list = []

    def Calculating_The_Moles_Number_And_Weight_Each_Compound_In_Equation(self, symbol = None, Mass = None, Moles = None):
        if symbol == None:
            return "Error";
        elif Mass is not None and Moles is None and symbol is not None:
            Selected_Element_Dictionary = self.Compound_key_Information_Dictionary.get(symbol)
            Selected_Element_Dictionary["Moles"] = round(Mass * (1 / float(Selected_Element_Dictionary.get("Molar Mass"))), 5);
            Selected_Element_Dictionary["Mass"] = Mass;
            Selected_Element_Dictionary["Selected"] = True;

            for Element,Information in self.Compound_key_Information_Dictionary.items():
                if Information["Selected"] is False:
                    Information["Moles"] = round(Selected_Element_Dictionary["Moles"] * (Information["Coefficient"]/Selected_Element_Dictionary["Coefficient"]),5);
                    Information["Mass"] = round(Information["Moles"] * Information["Molar Mass"],5);
                else:
                    pass

            # Turn the Selected back to False again
            for Element,Information in self.Compound_key_Information_Dictionary.items():
                Information["Selected"] = False;

            return self.Compound_key_Information_Dictionary;

        elif Mass is None and Moles is not None and symbol is not None:
            Selected_Element_Dictionary = self.Compound_key_Information_Dictionary.get(symbol)
            Selected_Element_Dictionary["Moles"] = Moles;
            Selected_Element_Dictionary["Mass"] = round(Moles * Selected_Element_Dictionary.get("Molar Mass"), 5);
            Selected_Element_Dictionary["Selected"] = True;

            for Element,Information in self.Compound_key_Information_Dictionary.items():
                if Information["Selected"] is False:
                    Information["Moles"] = round(Selected_Element_Dictionary["Moles"] * (Information["Coefficient"]/Selected_Element_Dictionary["Coefficient"]),5);
                    Information["Mass"] = round(Information["Moles"] * Information["Molar Mass"],5);
                else:
                    pass

            # Turn the Selected back to False again
            for Element,Information in self.Compound_key_Information_Dictionary.items():
                Information["Selected"] = False;

            return self.Compound_key_Information_Dictionary;

        else:
            print("Please input one or the other please");


    def Get_Compound_Name_Element_Coefficient_Molar_Mass_To_Dictionary(self, compound):
        Information_Detail_Dictionary = {};
        if self.check_key(new_key = "Coefficient", dictionary = Information_Detail_Dictionary) is False:
            self.create_key_value(key = "Coefficient",value = self.Compound_Key_To_Coefficient_Dictionary.get(compound), dictionary = Information_Detail_Dictionary);
        else:
            pass

        if self.check_key(new_key = "Name", dictionary = Information_Detail_Dictionary) is False:
            #print(self.NameCompound.Naming_Compound_From_Symbol(compound = compound))
            self.create_key_value(key = "Name", value = self.NameCompound.Naming_Compound_From_Symbol(compound = compound), dictionary = Information_Detail_Dictionary);
            self.create_key_value(key = "Molar Mass", value = self.NameCompound.Calculating_Molar_Mass_Chemical_Compound(), dictionary = Information_Detail_Dictionary);
            self.create_key_value(key="Selected", value= False,
                                  dictionary=Information_Detail_Dictionary);
        else:
            pass

        if self.check_key(new_key = compound, dictionary = Information_Detail_Dictionary) is False:
            self.create_key_value(key = compound, value = Information_Detail_Dictionary, dictionary = self.Compound_key_Information_Dictionary);
        else:
            pass

        return Information_Detail_Dictionary;

    # Balancing all the equations
    def Balance_Chemistry_Equation(self, equation):
        self.product = "";
        self.reactant = "";
        self.product_list = None;
        self.reactant_list = None;
        self.Chemistry_Equation = None;
        self.System_Equation_Preparation_Dictionary.clear();
        self.order_letter = None;
        self.element_list = [];
        self.Coefficient_List = [];
        self.element_list_dictionary.clear();
        self.System_Equation_Dictionary = {};
        self.System_Equation = []
        self.System_Equation_Temporary = []
        self.number_order_to_letter = {};
        self.answer = {};
        self.Compound_list = [];
        self.Compound_Key_To_Coefficient_Dictionary = {};
        self.Compound_key_Information_Dictionary.clear();
        self.Compound_symbol.clear()
        self.check_number = 0;
        self.reactant_element_list = []
        self.product_element_list = []

        if self.Identifying_The_Numbers_of_Coefficient(equation) == "Error":
            return None;
        else:
            pass

        self.Chemistry_Equation = equation;
        equation = equation.split("=");


        if len(equation) == 2:
            # Separating the equation to reactant and products
            self.reactant = str(equation[0]);
            if self.Identifying_Element_of_Equation(self.reactant, self.reactant_element_list) == "Error":
                return None;
            else:
                pass
            self.element_list.clear()
            self.product = str(equation[1]);

            if self.Identifying_Element_of_Equation(self.product, self.product_element_list) == "Error":
                return None;
            else:
                pass
        else:
            return None

        if len(self.reactant_element_list) != len(self.product_element_list):
            return None;
        else:
            pass


        # Break the equation down into elements
        self.reactant_list = self.reactant.split("+");
        self.product_list = self.product.split("+")


        # Stripping all the string in the list
        for reactant_index in range(0, len(self.reactant_list)):
            self.reactant_list[reactant_index] = self.reactant_list[reactant_index].replace(" ", "");
            self.Separating_Product_Reactant_To_Element_AtomicNumber(self.reactant_list[reactant_index], "Reactant")
            self.Compound_list.append(self.reactant_list[reactant_index])
            self.Compound_symbol.append(self.reactant_list[reactant_index])

        for product_index in range(0, len(self.product_list)):
            self.product_list[product_index] = self.product_list[product_index].replace(" ", "");
            self.Separating_Product_Reactant_To_Element_AtomicNumber(self.product_list[product_index], "Product")
            self.Compound_list.append(self.product_list[product_index])
            self.Compound_symbol.append(self.product_list[product_index])

        #print(self.System_Equation_Preparation_Dictionary)
        for key, element_dictionary in self.System_Equation_Preparation_Dictionary.items():
            for element_key, element_atomic_number in element_dictionary.items():
                self.Completing_System_Equation_Preparation_Dictionary(element_key=element_key,
                                                                       element_atomic_number=element_atomic_number, character_key=key);

        #print(self.System_Equation_Dictionary);
        # Putting element with its atomic number to a dictionary of order to  put in systems of equations
        self.Combining_Value_From_System_Equation_Dictionary_To_Equation();

        self.Calculating_The_System_Equation();

        self.Completing_Chemistry_Equation();

        for compound_name in self.Compound_symbol:
            self.create_key_value(key = compound_name, value = self.Get_Compound_Name_Element_Coefficient_Molar_Mass_To_Dictionary(compound = compound_name), dictionary = self.Compound_key_Information_Dictionary);

        #print(self.Compound_key_Information_Dictionary)

        return self.Chemistry_Equation

    def Get_Compound_List(self):
        return self.Compound_symbol;

    def Get_Compound_Key_To_Coefficient_Dictionary(self):
        return self.Compound_Key_To_Coefficient_Dictionary;

    def Get_Chemistry_Balanced_Equation(self):
        return self.Chemistry_Equation;

    def Completing_Chemistry_Equation(self):

        for answer_key, answer_value in self.answer.items():
            for number_order_to_letter_key, number_order_to_letter_value in self.number_order_to_letter.items():
                if answer_key == str(number_order_to_letter_value):
                    if self.check_key(new_key = self.Compound_list[int(number_order_to_letter_key)],dictionary = self.Compound_Key_To_Coefficient_Dictionary) is True:
                        pass
                    elif self.check_key(new_key = self.Compound_list[int(number_order_to_letter_key)],dictionary = self.Compound_Key_To_Coefficient_Dictionary) is False:
                        self.create_key_value(key = self.Compound_list[int(number_order_to_letter_key)], value = int(answer_value), dictionary = self.Compound_Key_To_Coefficient_Dictionary);
                    self.Compound_list[int(number_order_to_letter_key)] = str(answer_value) + self.Compound_list[int(number_order_to_letter_key)]
                else:
                    pass

        # Adding all the compound together
        for reactant_index in range(0, len(self.reactant_list)):
            self.reactant_list[reactant_index] = self.Compound_list[reactant_index]

        # Removing the element in the compound list:
        for reactant_index in range(0, len(self.reactant_list)):
            self.Compound_list.pop(0);

        for product_index in range(0, len(self.product_list)):
            self.product_list[product_index] = self.Compound_list[product_index]

        for product_index in range(0, len(self.product_list)):
            self.Compound_list.pop(0);


        temporary_equation = [];

        reactant_equation = " + ".join(self.reactant_list);
        temporary_equation.append(reactant_equation)

        product_equation = " + ".join(self.product_list);
        temporary_equation.append(product_equation)

        self.Chemistry_Equation = " = ".join(temporary_equation);

        return self.Chemistry_Equation

    def Combining_Value_From_System_Equation_Dictionary_To_Equation(self):
        for value_list in self.System_Equation_Dictionary.values():
            if len(value_list) == 1:
                temporary_equation = value_list[0];
            elif len(value_list) == 2:
                temporary_equation = value_list[0] + value_list[1];
            elif len(value_list) == 3:
                temporary_equation = value_list[0] + value_list[1] + value_list[2];
            elif len(value_list) == 4:
                temporary_equation = value_list[0] + value_list[1] + value_list[2] + value_list[3];
            elif len(value_list) == 5:
                temporary_equation = value_list[0] + value_list[1] + value_list[2] + value_list[3] + value_list[4];
            self.System_Equation_Temporary.append(temporary_equation)

    # Calculating the system of equation
    def Calculating_The_System_Equation(self):

        for equation in self.System_Equation_Temporary:
            self.System_Equation.append(sp.Eq(equation, 0));

        temporary_symbol_list = []
        for symbols in self.order_letter:
            temporary_symbol_list.append(symbols);

        # Solving the system of equation
        self.temporary_answer = sp.solve(self.System_Equation, temporary_symbol_list);
        #print(self.temporary_answer);

        # Determining the exact value for the variable
        for key, value in self.temporary_answer.items():
            value = str(value);
            if len(value) == 1:
                if self.check_key(new_key = str(key), dictionary = self.answer) is False:
                    self.create_key_value(value = 1, key = str(key), dictionary = self.answer);

                    if self.check_key(new_key = str(value[0]), dictionary = self.answer) is False:
                        self.create_key_value(key = str(value[0]), value = 1, dictionary = self.answer);

                    elif self.check_key(new_key = str(value[0]),dictionary = self.answer) is True:
                        self.Updating_The_Answer_Dictionary(key_dictionary = str(key), key_in_value = str(value[0]), value = int(self.answer.get(str(value[0]))), dictionary = self.answer);

                elif self.check_key(new_key = str(key), dictionary = self.answer) is True:
                    pass

            elif len(value) == 3:
                if self.check_key(new_key = str(key), dictionary = self.answer) is False:
                    try:
                        self.create_key_value(value = int(value[0]), key = str(key), dictionary = self.answer);
                        if self.check_key(new_key=str(value[2]), dictionary=self.answer) is False:
                            self.create_key_value(key=str(value[2]), value=1, dictionary=self.answer);

                        elif self.check_key(new_key=str(value[2]), dictionary=self.answer) is True:
                            self.Updating_The_Answer_Dictionary(key_dictionary=str(key), key_in_value=str(value[2]),
                                                         value = 1, dictionary = self.answer);
                    except:
                        self.create_key_value(value= 1, key=str(key), dictionary=self.answer);
                        if self.check_key(new_key=str(value[0]), dictionary=self.answer) is False:
                            self.create_key_value(key=str(value[0]), value= int(value[2]), dictionary=self.answer);

                        elif self.check_key(new_key=str(value[2]), dictionary=self.answer) is True:
                            self.Updating_The_Answer_Dictionary(key_dictionary=str(key), key_in_value=str(value[2]),
                                                                value=int(value[2]), dictionary=self.answer);


                elif self.check_key(new_key = str(key), dictionary = self.answer) is True:
                    pass

            elif len(value) == 4:
                if self.check_key(new_key= str(key), dictionary=self.answer) is False:
                    self.create_key_value(value= int(value[:2]), key= str(key), dictionary=self.answer);

                    if self.check_key(new_key= str(value[4]), dictionary=self.answer) is False:
                        self.create_key_value(key= str(value[4]), value= 1, dictionary=self.answer);

                    elif self.check_key(new_key= str(value[4]), dictionary=self.answer) is True:
                        self.Updating_The_Answer_Dictionary(key_dictionary= str(key), key_in_value= str(value[4]), value= 1,
                                                            dictionary=self.answer);

                elif self.check_key(new_key= str(key), dictionary=self.answer) is True:
                    pass

            elif len(value) == 5:
                if self.check_key(new_key= str(key), dictionary=self.answer) is False:
                    self.create_key_value(value= int(value[0]), key= str(key), dictionary=self.answer);

                    if self.check_key(new_key= str(value[2]), dictionary=self.answer) is False:
                        self.create_key_value(key= str(value[2]), value= int(value[4]), dictionary=self.answer);

                    elif self.check_key(new_key= str(value[2]), dictionary=self.answer) is True:
                        self.Updating_The_Answer_Dictionary(key_dictionary= str(key), key_in_value= str(value[2]), value= int(value[4]),
                                                            dictionary=self.answer);

                elif self.check_key(new_key= str(key), dictionary=self.answer) is True:
                    pass

            elif len(value) == 6:
                if self.check_key(new_key= str(key), dictionary=self.answer) is False:
                    self.create_key_value(value= int(value[0]), key= str(key), dictionary=self.answer);

                    if self.check_key(new_key= str(value[2]), dictionary=self.answer) is False:
                        self.create_key_value(key= str(value[2]), value= int(value[4:]), dictionary=self.answer);

                    elif self.check_key(new_key= str(value[2]), dictionary=self.answer) is True:
                        self.Updating_The_Answer_Dictionary(key_dictionary= str(key), key_in_value= str(value[2]), value= int(value[4:]),
                                                            dictionary=self.answer);

                elif self.check_key(new_key= str(key), dictionary=self.answer) is True:
                    pass

            elif len(value) == 7:
                if self.check_key(new_key= str(key), dictionary=self.answer) is False:
                    self.create_key_value(value= int(value[:2]), key= str(key), dictionary=self.answer);

                    if self.check_key(new_key= str(value[3]), dictionary=self.answer) is False:
                        self.create_key_value(key= str(value[3]), value= int(value[6:]) , dictionary=self.answer);

                    elif self.check_key(new_key= str(value[3]), dictionary=self.answer) is True:
                        self.Updating_The_Answer_Dictionary(key_dictionary= str(key), key_in_value= str(value[3]), value= int(value[6:]),
                                                            dictionary=self.answer);

                elif self.check_key(new_key= str(key), dictionary=self.answer) is True:
                    pass

        #print(self.answer)


    def Updating_The_Answer_Dictionary(self,key_dictionary,key_in_value, value,dictionary):
        #print(key_dictionary, key_in_value, value )
        for answer_key,answer_value in self.answer.items():
            if answer_key == key_in_value:
                if int(self.answer.get(key_dictionary)) == int(answer_value):
                    if answer_value <= value:
                        dictionary[answer_key] = value;
                        dictionary[key_dictionary] = value;
                    else:
                        pass
                else:
                    pass
            else:
                pass


    # Putting in a list of dictionary that contain the element like "C": [1*a, 3*c,...];
    def Completing_System_Equation_Preparation_Dictionary(self, element_key, element_atomic_number, character_key):
        #print(element_key, element_atomic_number, character_key);
        if self.check_key(new_key = element_key, dictionary = self.System_Equation_Dictionary) is True:
            value = int(element_atomic_number) * character_key;
            self.Update_Value_System_Equation_Dictionary(input_key = element_key, new_value = value);

        elif self.check_key(new_key = element_key, dictionary = self.System_Equation_Dictionary) is False:
            value = int(element_atomic_number) * character_key
            self.Create_Key_Value_System_Equation_Dictionary(input_key = element_key, new_value= value);


    def Update_Value_System_Equation_Dictionary(self, input_key, new_value):
        for key, value in self.System_Equation_Dictionary.items():
            if key == input_key:
                value.append(new_value)
            else:
                pass

    def Create_Key_Value_System_Equation_Dictionary(self, input_key, new_value):
        self.System_Equation_Dictionary[input_key] = [new_value]

    ''' Identifying all the element in the equation'''
    def Identifying_Element_of_Equation(self, equation, type_list):
        equation = equation.split();
        self.check_number = 0

        for element in equation:
            if not element[0].isupper():
                equation.remove(element);
            else:
                pass

        if len(equation) != 0:
            for compound in equation:
                while len(compound) != 0:
                    self.check_number += 1;
                    if self.check_number > 10:
                        Error = "Error";
                        return Error;
                    else:
                        pass
                    if compound[0].isupper() and len(compound) == 1:
                        if self.Checking_Element_in_List(new_element=compound[0]) is True:
                            compound = compound[1:]
                        elif self.Checking_Element_in_List(new_element=compound[0]) is False:
                            self.element_list.append(compound[0])
                            type_list.append(compound[0])
                            compound = compound[1:]

                    elif compound[0].isupper() and compound[1].islower() and len(compound) == 2:
                        if self.Checking_Element_in_List(new_element=compound[:2]) is True:
                            compound = compound[2:]
                        elif self.Checking_Element_in_List(new_element=compound[:2]) is False:
                            self.element_list.append(compound[:2])
                            type_list.append(compound[:2])
                            compound = compound[2:]

                    elif compound[0].isupper() and compound[1].isdigit() and len(compound) == 2:
                        if self.Checking_Element_in_List(new_element=compound[0]) is True:
                            compound = compound[2:]
                        elif self.Checking_Element_in_List(new_element=compound[0]) is False:
                            self.element_list.append(compound[0])
                            type_list.append(compound[0])
                            compound = compound[2:]

                    elif compound[0].isupper() and compound[1].isdigit() and compound[2].isdigit() and len(
                            compound) == 3:
                        if self.Checking_Element_in_List(new_element=compound[0]) is True:
                            compound = compound[4:]
                        elif self.Checking_Element_in_List(new_element=compound[0]) is False:
                            self.element_list.append(compound[0])
                            type_list.append(compound[0])
                            compound = compound[4:]

                    elif compound[0].isupper() and compound[1].islower() and compound[2].isdigit and len(compound) == 3:
                        if self.Checking_Element_in_List(compound[:2]) is True:
                            compound = compound[4:]
                        elif self.Checking_Element_in_List(compound[:2]) is False:
                            self.element_list.append(compound[:2]);
                            type_list.append(compound[:2])
                            compound = compound[4:]

                    elif compound[0].isupper() and compound[1].islower() and compound[2].isdigit() and compound[
                        3].isdigit() and len(compound) == 4:
                        if self.Checking_Element_in_List(compound[:2]) is True:
                            compound = compound[5:]
                        elif self.Checking_Element_in_List(compound[:2]) is False:
                            self.element_list.append(compound[:2])
                            type_list.append(compound[:2])
                            compound = compound[5:]

                    elif compound[0] == "(":
                        for character_index in range(0, len(compound)):
                            if compound[character_index] == ")" and compound[character_index + 1].isdigit():
                                compound = self.Reformatting_Polyatomic_Ion_Atomic_Number(
                                    compound=compound[1:character_index], digit=compound[character_index + 1]);
                                break;
                            else:
                                pass

                    elif compound[0].isupper():
                        if compound[1].isupper():
                            if self.Checking_Element_in_List(compound[0]) is True:
                                compound = compound[1:]
                            elif self.Checking_Element_in_List(compound[0]) is False:
                                self.element_list.append(compound[0])
                                type_list.append(compound[0])

                                compound = compound[1:]

                        elif compound[1].isdigit() and compound[2].isupper():
                            if self.Checking_Element_in_List(compound[0]) is True:
                                compound = compound[2:]
                            elif self.Checking_Element_in_List(compound[0]) is False:
                                self.element_list.append(compound[0])
                                type_list.append(compound[0])
                                compound = compound[2:]

                        elif compound[1].isdigit() and compound[2].isdigit() and compound[3].isupper():
                            if self.Checking_Element_in_List(compound[0]) is True:
                                compound = compound[4:];
                            elif self.Checking_Element_in_List(compound[0]) is False:
                                self.element_list.append(compound[0])
                                type_list.append(compound[0])
                                compound = compound[4:];

                        elif compound[1].islower() and compound[2].isupper() or compound[2] == "(":
                            if self.Checking_Element_in_List(compound[:2]) is True:
                                compound = compound[2:]
                            elif self.Checking_Element_in_List(compound[:2]) is False:
                                self.element_list.append(compound[:2])
                                type_list.append(compound[:2])
                                compound = compound[2:]

                        elif compound[1].islower() and compound[2].isdigit():
                            if self.Checking_Element_in_List(compound[:2]) is True:
                                compound = compound[3:]
                            elif self.Checking_Element_in_List(compound[:2]) is False:
                                self.element_list.append(compound[:2])
                                type_list.append(compound[:2])
                                compound = compound[3:]
        else:
            return "Error";


    def Checking_Element_in_List(self, new_element):
        for element in self.element_list:
            if new_element == element:
                return True;
            else:
                pass
        return False;

    # Identifying the numbers of coefficient
    def Identifying_The_Numbers_of_Coefficient(self, equation):
        equation = equation.split()

        for element in equation:
            if not element[0].isupper():
                equation.remove(element)

        if len(equation) == 1:
            return "Error";
        else:
            pass

        # Creating the key order related to a specific alphabetical letter;
        variables = self.alphabet[:(len(equation) * 2) - 1];

        # Assigning dictionary letter to sympy symbol
        self.order_letter = sp.symbols(variables);

        for index in range(0, len(equation)):
            if self.check_key(new_key = index, dictionary = self.number_order_to_letter) is True:
                pass
            elif self.check_key(new_key = index, dictionary = self.number_order_to_letter) is False:
                self.create_key_value(key = index, value = self.order_letter[index],dictionary = self.number_order_to_letter);

    # Separating the product and reactant list into element dictionary and add to the order_element_dictionary
    def Separating_Product_Reactant_To_Element_AtomicNumber(self, compound, type):
        # Separating the compound into element with atomic numbers
        temporary_element_dictionary = {};
        original_compound = compound;
        if type == "Reactant":
            while len(compound) != 0:
                if compound[0].isupper() and len(compound) == 1:
                    if self.check_key(new_key=compound[0], dictionary=temporary_element_dictionary) is True:
                        self.update_value(key=compound[0], value=1, dictionary=temporary_element_dictionary)
                        compound = compound[1:]
                    elif self.check_key(new_key=compound[0], dictionary=temporary_element_dictionary) is False:
                        self.create_key_value(key=compound[0], value=1, dictionary=temporary_element_dictionary);
                        compound = compound[1:]

                elif compound[0].isupper() and compound[1].islower() and len(compound) == 2:
                    if self.check_key(new_key=compound[:2], dictionary=temporary_element_dictionary) is True:
                        self.update_value(key=compound[:2], value=1, dictionary=temporary_element_dictionary)
                        compound = compound[2:]
                    elif self.check_key(new_key=compound[:2], dictionary=temporary_element_dictionary) is False:
                        self.create_key_value(key=compound[:2], value=1, dictionary=temporary_element_dictionary)
                        compound = compound[2:]

                elif compound[0].isupper() and compound[1].isdigit() and len(compound) == 2:
                    if self.check_key(new_key=compound[0], dictionary=temporary_element_dictionary) is True:
                        self.update_value(key=compound[0], value=compound[1], dictionary=temporary_element_dictionary)
                        compound = compound[2:]
                    elif self.check_key(new_key=compound[0], dictionary=temporary_element_dictionary) is False:
                        self.create_key_value(key=compound[0], value=compound[1],
                                              dictionary=temporary_element_dictionary)
                        compound = compound[2:]

                elif compound[0].isupper() and compound[1].isdigit() and compound[2].isdigit() and len(compound) == 3:
                    if self.check_key(new_key=compound[0], dictionary=temporary_element_dictionary) is True:
                        self.update_value(key=compound[0], value=int(compound[1:3]),
                                          dictionary=temporary_element_dictionary);
                        compound = compound[4:]
                    elif self.check_key(new_key=compound[0], dictionary=temporary_element_dictionary) is False:
                        self.create_key_value(key=compound[0], value=int(compound[1:3]),
                                              dictionary=temporary_element_dictionary);
                        compound = compound[4:]

                elif compound[0].isupper() and compound[1].islower() and compound[2].isdigit and len(compound) == 3:
                    if self.check_key(new_key=compound[:2], dictionary=temporary_element_dictionary) is True:
                        self.update_value(key=compound[:2], value=int(compound[2]),
                                          dictionary=temporary_element_dictionary);
                        compound = compound[3:]
                    elif self.check_key(new_key=compound[:2], dictionary=temporary_element_dictionary) is False:
                        self.create_key_value(key=compound[:2], value=int(compound[2]),
                                              dictionary=temporary_element_dictionary);
                        compound = compound[3:]


                elif compound[0].isupper() and compound[1].islower() and compound[2].isdigit() and compound[
                    3].isdigit() and len(compound) == 4:
                    if self.check_key(new_key=compound[:2], dictionary=temporary_element_dictionary) is True:
                        self.update_value(key=compound[:2], value=int(compound[2]),
                                          dictionary=temporary_element_dictionary);
                        compound = compound[3:]
                    elif self.check_key(new_key=compound[:2], dictionary=temporary_element_dictionary) is False:
                        self.create_key_value(key=compound[:2], value=int(compound[2]),
                                              dictionary=temporary_element_dictionary);
                        compound = compound[3:]

                elif compound[0] == "(":
                    for character_index in range(0, len(compound)):
                        if compound[character_index] == ")" and compound[character_index + 1].isdigit():
                            compound = self.Reformatting_Polyatomic_Ion_Atomic_Number(
                                compound=compound[1:character_index], digit=compound[character_index + 1]);
                            break;
                        else:
                            pass

                elif compound[0].isupper():
                    if compound[1].isupper():
                        if self.check_key(new_key=compound[0], dictionary=temporary_element_dictionary) is True:
                            self.update_value(key=compound[0], value=1, dictionary=temporary_element_dictionary);
                            compound = compound[1:]
                        elif self.check_key(new_key=compound[0], dictionary=temporary_element_dictionary) is False:
                            self.create_key_value(key=compound[0], value=1, dictionary=temporary_element_dictionary);
                            compound = compound[1:]

                    elif compound[1].isdigit() and compound[2].isupper():
                        if self.check_key(new_key=compound[0], dictionary=temporary_element_dictionary) is True:
                            self.update_value(key=compound[0], value=int(compound[1]),
                                              dictionary=temporary_element_dictionary);
                            compound = compound[2:]
                        elif self.check_key(new_key=compound[0], dictionary=temporary_element_dictionary) is False:
                            self.create_key_value(key=compound[0], value=int(compound[1]),
                                                  dictionary=temporary_element_dictionary);
                            compound = compound[2:]

                    elif compound[1].isdigit() and compound[2].isdigit() and compound[3].isupper():
                        if self.check_key(new_key=compound[0], dictionary=temporary_element_dictionary) is True:
                            self.update_value(key=compound[0], value=int(compound[1:3]),
                                              dictionary=temporary_element_dictionary)
                            compound = compound[4:];
                        elif self.check_key(new_key=compound[0], dictionary=temporary_element_dictionary) is False:
                            self.create_key_value(key=compound[0], value=int(compound[1:3]),
                                                  dictionary=temporary_element_dictionary);
                            compound = compound[4:];

                    elif compound[1].islower() and compound[2].isupper() or compound[2] == "(":
                        if self.check_key(new_key=compound[:2], dictionary=temporary_element_dictionary) is True:
                            self.update_value(key=compound[:2], value=1, dictionary=temporary_element_dictionary);
                            compound = compound[2:]
                        elif self.check_key(new_key=compound[:2], dictionary=temporary_element_dictionary) is False:
                            self.create_key_value(key=compound[:2], value=1, dictionary=temporary_element_dictionary);
                            compound = compound[2:]

                    elif compound[1].islower() and compound[2].isdigit():
                        if self.check_key(new_key=compound[:2], dictionary=temporary_element_dictionary) is True:
                            self.update_value(key=compound[:2], value=int(compound[2]),
                                              dictionary=temporary_element_dictionary);
                            compound = compound[3:]
                        elif self.check_key(new_key=compound[:2], dictionary=temporary_element_dictionary) is False:
                            self.create_key_value(key=compound[:2], value=int(compound[2]),
                                                  dictionary=temporary_element_dictionary);
                            compound = compound[3:]

        # IF the type is the Product type
        elif type == "Product":
            while len(compound) != 0:
                if compound[0].isupper() and len(compound) == 1:
                    if self.check_key(new_key=compound[0], dictionary=temporary_element_dictionary) is True:
                        self.update_value(key=compound[0], value=-1, dictionary=temporary_element_dictionary)
                        compound = compound[1:]
                    elif self.check_key(new_key=compound[0], dictionary=temporary_element_dictionary) is False:
                        self.create_key_value(key=compound[0], value=-1, dictionary=temporary_element_dictionary);
                        compound = compound[1:]

                elif compound[0].isupper() and compound[1].islower() and len(compound) == 2:
                    if self.check_key(new_key=compound[:2], dictionary=temporary_element_dictionary) is True:
                        self.update_value(key=compound[:2], value=-1, dictionary=temporary_element_dictionary)
                        compound = compound[2:]
                    elif self.check_key(new_key=compound[:2], dictionary=temporary_element_dictionary) is False:
                        self.create_key_value(key=compound[:2], value=-1, dictionary=temporary_element_dictionary)
                        compound = compound[2:]

                elif compound[0].isupper() and compound[1].isdigit() and len(compound) == 2:
                    if self.check_key(new_key=compound[0], dictionary=temporary_element_dictionary) is True:
                        self.update_value(key=compound[0], value=-int(compound[1]),
                                          dictionary=temporary_element_dictionary)
                        compound = compound[2:]
                    elif self.check_key(new_key=compound[0], dictionary=temporary_element_dictionary) is False:
                        self.create_key_value(key=compound[0], value=-int(compound[1]),
                                              dictionary=temporary_element_dictionary)
                        compound = compound[2:]

                elif compound[0].isupper() and compound[1].isdigit() and compound[2].isdigit() and len(compound) == 3:
                    if self.check_key(new_key=compound[0], dictionary=temporary_element_dictionary) is True:
                        self.update_value(key=compound[0], value=-int(compound[1:3]),
                                          dictionary=temporary_element_dictionary);
                        compound = compound[4:]
                    elif self.check_key(new_key=compound[0], dictionary=temporary_element_dictionary) is False:
                        self.create_key_value(key=compound[0], value=-int(compound[1:3]),
                                              dictionary=temporary_element_dictionary);
                        compound = compound[4:]

                elif compound[0].isupper() and compound[1].islower() and compound[2].isdigit and len(compound) == 3:
                    if self.check_key(new_key=compound[:2], dictionary=temporary_element_dictionary) is True:
                        self.update_value(key=compound[:2], value=-int(compound[2]),
                                          dictionary=temporary_element_dictionary);
                        compound = compound[3:]
                    elif self.check_key(new_key=compound[:2], dictionary=temporary_element_dictionary) is False:
                        self.create_key_value(key=compound[:2], value=-int(compound[2]),
                                              dictionary=temporary_element_dictionary);
                        compound = compound[3:]


                elif compound[0].isupper() and compound[1].islower() and compound[2].isdigit() and compound[
                    3].isdigit() and len(compound) == 4:
                    if self.check_key(new_key=compound[:2], dictionary=temporary_element_dictionary) is True:
                        self.update_value(key=compound[:2], value=-int(compound[2]),
                                          dictionary=temporary_element_dictionary);
                        compound = compound[3:]
                    elif self.check_key(new_key=compound[:2], dictionary=temporary_element_dictionary) is False:
                        self.create_key_value(key=compound[:2], value=-int(compound[2]),
                                              dictionary=temporary_element_dictionary);
                        compound = compound[3:]

                elif compound[0] == "(":
                    for character_index in range(0, len(compound)):
                        if compound[character_index] == ")" and compound[character_index + 1].isdigit():
                            compound = self.Reformatting_Polyatomic_Ion_Atomic_Number(
                                compound=compound[1:character_index], digit=compound[character_index + 1]);
                            break;
                        else:
                            pass

                elif compound[0].isupper():
                    if compound[1].isupper():
                        if self.check_key(new_key=compound[0], dictionary=temporary_element_dictionary) is True:
                            self.update_value(key=compound[0], value=-1, dictionary=temporary_element_dictionary);
                            compound = compound[1:]
                        elif self.check_key(new_key=compound[0], dictionary=temporary_element_dictionary) is False:
                            self.create_key_value(key=compound[0], value=-1, dictionary=temporary_element_dictionary);
                            compound = compound[1:]

                    elif compound[1].isdigit() and compound[2].isupper():
                        if self.check_key(new_key=compound[0], dictionary=temporary_element_dictionary) is True:
                            self.update_value(key=compound[0], value=-int(compound[1]),
                                              dictionary=temporary_element_dictionary);
                            compound = compound[2:]
                        elif self.check_key(new_key=compound[0], dictionary=temporary_element_dictionary) is False:
                            self.create_key_value(key=compound[0], value=-int(compound[1]),
                                                  dictionary=temporary_element_dictionary);
                            compound = compound[2:]

                    elif compound[1].isdigit() and compound[2].isdigit() and compound[3].isupper():
                        if self.check_key(new_key=compound[0], dictionary=temporary_element_dictionary) is True:
                            self.update_value(key=compound[0], value=-int(compound[1:3]),
                                              dictionary=temporary_element_dictionary)
                            compound = compound[4:];
                        elif self.check_key(new_key=compound[0], dictionary=temporary_element_dictionary) is False:
                            self.create_key_value(key=compound[0], value=-int(compound[1:3]),
                                                  dictionary=temporary_element_dictionary);
                            compound = compound[4:];

                    elif compound[1].islower() and compound[2].isupper() or compound[2] == "(":
                        if self.check_key(new_key=compound[:2], dictionary=temporary_element_dictionary) is True:
                            self.update_value(key=compound[:2], value=-1, dictionary=temporary_element_dictionary);
                            compound = compound[2:]
                        elif self.check_key(new_key=compound[:2], dictionary=temporary_element_dictionary) is False:
                            self.create_key_value(key=compound[:2], value=-1, dictionary=temporary_element_dictionary);
                            compound = compound[2:]

                    elif compound[1].islower() and compound[2].isdigit():
                        if self.check_key(new_key=compound[:2], dictionary=temporary_element_dictionary) is True:
                            self.update_value(key=compound[:2], value=-int(compound[2]),
                                              dictionary=temporary_element_dictionary);
                            compound = compound[3:]
                        elif self.check_key(new_key=compound[:2], dictionary=temporary_element_dictionary) is False:
                            self.create_key_value(key=compound[:2], value=-int(compound[2]),
                                                  dictionary=temporary_element_dictionary);
                            compound = compound[3:]


        self.Setting_System_Equation_Preparation_Dictionary(dictionary=temporary_element_dictionary);

    def Setting_System_Equation_Preparation_Dictionary(self, dictionary):
        for character in self.order_letter:
            if self.check_key(new_key=character, dictionary=self.System_Equation_Preparation_Dictionary) is False:
                self.create_key_value(key=character, value=dictionary,
                                      dictionary=self.System_Equation_Preparation_Dictionary);
                break;
            elif self.check_key(new_key=character, dictionary=self.System_Equation_Preparation_Dictionary) is True:
                pass

    def Reformatting_Polyatomic_Ion_Atomic_Number(self, compound, digit):
        element_dictionary = {};
        while len(compound) != 0:
            if len(compound) == 1 and compound[0].isupper():
                if self.check_key(new_key=compound[0], dictionary=element_dictionary) is True:
                    self.update_value(key=compound[0], value=1,
                                      dictionary=element_dictionary);
                    compound = compound[1:];

                elif self.check_key(new_key=compound[0], dictionary=element_dictionary) is False:
                    self.create_key_value(key=compound[0], value=1,
                                          dictionary=element_dictionary);
                    compound = compound[1:];


            elif compound[0].isupper():
                if compound[1].isupper():
                    if self.check_key(new_key=compound[0], dictionary=element_dictionary) is True:
                        self.update_value(key=compound[0], value=1,
                                          dictionary=element_dictionary);
                        compound = compound[1:];

                    elif self.check_key(new_key=compound[0], dictionary=element_dictionary) is False:
                        self.create_key_value(key=compound[0], value=1,
                                              dictionary=element_dictionary);
                        compound = compound[1:];

                elif compound[1].isdigit():
                    if self.check_key(new_key=compound[0], dictionary=element_dictionary) is True:
                        self.update_value(key=compound[0], value=compound[1],
                                          dictionary=element_dictionary);
                        compound = compound[2:];

                    elif self.check_key(new_key=compound[0], dictionary=element_dictionary) is False:
                        self.create_key_value(key=compound[0], value=compound[1],
                                              dictionary=element_dictionary);
                        compound = compound[2:];

                elif compound[1].islower() and compound[2].isupper():
                    if self.check_key(new_key=compound[:2], dictionary=element_dictionary) is True:
                        self.update_value(key=compound[:2], value=1,
                                          dictionary=element_dictionary);
                        compound = compound[3:];

                    elif self.check_key(new_key=compound[:2], dictionary=element_dictionary) is False:
                        self.create_key_value(key=compound[:2], value=1,
                                              dictionary=element_dictionary);
                        compound = compound[3:];

                elif compound[1].islower() and compound[2].isdigit():
                    if self.check_key(new_key=compound[:2], dictionary=element_dictionary) is True:
                        self.update_value(key=compound[:2], value=compound[2],
                                          dictionary=element_dictionary);
                        compound = compound[3:];
                    elif self.check_key(new_key=compound[:2], dictionary=element_dictionary) is False:
                        self.create_key_value(key=compound[:2], value=compound[2],
                                              dictionary=element_dictionary);
                        compound = compound[3:];

        # Updating the atomic number of the polyatomic number
        for key, existedValue in element_dictionary.items():
            new_Value = int(existedValue) * int(digit)
            element_dictionary[key] = new_Value

        # Reformat the compound
        for key, Value in element_dictionary.items():
            compound += key + str(Value)

        return compound;

    # Getting the key from the dictionary
    def get_key(self, val, dictionary):
        for key, value in dictionary.items():
            if val == value:
                return key

        return "key doesn't exist"

    # Checking the key from the dictionary
    def check_key(self, new_key, dictionary):
        for key, value in dictionary.items():
            if new_key == key:
                return True;
        return False;

    # Updating the value from the in the dictionary
    def update_value(self, key, value, dictionary):
        dictionary[key] = dictionary.get(key) + value;

    # Creating new key and value in the dictionary
    def create_key_value(self, key, value, dictionary):
        try:
            dictionary[key] = value;
            return True
        except:
            return False


if __name__ == "__main__":
    main()
