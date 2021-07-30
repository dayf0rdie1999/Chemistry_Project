import sqlite3


def main():
    User = Using_Database();
    #print(User.get_symbol_suffix_PeriodicTable("Sulfide"));
    print(User.get_everything_From_element_except_Suffix_Periodic())

class Using_Database():
    # Connecting to the database
    def __init__(self):
        self.conn = sqlite3.connect('Periodic_Data.db');
        self.cursor = self.conn.cursor()

    def get_everything_From_element_except_Suffix_Periodic(self):
        self.cursor.execute("SELECT Atom,Name,Symbol,Mass,Type,Charge FROM PeriodicTable");
        return self.cursor.fetchall();

    def get_everything_From_element_except_Suffix_Polyatomic(self):
        self.cursor.execute("SELECT Name,Symbol,Mass,Type,Charge FROM PolyatomicTable");
        return self.cursor.fetchall();

    def get_everything_element_Periodic_From_Symbol(self, symbol):
        self.cursor.execute("SELECT Atom,Name,Symbol,Mass,Type,Charge FROM PeriodicTable WHERE Symbol = :Symbol", {'Symbol': symbol});
        value = self.cursor.fetchall();
        print(value)
        if len(value) == 0:
            return None;
        else:
            return value

    def get_everything_element_Periodic_From_Name(self, name):
        self.cursor.execute("SELECT Atom,Name,Symbol,Mass,Type,Charge FROM PeriodicTable Where Name = :Name", {'Name': name});
        value = self.cursor.fetchall();
        print(value)
        if len(value) == 0:
            return None;
        else:
            return value

    def get_everything_element_Polyatomic_From_Symbol(self, symbol):
        self.cursor.execute("SELECT Name,Symbol,Mass,Type,Charge FROM PolyatomicTable WHERE Symbol = :Symbol", {'Symbol': symbol});
        value = self.cursor.fetchall();
        print(value)
        if len(value) == 0:
            return None;
        else:
            return value

    def get_everything_element_Polyatomic_From_Name(self, name):
        self.cursor.execute("SELECT Name,Symbol,Mass,Type,Charge FROM PolyatomicTable Where Name = :Name", {'Name': name});
        value = self.cursor.fetchall();
        print(value)
        if len(value) == 0:
            return None;
        else:
            return value

    def get_name_sym_element(self, symbol):
        self.cursor.execute("SELECT Name FROM PeriodicTable WHERE Symbol = :Symbol", {'Symbol': symbol});
        # Read the rows that containing the symbol
        name_tuple = self.cursor.fetchone();
        # Take the name out of the tuple
        name = name_tuple[0];
        # Return the value
        return name;

    def get_type_name_element(self, name):
        self.cursor.execute("SELECT Type FROM PeriodicTable WHERE Name = :Name", {'Name': name});
        # Read the rows that containing that element name
        type_tuple = self.cursor.fetchone();
        if type_tuple == None:
            type = None;
        else:
            # Take the type out of the tuple
            type = type_tuple[0];
            # Return the type
        return type;

    def get_type_suffix_element(self, name):
        self.cursor.execute("SELECT Type FROM PeriodicTable WHERE Suffix = :Suffix", {'Suffix': name});
        # Read the rows that containing that element name
        type_tuple = self.cursor.fetchone();
        if type_tuple == None:
            type = None;
        else:
            # Take the type out of the tuple
            type = type_tuple[0];
            # Return the type
        return type;

    def get_type_sym_element(self, symbol):
        self.cursor.execute("SELECT Type FROM PeriodicTable WHERE Symbol = :Symbol", {'Symbol': symbol});
        # Read the rows that containing that element name
        type_tuple = self.cursor.fetchone();
        if type_tuple == None:
            type = None;
        else:
            # Take the type out of the tuple
            type = type_tuple[0];
            # Return the type
        return type;

    def get_charge_sym_element(self, symbol):
        self.cursor.execute("SELECT Charge FROM PeriodicTable WHERE Symbol = :Symbol", {'Symbol': symbol});
        # Read the rows that containing that element name
        type_tuple = self.cursor.fetchone();
        # Take the type out of the tuple
        charges = type_tuple[0];
        charges = charges.split(",")
        return charges

    def get_charge_sym_polyatomic(self, symbol):
        self.cursor.execute("SELECT Charge FROM PolyatomicTable WHERE Symbol = :Symbol", {'Symbol': symbol});
        # Read the rows that containing that element name
        type_tuple = self.cursor.fetchone();
        # Take the type out of the tuple
        charges = type_tuple[0];
        charges = charges.split(",")
        return charges

    def get_name_sym_polyatomic(self, symbol):
        self.cursor.execute("SELECT Name FROM PolyatomicTable WHERE Symbol = :Symbol", {'Symbol': symbol});
        # Read the rows that containing the symbol
        name_tuple = self.cursor.fetchone();
        # Take the name out of the tuple
        name = name_tuple[0];
        # Return the value
        return name;

    def get_sym_name_polyatomic(self,name):
        self.cursor.execute("SELECT Symbol FROM PolyatomicTable WHERE Name = :Name", {'Name': name});
        # Read the rows that containing the symbol
        name_tuple = self.cursor.fetchone();
        if name_tuple == None:
            name = None;
        else:
            # Take the name out of the tuple
            name = name_tuple[0];
        # Return the value
        return name;


    def get_suffix_name_PeriodicTable(self,name):
        self.cursor.execute("SELECT Suffix FROM PeriodicTable WHERE Name = :Name", {'Name': name});
        # Read the rows that containing the symbol
        name_tuple = self.cursor.fetchone();
        # Take the name out of the tuple
        name = name_tuple[0];
        # Return the value
        return name;

    def get_type_name_polyatomic(self, name):
        self.cursor.execute("SELECT Type FROM PolyatomicTable WHERE Name = :Name", {'Name': name});
        # Read the rows that containing the symbol
        type_tuple = self.cursor.fetchone();
        if type_tuple == None:
            type = None;
        else:
            # Take the name out of the tuple
            type = type_tuple[0];
            # Return the value
        return type;

    def get_name_name_PeriodicTable(self,name):
        self.cursor.execute("SELECT Name FROM PeriodicTable WHERE Name = :Name", {'Name': name});
        # Read the rows that containing the symbol
        name_tuple = self.cursor.fetchone();
        if name_tuple == None:
            name = None;
        else:
            # Take the name out of the tuple
            name = name_tuple[0];
        # Return the value
        return name;

    def get_symbol_suffix_PeriodicTable(self,suffix):
        self.cursor.execute("SELECT Symbol FROM PeriodicTable WHERE Suffix = :Suffix", {'Suffix': suffix});
        name_tuple = self.cursor.fetchone();
        if name_tuple == None:
            symbol = None;
        else:
            # Take the name out of the tuple
            symbol = name_tuple[0];
        # Return the value
        return symbol;

    def get_symbol_name_PeriodicTable(self,name):
        self.cursor.execute("SELECT Symbol FROM PeriodicTable WHERE Name = :Name", {'Name': name});
        name_tuple = self.cursor.fetchone();
        if name_tuple == None:
            symbol = None;
        else:
            # Take the name out of the tuple
            symbol = name_tuple[0];
        # Return the value
        return symbol;

    def get_charge_suffix_PeriodicTable(self, Suffix):
        self.cursor.execute("SELECT Charge FROM PeriodicTable WHERE Suffix = :Suffix", {'Suffix': Suffix});
        # Read the rows that containing that element name
        type_tuple = self.cursor.fetchone();
        if type_tuple == None:
            charges = None;
        else:
            # Take the type out of the tuple
            charges = type_tuple[0];
            charges = charges.split(",")

        return charges

    def get_charge_sym_polyatomic(self, symbol):
        self.cursor.execute("SELECT Charge FROM PolyatomicTable WHERE Symbol = :Symbol", {'Symbol': symbol});
        # Read the rows that containing that element name
        type_tuple = self.cursor.fetchone();
        if type_tuple == None:
            charges = None;
        else:
            # Take the type out of the tuple
            charges = type_tuple[0];
            charges = charges.split(",")
        return charges

    def get_charge_name_polyatomic(self, name):
        self.cursor.execute("SELECT Charge FROM PolyatomicTable WHERE Name = :Name", {'Name': name});
        # Read the rows that containing that element name
        type_tuple = self.cursor.fetchone();
        if type_tuple == None:
            charges = None;
        else:
            # Take the type out of the tuple
            charges = type_tuple[0];
            charges = charges.split(",")
        return charges

    def get_molar_mass_periodicTable(self, symbol):
        self.cursor.execute("SELECT Mass FROM PeriodicTable WHERE Symbol = :Symbol", {'Symbol': symbol});
        mass_tuple = self.cursor.fetchone();
        if mass_tuple == None:
            mass = None;
        else:
            mass = mass_tuple[0];

        return mass

    def get_molar_mass_polyatomicTable(self, symbol):
        self.cursor.execute("SELECT Mass FROM PolyatomicTable WHERE Symbol = :Symbol", {'Symbol': symbol});
        mass_tuple = self.cursor.fetchone();
        if mass_tuple == None:
            mass = None;
        else:
            mass = mass_tuple[0];

        return mass



if __name__ == "__main__":
    main();
