import time
cyber=[{"Communicative English":3,"Engineering Mathematics":4,"Engineering Physics":3,"Engineering Chemistry":3,"Programming in C":3,"Engineering Graphics":4,"Physics and Chemistry Lab":2,"C Programming Lab":2},
   {"Technical English":3,"Engineering maths 2":4,"Physics for information Science":3,"Environmental Science":3,"BCME":3,"PSPP":3,"APES LAB":2,"PSPP LAB":2,"EP LAB":2,"NCC/NSS/YRC/NSO":1},
   {"Discrete Mathematics":4,"Programming & Data Structures in C":3,"Object Oriented Programming":3,"DFC":3,"ICT":3,"DBMS":3,"PDS LAB":2,"OOPS LAB":2,"DBMS LAB":2},
   {"Probability & Queueing Theory":4,"Computer Architecture":3,"Linux Operating System":3,"Database Security":3,"Cyber Laws and Ethics":3,"Professional Ethics":3,"Linux Operating System Laboratory":2,"Programming for Security Professionals Laboratory":2},
   {"Mathematical Foundation for Cyber Security System":4,"Cyber Security and Digital Forensics":3,"Ethical Hacking":3,"Intrusion Detection Systems":3,"Open Elective-1":3,"Ethical Hacking Laboratory":2,"Cyber Forensics Laboratory":2},
   {"Information Warfare":3,"Cryptography and Network Security":3,"Vulnerability Discovery and Exploit Development":3,"Security in Cloud Computing":3,"Professional Elective-1":3,"Security Laboratory":2,"Network Threats and Attacks Laboratory":2,"Professional Communication":1,"Mini Project":2},
   {"Biometric Security":3,"Cyber Threat Intelligence":3,"Open Elective-2":3,"Professional Elective-2":3,"Professional Elective-3":3,"Biometric Image Processing Laboratory":2,"Security and Penetration Testing Laboratory":2,"Project Work-Phase 1":2,"Internship":1},
   {"Professional Elective-4":3,"Professional Elective-5":3,"Project Work-Phase 2":6}]

aids=[{"Communicative English":3,"Engineering Mathematics":4,"Engineering Physics":3,"Engineering Chemistry":3,"Programming in C":3,"Engineering Graphics":4,"Physics and Chemistry Lab":2,"C Programming Lab":2},
   {"Technical English":3,"Engineering maths 2":4,"Physics for information Science":3,"Environmental Science":3,"BCME":3,"PSPP":3,"APES LAB":2,"PSPP LAB":2,"EP LAB":2,"NCC/NSS/YRC/NSO":1},
   {"Discrete Mathematics":4,"Programming & Data Structures":3,"Computational Intelligence Essentials":3,"Digital Principles and System Design":3,"Operating Systems Concepts":3,"Computational Intelligence Essentials Laboratory":2,"Programming and Data Structures Laboratory":2},
   {"Numerical Linear Algebra ":4,"Database Management Systems and Mining":3,"Data Communication and Networks":3,"Data Science Concepts":3,"Professional Ethics":3,"Database Management Systems and Mining Laboratory":2,"Data Science Laboratory":2},
   {"Probability Random Processes and Statistics":4,"Software Engineering and Management":3,"R Programming in Data Science":3,"Professional Elective – I":3,"Open Elective-1":3,"Software Engineering and Management Laboratory":2,"R Programming in Data Science Laboratory":2},
   {" Digital Image Processing":3,"Artificial Intelligence":3,"Big Data Analytics":3,"Professional Elective – II ":3,"Professional Elective – III":3,"Big Data Analytics Laboratory":2,"Artificial Intelligence Laboratory":2,"Professional Communication":1,"Mini Project":2},
   {"Statistical Approaches for Data Science":3,"Virtual Reality":3,"Deep Learning and its Applications ":3,"Professional Elective – IV":3,"Open Elective – II ":3,"Statistical Approaches for Data Science Laboratory ":2,"Virtual reality Laboratory":2,"Project Work-Phase 1":2,"Internship":1},
   {"Professional Elective-5":3,"Professional Elective-6":3,"Project Work-Phase 2":6}]

