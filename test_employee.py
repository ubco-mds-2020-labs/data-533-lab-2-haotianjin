import hospital.employee.doctor as doc
import hospital.employee.nurse as ns

## For doctor module:
## Initialize doctor with his/her name, age, phone number, annual salary, and number of treated patients.
doctor1 = doc.Doctor("David Jones", 35, '778-935-1748', 250000, 2130)

## Show information about the doctor.
doctor1.display()

## Change doctor's phone number.
doctor1.change_in_phone_num('604-172-3846')

## Show information about the doctor after change in phone number.
doctor1.display()

## Change doctor's salary.
doctor1.change_in_salary(370000)

## Show information about the doctor after change in salary.
doctor1.display()

## Show amount of bonus this doctor earned and also the total amount of salary.
doctor1.bonus()

## For nurse module:
## Initialize nurse with his/her name, age, phone number, annual salary, and number of treated patients.
nurse1 = ns.Nurse("Jane Stone", 32, '778-627-8462', 45000, 1755)

## Show information about the nurse.
nurse1.display()

## Change nurse's phone number.
nurse1.change_in_phone_num('604-172-4817')

## Show information about the nurse after change in phone number.
nurse1.display()

## Change doctor's salary.
nurse1.change_in_salary(48000)

## Show information about the doctor after change in salary.
nurse1.display()

## Show amount of bonus this doctor earned and also the total amount of salary.
nurse1.bonus()