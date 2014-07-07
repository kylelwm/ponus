from modules.models import Module
import json
import io

json_modules = io.open('modules.json', encoding='utf-8').read()
decoded_modules = json.loads(json_modules)

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
	
	else:
		entry_preclusion = None
		
	if 'Prerequisite' in module:
		entry_prerequisite = module["Prerequisite"]
	
	else:
		entry_prerequisite = None
		
	if 'ExamDate' in module:
		entry_exam_date = module["ExamDate"]
	
	else:
		entry_exam_date = None
	
	if 'ExamDuration' in module:
		entry_exam_duration = module["ExamDuration"]
	
	else:
		entry_exam_duration = None
			
	entry = Module(module_code = entry_code, module_title = entry_title, department = entry_department, faculty = entry_faculty,
					module_description = entry_description, module_credit = entry_credit, prerequisite = entry_prerequisite,
					preclusion = entry_preclusion, exam_date = entry_exam_date, exam_duration = entry_exam_duration)
	entry.save()

Module.objects.all()

json_modules.close()
