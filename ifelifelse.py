num_of_patients = 21
if num_of_patients % 3 == 0 and num_of_patients % 7 == 0:
    print(f"{num_of_patients}은 3과 7의 배수.")
elif num_of_patients % 3 == 0:
    print(f"{num_of_patients}은 3의 배수.")
elif num_of_patients % 7 == 0:
    print(f"{num_of_patients}은 7의 배수")
else:
    print(f"{num_of_patients}은 3의 배수, 7의 배수가 아님.")
