import webapp2
from google.appengine.ext import ndb
import db_models
import json
import random

#validates story string by extracting each angle-bracketed keyword and comparing it
#to a predefined list of acceptable keywords. 
def validate(story):
	copy = False
	accepted_types = ["noun", "pronoun", "verb", "adjective", "adverb", "exclamation"]
	temp = []
	for letter in story:
		if letter == '<':
			copy = True
		elif letter == '>':
			copy = False
			if "".join(temp) not in accepted_types:
				return False
			temp = []
		elif copy:
			temp.append(letter.lower())
	return True
	
class Story(webapp2.RequestHandler):
	def post(self, **kwargs):
		#Create a new story
		#title - the title, required
		#the_story - the story, required
		#random_index - not passed, will be determined automatically
		self.response.headers.add_header("Content-Type", "application/json")
		self.response.headers.add_header("Access-Control-Allow-Origin", "*")
		self.response.headers.add_header("Access-Control-Allow-Methods", "GET, POST, PUT, DELETE, OPTIONS");
		if kwargs:
			self.response.status = 405
			self.response.status_message = "POST not allowed, use PUT instead"
			return	
		data_title = self.request.get('title', default_value=None)
		data_the_story = self.request.get('the_story', default_value=None)
		new_story = db_models.StoryStory()
		if not data_title or not data_the_story:
			self.response.status = 400
			self.response.status_message = "Both title and story are required"
			return
		elif not validate(data_the_story):
			self.response.status = 400
			self.response.status_message = "Story malformed. Keywords must be enclosed in angle brackets and only be noun, pronoun, verb, adjective, adverb, exclamation"
			return				
		else:
			new_story.title = data_title
			new_story.the_story = data_the_story
		new_story.random_index = random.random()
		key = new_story.put()
		out = new_story.to_dict()
		self.response.status = 200
		self.response.write(json.dumps(out))

	def get(self, **kwargs):
		self.response.headers.add_header("Content-Type", "application/json")
		self.response.headers.add_header("Access-Control-Allow-Origin", "*")
		self.response.headers.add_header("Access-Control-Allow-Methods", "GET, POST, PUT, DELETE, OPTIONS");
		if not kwargs:
			#return random story
			random_number = random.random()
			#get words with closest random index
			q1 = db_models.StoryStory.query(db_models.StoryStory.random_index <= random_number).order(-db_models.StoryStory.random_index)
			q2 = db_models.StoryStory.query(db_models.StoryStory.random_index >= random_number).order(db_models.StoryStory.random_index)
			result1 = q1.get()
			result2 = q2.get()
			#deal with empty results
			if not result1: 
				result1=result2
			if not result2: 
				result2=result1
			if not result1 and not result2:
				self.response.status = 204
				self.response.status_message = "No stories to retrieve"
				return
			#find story with closest random_index to random_number
			if (result1.random_index - random_number) <= (result2.random_index - random_number):
				out = result1.to_dict()
			else:
				out = result2.to_dict()
			self.response.write(json.dumps(out))
		else:
			target_story = ndb.Key(db_models.StoryStory, int(kwargs['sid'])).get()
			if not target_story:
				self.response.status = 204
				self.response.status_message = "Story not found."
				return
			self.response.status = 200
			self.response.write(json.dumps(target_story.to_dict()))

	def delete(self, **kwargs):
		self.response.headers.add_header("Content-Type", "application/json")
		self.response.headers.add_header("Access-Control-Allow-Origin", "*")
		self.response.headers.add_header("Access-Control-Allow-Methods", "GET, POST, PUT, DELETE, OPTIONS");
		target_story = ndb.Key(db_models.StoryStory, int(kwargs['sid'])).get()
		if not target_story:
			self.response.status = 204
			self.response.status_message = "Story not found, cannot delete"
			return
		target_story.key.delete()
		self.response.status = 200
		self.response.status_message = "Word deleted"
			
	def put(self, **kwargs):
		self.response.headers.add_header("Content-Type", "application/json")
		self.response.headers.add_header("Access-Control-Allow-Origin", "*")
		self.response.headers.add_header("Access-Control-Allow-Methods", "GET, POST, PUT, DELETE, OPTIONS");
		if not kwargs:
			self.response.status = 405
			self.response.status_message = "Story id required"
			return	
		target_story = ndb.Key(db_models.StoryStory, int(kwargs['sid'])).get()
		if not target_story:
			self.response.status = 204
			self.response.status_message = "Story not found"
			return
		data_title = self.request.get('title', default_value=None)
		data_the_story = self.request.get('the_story', default_value=None)
		if data_title:
			target_story.title = data_title
		if data_the_story:
			if validate(data_the_story):
				target_story.the_story = data_the_story
			else:
				self.response.status = 400
				self.response.status_message = "Story malformed. Keywords must be enclosed in angle brackets and only be noun, pronoun, verb, adjective, adverb, exclamation"
				return
		target_story.put()
		self.response.status = 200
		self.response.write(json.dumps(target_story.to_dict()))

	def options(self, **kwargs):   
        	self.response.headers['Access-Control-Allow-Origin'] = '*'
        	self.response.headers['Access-Control-Allow-Headers'] = 'Origin, X-Requested-With, Content-Type, Accept'
        	self.response.headers['Access-Control-Allow-Methods'] = 'POST, GET, PUT, DELETE, OPTIONS'
				
