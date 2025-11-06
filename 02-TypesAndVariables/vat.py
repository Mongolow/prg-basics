cena_z_Vat = float(input("podaj cenę "))
Vat = cena_z_Vat / 100 * 23 
do_zapłaty = cena_z_Vat - Vat
print(f"płacisz {do_zapłaty}")
