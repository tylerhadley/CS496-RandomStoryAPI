import webapp2
from google.appengine.ext import ndb
import db_models
import json
import random

#NOUN----------------------------------------------------------------------------------------
class Noun(webapp2.RequestHandler):
	def post(self):
		#Create a new word
		#word - the word, required
		#tags - optional categories the word can apply to
		#random_index - not passed, will be determined automatically

		data_word = self.request.get('word', default_value=None)
		data_tags = self.request.get('tags', default_value=None)
		
		#convert to lower case
		if not data_word:
			self.response.status=400
			self.response.status_message = "Invalid request"
			return
		else:
			data_word = data_word.lower()
		if data_tags:
			data_tags = data_tags.lower()

		#check for duplicates
		store = False #if duplicate found, will track if it needs to be updated
		q = db_models.WordNoun.query(db_models.WordNoun.word == data_word)
		update_word = q.get()
		if update_word != None: #word already exists
			if data_tags:
				if data_tags not in update_word.tags: 
					update_word.tags.append(data_tags)
					store = True					
		else:     
			update_word = db_models.WordNoun()
			store = True
			update_word.word = data_word
			if data_tags:
				update_word.tags.append(data_tags)
			update_word.random_index = random.random()
		if store:
			key = update_word.put()
			out = update_word.to_dict()
			self.response.write(json.dumps(out))

	def get(self):
		self.response.headers.add_header("Content-Type", "application/json")
		self.response.headers.add_header("Access-Control-Allow-Origin", "*")
		#return random word of specified type.
		random_number = random.random()
		#get words with closest random index
		q1 = db_models.WordNoun.query(db_models.WordNoun.random_index <= random_number).order(-db_models.WordNoun.random_index)
		q2 = db_models.WordNoun.query(db_models.WordNoun.random_index >= random_number).order(db_models.WordNoun.random_index)
		result1 = q1.get()
		result2 = q2.get()
		#deal with empty results
		if not result1: 
			result1=result2
		if not result2: 
			result2=result1
		if not result1 and not result2:
			self.response.status = 204
			self.response.status_message = "No words to retrieve"
			return
		#find word with closest random_index to random_number
		if (result1.random_index - random_number) <= (result2.random_index - random_number):
			out = result1.to_dict()
		else:
			out = result2.to_dict()
		self.response.write(json.dumps(out))
	
	def delete(self, **kwargs):
		q = db_models.WordNoun.query(db_models.WordNoun.word == kwargs['wid'].lower())
		target_word = q.get()
		if not target_word:
			self.response.status = 204
			self.response.status_message = "Word not found, cannot delete"
			return
		target_word.key.delete()
		self.response.status = 200
		self.response.status_message = "Word deleted"
			 
