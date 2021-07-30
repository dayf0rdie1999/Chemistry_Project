import DatabaseClass
import NamingCompound




def main():
    print("Let's get this challenge going")
    Redox_Reaction = Redox_Reaction_Calculator();

    print(Redox_Reaction.Determining_Element_Oxidation_Number(""))


class Redox_Reaction_Calculator():
    def __init__(self):
        self.database = DatabaseClass.Using_Database();
        self.Naming_Compound_Object = NamingCompound.NamingChemical();

    def Determining_Element_Oxidation_Number(self, compound):
        temporary_oxidation_number_dictionary = {}
        if self.Naming_Compound_Object.Naming_Compound_From_Symbol(compound) is not None:
            if self.Naming_Compound_Object.get_compound_type() == "Molecular Compound":
                temporary_oxidation_number_dictionary = self.Naming_Compound_Object.get_molecular_key_as_element_value_as_charge_dictionary();
            elif self.Naming_Compound_Object.get_compound_type() == "Ionic Compound":
                temporary_oxidation_number_dictionary = self.Naming_Compound_Object.get_ionic_dictionary_charge_list();
        elif compound == "Na2O2":
            temporary_oxidation_number_dictionary["Na2"] = "+1";
            temporary_oxidation_number_dictionary["O2"] = "-1";
        elif compound == "H2O2":
            temporary_oxidation_number_dictionary["H2"] = "+1";
            temporary_oxidation_number_dictionary["O2"] = "-1";

        elif compound[-1] == "}":
            print("Haha")
        return temporary_oxidation_number_dictionary

if __name__ == "__main__":
    main()
