f = open("cmudict.0.7a.txt", 'r')
lines = f.readlines()

phoneDict = {}
vowelDict = {}
stressDict = {}
lexicon = {}
rhymes = {}

class Lexeme:
	
	def __init__(self, graphemes, phonemes, stress, stressIndices):
		self.graphemes = graphemes
		self.phonemes = phonemes
		self.stress = stress
		self.stressIndices = stressIndices
		lastStressIndex = 0
		for i in range(len(self.stress)):
			if self.stress[i] > 0:
				lastStressIndex = self.stressIndices[i]
		self.rhyme = " ".join(phonemes[lastStressIndex:])
		if not self.rhyme in rhymes:
			rhymes[self.rhyme] = []
		rhymes[self.rhyme].append(self)
		
	def rhymes(self):
		return rhymes[self.rhyme]
		
	def __str__(self):
		return "<Lexeme \"" + self.graphemes + "\">"
		
	def __repr__(self):
		return "<Lexeme \"" + self.graphemes + "\">"
        		
for line in lines:
	line = line[:-1]
	parts = line.split(" ")
	word = parts[0]
  	word = word.lower()
  	phonemes = []
  	stress = []
  	stressIndices = []
  	j = 0
  	for i in range(1, len(parts)):
		part = parts[i]
		if not parts[i] == '':
			if ord(part[-1]) in range(47, 58):
				phonemes.append(part[:-1])
				stress.append(int(part[-1]))
				stressIndices.append(j)
			else:
				phonemes.append(part)
			j += 1
	lexeme = Lexeme(word, phonemes, stress, stressIndices)
	lexicon[lexeme.graphemes] = lexeme
    