eee=[{"Communicative English":3,"Engineering Mathematics":4,"Engineering Physics":3,"Engineering Chemistry":3,"PSPP":3,"BCME":3,"Physics and Chemistry Lab":2,"Problem solving and Python Programming Laboratory ":2},
   {"Technical English":3,"Engineering maths 2":4,"Physics for Electronics Engineering":3,"Environmental Science":3,"Programming in C":3,"Engineering Graphics":4,"C Programming Laboratory":2,"Engineering Practices Laboratory":2,"Applied Physics and Environmental Chemistry Laboratory":2,"NCC/NSS/YRC/NSO":1},
   {"Transforms and Partial Differential Equations":4,"Digital Electronics":3,"Electrical Machines – I":3,"Analog Electronics":3,"Circuit Theory":3,"Analog Electronics Laboratory":2,"Electrical Machines Laboratory–I":2,"Electric Circuits Laboratory":2},
   {"Numerical Methods":4,"Electrical Machines – II":3,"Transmission and Distribution":3,"Measurements and Instrumentation":3,"Electromagnetic Theory":3,"Professional Ethics":3,"Electrical Machines Laboratory–II":2,"Technical Seminar":1},
   {"Power System Analysis":3,"Microprocessors and Microcontrollers":3,"Power Electronics":3,"Control Systems":3,"Digital Signal Processing":3,"Open Elective I":3,"Control and Instrumentation Laboratory":2,"Microprocessors and Microcontrollers Laboratory":2},
   {"Solid State Drives":3,"Power System Operation and Control":3,"Design of Electrical Apparatus":3,"Professional Elective – I":3,"Professional Elective – II":3,"Power Electronics Laboratory":2,"Power System Simulation Laboratory":2,"Mini Project":2,"Professional Communication":1},
   {"High Voltage Engineering":3,"Renewable Energy Systems":3,"Protection and Switchgear":3,"Professional Elective – III":3,"Professional Elective – IV":3,"Open Elective – II ":3,"Renewable Energy Systems Laboratory":2,"Project Work-Phase 1":2,"Internship":1},
   {"Professional Elective-V":3,"Professional Elective-VI":3,"Project Work-Phase 2":6}]

ece=[{"Communicative English":3,"Engineering Mathematics":4,"Engineering Physics":3,"Engineering Chemistry":3,"Programming in C":3,"Engineering Graphics":4,"Physics and Chemistry Lab":2,"C Programming Lab":2},
   {"Technical English":3,"Engineering maths 2":4,"Physics for Electronics Engineering":3,"Environmental Science":3,"BCME":3,"PSPP":3,"APES LAB":2,"PSPP LAB":2,"EP LAB":2,"NCC/NSS/YRC/NSO":1},
   {"Transforms and Partial Differential Equations":4,"Electronic Devices and circuits":3,"Analog Electronics-I":3,"Signals and Systems":3,"Digital Electronics":3,"Control Systems Engineering":3,"Electronic Devices and circuits Laboratory":2,"Analog and Digital Electronics Laboratory":2},
   {"Probability and Random Processes":4,"Linear Integrated Circuits":3,"Analog Electronics-II":3,"Communication Theory":3,"Electromagnetic Fields":3,"Professional Ethics":3,"Linear Integrated Circuits Laboratory":2,"Circuits Design and Simulation Laboratory":2},
   {"Discrete Time Signal Processing":3,"Digital Communication":3,"Communication Networks":3,"Transmission Lines and RF Systems":3,"Professional Elective-I":3,"Open Elective-I":3,"Digital Signal Processing Laboratory":2,"Communication Systems and Networks Laboratory":2,"Professional Communication":1},
   {"Microprocessors and Microcontrollers":3,"VLSI Design":3,"Embedded and Real Time Systems":3,"Wireless Networks":3,"Professional Elective-II":3,"Professional Elective -III":3,"Microcontrollers and Embedded Laboratory":2,"VLSI Design Laboratory":2,"Mini Project":2},
   {"Antennas and Microwave Engineering":3,"Optical Communication":3,"Wireless Communication":3,"Digital Image Processing":3,"Open Elective-II":3,"Advanced Communication Laboratory":2,"Project Work-Phase 1":2,"Internship":1},
   {"Professional Elective-4":3,"Professional Elective-5":3,"Project Work-Phase 2":6}]

cse=[{"Communicative English":3,"Engineering Mathematics":4,"Engineering Physics":3,"Engineering Chemistry":3,"Programming in C":3,"Engineering Graphics":4,"Physics and Chemistry Lab":2,"C Programming Lab":2},
   {"Technical English":3,"Engineering maths 2":4,"Physics for information Science":3,"Environmental Science":3,"BCME":3,"PSPP":3,"APES LAB":2,"PSPP LAB":2,"EP LAB":2,"NCC/NSS/YRC/NSO":1},
   {"Discrete Mathematics":4,"Programming & Data Structures in C":3,"Object Oriented Programming":3,"DFC":3,"Software Engineering":3,"Operating Systems":3,"PDS LAB":2,"OOPS LAB":2,"Operating Systems Laboratory":2},
   {"Probability & Queueing Theory":4,"Computer Architecture":3,"Database Management System ":3,"Design and Analysis of Algorithm":3,"Object Oriented Analysis and Design":3,"Professional Ethics":3,"Database Management System Laboratory ":2,"Object Oriented Analysisand Design Laboratory":2},
   {"Computer Networks":3,"Automata Theory":4,"Web Technology":3,"Data Warehousing and Data Mining":3,"Open Elective-1":3,"Web Technology Laboratory":2,"Networks Laboratory":2},
   {"Mobile Computing":3,"Compiler Design":3,"Software Testing":3,"Grid and Cloud Computing":3,"Professional Elective-1":3,"Mobile Application Development Laboratory":2,"Compiler Design Laboratory":2,"Professional Communication":1,"Mini Project":2},
   {"Cryptography and Network Security":3,"Artificial Intelligence":3,"Open Elective-2":3,"Professional Elective-2":3,"Professional Elective-3":3,"Security Laboratory":2,"Artificial Intelligence Laboratory":2,"Project Work-Phase 1":2,"Internship":1},
   {"Professional Elective-4":3,"Professional Elective-5":3,"Project Work-Phase 2":6}]