#VERB-----------------------------------------------------------------------------------------------
class Verb(webapp2.RequestHandler):
	def post(self):
		#Create a new word
		#word - the word, required
		#tags - optional categories the word can apply to
		#random_index - not passed, will be determined automatically

		data_word = self.request.get('word', default_value=None)
		data_tags = self.request.get('tags', default_value=None)
		
		#convert to lower case
		if not data_word:
			self.response.status=400
			self.response.status_message = "Invalid request"
			return
		else:
			data_word = data_word.lower()
		if data_tags:
			data_tags = data_tags.lower()

		#check for duplicates
		store = False #if duplicate found, will track if it needs to be updated
		q = db_models.WordVerb.query(db_models.WordVerb.word == data_word)
		update_word = q.get()
		if update_word != None: #word already exists
			if data_tags:
				if data_tags not in update_word.tags: 
					update_word.tags.append(data_tags)
					store = True					
		else:     
			update_word = db_models.WordVerb()
			store = True
			update_word.word = data_word
			if data_tags:
				update_word.tags.append(data_tags)
			update_word.random_index = random.random()
		if store:
			key = update_word.put()
			out = update_word.to_dict()
			self.response.write(json.dumps(out))

	def get(self):
		self.response.headers.add_header("Content-Type", "application/json")
		self.response.headers.add_header("Access-Control-Allow-Origin", "*")
		#return random word of specified type.
		random_number = random.random()
		#get words with closest random index
		q1 = db_models.WordVerb.query(db_models.WordVerb.random_index <= random_number).order(-db_models.WordVerb.random_index)
		q2 = db_models.WordVerb.query(db_models.WordVerb.random_index >= random_number).order(db_models.WordVerb.random_index)
		result1 = q1.get()
		result2 = q2.get()
		#deal with empty results
		if not result1: 
			result1=result2
		if not result2: 
			result2=result1
		if not result1 and not result2:
			self.response.status = 204
			self.response.status_message = "No words to retrieve"
			return
		#find word with closest random_index to random_number
		if (result1.random_index - random_number) <= (result2.random_index - random_number):
			out = result1.to_dict()
		else:
			out = result2.to_dict()
		self.response.write(json.dumps(out))
	
	def delete(self, **kwargs):
		q = db_models.WordVerb.query(db_models.WordVerb.word == kwargs['wid'].lower())
		target_word = q.get()
		if not target_word:
			self.response.status = 204
			self.response.status_message = "Word not found, cannot delete"
			return
		target_word.key.delete()
		self.response.status = 200
		self.response.status_message = "Word deleted"

#PRONOUN-------------------------------------------------------------------------------------------------
class Pronoun(webapp2.RequestHandler):
	def post(self):
		#Create a new word
		#word - the word, required
		#tags - optional categories the word can apply to
		#random_index - not passed, will be determined automatically

		data_word = self.request.get('word', default_value=None)
		data_tags = self.request.get('tags', default_value=None)
		
		#convert to lower case
		if not data_word:
			self.response.status=400
			self.response.status_message = "Invalid request"
			return
		else:
			data_word = data_word.lower()
		if data_tags:
			data_tags = data_tags.lower()

		#check for duplicates
		store = False #if duplicate found, will track if it needs to be updated
		q = db_models.WordPronoun.query(db_models.WordPronoun.word == data_word)
		update_word = q.get()
		if update_word != None: #word already exists
			if data_tags:
				if data_tags not in update_word.tags: 
					update_word.tags.append(data_tags)
					store = True					
		else:     
			update_word = db_models.WordPronoun()
			store = True
			update_word.word = data_word
			if data_tags:
				update_word.tags.append(data_tags)
			update_word.random_index = random.random()
		if store:
			key = update_word.put()
			out = update_word.to_dict()
			self.response.write(json.dumps(out))

	def get(self):
		self.response.headers.add_header("Content-Type", "application/json")
		self.response.headers.add_header("Access-Control-Allow-Origin", "*")
		#return random word of specified type.
		random_number = random.random()
		#get words with closest random index
		q1 = db_models.WordPronoun.query(db_models.WordPronoun.random_index <= random_number).order(-db_models.WordPronoun.random_index)
		q2 = db_models.WordPronoun.query(db_models.WordPronoun.random_index >= random_number).order(db_models.WordPronoun.random_index)
		result1 = q1.get()
		result2 = q2.get()
		#deal with empty results
		if not result1: 
			result1=result2
		if not result2: 
			result2=result1
		if not result1 and not result2:
			self.response.status = 204
			self.response.status_message = "No words to retrieve"
			return
		#find word with closest random_index to random_number
		if (result1.random_index - random_number) <= (result2.random_index - random_number):
			out = result1.to_dict()
		else:
			out = result2.to_dict()
		self.response.write(json.dumps(out))
	
	def delete(self, **kwargs):
		q = db_models.WordPronoun.query(db_models.WordPronoun.word == kwargs['wid'].lower())
		target_word = q.get()
		if not target_word:
			self.response.status = 204
			self.response.status_message = "Word not found, cannot delete"
			return
		target_word.key.delete()
		self.response.status = 200
		self.response.status_message = "Word deleted"

