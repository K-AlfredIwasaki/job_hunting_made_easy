def get_company_from_title(title):
	"""
	algorithm to extract a company name to tech cruch article title
	"""
	import re

	# remove "word word word: "
	regex_intro = re.compile(r'\w+(\s+\w+)*\s*:\s')
	title = re.sub(regex_intro, "", title)

	# remove ", word word word,"
	regex_middle = re.compile(r',\s.+,')
	title = re.sub(regex_middle, "", title)
	
	# split the title by strong verb and keep the head
	regex_verb = re.compile(r" (raise|land|grab|hire|march|cook|is|head|scoop|launch|step|aim|rocket|order|receive|get|bag|emerge|collect|pull|close|secure|take|tap|score|snare|snag|grab|nab|win)",
                   re.IGNORECASE)
	title = re.split(regex_verb, title)[0].strip(" ")

	# remove "word word word,"
	regex_intro2 = re.compile(r'.+,\s')
	title = re.sub(regex_intro2, "", title).strip(" ")

	# count the number of spaces in the head
	if count_word(title) == 1:
		return title
	elif count_word(title) == 2:
		return two_words_check(title)
	else:

		# split the remained title by strong noun and keep the tail
		regex_noun = re.compile(r" (marketplace|maker|juggernaut|system|finalist|alum|solution|dashboard|editor|restaurant|app|firm|rival|lender|site|startup|company|competitor|platform|network|service|leader|house|developer|retailer)",
                    re.IGNORECASE)
		title = re.split(regex_noun, title)[-1].strip(" ")

		if count_word(title) == 1:
			return title
		elif count_word(title) == 2:
			return two_words_check(title)

		else:
			# 
			title = title.split("$")[0]
			title = title.split("Series")[0]
			regex_lead = re.compile(r"\s[Ll]eads\s",
                    re.IGNORECASE)
			title = re.split(regex_lead, title)[-1].strip(" ")

			if count_word(title) == 2:
				return two_words_check(title)
			else:
				return title


def count_word(title):
	import re
	regex_space = re.compile(r'\s')
	return len(re.findall(regex_space, title)) + 1

def two_words_check(title):
	import re
	regex = re.compile(r'([A-Z]\w+)\s[a-z]')
	match = re.search(regex, title)
	if match:
		return match.group(1)
	else:
		return title