it=[{"Communicative English":3,"Engineering Mathematics":4,"Engineering Physics":3,"Engineering Chemistry":3,"Programming in C":3,"Engineering Graphics":4,"Physics and Chemistry Lab":2,"C Programming Lab":2},
   {"Technical English":3,"Engineering maths 2":4,"Physics for information Science":3,"Environmental Science":3,"BCME":3,"PSPP":3,"APES LAB":2,"PSPP LAB":2,"EP LAB":2,"NCC/NSS/YRC/NSO":1},
   {"Discrete Mathematics":4,"Data Structures and Algorithms":3," Digital Principles and System Design":3,"Object Oriented Programming":3,"Analog and Digital Communication":3,"Information Technology Essentials":3,"Data Structures Laboratory":2,"Object Oriented Programming Laboratory":2,"Digital system and communication laboratory":2},
   {"Probability and Statistics":4,"Principles of Compiler Design":3,"Operating Systems Concepts":3,"Database Management System":3,"Professional Ethics":3,"Principles of Operating Systems Laboratory":2,"Compiler Laboratory":2,"Database Management System Laboratory":2},
   {"Web Technology":3,"Software Engineering":3,"Computer Architecture":3,"Computer Networks":3,"Professional Elective - I":3,"Open Elective-1":3,"Web Technology Laboratory":2,"Networks Laboratory":2},
   {"Mobile Communication":3,"Computational Intelligence":3,"Object Oriented Analysis and Design":3,"Professional Elective - II ":3,"Professional Elective - III":3,"Object Oriented Analysis and Design Laboratory":2,"Mobile Application Development Laboratory":2,"Professional Communication":1,"Mini Project":2},
   {"Cloud Computing":3,"Software Project Management":3,"Cryptography and Network Security":3,"Professional Elective - IV":3,"Open Elective – II":3,"FOSS and Cloud Computing Laboratory":2,"Security Laboratory":2,"Project Work-Phase 1":2,"Internship":1},
   {"Professional Elective-5":3,"Professional Elective-6":3,"Project Work-Phase 2":6}]

civil=[{"Communicative English":3,"Engineering Mathematics":4,"Engineering Physics":3,"Engineering Chemistry":3,"Problem Solving and Python Programming":3,"Basic Electrical and Electronics Engineering":3,"Physics and Chemistry Lab":2,"Problem Solving and Python Programming Laboratory":2},
   {"Technical English":3,"Engineering maths 2":4,"Physics for Civil Engineering":3,"Environmental Science and Engineering":3,"Engineering Graphics":4,"Programming in C":3,"APES LAB":2,"C Programming Laboratory":2,"EP LAB":2,"NCC/NSS/YRC/NSO":1},
   {"Transforms and Partial Differential Equations":4,"Applied Mechanics":3,"Fluid Mechanics":3,"Surveying":3,"Construction Materials":3,"Applied Geology":3,"Construction Materials Laboratory":2,"Surveying Laboratory":2},
   {"Numerical Methods":4,"Strength of Materials":3,"Applied Hydraulic Engineering":3,"Soil Mechanics":3,"Construction Techniques and Practices":3,"Professional Elective-1":3,"Strength of Materials Laboratory":2,"Hydraulic Engineering Laboratory":2},
   {"Design of Reinforced Cement Concrete Elements":4,"Structural Analysis-1":3,"Highway Engineering":3,"Foundation Engineering":3,"Professional Elective - II":3,"Open Elective-1":3,"Soil Mechanics Laboratory":2,"Highway Engineering Laboratory":2,"Survey Camp":2,"Professional Communication":1},
   {"Design of Steel structural elements":4,"Structural Analysis II":3,"Railways, Airports, Docks and Harbour Engineering":3,"Water Supply and Waste water Engineering":3,"Professional Elective - III":3,"Water and Waste water Analysis Laboratory":2,"Mini Project":2},
   {"Estimation, Costing and valuation Engineering":3,"Irrigation Engineering":3,"Structural Dynamics":3,"Professional Elective - IV":3,"Open Elective – II":3,"Computer Aided Design and Drafting Laboratory":2,"Project Work-Phase 1":2,"Internship":1},
   {"Professional Elective-5":3,"Professional Elective-6":3,"Project Work-Phase 2":6}]

