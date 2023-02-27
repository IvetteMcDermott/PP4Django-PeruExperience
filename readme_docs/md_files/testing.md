## Responsiveness

The site had been test for the following devices:

Mobile: 360 * 740 / 414 * 896 / 828 * 1792  

Tablet: 768 * 1024 / 820 * 1180 / 1280 * 800

Monitor: 1280 * 1024 / 1600 * 900 / 2560 * 1440

The site had been test in Chrome seeming all according to the design. In Firefox, the animation for the regions in the index come out a bit out of shape but still fully functional. In Internet Explorer all seems to work as the design.

<br>

# Manual Testing

The following features are present in all the pages.


## Navbar


The features will be displayed according to the logged user, as marked in [features](/readme_docs/md_files/features.md) page 


| Feature   	| Expected Action   	| Result   	|
|---	|---	|---	|
| Logo    	| Brings the user to the landing page   	| Pass   	|
| Toggle button  	| Toggle to reveal the menu   	| Pass  	|
| Register  	| Brings the user to the Sign Up page  	| Pass  	|
| Log In  	| Brings the user to the Log In page  	| Pass   	|
| My Profile   	| Brings the user to their Profile page  	| Pass  	|
| Community  	| Brings the user to the Community page   	| Pass  	|
| Interests  	| Brings the user to the Interests page   	| Pass  	|
| Search   	| Brings the user to the Search page   	| Pass  	|
| Log Out  	| Brings the users to the Sign Out page  	| Pass   	|
| Admin Page  	| Brings the user to the Admin Page   	| Pass  	|


## Messages


| Feature   	| Expected Action   	| Result   	|
|---	|---	|---	|
| Messages    	| They will be displayed in a div in top left of the screen when an action happens.   	| Pass   	|


## Previous Button


| Feature   	| Expected Action   	| Result   	|
|---	|---	|---	|
| Previous Button    	| Once clicked it takes the user to the previous page according to the browser story.   	| Pass   	|


## Footer


| Feature   	| Expected Action   	| Result   	|
|---	|---	|---	|
| Facebook Icon    	| Opens facebook in a new tab.   	| Pass   	|
| Twitter Icon  	| Opens twitter in a new tab.	| Pass  	|
| Instagram Icon  	| Opens instagram in a new tab.  	| Pass  	|


From here the features are present just in the page they are mentioned.


## Index Page


| Feature   	| Expected Action   	| Result   	|
|---	|---	|---	|
| Main Image    	| Brings the user to the regions section.   	| Pass   	|
| Coast Region  	| Brings the user to the Coast region.  	| Pass  	|
| Andes Region  	| Brings the user to the Andes region.  	| Pass  	|
| Jungle Region  	| Brings the user to the Jungle region.  	| Pass  	|


## Region (Coast, Andes and Jungle)


Each region will display the same functionality.

| Feature   	| Expected Action   	| Result   	|
|---	|---	|---	|
| Pin Icon    	| Display fill if the place is in the logged user interests list. | Pass   	|
|| Display like siluette otherwise.  	||
| Title    	| Brings the user to the first page of the region, according to pagination.  	| Pass   	|
| Pagination  	| Displays 4 cards at a time and displays the number of pages available for | Pass  	|
| |the user to navigate and visualize all the places/posts.  	| |
| Cards (for each place/post to display)    	| Brings the user to the selected place/post information in detail.   	| Pass   	|
| Previous Button  	| Brings the user to the previous page according to the browser history.  	| Pass  	|


## Detail Page


The features will be displayed according to the logged user, as marked in [features](/readme_docs/md_files/features.md) page. 

| Feature   	| Expected Action   	| Result   	|
|---	|---	|---	|
| Pin Icon    	| Display fill if the place is in the logged user interests list. | Pass   	|
|| Display like siluette otherwise.  	||
| Leave a Comment button  	| Opens a popup that contains the form for to leave the comment.  	| Pass  	|
| Form for comment | Once submit button is clicked it saves and renders the comment in the place card. | Pass |
| Edit Comment button  	| Opens a popup that contains the populated form for editing the comment.  	| Pass  	|
| Form for edit the comment | Once submit button is clicked it saves and renders the updated comment in the place card. | Pass |
| Delete Comment button  	| Opens a popup that contains the form for to delete the comment.  	| Pass  	|
| Form for delete the comment | Onces submit button is clicked it deletes and the comment won't show any more in the place card. | Pass |
| Update the place/post button 	| Opens a popup that contains the populated form for updating the place/post.  	| Pass  	|
| Form for update the place/post | Once submit button is clicked it saves and renders the updated place/post in the place card. | Pass |
| Delete place/post button  	| Opens a popup that contains the form for deleting the place/post.  	| Pass  	|
| Form for delete the place/post | Once submit button is clicked it deletes the place card, so that the place and the comments in it don't show anymore. | Pass |


## Search Page


This page is just deployed for registered users.

| Feature   	| Expected Action   	| Result   	|
|---	|---	|---	|
| Search bar by name    	| Input takes a string and searches with icontains in the name field of the places/posts | Pass   	|
||and renders them to the page, or prints to the screen a message that there is nothing to display.   	||
| Text  | Text prints what the user had enter in the input to search | Pass |


## My Profile


This page is just deployed for registered users.

| Feature   	| Expected Action   	| Result   	|
|---	|---	|---	|
| Link to form     	| Opens a popup form where user can enter their information. | Pass   	|
| Form for entry user information| Save and display in the page the information that was entered once the submit button is clicked.   	| Pass |

If user does not enter their information there is a place holder image that will be displayed by default.


## Community


This page is just deployed for registered users.

| Feature   	| Expected Action   	| Result   	|
|---	|---	|---	|
| Pagination     	| According to the number of members at the moment. | Pass   	|

The users considered for this page are the ones that enter their information. If the profile is still in default they will not be displayed here.
