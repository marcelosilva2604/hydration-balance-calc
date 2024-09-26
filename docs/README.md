###Hydration Balance Calculation Project###
#Overview
The Hydration Balance Calculation Project is a Python-based application designed to assist healthcare professionals in calculating and monitoring the hydration balance of patients, particularly in neonatal and pediatric intensive care settings. Proper hydration management is critical, especially in vulnerable populations like newborns, where small variations in fluid intake and loss can significantly impact health outcomes.

This application uses the Tkinter library to create a user-friendly graphical interface (GUI) that simplifies the input of patient data and vital signs, automates hydration calculations, and displays results in an intuitive format for healthcare professionals.

#Features
Graphical User Interface (GUI): A clean, simple, and intuitive interface built with Tkinter, designed to streamline data entry and present the hydration balance results.

Patient Data Entry: Users can input basic patient information:

Patient Name: Identifies the patient.
Bed Number: The bed number, which must be numeric for validation purposes.
Patient Weight: The patient's weight in kilograms, validated to ensure it does not exceed 5 kg (useful in neonatal care).
Vital Sign Measurement Entry: The program allows users to record essential patient measurements such as:

Body Temperature
Incubator Temperature
Heart Rate
Respiratory Rate
Mean Arterial Blood Pressure (MAP)
Oxygen Saturation
Blood Glucose
Hydration Balance Calculation: The application computes the patient's hydration balance based on fluid intake and fluid losses:

Fluid Intake: Captures values for dietary intake, IV fluids, and medications.
Fluid Loss: Records fluid losses through diuresis (urine output), gastric residuals, vomiting (emesis), and bowel movements (evacuations).
Net Hydration Balance: Calculates the net fluid balance (intake minus losses), expressed both in total milliliters (ml) and milliliters per kilogram (ml/kg).
Dynamic Result Display: The results are displayed in an organized, detailed report that summarizes the fluid intake, losses, and final hydration balance.

Copy Functionality: Users can copy the hydration balance results to the clipboard for documentation or further analysis.

New Patient Function: After completing one patient's calculation, the program allows users to clear all fields and enter a new patient's data without restarting the application.

#Installation
Prerequisites
Python 3: Ensure that Python 3 is installed on your system. You can download it from here.

Tkinter: Tkinter is included with many Python distributions. If it's not installed, you can install it using the following command:

sudo apt-get install python3-tk


#Installation Steps
Clone this repository to your local machine:

git clone https://github.com/marcelosilva2604/hydration-balance-calc.git

Navigate to the project directory:

cd hydration-balance-calc

Install the required dependencies: The necessary libraries are listed in the requirements.txt file. To install them, run:


pip install -r requirements.txt
Run the application: To start the application, use:

python3 project.py

#Usage
Once the application is running:

Enter Patient Information: Input the patient's name, bed number, and weight.
Record Measurements: Enter vital sign data, such as temperature, heart rate, and oxygen saturation, in their respective fields.
Fluid Balance Data: Input values for fluid intake (e.g., diet, IV fluids) and fluid loss (e.g., diuresis, gastric residuals).
Calculate Hydration Balance: Click the "Calcular" button to compute the patient's hydration balance.
Copy Results: Click the "Copiar Valores" button to copy the results for further use in reports or other documentation.
New Patient: To start over with a new patient, click "Novo Paciente" to clear all input fields.
#Testing
This project includes unit tests that validate the behavior of key functions, such as patient name input, bed number validation, and weight limits. The tests are written using pytest.

To run the tests, use the following command:


pytest

Ensure that pytest is installed using:

pip install pytest

#License
This project is licensed under the MIT License, which allows free use, modification, and distribution of the software, as long as the original authors are credited.