from modules.models import Module, Lesson
import json

json_modules = open('modules.json', encoding='utf-8').read()
decoded_modules = json.loads(json_modules)

for module in decoded_modules:

	if 'ModuleCode' in module:
		entry_code = module["ModuleCode"]
		
	if 'ModuleTitle' in module:
		entry_title = module["ModuleTitle"]
		
	if 'Department' in module:
		entry_department = module["Department"]
		
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
			
	entry = Module(module_code = entry_code, module_title = entry_title, department = entry_department, 
					module_description = entry_description, module_credit = entry_credit, prerequisite = entry_prerequisite,
					preclusion = entry_preclusion, exam_date = entry_exam_date, exam_duration = entry_exam_duration)
	entry.save()

Module.objects.all()