mech=[{"Communicative English":3,"Engineering Mathematics":4,"Engineering Physics":3,"Engineering Chemistry":3,"Problem Solving and Python Programming":3,"Basic Electrical and Electronics Engineering":3,"Physics and Chemistry Lab":2,"Problem Solving and Python Programming Laboratory":2},
   {"Technical English":3,"Engineering maths 2":4,"Physics for Mechanical Engineering":3,"Environmental Science and Engineering":3,"Engineering Graphics":4,"Programming in C":3,"APES LAB":2,"C Programming Laboratory":2,"EP LAB":2,"NCC/NSS/YRC/NSO":1},
   {"Transforms and Partial Differential Equations":4,"Engineering Mechanics":3,"Engineering Thermodynamics":3,"Manufacturing Processes":3,"Fluid Mechanics and Machinery":3,"Manufacturing Technology Laboratory":2,"Fluid Mechanics and Machinery Laboratory":2},
   {"Statistics and Numerical Methods":4,"Kinematics of Machinery":3,"Metal Cutting and Machine Tools":3,"Strength of Materials":3,"Applied Thermodynamics":3,"Professional Ethics":3,"Computer Aided Machine Drawing Practices Laboratory":2,"Strength of Materials Laboratory":2},
   {"Thermal Engineering":3,"Design of Machine Elements ":3,"Metrology and Measurements":3,"Dynamics of Machines":3,"Professional Elective - I":3,"Open Elective - I":3,"Dynamics and Metrology Laboratory":2,"Thermal Engineering Laboratory":2,"Professional Communication":1},
   {"Design of Transmission System ":3,"Heat and Mass Transfer":4,"Finite Element Analysis ":4,"Professional Elective - II":3,"Professional Elective - III":3,"CAD / CAM and Analysis Laboratory":2,"Heat Transfer Laboratory":2,"Design and Fabrication Project":2},
   {"Electric Vehicles":3,"Process Planning and Cost Estimation":3,"Mechatronics and Automation":3,"Professional Elective - IV":3,"Professional Elective - V":3,"Open Elective – II":3,"Mechatronics and Automation Laboratory":2,"Project Work-Phase 1":2,"Internship":1},
   {"Green Manufacturing":3,"Professional Elective-6":3,"Project Work-Phase 2":6}]

mde=[{"Communicative English":3,"Engineering Mathematics":4,"Engineering Physics":3,"Engineering Chemistry":3,"Programming in C":3,"Engineering Graphics":4,"Physics and Chemistry Lab":2,"C Programming Lab":2},
   {"Technical English":3,"Engineering maths 2":4,"Physics for Electronics Engineering":3,"Environmental Science":3,"BCME":3,"PSPP":3,"APES LAB":2,"PSPP LAB":2,"EP LAB":2,"NCC/NSS/YRC/NSO":1},
   {"Transforms and Partial Differential Equations":4,"Electrical and Electronic Measurements ":3,"Analog Electronics":3,"Digital Electronics":3,"Anatomy and Human Physiology":3,"Signals and Systems":3,"Instrumentation Laboratory":2,"Analog and Digital Electronics Laboratory":2},
   {"Discrete-Time Signal Processing":3,"Linear Integrated Circuits":3,"Electrical Engineering ":3,"BioMaterials and Artificial Organs":3,"Control Systems Engineering":3,"Professional Ethics":3,"Digital Signal Processing Laboratory":2,"Linear Integrated Circuits Laboratory":2},
   {"Therapeutic Equipments":3,"Medical Instrumentation":3,"Analog and Digital Communication":3,"Professional Elective – I":3,"Professional Elective – II":3,"Open Elective I":3,"Medical Equipment Laboratory":2,"Medical Instrumentation Laboratory":2,"Professional Communication":1},
   {"Microprocessors and Microcontrollers":3,"Human Assist Devices":3,"Medical Imaging Techniques":3,"Biomechanics":3,"Internet of Things and its Applications ":3,"Professional Elective-III":2,"Microprocessors and Microcontrollers Laboratory":2,"Medical Electronics System Design Laboratory":2,"Mini Project":2},
   {"Digital Image Processing":3,"Physiological Modelling":3,"Body Area Networks ":3,"Professional Elective IV":3,"Open Elective – II ":3,"Digital Image Processing Laboratory ":2,"Project Work-Phase 1":2,"Hospital Internship":1},
   {"Professional Elective-V":3,"Professional Elective-VI":3,"Project Work-Phase 2":6}]

