from modules.models import Module
import json
import io
import re

json_modules = io.open('modules.json', encoding='utf-8').read()
decoded_modules = json.loads(json_modules)

#Regular expressions for Module Codes
#"CS1010," ",CS1010" ", CS1010" "CS1010 ," 
withcomma = re.compile('[A-Z]{2,3}[0-9]{4}[A-Z]*|[A-Z]{2,3}[0-9]{4}[A-Z]*(?= ,)|[A-Z]{2,3}[0-9]{4}[A-Z]*(?=,)|(?<=,)[A-Z]{2,3}[0-9]{4}[A-Z]*|(?<=, )[A-Z]{2,3}[0-9]{4}[A-Z]*', re.IGNORECASE)
#module code: " and CS1010", "CS1010 and ", "CS1010"
withand = re.compile('[A-Z]{2,3}[0-9]{4}[A-Z]*(?= and )|(?<= and )[A-Z]{2,3}[0-9]{4}[A-Z]*', re.IGNORECASE)
#module code: " or CS1010", "CS1010 or " 
withor = re.compile('[A-Z]{2,3}[0-9]{4}[A-Z]*(?= or )|(?<= or )[A-Z]{2,3}[0-9]{4}[A-Z]*|[A-Z]{2,3}[0-9]{4}[A-Z]*(?= / )|(?<= / )[A-Z]{2,3}[0-9]{4}[A-Z]*|[A-Z]{2,3}[0-9]{4}[A-Z]*(?=/)|(?<=/)[A-Z]{2,3}[0-9]{4}[A-Z]*', re.IGNORECASE)


departmentfaculty = {"THE LOGISTICS INSTITUTE - ASIA PACIFIC": "OTHER",
"MATERIALS SCIENCE AND ENGINEERING": "ENGINE",
"POLITICAL SCIENCE": "FASS",
"MECHANICAL ENGINEERING": "ENGINE",
"MANAGEMENT AND ORGANISATION": "BUSINESS",
"LEE KUAN YEW SCHOOL OF PUBLIC POLICY": "OTHER",
"SAW SWEE HOCK SCHOOL OF PUBLIC HEALTH": "OTHER",
"DIVISION OF GRADUATE MEDICAL STUDIES": "MEDICINE",
"YALE-NUS COLLEGE": "OTHER",
"MATHEMATICS": "SCIENCE",
"SOCIOLOGY": "FASS",
"COMPUTER SCIENCE": "SOC",
"BIOLOGICAL SCIENCES": "SCIENCE",
"DEAN'S OFFICE (ARTS & SOCIAL SC.)": "OTHER",
"CHEMISTRY": "SCIENCE",
"PHYSICS": "SCIENCE",
"NUS GRAD SCH FOR INTEGRATIVE SCI & ENGG": "OTHER",
"CIVIL & ENVIRONMENTAL ENGINEERING": "ENGINE",
"YONG SIEW TOH CONSERVATORY OF MUSIC": "OTHER",
"INFORMATION SYSTEMS": "SOC",
"SOUTHEAST ASIAN STUDIES": "FASS",
"FINANCE": "BUSINESS",
"DUKE-NUS GRADUATE MEDICAL SCHOOL S'PORE": "MEDICINE",
"ENGINEERING SCIENCE PROGRAMME": "ENGINE",
"MARKETING": "BUSINESS",
"DECISION SCIENCES": "BUSINESS",
"DEAN'S OFFICE (MEDICINE)": "OTHER",
"MICROBIOLOGY": "MEDICINE",
"CENTRE FOR LANGUAGE STUDIES": "FASS",
"ANATOMY": "MEDICINE",
"HUMAN RESOURCE MANAGEMENT UNIT": "BUSINESS",
"LAW": "LAW",
"STRATEGY AND POLICY": "BUSINESS",
"REAL ESTATE": "SDE",
"CHEMICAL & BIOMOLECULAR ENGINEERING": "ENGINE",
"DIVISION OF GRADUATE DENTAL STUDIES": "DENTISTRY",
"SOUTH ASIAN STUDIES PROGRAMME": "FASS",
"BIOCHEMISTRY": "MEDICINE",
"DEAN'S OFFICE (BIZ)": "OTHER",
"DEAN'S OFFICE (SCHOOL OF COMPUTING)": "OTHER",
"INSTITUTE OF SYSTEMS SCIENCE": "OTHER",
"SINGAPORE-MIT ALLIANCE": "OTHER",
"ECONOMICS": "FASS",
"OFFICE OF STUDENT AFFAIRS": "OTHER",
"RISK MANAGEMENT INSTITUTE": "OTHER",
"TEMBUSU COLLEGE": "OTHER",
"SOCIAL WORK": "FASS",
"COLLEGE OF ALICE & PETER TAN": "OTHER",
"DIVISION OF ENGINEERING AND TECH MGT": "ENGINE",
"ELECTRICAL & COMPUTER ENGINEERING": "ENGINE",
"DIVISION OF INDUSTRIAL DESIGN": "SDE",
"CENTRE FOR QUANTUM TECHNOLOGIES": "OTHER",
"CTR FOR ENGLISH LANGUAGE COMMUNICATION": "OTHER",
"COMPUTING & ENGINEERING": "OTHER",
"NURSING/ALICE LEE CTR FOR NURSING STUD": "MEDICINE",
"PHILOSOPHY": "FASS",
"ACCOUNTING": "BUSINESS",
"ENGLISH LANGUAGE & LITERATURE": "FASS",
"PHYSIOLOGY": "MEDICINE",
"MALAY STUDIES": "FASS",
"HISTORY": "FASS",
"BUILDING": "SDE",
"PHARMACOLOGY": "MEDICINE",
"COMMUNICATIONS AND NEW MEDIA": "FASS",
"BACHELOR OF TECHNOLOGY PROGRAMME": "ENGINE",
"STATISTICS & APPLIED PROBABILITY": "SCIENCE",
"PSYCHOLOGY": "FASS",
"CHINESE STUDIES": "FASS",
"UNIVERSITY SCHOLARS PROGRAMME": "OTHER",
"PHARMACY": "SCIENCE",
"TEMASEK DEFENCE SYSTEMS INSTITUTE": "OTHER",
"DEAN'S OFFICE (SCHOOL OF DESIGN & ENV)": "OTHER",
"JAPANESE STUDIES": "FASS",
"ARCHITECTURE": "SDE",
"DENTISTRY": "DENTISTRY",
"INDUSTRIAL & SYSTEMS ENGINEERING": "ENGINE",
"MECHANOBIOLOGY INSTITUTE": "OTHER",
"PATHOLOGY": "MEDICINE",
"GEOGRAPHY": "FASS",
"BIOMEDICAL ENGINEERING": "ENGINE",
"DEAN'S OFFICE (SCIENCE)": "OTHER",
"DEAN'S OFFICE (ENGINEERING)": "OTHER"}

