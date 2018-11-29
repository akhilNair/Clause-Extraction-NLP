import spacy
nlp = spacy.load('en_full')

sent = 'the little yellow dog barked at the cat'
doc = nlp(sent)
clause = {}
clause['S'] = []
clause['V'] = []
clause['O'] = []
clause['A'] = []
clauses = []
# amod -- adjectival modifier (compund of attribute words that modifies noun)
# pobj -- object of preposition (to complete the phrase preposition teams up with noun or pronoun)

def create_clauses(clauses):
	for clause in clauses:
		subj = [subj for subj in clause['S'].lefts] + [clause['S']]
		obj = []
		print('Subj :',subj)
		verbs = clause['V']
		print('Verb :',verbs)
		
for token in doc:
	def process_dependants(token,clause):
		dependants = [t for t in token.head.subtree if t not in token.subtree]
		for d in dependants:
			print('Depdnts dep :',d.dep_)
			if d.dep_ in ['prep']:
				for child in d.children:
					if child.dep_ in ['pobj']:
						clause['A'] = d
	print(token.text,token.pos_,token.head,token.dep_)
	
	#First, we construct a clause for every subject dependency in the DP (e.g., nsubj); the dependant constitutes the subject (S) and the governor the verb (V).
	if token.dep_ in ['nsubj']:
		clause['S'] = token
		clause['V'] = token.head
		
		subtree = token.subtree
		print([t.text for t in subtree])
		
		#take dependants
		 #All other constituents of the clause are dependants of the verb: objects (O) and complements (C) via dobj, iobj, xcomp, or ccomp; and adverbials (A) via dependency relations such as advmod, advcl, or prep_in.
		 
		process_dependants(token,clause)
		clauses.append(clause)
		
print(clauses)
create_clauses(clauses)
