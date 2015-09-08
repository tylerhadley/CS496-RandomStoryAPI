import webapp2
from google.appengine.ext import ndb
import db_models
import json

def buildNestedJSON(obj):
	to_return = {}
	stories = []
	to_return['name'] = obj.name
	for x in obj.stories:
		temp = ndb.Key(db_models.StoryStory, x.id()).get()
		stories.append({'key' : x.id(), 'title' : temp.title})
	to_return['stories'] = stories
	return to_return
	
class User(webapp2.RequestHandler):
	def post(self, **kwargs):
		self.response.headers.add_header("Content-Type", "application/json")
		self.response.headers.add_header("Access-Control-Allow-Origin", "*")
		self.response.headers.add_header("Access-Control-Allow-Methods", "GET, POST, PUT, DELETE, OPTIONS");
		#Create a new user
		#name required
		if kwargs:
			self.response.status = 405
			self.response.status_message = "POST not allowed, use PUT instead"
			return	
		data_name = self.request.get('name', default_value=None)
		
		if not data_name:
			self.response.status = 400
			self.response.status_message = "Username is required"
			return
		elif ndb.Key(db_models.UserUser, data_name).get():
			self.response.status = 403
			self.response.status_message = "Username already taken, please choose another."
			return				
		else:
			new_user = db_models.UserUser(id=data_name)
			new_user.name = data_name
		key = new_user.put()
		out = new_user.to_dict()
		self.response.status = 200
		self.response.write(json.dumps(out))

	def get(self, **kwargs):
		self.response.headers.add_header("Content-Type", "application/json")
		self.response.headers.add_header("Access-Control-Allow-Origin", "*")
		self.response.headers.add_header("Access-Control-Allow-Methods", "GET, POST, PUT, DELETE, OPTIONS");
		if not kwargs:
			self.response.status = 400
			self.response.status_message = "Username is required" 
			return
		print kwargs['uid']
		target_user = ndb.Key(db_models.UserUser, kwargs['uid']).get()
		if not target_user:
			self.response.status = 204
			self.response.status_message = "User not found."
			return
		else:
			self.response.status = 200
			out = buildNestedJSON(target_user)
			self.response.write(json.dumps(out))

	def delete(self, **kwargs):
		self.response.headers.add_header("Content-Type", "application/json")
		self.response.headers.add_header("Access-Control-Allow-Origin", "*")
		self.response.headers.add_header("Access-Control-Allow-Methods", "GET, POST, PUT, DELETE, OPTIONS");
		target_user = ndb.Key(db_models.UserUser, kwargs['uid']).get()
		if not target_user:
			self.response.status = 204
			self.response.status_message = "User not found, cannot delete"
			return
		target_user.key.delete()
		self.response.status = 200
		self.response.status_message = "User deleted"
			
	def put(self, **kwargs):
		self.response.headers.add_header("Content-Type", "application/json")
		self.response.headers.add_header("Access-Control-Allow-Origin", "*")
		self.response.headers.add_header("Access-Control-Allow-Methods", "OPTIONS, GET, POST, PUT, DELETE");
		if not kwargs:
			self.response.status = 400
			self.response.status_message = "Username required"
			return	
		target_user = ndb.Key(db_models.UserUser, kwargs['uid']).get()
		if not target_user:
			self.response.status = 204
			self.response.status_message = "User not found"
			return
		story_id = self.request.get('stories', default_value=None)
		target_story = ndb.Key(db_models.StoryStory, int(story_id)).get()
		if not target_story:
			self.response.status = 204
			self.response.status_message = "Story not found"
			return
		if target_story.key not in target_user.stories:
			target_user.stories.append(target_story.key)
			target_user.put()
		print target_user
		self.response.status = 200
		self.response.status_message = "User updated"

	def options(self, **kwargs):   
        	self.response.headers['Access-Control-Allow-Origin'] = '*'
        	self.response.headers['Access-Control-Allow-Headers'] = 'Origin, X-Requested-With, Content-Type, Accept'
        	self.response.headers['Access-Control-Allow-Methods'] = 'POST, GET, PUT, DELETE, OPTIONS'
		
				
