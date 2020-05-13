# ExpShare

### Basic  Info:

##### ExpShare is a place for people with like minded interests to meetup and share experiences together. Enjoy hobbies together, meet new people, and learn from each other. Many hobbists and activities really have to take the weather into account. ExpShare takes care of that and keeps everyone up to date and prepared. Whether its a group motorcycle ride, a soccer scrimage game, or r/c flying group, users can take be ready for rain or heavy winds.


### Routes:

| Route Name 	| URL, api/v1                	| HTTP Verb 	| Description                      	|
|------------	|----------------------------	|-----------	|----------------------------------	|
|            	| /users/login               | POST      	| User Logs in                     	|
|            	| /users/register            | POST      	| Creates new user                 	|
|            	| /users/logout              | GET       	| Logs Out User                    	|
|            	| /loggedInUser              | GET       	| Gets loggedInUser Info           	|
|            	| /events                    | GET       	| Today's events show page         	|
|            	| /events/search             | POST      	| Find Search event name           	|
|            	| /events/add                | POST      	| Add Event                        	|
|            	| /events/id               	| GET       	| event show page                  	|
|            	| /events/id               	| POST      	| Add Comment to event page        	|
|            	| /events/manage/id        	| UPDATE    	| edit event info                  	|
|            	| /events/manage/id        	| DELETE    	| delete event                     	|
|            	| /user/id                 	| GET       	| User Show Page                   	|
|            	| /user/id/mymessages      	| GET       	| Show loggedin users messages     	|
|            	| /user/id/mymessages/id 	|  GET      	| Show users chat w/ selected user 	|
|            	| /user/id/mymessages/id	| POST      	| Send New message in chat         	|
|            	| /user/id/mymessages/new  	| POST      	| Start new chat, with message                   	|
|            	|                            	|           	|                                  	|


### Models:

##### Event
-organizer
-date
-comments(array)
-picture
-description
-street_address
-city
-state
-zipcode

##### User
-city
-state
-username
-password
-email
-picture
-organized_events
-attending_events

##### Chats
-usernames (array)
-messages (array)

##### Messsage
-username (from)
-message
-datetime