#ADJECTIVE--------------------------------------------------------------------------------------------------
class Adjective(webapp2.RequestHandler):
	def post(self):
		#Create a new word
		#word - the word, required
		#tags - optional categories the word can apply to
		#random_index - not passed, will be determined automatically

		data_word = self.request.get('word', default_value=None)
		data_tags = self.request.get('tags', default_value=None)
		
		#convert to lower case
		if not data_word:
			self.response.status=400
			self.response.status_message = "Invalid request"
			return
		else:
			data_word = data_word.lower()
		if data_tags:
			data_tags = data_tags.lower()

		#check for duplicates
		store = False #if duplicate found, will track if it needs to be updated
		q = db_models.WordAdjective.query(db_models.WordAdjective.word == data_word)
		update_word = q.get()
		if update_word != None: #word already exists
			if data_tags:
				if data_tags not in update_word.tags: 
					update_word.tags.append(data_tags)
					store = True					
		else:     
			update_word = db_models.WordAdjective()
			store = True
			update_word.word = data_word
			if data_tags:
				update_word.tags.append(data_tags)
			update_word.random_index = random.random()
		if store:
			key = update_word.put()
			out = update_word.to_dict()
			self.response.write(json.dumps(out))

	def get(self):
		self.response.headers.add_header("Content-Type", "application/json")
		self.response.headers.add_header("Access-Control-Allow-Origin", "*")
		#return random word of specified type.
		random_number = random.random()
		#get words with closest random index
		q1 = db_models.WordAdjective.query(db_models.WordAdjective.random_index <= random_number).order(-db_models.WordAdjective.random_index)
		q2 = db_models.WordAdjective.query(db_models.WordAdjective.random_index >= random_number).order(db_models.WordAdjective.random_index)
		result1 = q1.get()
		result2 = q2.get()
		#deal with empty results
		if not result1: 
			result1=result2
		if not result2: 
			result2=result1
		if not result1 and not result2:
			self.response.status = 204
			self.response.status_message = "No words to retrieve"
			return
		#find word with closest random_index to random_number
		if (result1.random_index - random_number) <= (result2.random_index - random_number):
			out = result1.to_dict()
		else:
			out = result2.to_dict()
		self.response.write(json.dumps(out))
	
	def delete(self, **kwargs):
		q = db_models.WordAdjective.query(db_models.WordAdjective.word == kwargs['wid'].lower())
		target_word = q.get()
		if not target_word:
			self.response.status = 204
			self.response.status_message = "Word not found, cannot delete"
			return
		target_word.key.delete()
		self.response.status = 200
		self.response.status_message = "Word deleted"

