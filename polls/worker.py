from polls.models import Choice, Question

def vote(choice_id):
	print "Voting for choice id: " + str(choice_id)
	try:
		choice = Choice.objects.get(pk=choice_id)
	except Choice.DoesNotExist:
		print "ERROR: Choice does not exist"
	print("Q={0} : A={1}").format(choice.question.question_text, choice.choice_text)
	choice.votes += 1
	choice.save()
    