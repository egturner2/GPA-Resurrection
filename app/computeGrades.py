def computeSection(maximum, scores):
	total = 0.0
	scored = 0

	for score in scores:
		try:
			value = float(score)
			total += value
			scored += 1
		# skip elements of scores that are not numbers
		except ValueError:
			pass

	if scored == 0:
		return 0
	else:
		return (maximum / 100.0) * total / scored

def computeAll(maximum, scores):
	total = 0

	for i in range(0, len(maximum)):
		total += computeSection(maximum[i], scores[i])

	return total