#ADVERB------------------------------------------------------------------------------------------------
class Adverb(webapp2.RequestHandler):
	def post(self):
		#Create a new word
		#word - the word, required
		#tags - optional categories the word can apply to
		#random_index - not passed, will be determined automatically

		data_word = self.request.get('word', default_value=None)
		data_tags = self.request.get('tags', default_value=None)
		
		#convert to lower case
		if not data_word:
			self.response.status=400
			self.response.status_message = "Invalid request"
			return
		else:
			data_word = data_word.lower()
		if data_tags:
			data_tags = data_tags.lower()

		#check for duplicates
		store = False #if duplicate found, will track if it needs to be updated
		q = db_models.WordAdverb.query(db_models.WordAdverb.word == data_word)
		update_word = q.get()
		if update_word != None: #word already exists
			if data_tags:
				if data_tags not in update_word.tags: 
					update_word.tags.append(data_tags)
					store = True					
		else:     
			update_word = db_models.WordAdverb()
			store = True
			update_word.word = data_word
			if data_tags:
				update_word.tags.append(data_tags)
			update_word.random_index = random.random()
		if store:
			key = update_word.put()
			out = update_word.to_dict()
			self.response.write(json.dumps(out))

	def get(self):
		self.response.headers.add_header("Content-Type", "application/json")
		self.response.headers.add_header("Access-Control-Allow-Origin", "*")
		#return random word of specified type.
		random_number = random.random()
		#get words with closest random index
		q1 = db_models.WordAdverb.query(db_models.WordAdverb.random_index <= random_number).order(-db_models.WordAdverb.random_index)
		q2 = db_models.WordAdverb.query(db_models.WordAdverb.random_index >= random_number).order(db_models.WordAdverb.random_index)
		result1 = q1.get()
		result2 = q2.get()
		#deal with empty results
		if not result1: 
			result1=result2
		if not result2: 
			result2=result1
		if not result1 and not result2:
			self.response.status = 204
			self.response.status_message = "No words to retrieve"
			return
		#find word with closest random_index to random_number
		if (result1.random_index - random_number) <= (result2.random_index - random_number):
			out = result1.to_dict()
		else:
			out = result2.to_dict()
		self.response.write(json.dumps(out))
	
	def delete(self, **kwargs):
		q = db_models.WordAdverb.query(db_models.WordAdverb.word == kwargs['wid'].lower())
		target_word = q.get()
		if not target_word:
			self.response.status = 204
			self.response.status_message = "Word not found, cannot delete"
			return
		target_word.key.delete()
		self.response.status = 200
		self.response.status_message = "Word deleted"

#EXCLAMATION---------------------------------------------------------------------------------
class Exclamation(webapp2.RequestHandler):
	def post(self):
		#Create a new word
		#word - the word, required
		#tags - optional categories the word can apply to
		#random_index - not passed, will be determined automatically

		data_word = self.request.get('word', default_value=None)
		data_tags = self.request.get('tags', default_value=None)
		
		#convert to lower case
		if not data_word:
			self.response.status=400
			self.response.status_message = "Invalid request"
			return
		else:
			data_word = data_word.lower()
		if data_tags:
			data_tags = data_tags.lower()

		#check for duplicates
		store = False #if duplicate found, will track if it needs to be updated
		q = db_models.WordExclamation.query(db_models.WordExclamation.word == data_word)
		update_word = q.get()
		if update_word != None: #word already exists
			if data_tags:
				if data_tags not in update_word.tags: 
					update_word.tags.append(data_tags)
					store = True					
		else:     
			update_word = db_models.WordExclamation()
			store = True
			update_word.word = data_word
			if data_tags:
				update_word.tags.append(data_tags)
			update_word.random_index = random.random()
		if store:
			key = update_word.put()
			out = update_word.to_dict()
			self.response.write(json.dumps(out))

	def get(self):
		self.response.headers.add_header("Content-Type", "application/json")
		self.response.headers.add_header("Access-Control-Allow-Origin", "*")
		#return random word of specified type.
		random_number = random.random()
		#get words with closest random index
		q1 = db_models.WordExclamation.query(db_models.WordExclamation.random_index <= random_number).order(-db_models.WordExclamation.random_index)
		q2 = db_models.WordExclamation.query(db_models.WordExclamation.random_index >= random_number).order(db_models.WordExclamation.random_index)
		result1 = q1.get()
		result2 = q2.get()
		#deal with empty results
		if not result1: 
			result1=result2
		if not result2: 
			result2=result1
		if not result1 and not result2:
			self.response.status = 204
			self.response.status_message = "No words to retrieve"
			return
		#find word with closest random_index to random_number
		if (result1.random_index - random_number) <= (result2.random_index - random_number):
			out = result1.to_dict()
		else:
			out = result2.to_dict()
		self.response.write(json.dumps(out))
	
	def delete(self, **kwargs):
		q = db_models.WordExclamation.query(db_models.WordExclamation.word == kwargs['wid'].lower())
		target_word = q.get()
		if not target_word:
			self.response.status = 204
			self.response.status_message = "Word not found, cannot delete"
			return
		target_word.key.delete()
		self.response.status = 200
		self.response.status_message = "Word deleted"
				
