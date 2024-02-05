# Don't forget to run the tests (and create some of your own)

# Part 1
def is_character_match(string1, string2):
	# Your code here
	clean_str1 = (string1.replace(' ', '')).lower()
	clean_str2 = (string2.replace(' ', '')).lower()
	string_check_dict = {}

	for char in clean_str1:
		if char in string_check_dict:
			string_check_dict[char] += 1
		string_check_dict.update({char:1})
	
	for letter in clean_str2:
		if letter in string_check_dict:
			string_check_dict[letter] += 1
		else:
			string_check_dict[letter] = 1
		
	if 1 in string_check_dict.values():
		return False
	return True

# Part 2
def anagrams_for(word, list_of_words):
	list_ans = []
	for str in list_of_words:
		if is_character_match(word, str) == True:
			list_ans.append(str)
	return list_ans	
		


# print(is_character_match('charm', 'march'))
# print(is_character_match('charm', 'march'))
# print(is_character_match('zach', 'attack'))
# print(is_character_match('CharM', 'mARcH'))
# print(is_character_match('abcde2', 'c2abed'))
# print(is_character_match('Anna Madrigal', 'A man and a girl'))

# print(anagrams_for("saltier", ["cognac", "saltier", "realist", "retails"]))