for module in decoded_modules:

	if 'ModuleCode' in module:
		entry_code = module["ModuleCode"]
		
	if 'ModuleTitle' in module:
		entry_title = module["ModuleTitle"]
		
	if 'Department' in module:
		entry_department = module["Department"]
		entry_faculty = departmentfaculty[entry_department]
		
	if 'ModuleDescription' in module:
		entry_description = module["ModuleDescription"]
		
	if 'ModuleCredit' in module:
		entry_credit = module["ModuleCredit"]
		
	if 'Preclusion' in module:
		entry_preclusion = module["Preclusion"]
		c = module['Preclusion'].encode('utf-8')
		code = module['ModuleCode'].encode('utf-8')
	#CHECK FOR OR
		entry_precluOr = withor.findall(c)
	#REMOVE MODULES WITH OR
		c = withor.sub("",c)
	#REMOVE ALL OR
		c = re.sub(" or ","",c)
		entry_precluAnd = withand.findall(c)
		c = withand.sub("",c)
		c = re.sub(" and ","",c)
		entry_precluComma = withcomma.findall(c)
		c = withcomma.sub("",c)
		c = re.sub(",","",c)
		if not entry_precluOr:
			entry_precluAnd = entry_precluAnd + entry_precluComma
		else:
			entry_precluOr = entry_precluOr + entry_precluComma
		#REMOVE MATCHES THAT IS IDENTICAL TO MODULE CODE
		if entry_precluOr:
			for mod in entry_precluOr[:]:
				#To prevent things like CS2103 being removed from the preclusion of CS2103T
				if mod+" " in code:
					entry_precluOr.remove(mod)
		if entry_precluAnd:
			for mod in entry_precluAnd[:]:
				if mod+" " in code:
					entry_precluAnd.remove(mod)
		entry_preclu = entry_precluAnd + entry_precluOr
	
	else:
		entry_preclusion = None
		entry_preclu = None
		
	if 'Prerequisite' in module:
		entry_prerequisite = module["Prerequisite"]
		c = module['Prerequisite'].encode('utf-8')
		code = module['ModuleCode'].encode('utf-8')
	#CHECK FOR OR
		entry_prereqOr = withor.findall(c)
	#REMOVE MODULES WITH OR
		c = withor.sub("",c)
	#REMOVE ALL OR
		c = re.sub(" or ","",c)
		entry_prereqAnd = withand.findall(c)
		c = withand.sub("",c)
		c = re.sub(" and ","",c)
		entry_prereqComma = withcomma.findall(c)
		c = withcomma.sub("",c)
		c = re.sub(",","",c)
		if not entry_prereqOr:
			entry_prereqAnd = entry_prereqAnd + entry_prereqComma
		else:
			entry_prereqOr = entry_prereqOr + entry_prereqComma
	#REMOVE MATCHES THAT IS IDENTICAL TO MODULE CODE
		if entry_prereqOr:
			for mod in entry_prereqOr[:]:
				if mod+" " in code:
					entry_prereqOr.remove(mod)
		if entry_prereqAnd:
			for mod in entry_prereqAnd[:]:
				if mod+" " in code:
					entry_prereqAnd.remove(mod)
	
	else:
		entry_prerequisite = None
		entry_prereqAnd = None
		entry_prereqOr = None
		
	if 'ExamDate' in module:
		entry_exam_date = module["ExamDate"]
	
	else:
		entry_exam_date = None
	
	if 'ExamDuration' in module:
		entry_exam_duration = module["ExamDuration"]
	
	else:
		entry_exam_duration = None
	Module.objects.create(module_code = entry_code, module_title = entry_title, department = entry_department, faculty = entry_faculty,module_description = entry_description, module_credit = entry_credit, prerequisite = entry_prerequisite, preclusion = entry_preclusion, exam_date = entry_exam_date, exam_duration = entry_exam_duration, preclu = entry_preclu, prereqAnd = entry_prereqAnd, prereqOr = entry_prereqOr)

Module.objects.all()

json_modules.close()