eie=[{"Communicative English":3,"Engineering Mathematics":4,"Engineering Physics":3,"Engineering Chemistry":3,"Problem solving and Python Programming":3,"Basic Civil and Mechanical Engineering":3,"Physics and Chemistry Lab":2,"Problem solving and Python Programming Laboratory":2},
   {"Technical English":3,"Engineering maths 2":4,"Physics for Electronics Engineering":3,"Environmental Science":3,"Programming in C":3,"Engineering Graphics":4,"APES LAB":2,"C Programming Laboratory":2,"EP LAB":2,"NCC/NSS/YRC/NSO":1},
   {"Transforms and Partial Differential Equations":4,"Electron Devices and Circuits":3,"Applied Fluid Dynamics and Thermodynamics":3,"Electrical and Electronic Instruments":3,"Transducers Engineering":3,"Circuit Theory":3,"Measurements and Transducers Laboratory":2,"Circuits and Devices Laboratory":2},
   {"Numerical Methods":4,"Electrical Machines":3,"Digital Logic Circuits":3,"Linear Integrated Circuits and Applications":3,"Industrial Instrumentation - I":3,"Professional Ethics":3,"Electrical Machines Laboratory":2,"Linear and Digital Integrated Circuits Laboratory":2},
   {"Industrial Instrumentation - II":3,"Control Systems":3,"Communication Engineering":3,"Microprocessors and Microcontrollers":3,"Discrete Time Systems and Signal Processing":3,"Open Elective I":3,"Industrial Instrumentation Laboratory":2,"Microprocessors and Microcontrollers Laboratory":2},
   {"Logic and Distributed Control System":3,"Data Structures":3,"Process Control":3,"Professional Elective - I":3,"Professional Elective - II":3,"Data Structures Laboratory":2,"Process Control Laboratory":2,"Professional Communication":1,"Mini Project":2},
   {"Computer control of Processes":3,"Industrial data network":3,"Professional Elective - III ":3,"Professional Elective IV":3,"Open Elective – II ":3,"Industrial Automation Laboratory":2,"Instrumentation System Design Laboratory":2,"Project Work-Phase 1":2,"Internship":1},
   {"Professional Elective-V":3,"Professional Elective-VI":3,"Project Work-Phase 2":6}]

agri=[{"Communicative English":3,"Engineering Mathematics":4,"Engineering Physics":3,"Engineering Chemistry":3,"Problem solving and Python Programming":3,"Basic Electrical and Electronics for Agriculture Engineering":3,"Physics and Chemistry Lab":2,"Problem solving and Python Programming Laboratory":2},
   {"Technical English":3,"Engineering maths 2":4,"Physics for Agriculture Engineering":3,"Environmental Science":3,"Programming in C":3,"Engineering Graphics":4,"APES LAB":2,"C Programming Laboratory":2,"EP LAB":2,"NCC/NSS/YRC/NSO":1},
   {"Transforms and Partial Differential Equations":4,"Soil Science and Engineering":3,"Fluid Mechanics and Hydraulics":3,"Theory of Machines":3,"Surveying and Leveling":3,"Solar and Wind Energy Engineering":3,"Surveying and Leveling Laboratory":2,"Fluid Mechanics Laboratory":1},
   {"Probability and Statistics":4,"Unit Operations in Agricultural Processing":3,"Farm Tractors":3,"Hydrology and Water Resources Engineering":3,"Strength of Materials":3,"Principles and Practices of Crop Production":3,"Soil Science Laboratory":2,"Strength of Materials Laboratory":2,"Crop Husbandry Laboratory":2},
   {"Irrigation and Drainage Engineering":3,"Farm Machinery and Equipment":3,"Design of Basic Machine Elements":3,"Post-Harvest Technology":3,"Professional Elective - I":3,"Open Elective I":3,"Operation and Maintenance of Farm Machinery Lab":2,"Post Harvest Engineering Laboratory":2,"Irrigation Field Laboratory":2,"Professional Communication":1},
   {"Groundwater and Well Engineering":3,"Food and Dairy Engineering":3," Protected Cultivation":3,"Professional Elective - II":3,"Professional Elective - III":3,"CAD for Agricultural Engineering":2,"Food Process Engineering Laboratory":2,"Mini Project":2},
   {"Soil and Water Conservation Engineering":3,"Remote Sensing and Geographical Information System for Agriculture Engineers":3,"Bio-Energy Resource Technology":3,"Professional Elective - IV ":3,"Open Elective – II ":3,"Design and Drawing of Farm and irrigation Structures":2,"Project Work-Phase 1":2,"Internship":1},
   {"Professional Elective-V":3,"Professional Elective-VI":3,"Project Work-Phase 2":6}]

