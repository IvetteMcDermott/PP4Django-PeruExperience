## Form with richtextfield Bug

- ### Place details

An error is present in the last report. Small changes were done to adjust to the standards but this one is generated in the crispy form and by CkEditor, it adds tags when saved and when the updating form brings the item back the tags overlap as a picture show. 

![detail-page](/readme_docs/readme_images/validation/w3%20detail%20validation%20-%20error%20p.png)

Source Code

![source-code](/readme_docs/readme_images/validation/about%20p%20error.png)

FIX: It was sorted out changing the form.as_p to form | crispy in the front end HTML

- ### Profile

Same situation that previous, an error was generated between the form and the ckseditor.

![profiles](/readme_docs/readme_images/validation/w3%20profile%20validation%20-%20error%20p.png)

FIX: It was sorted out changing the form.as_p to form | crispy in the front end HTML

- ### Search by location 

This page was created for to give access to the user to find a specific place of their interest. It had suffered some changes in the proccess as there was some conflict with a type of search by location that was included and the validator would not accept it. So I decided to drop it, and keep in the research to in the future reinstall it.

- ### Messages timeout

As the function was placed in the Js file instead the base.html, the time out stopped working and messages would stay permanent as a new replace it.

Fix: Function was placed back in the base.html. I think was a glitch but for ensure it work I took this action.

- ### Footer

In big screens where the media had been set for the body to take the width of 80% instead of the 100%, the footer would keep streching over the right side until border of the screen.

Fix: Took the width 100% of the css for it.

- ### Messages for class views

The html was set with a conditional {% if messages %} but classes would give message_success so the div for display it in front end was not trigger.

Fix: Add an OR message_success to the conditional