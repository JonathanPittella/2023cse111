from formula import parse_formula, FormulaError
class FormulaError(ValueError):
    pass

SYMBOL_INDEX = 0
QUANTITY_INDEX = 1
NAME_INDEX = 0
ATOMIC_MASS_INDEX = 1

def make_periodic_table():
    periodic_table_lst = [
    ["Ac", "Actinium", 227.0],
    ["Ag", "Silver", 107.8682],
    ["Al", "Aluminum", 26.9815386],
    ["Am", "Americium", 243.0],
    ["Ar", "Argon", 39.948],
    ["As", "Arsenic", 74.921595],
    ["At", "Astatine", 210.0],
    ["Au", "Gold", 196.966569],
    ["B", "Boron", 10.81],
    ["Ba", "Barium", 137.327],
    ["Be", "Beryllium", 9.0122],
    ["Bh", "Bohrium", 270.0],
    ["Bi", "Bismuth", 208.9804],
    ["Bk", "Berkelium", 247.0],
    ["Br", "Bromine", 79.904],
    ["C", "Carbon", 12.011],
    ["Ca", "Calcium", 40.078],
    ["Cd", "Cadmium", 112.414],
    ["Ce", "Cerium", 140.116],
    ["Cf", "Californium", 251.0],
    ["Cl", "Chlorine", 35.453],
    ["Cm", "Curium", 247.0],
    ["Cn", "Copernicium", 285.0],
    ["Co", "Cobalt", 58.933194],
    ["Cr", "Chromium", 51.9961],
    ["Cs", "Cesium", 132.90545196],
    ["Cu", "Copper", 63.546],
    ["Db", "Dubnium", 270.0],
    ["Ds", "Darmstadtium", 281.0],
    ["Dy", "Dysprosium", 162.5],
    ["Er", "Erbium", 167.259],
    ["Es", "Einsteinium", 252.0],
    ["Eu", "Europium", 151.964],
    ["F", "Fluorine", 18.998403163],
    ["Fe", "Iron", 55.845],
    ["Fl", "Flerovium", 289.0],
    ["Fm", "Fermium", 257.0],
    ["Fr", "Francium", 223.0],
    ["Ga", "Gallium", 69.723],
    ["Gd", "Gadolinium", 157.25],
    ["Ge", "Germanium", 72.63],
    ["H", "Hydrogen", 1.008],
    ["He", "Helium", 4.0026],
    ["Hf", "Hafnium", 178.49],
    ["Hg", "Mercury", 200.592],
    ["Ho", "Holmium", 164.93033],
    ["Hs", "Hassium", 270.0],
    ["I", "Iodine", 126.90447],
    ["In", "Indium", 114.818],
    ["Ir", "Iridium", 192.217],
    ["K", "Potassium", 39.0983],
    ["Kr", "Krypton", 83.798],
    ["La", "Lanthanum", 138.90547],
    ["Li", "Lithium", 6.94],
    ["Lr", "Lawrencium", 262.0],
    ["Lu", "Lutetium", 174.9668],
    ["Lv", "Livermorium", 293.0],
    ["Mc", "Moscovium", 288.0],
    ["Md", "Mendelevium", 258.0],
    ["Mg", "Magnesium", 24.305],
    ["Mn", "Manganese", 54.938044],
    ["Mo", "Molybdenum", 95.95],
    ["Mt", "Meitnerium", 276.0],
    ["N", "Nitrogen", 14.007],
    ["Na", "Sodium", 22.99],
    ["Nb", "Niobium", 92.90637],
    ["Nd", "Neodymium", 144.242],
    ["Ne", "Neon", 20.1797],
    ["Nh", "Nihonium", 284.0],
    ["Ni", "Nickel", 58.6934],
    ["No", "Nobelium", 259.0],
    ["Np", "Neptunium", 237.0],
    ["O", "Oxygen", 15.999],
    ["Og", "Oganesson", 294.0],
    ["Os", "Osmium", 190.23],
    ["P", "Phosphorus", 30.973761998],
    ["Pa", "Protactinium", 231.03588],
    ["Pb", "Lead", 207.2],
    ["Pd", "Palladium", 106.42],
    ["Pm", "Promethium", 145.0],
    ["Po", "Polonium", 209.0],
    ["Pr", "Praseodymium", 140.90766],
    ["Pt", "Platinum", 195.084],
    ["Pu", "Plutonium", 244.0],
    ["Ra", "Radium", 226.0],
    ["Rb", "Rubidium", 85.4678],
    ["Re", "Rhenium", 186.207],
    ["Rf", "Rutherfordium", 267.0],
    ["Rg", "Roentgenium", 280.0],
    ["Rh", "Rhodium", 102.90549],
    ["Rn", "Radon", 222.0],
    ["Ru", "Ruthenium", 101.07],
    ["S", "Sulfur", 32.06],
    ["Sb", "Antimony", 121.76],
    ["Sc", "Scandium", 44.955912],
    ["Se", "Selenium", 78.971],
    ["Sg", "Seaborgium", 271.0],
    ["Si", "Silicon", 28.0855],
    ["Sm", "Samarium", 150.36],
    ["Sn", "Tin", 118.71],
    ["Sr", "Strontium", 87.62],
    ["Ta", "Tantalum", 180.94788],
    ["Tb", "Terbium", 158.92535],
    ["Tc", "Technetium", 98.0],
    ["Te", "Tellurium", 127.6],
    ["Th", "Thorium", 232.0377],
    ["Ti", "Titanium", 47.87],
    ["Tl", "Thallium", 204.38],
    ["Tm", "Thulium", 168.93422],
    ["Ts", "Tennessine", 294.0],
    ["U", "Uranium", 238.02891],
    ["V", "Vanadium", 50.9415],
    ["W", "Tungsten", 183.84],
    ["Xe", "Xenon", 131.293],
    ["Y", "Yttrium", 88.90584],
    ["Yb", "Ytterbium", 173.04],
    ["Zn", "Zinc", 65.38],
    ["Zr", "Zirconium", 91.224]
]

    table_list = []
    for symbol, name, atomic_mass in periodic_table_lst:
        table_list.append([symbol, name, float(atomic_mass)])
    return table_list

def compute_molar_mass(symbol_quantity_list, periodic_table_lst):
    total_molar_mass = 0
    for symbol, quantity in symbol_quantity_list:
        found = False
        for element_data in periodic_table_lst:
            element_symbol = element_data[SYMBOL_INDEX]
            element_atomic_mass = float(element_data[ATOMIC_MASS_INDEX])
            if symbol == element_symbol:
                total_molar_mass += element_atomic_mass * quantity
                found = True
                break
        if not found:
            print(f"Error: Element {symbol} not found in the periodic table.")
            return None
    return total_molar_mass

def main():
    periodic_table_lst = make_periodic_table()

    for element in periodic_table_lst:
        name = element[NAME_INDEX]
        act_mass = element[ATOMIC_MASS_INDEX]
        print(f"{name}: {act_mass}")

    try:
        compound = input("Enter a chemical compound: ")
        symbol_quantity_list = parse_formula(compound, dict((element[SYMBOL_INDEX], element) for element in periodic_table_lst))
        molar_mass = compute_molar_mass(symbol_quantity_list, periodic_table_lst)
        print(f"The molar mass of {compound} is {molar_mass:.3f} g/mol.")
    except FormulaError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
