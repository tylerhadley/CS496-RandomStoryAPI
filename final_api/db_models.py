from google.appengine.ext import ndb

class Model(ndb.Model):
	def to_dict(self):
		d = super(Model, self).to_dict()
		d['key'] = self.key.id()
		return d	

class WordNoun(ndb.Model):
	word = ndb.StringProperty(required=True)
	tags = ndb.StringProperty(repeated=True)
	random_index = ndb.FloatProperty(required=True)

class WordVerb(ndb.Model):
	word = ndb.StringProperty(required=True)
	tags = ndb.StringProperty(repeated=True)
	random_index = ndb.FloatProperty(required=True)

class WordPronoun(ndb.Model):
	word = ndb.StringProperty(required=True)
	tags = ndb.StringProperty(repeated=True)
	random_index = ndb.FloatProperty(required=True)

class WordAdjective(ndb.Model):
	word = ndb.StringProperty(required=True)
	tags = ndb.StringProperty(repeated=True)
	random_index = ndb.FloatProperty(required=True)

class WordAdverb(ndb.Model):
	word = ndb.StringProperty(required=True)
	tags = ndb.StringProperty(repeated=True)
	random_index = ndb.FloatProperty(required=True)

class WordExclamation(ndb.Model):
	word = ndb.StringProperty(required=True)
	tags = ndb.StringProperty(repeated=True)
	random_index = ndb.FloatProperty(required=True)

class StoryStory(Model):
	title = ndb.StringProperty(required=True)
	the_story = ndb.TextProperty(required=True)
	random_index = ndb.FloatProperty(required=True)

class UserUser(ndb.Model): #id will be username
	name = ndb.StringProperty(required=True)
	stories = ndb.KeyProperty(kind=StoryStory, repeated=True)
