from flask import Flask, render_template, request
import pickle


# setup application
app = Flask(__name__)

def prediction(lst):
    filename = 'model/predictor.pickle'
    with open(filename, 'rb') as file:
        model = pickle.load(file)
    pred_value = model.predict([lst])
    return pred_value

@app.route('/')
def home():
    return "Hello World"


@app.route('/predict', methods=['POST',"GET"])
def predict():
    Male = 0
    Female = 0

    pred_value = -1
    print(request.method)
    if request.method == 'POST':
    
        Salary = int(request.form['Salary'])
        PerformanceScore = int(request.form['PerformanceScore'])
        EngagementSurvey = float(request.form['EngagementSurvey'])
        SpecialProjectsCount= int(request.form['SpecialProjectsCount'])
        DaysLateLast30= int(request.form['DaysLateLast30'])
        Absences = int(request.form['Absences'])
        Position= request.form['Position']
        
        DateOfHire= request.form['DateOfHire']
        #get separatly year month and day
        DateOfHire = DateOfHire.split('-')
        DateOfHireYear = int(DateOfHire[0])
        DateOfHireMonth = int(DateOfHire[1])
        DateOfHireDay = int(DateOfHire[2])
        
        DateOfBirth= request.form['DateOfBirth']
        #get separatly year month and day
        DateOfBirth = DateOfBirth.split('-')
        DateOfBirthYear = int(DateOfBirth[0])
        DateOfBirthMonth = int(DateOfBirth[1])
        DateOfBirthDay = int(DateOfBirth[2])
        
        getGender = request.form['Gender']
        #Gender check
        if getGender == 'Female':
            Female = 1
        else:
            Male = 1
        
        MaritalStatus= request.form['MaritalStatus']
        Department= request.form['Department']
        ManagerName= request.form['ManagerName']
        RecruitmentSource= request.form['RecruitmentSource']

        position_list=['Architect','Director','Engineer','Manager','Other','TechnicianI','TechnicianII']
        Marital_Status_list=['Divorced','Married','Separated','Single','Widowed']
        Department_list=['AdminOffices','ExecutiveOffice','IT/IS','Production','Sales','SoftwareEngineering']
        ManagerName_list=['AlexSweetwater',
       'AmyDunn', 'BoardofDirectors', 'BrandonR.LeBlanc',
       'BrannonMiller', 'BrianChampaigne', 'DavidStanley',
       'DebraHoulihan', 'ElijiahGray', 'EricDougall',
       'JanetKing', 'JenniferZamora', 'JohnSmith',
       'KelleySpirea', 'KetsiaLiebig', 'KissySullivan',
       'LynnDaneault', 'MichaelAlbert', 'PeterMonroe',
       'SimonRoup', 'WebsterButler']
        RecruitmentSource_list=['CareerBuilder',
       'DiversityJobFair', 'EmployeeReferral', 'GoogleSearch',
       'Indeed', 'LinkedIn', 'On-lineWebApplication', 'Other',
       'Website']
       
        def traverse_list(lst, value):
            for item in lst:
                if item == value:
                    feature_list.append(1)
                else:
                    feature_list.append(0)
        
        feature_list = []
        feature_list.append(Salary)
        feature_list.append(PerformanceScore)
        feature_list.append(EngagementSurvey)
        feature_list.append(SpecialProjectsCount)
        feature_list.append(DaysLateLast30)
        feature_list.append(Absences)
        feature_list.append(DateOfBirthYear)
        feature_list.append(DateOfBirthMonth)
        feature_list.append(DateOfBirthDay)
        feature_list.append(DateOfHireYear)
        feature_list.append(DateOfHireMonth)
        feature_list.append(DateOfHireDay)
        traverse_list(position_list,Position)
        feature_list.append(Female)
        feature_list.append(Male)
        traverse_list(Marital_Status_list, MaritalStatus )
        traverse_list(Department_list, Department)
        traverse_list(ManagerName_list, ManagerName)
        traverse_list(RecruitmentSource_list, RecruitmentSource)

        # print(feature_list)
        pred_value = prediction(feature_list)
        print(pred_value)
    return render_template('index.html', pred_value=pred_value)



if __name__ == '__main__':
    app.run(debug=True)