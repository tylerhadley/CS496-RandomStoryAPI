import webapp2
from google.appengine.api import oauth

app = webapp2.WSGIApplication([('/story', 'story.Story'),], debug=True)
app.router.add(webapp2.Route(r'/story/<sid:[0-9]+><:/?>', 'story.Story'))
app.router.add(webapp2.Route(r'/noun', 'word.Noun'))
app.router.add(webapp2.Route(r'/noun/<wid:[a-zA-Z]+><:/?>', 'word.Noun'))
app.router.add(webapp2.Route(r'/verb', 'word.Verb'))
app.router.add(webapp2.Route(r'/verb/<wid:[a-zA-Z]+><:/?>', 'word.Verb'))
app.router.add(webapp2.Route(r'/pronoun', 'word.Pronoun'))
app.router.add(webapp2.Route(r'/pronoun/<wid:[a-zA-Z]+><:/?>', 'word.Pronoun'))
app.router.add(webapp2.Route(r'/adjective', 'word.Adjective'))
app.router.add(webapp2.Route(r'/adjective/<wid:[a-zA-Z]+><:/?>', 'word.Adjective'))
app.router.add(webapp2.Route(r'/adverb', 'word.Adverb'))
app.router.add(webapp2.Route(r'/adverb/<wid:[a-zA-Z]+><:/?>', 'word.Adverb'))
app.router.add(webapp2.Route(r'/exclamation', 'word.Exclamation'))
app.router.add(webapp2.Route(r'/exclamation/<wid:[a-zA-Z]+><:/?>', 'word.Exclamation'))
app.router.add(webapp2.Route(r'/user', 'user.User'))
app.router.add(webapp2.Route(r'/user/<uid:[a-zA-Z0-9]+><:/?>', 'user.User'))

