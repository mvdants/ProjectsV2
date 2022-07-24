
symbols_data = "../data/list_company_symbols"

with open(symbols_data, 'r') as file:
    lines = file.readlines()
    file.close()

lines.sort()

with open("../data/list_company_symbols", "w") as file:
    file.writelines(lines)
    file.close()
