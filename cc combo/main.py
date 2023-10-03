def extract_credit_card_info(card_info):
    parts = card_info.split('|')
    cc = parts[0]
    mes = parts[1]
    ano = parts[2]
    cvv = parts[3]
    return cc, mes, ano, cvv

with open("cc combo/cc.txt", "r") as file:
    cc_combo = file.readlines()

with open("cc combo/ccmain.txt", "w") as file1:
    for lista in cc_combo:
        cc, mes, ano, cvv = extract_credit_card_info(lista.strip())  
        new_lista = f"{cc}|12|{ano}|{cvv}"
        file1.write(new_lista + '\n') 

print("Credit card information has been processed and saved to ccmain.txt.")
