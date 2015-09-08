# CS496-RandomStoryAPI
Final project for CS496 - mobile/cloud development

API documentation (If an HTTP verb isn’t listed under a URI, it isn’t supported by that URI): 
 
URIs 
/story 
GET: retrieves a random story 
POST: adds a new story to the datastore. Required fields are ‘title’ and ‘the_story’.  
 
/story/<sid> 
GET: retrieves a specific story 
PUT: updates the story with this id.  
DELETE: deletes the story with this id. 
 
/noun, /verb, /adverb, /adjective, /pronoun, /exclamation 
GET: gets a random word of specified type. 
POST: adds a word of specified type to the datastore. Required field is ‘word’.  
 
/user 
POST: adds a new user. Required is ‘name’. 
 
/user/<uid> 
GET: get user with this id. 
PUT: update specified user. The only updatable field is ‘stories’, which only accepts keys of 
stories already in the datastore. 
DELETE: deletes the user with this id. 
 
The user account system is extremely simple. The user enters their username before writing a 
story. If it exists, all stories written by that username are pulled. If it doesn’t, it creates a new 
user.  