mtds=[{"Mathematical Foundation for Data Science":4,"Introduction to Big Data Analytics":3,"Data Science and R Essentials":3,"Machine Learning":3,"Next Generation Databases":3,"Data Science and R Essentials Laboratory":2,"Machine Learning Laboratory":2},
      {"Statistical Learning for Data Science":4,"Image and Video Processing":3,"Data Preprocessing and Optimization Techniques":3,"Advanced Data Visualization Techniques":3,"Professional Elective - I":3,"Data Visualization Laboratory":2,"Mini Project with Research Paper Writing":2},
      {"Deep Learning":3,"Professional Elective - II":3,"Professional Elective - III":3,"Project Work – Phase I":6,"Online Course (NPTEL,MOOC etc.)/Internship from Industry":1},
      {"Project Work - Phase II":12}]

mecse=[{"Applied Probability and Statistics":4,"Advanced Data Structures and Algorithms":4,"Advanced Computer Architecture":3,"Operating System Internals":3,"Advanced Software Engineering":3,"Machine Learning Techniques":3,"Data Structures Laboratory":2},
      {"Network Design and Technologies":3,"Security Practices":3,"Internet of Things":3,"Big Data Analytics":3,"Professional Elective - I":3,"Professional Elective – II ":3,"Data Analytics Laboratory":2,"Term Paper Writing and Seminar":1},
      {"Professional Elective –III ":3,"Professional Elective –IV":3,"Professional Elective –V":3,"Project Work – Phase I":6},
      {"Project Work - Phase II":12}]

mese=[{"Advanced Mathematical Methods":4,"Advanced Concrete and Steel Structures ":3,"Dynamics of Structures":3,"Theory of Elasticity and Plasticity":3,"Professional Elective-I":3,"Professional Elective-II":3,"Advanced Structural Engineering Laboratory":2},
      {"Stability of Structures":3,"Experimental Techniques":3,"Finite Element Analysis of structures":3,"Professional Elective-III":3,"Professional Elective - IV":3,"Practical Training I ":1},
      {"Earthquake Analysis and Design of Structures":3,"Advanced Concrete Technology":3,"Professional Elective –V":3,"Professional Elective-VI":3,"Seminar":1,"Project Work – Phase I":6,"Practical Training II":1},
      {"Practical Training III":1,"Project Work - Phase II":12}]

mecs=[{"Applied Mathematics for Communication Engineers":4,"Advanced Radiation Systems":3,"Advanced Digital Communication Techniques":3,"Advanced Digital Signal Processing":4,"Optical Networks":3,"Professional Elective-I":3,"Communication Systems Laboratory ":2},
      {"Advanced Wireless Communication Systems":3,"MIC and RF System Design":3,"Electromagnetic Interference and Compatibility":3,"Professional Elective-II":3,"Professional Elective - III":3,"Professional Elective IV":3,"RF System Design Laboratory":2,"Term Paper Writing and Seminar":1},
      {"Millimeter Wave Communications":3,"Professional Elective –V":3,"Professional Elective-VI":3,"Project Work – Phase I":6},
      {"Project Work - Phase II":12}]

meps=[{"Applied Mathematics for Electrical Engineers":4,"Advanced Power System Analysis":4,"Power System Operation and Control":3,"Analysis and Computation of Electromagnetic Transients in Power Systems":3,"System Theory":4,"Professional Elective-I":3,"Power System Simulation Laboratory":2},
      {"Power System Dynamics":3,"HVDC and FACTS":3,"Advanced Power System Protection":3,"Restructured Power System":3,"Professional Elective-II":3,"Professional Elective - III":3,"Advanced Power System Simulation Laboratory":2,"Technical Seminar":1},
      {"Professional Elective IV":3,"Professional Elective –V":3,"Professional Elective-VI":3,"Project Work – Phase I":6},
      {"Project Work - Phase II":12}]

mecie=[{"Applied Mathematics for Electrical Engineers":4,"Transducers and Smart Instruments ":3,"System Theory ":4,"Control System Design":4,"Design of Embedded Systems ":3,"Modeling and Simulation Laboratory ":2},
      {"Advanced Process Control ":4,"Industrial Automation":3,"Advanced Control Systems":3,"Professional Elective - I":3,"Professional Elective-II":3,"Professional Elective - III":3,"Digital Control and Instrumentation Laboratory":2,"Automation Laboratory":2},
      {"Professional Elective IV":3,"Professional Elective –V":3,"Professional Elective-VI":3,"Project Work – Phase I":6},
      {"Project Work - Phase II":12}]

meise=[{"Probability and Statistical Methods":4,"Principles of Safety Management":3,"Environmental Safety":4,"Occupational Health and Industrial Hygiene":3,"Industrial Safety, Health and Environment Acts":4,"Professional Elective - I":3,"Technical Seminar - I":1},
      {"Fire Engineering and Explosion Control":3,"Computer Aided Hazard Analysis":4,"Electrical Safety ":3,"Safety in Chemical Industries ":3,"Professional Elective-II":3,"Professional Elective - III":3,"Industrial Safety Laboratory":2,"Technical Seminar - II":1},
      {"Reliability Engineering ":3,"Professional Elective IV":3,"Professional Elective –V":3,"Project Work – Phase I":6,"Industrial Safety Assessment - Internship":2},
      {"Project Work - Phase II":12}]

