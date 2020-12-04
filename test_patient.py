import hospital.patient.patients as p
import hospital.patient.covid_patient as cp

#For Patient Module
#Initialize the general patient with name, age, the date they come to hospital, height, weight and their symptom
p1 = p.GeneralPatient("Emma Jones", 25, "11/23/2020",1.66, 60, ['cold'])

#Show information about the patient
p1.display()

#Calculate patient's BMI
p1.bmi()

#Test whether patient is ready to leave the hospital
p1.full_recovered()

#Patient gain other disease
p1.addition_symptom("diabetes")

#Display patient current disesase
p1.display()

#Patient can also gain multiple disesase at the same time
p1.addition_symptom(["back pain","headache"])

#Treated the patient
p1.recovered_symptom("cold")
p1.display()

#The patient will not be mistreated with disease they do not have
p1.recovered_symptom("Pneumonoultramicroscopicsilicovolcanoconiosis")

#Treaded multiple disease at the same time
p1.recovered_symptom(["back pain","headache","diabetes"])

#Healthy patient can leave the hospital
p1.full_recovered()

#Covid-patient module
#Initialize the general patient with name, age, the date they come to hospital, height, weight and their symptom
p2 = cp.CovidPatient("Joe Mason", 70, "12/01/2020", 1.90, 100, "fever")

#Display patient info
p2.display()

#Calculate patient's BMI
p2.bmi()

#Whether the patient is fully recovered and ready to leave
p2.full_recovered()

#The patient get extra disease 
p2.addition_symptom("vomitting")
p2.display()

#The patient get treated
p2.recovered_symptom(["vomitting","fever"])
p2.display()

#The patient cannot leave the hospial with a positive covid result, even the symptom has all treated
p2.full_recovered()

#Patient's covid test has been negative, changing the test result
p2.test_result("negative")
p2.display()

#Test whether patient is fully recovered and ready to leave
p2.full_recovered()
