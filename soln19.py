# Write a Python class to find validity of a string of parentheses, '(', ')', '{', '}', '[' and ']. 
# These brackets must be close in the correct order, for example "()" and "()[]{}" are valid but "[)", "({[)]" and "{{{" are invalid 

class ParenthesisValidator:
	stack = []

	def __init__(self, inputString):
		self.validationString = inputString

	def runValidator(self):
		for character in self.validationString:
			if character in [ "{", "(", "["]:
				self.stack.append(character)
			elif character == "]" and self.stack.pop() != "[":
				return False
			elif character == "}" and self.stack.pop() != "{":
				return False
			elif character == ")" and self.stack.pop() != "(":
				return False
			else :
				return False
		if len(self.stack) > 0 :
			return False
		return True


object = ParenthesisValidator("{{[()]}}")
if object.runValidator():
	print("valid bracket sequence")
else:
	print("not a valid bracket sequence")