mba=[{"Statistics for Management":4,"Economic Analysis for Business":4,"Principles of Management":3,"Accounting for Management ":4,"Legal Aspects of Business":4,"Organizational Behaviour":3,"Total Quality Management":3,"Spoken and Written Communication":2},
      {"Applied Operations Research ":4,"Business Research Methods":3,"Financial Management":4,"Human Resource Management":3,"Information Management":4,"Operations Management":4,"Marketing Management":3,"Data Analysis and Business Modelling":3},
      {"Strategic Management ":3,"International Business Management":3,"Professional Elective-I":3,"Professional Elective II":3,"Professional Elective III":3,"Professional Elective IV":3,"Professional Elective V":3,"Professional Elective VI":3,"Creativity and Innovation Laboratory":3,"Mini Project":3},
      {"Project Work":17}]

sgpa=0
sc=0
total_credits=[]
print("---------- GPA and CGPA calculator ----------")
print("1. GPA calculation\n2. CGPA calculation")
a = int(input("Enter your option :"))
def calculate():
    global sum,g,sum1
    if g=="O":
        sum+=10*s[i][subject1[i][j]]
        sum1+=10*s[i][subject1[i][j]]
    elif g=="A+":
        sum+=9*s[i][subject1[i][j]]
        sum1+=9*s[i][subject1[i][j]]
    elif g=="A":
        sum+=8*s[i][subject1[i][j]]
        sum1+=8*s[i][subject1[i][j]]
    elif g=="B+":
        sum+=7*s[i][subject1[i][j]]
        sum1+=7*s[i][subject1[i][j]]
    elif g=="B":
        sum+=6*s[i][subject1[i][j]]
        sum1+=6*s[i][subject1[i][j]]
    elif g=="C":
        sum+=5*s[i][subject1[i][j]]
        sum1+=5*s[i][subject1[i][j]]
    elif g=="RA":
        sum+=0
        sum1+=0
        s[i][subject1[i][j]]=0
        credit1[i][j]=0
    else:
        pass
def choose():
    global a,a1,s,cyber,aids,eee,civil,mech,agri,cse,it,ece,mde,eie,subject
    print('''1 : UG
2 : PG
3 : MBA''')
    deg=int(input("Choose the degree : "))
    while(1):
        if deg==1:
            print('''1 : Cyber Security
2 : Arificial Intelligence & Data Science
3 : Electrical and Electronics Engineering
4 : Civil
5 : Mechanical
6 : Agri
7 : Computer Science and Engineering
8 : Information Technology
9 : Electronics and Communication Engineering
10 : Medical Electronics
11 : Electronics and Instrumentation Engineering''')
            dept=int(input("Choose your department (1-11) : "))
            while(1):
                if dept==1:
                    s=cyber
                    break
                elif dept==2:
                    s=aids
                    break
                elif dept==3:
                    s=eee
                    break
                elif dept==4:
                    s=civil
                    break
                elif dept==5:
                    s=mech
                    break
                elif dept==6:
                    s=agri
                    break
                elif dept==7:
                    s=cse
                    break
                elif dept==8:
                    s=it
                    break
                elif dept==9:
                    s=ece
                    break
                elif dept==10:
                    s=mde
                    break
                elif dept==11:
                    s=eie
                    break
                else:
                    print("Invalid Choice")
                    dept=int(input("Choose your department (1-11) : "))
                    continue
            break
        elif deg==2:
            print('''1 : Data Science
2 : Computer Science and Engineering
3 : Structural Engineering
4 : Communication Systems
5 : Power Systems
6 : Control and Instrumentation Engineering
7 : Industrial Safety Engineering''')
            dept=int(input("Choose your department (1-7) : "))
            while(1):
                if dept==1:
                    s=mtds
                    break
                elif dept==2:
                    s=mecse
                    break
                elif dept==3:
                    s=mese
                    break
                elif dept==4:
                    s=mecs
                    break
                elif dept==5:
                    s=meps
                    break
                elif dept==6:
                    s=mecie
                    break
                elif dept==7:
                    s=meise
                    break
                else:
                    print("Invalid Choice")
                    dept=int(input("Choose your department (1-7) : "))
                    continue
            break
        elif deg==3:
            s=mba
            break
        else:
            print("Invalid Choice")
            deg=int(input("Choose your degree : "))
            continue
