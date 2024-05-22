annual_salary = float(input("Ingrese su salario anual: "))
portion_saved = float(input("Ingrese el porcentaje de su salario para ahorrar, como un decimal: "))
total_cost = float(input("Ingresa el costo de la casa de sus sueños: "))

portion_down_payment = 0.25*total_cost
current_savings = 0
r = 0.04
monthly_salary = annual_salary/12
months = 0

while current_savings < portion_down_payment:
    current_savings += current_savings*r/12
    current_savings += monthly_salary*portion_saved
    months += 1
print("la cantidad de meses es:", months)