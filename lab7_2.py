#class which represents progress of some student
class Student(object) :
	exam = 0	#marks of the student for an exam
	result = 0	#whole result of the student
	unmade = 0	#index of lab that student didn't made yet
	labs = []	#list for marks of all labs of student

	#constructor
	def __init__(self, name, conf = {'exam_max': 30, 'lab_max': 7, 'lab_num': 10, 'k': 0.61}) :
		self.name = name
		self.conf = conf
		self.labs = []
		self.result = 0
		self.exam = 0
		for i in range(conf['lab_num']) :	#create a list with zeros (labs are not made yet)
			self.labs.append(0)

	#function for making lab
	def make_lab(self, m, n = 99999999) :	
		if n == 99999999 :
			n = self.unmade	#if n is not defined lab that student makes is the first of his unmade labs
		if n < self.conf['lab_num'] :	#if number of lab exists
			if m > self.conf['lab_max'] :	#if mark for this lab is more than max mark for lab
				self.labs[n] = self.conf['lab_max']	#lab is evaluated for max mark
			else :
				self.labs[n] = m 	#set element of list to m (lab number n is evaluated on m)
			for index, lab_mark in enumerate(self.labs) :	#iterate through list of labs
				if lab_mark == 0 :	#if lab is not made yet
					self.unmade = index
					break
		return self


	#function for making exam 
	def make_exam(self, m) :
		if m > self.conf['exam_max'] :	#if mark for exam is more than max mark for exam
			self.exam = self.conf['exam_max']	#exam is evaluated for max mark
		else :
			self.exam = m 	#exam is evaluated on m
	return self 


	#function for defining whether the student is certified
	def is_certified(self) :
		self.result = sum(self.labs) + self.exam 	#summarize all marks of student
		if self.result < self.conf['k'] * 100 :	#if the result of student is less than pass mark
			return (self.result, False)	
		else :	#if student finished successfully the course
			return (self.result, True)

