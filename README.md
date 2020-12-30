## Code Institute Full Stack Milestone Project
# Panther Fitness

Panther Fitness is an online sports product and membership shop using 'full stack frameworks with django' where user can purchase products and gain access
to a membership programme.

![site logo](static/media/homepage_logo.jpg) 

[Visit deployed site](https://sid-howes-panther-fitness.herokuapp.com/)


### Admin Account 
* Email: Admin@hotmail.com
* Username: admin
* Password: Admintest12


## Device Viewings

![device viewings](static/wireframes/wireframe-31.png)


## UI/UX
### Project Goal
This Project is a milestone project for Code Institute full stack frameworks moduke. The criteria for this project is to create a website where user can buy some sort of products and be able to register and log in to there personal account using frameworks such a django.
I have created a online Fitness oriented website that uses the full stack frameworks of django to help target the fitness industry.


### User Stories
#### Anonymous user (a user that is not signed in) can:
* Navigate through the website and see fitness programme page (not access to the lssons) and Products page.
* Search for products
* Purchase products and fitness programme
* Register an account

#### The user can:
* Register an account
* Log in to their account
* Search for products
* Purchase products and fitness programme
* If registered, user can log in to their account and:
    * Access "My profile" page
    * Access Order history
    * Access weeks worth of fitness lessons

#### Site owner (superuser) can:
* Log in into their account
* Search for products
* Purchase products and fitness programme
* Access "Product Management" page
* Access edit lessons page
* Access "My profile" page
* Access Order history
* Access weeks worth of fitness lessons
* Add, edit and delete products
* Edit fitness lessons 
* Access the Django Admin page:
    * Access Accounts
    * Access Authentication and Authorization
    * Access a list of Product Orders
    * Edit fitness lesson
    * Add, edit and delete products
    * Edit subscription 
    * Access a list of user profiles


## Wireframes

### Home page

![desktop view](static/wireframes/wireframe-1.png)

![ipad view](static/wireframes/wireframe-2.png)

![mobile view](static/wireframes/wireframe-3.png)

### Fitness subscription page

![desktop view](static/wireframes/wireframe-4.png)

![ipad view](static/wireframes/wireframe-5.png)

![mobile view](static/wireframes/wireframe-6.png)

### Fitness Lesson page

![desktop view](static/wireframes/wireframe-7.png)

![ipad view](static/wireframes/wireframe-8.png)

![mobile view](static/wireframes/wireframe-9.png)

### Products page

![desktop view](static/wireframes/wireframe-10.png)

![ipad view](static/wireframes/wireframe-11.png)

![mobile view](static/wireframes/wireframe-12.png)

### Products detail page

![desktop view](static/wireframes/wireframe-13.png)

![ipad view](static/wireframes/wireframe-14.png)

![mobile view](static/wireframes/wireframe-15.png)

### Cart page

![desktop view](static/wireframes/wireframe-16.png)

![ipad view](static/wireframes/wireframe-17.png)

![mobile view](static/wireframes/wireframe-18.png)

### Checkout page

![desktop view](static/wireframes/wireframe-19.png)

![ipad view](static/wireframes/wireframe-20.png)

![mobile view](static/wireframes/wireframe-21.png)

### My Profile page

![desktop view](static/wireframes/wireframe-22.png)

![ipad view](static/wireframes/wireframe-23.png)

![mobile view](static/wireframes/wireframe-24.png)

### Login page

![desktop view](static/wireframes/wireframe-25.png)

![ipad view](static/wireframes/wireframe-26.png)

![mobile view](static/wireframes/wireframe-27.png)

### Register page

![desktop view](static/wireframes/wireframe-28.png)

![ipad view](static/wireframes/wireframe-29.png)

![mobile view](static/wireframes/wireframe-30.png)


## Design
Fully responsive design layout for mobile, ipad and desktop

### Color Scheme
 
* ![#b71c1c](https://placehold.it/15/b71c1c/b71c1c)
* ![#00000](https://placehold.it/15/00000/00000)

### Typogaphy
For this website I used fonts from Google fonts as they are easy to use and import into the css folder.
I used Roboto sans-serif.

### Defensive Design
* All forms cannot be left empty and must be filled out.
* Forms give feedback if a option is left blank or the right syntax is not used.
* Cannot gain acccess to fitness programme unless registered.


## Features
### Existing Features
* Panther Fitness logo acts as home button.
* Nav links to navagate through the website.
* Index page main image with inspirational wording.
* Fitness programme page displays a Fitness programme available for purchase. 
* Signed in users can purchase the programme clicking on "Buy Fitness Programme" button which will direct you to the members cateory in products.
* Signed in users who have already purchased the programme it displays "See Your Programme" button which will direct you to the Fitness lesson.
* For anonymous users it displays a "Register to buy" button which will direct you to the register an account.
* For superusers  Lesson has an edit button at bottom of the page to edit the fitness lesson.
* Products page that displays all products
* Category nav that directs you to each category (activewear, equipment, clearance, special offers, new arrivals, memberships and all products)
* Sort by: button to sort products by name, price, category and rating.
* Search bar that can search key words with in the name of product and description.

* Products Details - this page displays product details such as product name, rating, category, price, size and a add to cart button which directs you to see what is in your cart.

* My Profile - this page displays the user profile details, Order history.
* Registered user and superuser can:
    * Update their personal details
    * Check their Product Order history
* Anonymous can not access my profile page.
* Sign Out - this page displays a question "Are you sure you want to sign out?" and two buttons: "Cancel and Sign out". Both buttons redirects the user back to index page.
* Superusers can use the product management page to add products and use edit and delete buttons under products to edit or delete. The superuser account can also access fitness lesson page.
* Register page has five inputs: e-mail address, e-mail address confirmation, username, password and password(again). 
* Once registered you are thenm redirected to verify email address.
* Sign In - this page has two inputs, username or e-mail and password. 
* "Forgot Password?" link which redirects to a "Password Reset" page where the user have to type in their e-mail address and click on the "Reset My Password" button, then wait for an e-mail to arrive with instructions to reset the password.


### Future Features
* Monthly membership payment plan for fitness programme
* Expiry date on the payment instead of the super user changing it in the admin
* Add more programme lessons for a month rather than the week.


## Technologies used
#### Below is a list of the programming languages, technologies, frameworks and resources used for this website.

* HTML5
* CSS3
* AWS amazon
    * AWS s3 bucket
* Django
    * Django crispy forms
    * Django allauth
    * Django Storages
* Javascript 
    * jQuery
* Python 3.8.2
    * Jinja
* Bootstrap CDN
* Git & GitHub.com
* Heroku.com pages
* Markdown
* Google Fonts
* Canva: Design of main image
* Google Chrome Developer tools
* Firefox Developer tools
* Cloudinary.com: Download image from Canva through Cloudinary to Gitpod.
* Materialize - base project layout

### Dtabases used
#### Stripe API
[Stripe API](https://stripe.com/en-ie) - Payment processor.
 
#### PostgresSQL
[PostgresSQL](https://www.postgresql.org/) Open source object-relational database system.
 
#### SQlite3
 
[SQLite](https://www.sqlite.org/) is a C-language library that implements a small, fast, self-contained, high-reliability, full-featured, SQL database engine.


## Testing
### Used multiple devices to test functionality and visual appeal:

* Iphone - Safari
    * Iphone 10
    * Iphone 11
* Ipad - Safari
    * Ipad pro
* Sony 15.6inch laptop - Chrome
* Windows Toshiba tablet/laptop - Chrome

### Manual testing

Continuously testing the functionality and visuals on a laptop, ipad and mobile after every change or code inputted.
Used force refresh to ensure everything was how I intended it to be.

1. Home page

* Test if navigation bar works correctly on phone, tablet and desktop browsers
* Test if page is responsive at all sizes

2. Add 

* Test the add product form that it adds to the database.
* Test that the product shows up on website after adding.
* Test that the form has to be  entered correctly and if not gives guidance on how to syntax the form.

3. Edit 

* Test that the edit button brings you to the edit page.
* Test that once edited it corrrectly shows the new edit on the product detail page.
* Test that the form has to be entered correctly and if not gives guidance on how to syntax the form.

4. Delete

* Test that once deleted product it is also deleted off the database.

5. messages/toast

* Test once added a product to cart, a message/toast appears.
* Test once edited a product, a  message/toast appears.
* Test once deleted a product, a message/toast appears.

6. Fitness programme

* Test that cannot buy without registering
* Test once bought gives access to fitness lessson.

### Validators

* [W3Cschools css validator](https://jigsaw.w3.org/css-validator/validator) - Validate my css code to make sure there are no errors.
* [W3Cschools html validator](https://validator.w3.org/) - Validate my html code to make sure there are no errors.
* [beautifytools javascript validator](http://beautifytools.com/javascript-validator.php) - Validate my javascript code.
* [JSHint](https://jshint.com) - Check for errors.
* [PEP8](http://pep8online.com) - Warnings for lines too long when attempted to fix AUTOPEP8 would break code but other than this no errors.


## Deployment

For this project we used Heroku to deploy the app. We also used AWS as a databse holder for static and media files and then Gitpod as our IDE.

#### Heroku

Firstly we need to set up files that Heroku needs to run the app.

These are the applications and dependencies to run the app.
```
pip3 freeze --local > requirements.txt
```
Next the Procfile is what heroku looks for to know which file runs the app and how to run it.
```
echo web: python app.py > Procfile
```

Once the files have been created. Log on or create an account with Heroku and create an app.
* The app name must be unique with no spaces and in lower case.
* Link that app to the GitHub repository by going to the "Deployment method".
* Once linked scroll down to "Connect to Github" and add your repository name and click search and then connect.
* In the Settings tab, add the corresponding Config Variables as present in local development:
```
DATABASE_URL postgress://...
SECRET_KEY FJHFJD7474...
```
* Now that the config variables are inserted but before deployment you must go back and git push the Procfile and Requirements.txt
to github.
```
git add -A
```
```
git commit -m "Add Procfile and requirements.txt"
```
```
git push
```

* Next enable deployment on heroku
* Deploy master branch
* Now that we have Deployed Branch Heroku will start buliding the app which takes 2 minute.
* Once bulit it will have a message "Your app was successfully deployed."
* Click view underneath the message to launch the app.
* The app is now deployed on heroku and whenever you push changes to github it will also be linked to the heroku app.

#### AWS

AWS amazon account was created for holding media and static files and will need to create a s3 bucket to put them in - [AWS - S3 bucket](https://docs.aws.amazon.com/AmazonS3/latest/gsg/CreatingABucket.html)


## Credits

### Content

* [Nav](https://materializecss.com/navbar.html)
* [Side-nav](https://materializecss.com/navbar.html)
* [Dropdown](https://materializecss.com/dropdown.html)
* [form](https://materializecss.com/text-inputs.html)
* [Image-card](https://materializecss.com/cards.html)
* [Stipe API](https://stripe.com/) - Database payment integration

## Media

Majority of the images used are from google images

* [Home page and logo image](https://www.canva.com/q/pro/?v=2&utm_source=google_sem&utm_medium=cpc&utm_campaign=REV_UK_EN_CanvaPro_Branded_Tier1_Core_EM&utm_term=REV_UK_EN_CanvaPro_Branded_Tier1_Canva_EM&gclsrc=aw.ds&&gclid=CjwKCAiA57D_BRAZEiwAZcfCxS1r2A6K6RbcJkAtuN2r1_yHKOvyTpoZdYPBrb7o39scG68WCw06NBoCXcwQAvD_BwE&gclsrc=aw.ds)

## Acknowlegements

* Help and guidance from my mentor _Akshat Grag_.
* Inspiration and code guidance from code institue Boutique Ado project from Chris Zielinski