def choice():
    global a,a1,s,cyber,aids,eee,civil,mech,agri,cse,it,ece,mde,eie,total,subject
    total=0
    while(1):
        if a==1:
            choose()
            break
        elif a==2:
            print('''1: Using GPA
2: Using Grade''')
            a1=int(input("Enter your choice : "))
            if a1==1:
                choose()
                break
            elif a1==2:
                choose()
                break
            else:
                print("Invalid Choice")
                continue
while(a>0):
    if (a == 1):
        # GPA calculator
        print("\n****GPA CALCULATOR****\n")
        choice()
        subject=[]
        credit=[]
        n=int(input("Enter the Semester to calculate GPA : "))
        grade=["O","A+","A","B+","B","C","RA"]
        sum=0
        gpa=[]
        tc=0
        t=n-1
        i=n-1
        for j in s[i]:
            subject.append(j)
            credit.append(s[i][j])
        j=n-1
        def calculate():
            global sum,g
            if g=="O":
                sum+=10*s[i][subject[k]]
            elif g=="A+":
                sum+=9*s[i][subject[k]]
            elif g=="A":
                sum+=8*s[i][subject[k]]
            elif g=="B+":
                sum+=7*s[i][subject[k]]
            elif g=="B":
                sum+=6*s[i][subject[k]]
            elif g=="C":
                sum+=5*s[i][subject[k]]
            elif g=="RA":
                sum+=0
                s[i][subject[k]]=0
                credit[k]=0
            else:
                pass
        for k in range(len(subject)):
            g=input("Enter the grade for "+subject[k]+" : ")
            g=g.upper()
            calculate()
            while(g not in grade):
                print("Invalid grade ... Enter the grade again")
                g=input("Enter the grade for "+subject[k]+" : ")
                g=g.upper()
                calculate()
            else:
                continue
        for i in range(len(credit)):
            tc=tc+credit[i]
        gpa=round(sum/tc,2)
        print("\nCalculating GPA....")
        time.sleep(5)
        print("The GPA of your "+str(n)+" Semester is : ",gpa)
        break
    elif (a == 2):
        # CGPA calculator
        print("\n****CGPA CALCULATOR****\n")
        choice()
        subject=[]
        credit=[]
        n=int(input("Enter the Semester to calculate CGPA : "))
        if a1==1:
            print("\nMaximum Credits\n")
            for i in range(n):
                total=0
                for j in s[i]:
                    total+=s[i][j]
                total_credits.append(total)
                print("Semester",i+1,":",total)
            for i in range(n):
                print()
                gpa=float(input("Enter the GPA for Semester "+str(i+1)+" :"))
                while(1):
                    if gpa>0 and gpa<=10:
                        credits1=int(input("Enter the credits you got for Semester "+str(i+1)+" :"))
                        break
                    else:
                        print("Invalid GPA...")
                        gpa=float(input("Enter the GPA for Semester "+str(i+1)+" :"))
                        continue
                while(1):
                    if credits1<=total_credits[i]:
                        sgpa+=(gpa*credits1)
                        sc+=credits1
                        break
                    else:
                        print("Maximum credit exceeded...")
                        credits1=int(input("Enter the credits you got for Semester "+str(i+1)+" :"))
                        continue
                        
            sgpa=round(sgpa,0)
            cgpa=round(sgpa/sc,2)
            print("\nCalculating CGPA....")
            time.sleep(5)
            print("CGPA : ",cgpa)
            break
        elif a1==2:
            grade=["O","A+","A","B+","B","C","RA"]
            sum=0
            gpa=[]
            tc=0
            t=n-1
            subject1=[]
            credit1=[]
            sum1=0
            gpal=[]
            for i in range(n):
                subject=[]
                credit=[]
                for j in s[i]:
                    subject.append(j)
                    credit.append(s[i][j])
                subject1.append(subject)
                credit1.append(credit)
            for i in range(len(subject1)):
                tc=0
                sum1=0
                print()
                for j in range(len(subject1[i])):
                    g=input("Enter the grade for "+subject1[i][j]+" : ")
                    g=g.upper()
                    calculate()
                    tc+=credit1[i][j]
                    while(g not in grade):
                        print("Invalid grade ... Enter the grade again")
                        g=input("Enter the grade for "+subject1[i][j]+" : ")
                        g=g.upper()
                        calculate()
                    else:
                        continue
                gpa=round(sum1/tc,2)
                gpal.append(gpa)
            tc=0
            for i in range(len(credit1)):
                for j in range(len(credit1[i])):
                    tc=tc+credit1[i][j]
            cgpa=round(sum/tc,2)
            print()
            for i in range(len(gpal)):
                print("GPA for Semester",i+1,":",gpal[i])
            print("\nCalculating CGPA....")
            time.sleep(5)
            print("The CGPA of your "+str(n)+" Semester is : ",cgpa)
            break
    else:
        print("Invalid Choice")
        a = int(input("Enter your option :"))
        continue
else:
    print("Enter your option correctly")
    
