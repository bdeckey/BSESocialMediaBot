

def get_first_nonempty_post_index(all_queued_posts):
	"""
	Method to figure out what row number to delete from queued worksheet
	Input: all_queued_posts, list of all queued response lists
	Output: an int representing th number of empty rows already skipped
	we should really find a better way to do this (without such a method at
	all, ideally)
	"""

	if len(all_queued_posts) > 1:
		return get_first_nonempty_post_index_helper(all_queued_posts[1:])
	else:
		raise ValueError("Bad input! (input must be list of size 2 or more)")
def get_first_nonempty_post_index_helper(all_queued_posts):
    # print(all_queued_posts)
    if not all_queued_posts:
    	raise ValueError("this should be impossible") # this should really throw an error b/c this should be impossible
    elif all_queued_posts[0][0]:
    	# this means the recursion has reached the response with an actual response
        return 1
    else:
        return (1 + get_first_nonempty_post_index_helper(all_queued_posts[1:]))

# assert(get_first_nonempty_post_index(
# 	[['Timestamp', 'What is your name?', 'What is your Banner ID?', 
# 	'Which platform(s)?', 'Enter text for the post', 
# 	'Do you want to post an image as well?', 'Upload your image', 
# 	'Email Address']]) == 0)
assert(get_first_nonempty_post_index(
	[['Timestamp', 'What is your name?', 'What is your Banner ID?', 
	'Which platform(s)?', 'Enter text for the post', 
	'Do you want to post an image as well?', 'Upload your image', 
	'Email Address'], 
	['7/1/2018 3:23:14', 'asdf', 'fnaskldfn', 
	'Twitter', '123', 'No', '', 'a@a.cs']]) == 1)
assert(get_first_nonempty_post_index(
	[['Timestamp', 'What is your name?', 
	'What is your Banner ID?', 'Which platform(s)?', 
	'Enter text for the post', 'Do you want to post an image as well?', 
	'Upload your image', 'Email Address'], 
	['', '', '', '', '', '', '', ''], 
	['', '', '', '', '', '', '', ''], 
	['', '', '', '', '', '', '', ''], 
	['7/1/2018 3:23:14', 'asdf', 'fnaskldfn', 
	'Twitter', '123', 'No', '', 'a@a.cs']]) == 4)
