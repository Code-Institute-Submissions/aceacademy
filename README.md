# Ace Academy

### Full Stack Frameworks with Django Project (Code Institute)

This project is built as a platform for students looking to learn Math conveniently affordably without having to pay a full tuition price! The webpage seeks to also build a community of learning to encourage students through their math journey.

***

## Objective
The education landscape in Singapore is ever-competitive and students feel pressued to fork out a hefty sum of money to keep up with their peers. However, it is no doubt that not every student can afford additional tuition. This website seeks to equalise the education scene, beginning with mathematics, by introducing cost-saving and effective classes distributed digitally. Likewise, this also seeks to boost the gig economy by allowing freelance educators to partake in this movement and help build the community. 

In short, this website seeks to achieve two main objectives:
1. Allow students to purchase mathematic lessons taught by qualified tutors
2. Build a community to help each other with math problems

### External user’s goal:
* To gain knowledge in mathematics without having to pay full tuition fees
* Able to pick and choose topics that are catered to their needs
* To learn from mathematical problems posed by other users

### Site owner’s goal:
* To build a mobile responsive site to provide a means for users to learn and equip themselves with GSCE syllabus content
* To build a supportive community for students with math questions
* To profit from the sales, which can be used to support freelance educators and in the future expand into other subjects

***

## Objective-based design

## UX
The UX is designed to deliver the webpage objective as seamlessly and as lean as possible to prevent users from "dropping off" due to undesirable experience. With minimal clicks, users can easily set up an account, browse through selections, information and posts, and very easily purchase the resource materials easily.

The backend infrastructure is divided into 4 main sections - **Lessons**,**Instructors**, **Reviews**, **Forum**, **Comment** and **Checkout/Cart**. The webpage is also deliberate in providing different functions to the following 3 groups of users: **Admin**, **User**, **Public**. A public user can view most pages, but additional functions/viewings will be gated. Users have access to all materials and can purchase them but cannot edit content on webpage. Administrators are for teachers and they have access to CRUD content.

* Each section is easily accessible from the dynamic navigation bar at the top of the page which changes based on the user authentication. (navbar catered uniquely to each group_
* Webpage is broken down into short segments
* Each page is made mobile responsive for devices with smaller screens.

#### Wireframe:
<img src="/static/img/readme/wireframe.png" alt="Devices Mockup">

### Home Page
<img src="/static/img/readme/homepage.png" alt="Devices Mockup">
* Modern vector designs were deliberately used to appeal to young users

### Lessons
The page displays a comprehensive library of math lessons
Each course also has its own separate details page with its own review section which can only be contributed by acccount users. 

**Non-Authenticated Users**
* As a public user, I am able to view all lessons - including, price, title, content (but truncated)
* As a public user, I am redirected to register page if I click on a button to start learning
* As a public user, I am redirected to register page if I click on read more
* As a public user, I am able to search the lessons

**Authenticated**
* As a user, I am able to view all lessons - including price, title, content (truncated) etc.
* As a user, I am directed to lesson details if I click on read more or details
* As a user, I can add item to my cart if I want the lesson
* As a user, I am able to leave a review for the lesson
* As a user, I am able to search the lessons

**Administrators**
* As an admin, I am able to CRUD lessons
* As an admin, I am able to search lessons

### Instructors
**Non-Authenticated Users**
* As a public user, I am able to view all instructors
* As a public user, I am able to search the instructors

**Authenticated**
* As a public user, I am able to view all instructors
* As a public user, I am able to search the instructors

**Admin**
* As an admin, I am ale to CRUD instructors
* As an admin, I am able to search instructors

### Cart

**Authenticated only**
Only authenticated users have access to this shopping cart page. These users will be able to view the items they have added to the cart, update the quantity and even remove line items. The cart is dynamic and re-calculates based on the item, quantity and price. Once they click 'checkout', it will direct them through the Stripe Payment process.

### Forum
**Public User** & **Authenticated**
* As a public user & user, I am able to view all threads posted on the forum
* As a public user & user, I am able to create a thread in the forum
* As a public user & user, I am able to view the answers in the thread 

**Forum**
* As an admin, I am able to CRUD the forum
* As an admin, I am able to CRUD the answers

***

## UI
The UI is designed with simplicity in mind. The color scheme seeks to evoke excitement for learning and vector designed graphics aims to appeal to the students, who are mostly teenagers. The site was designed-first with desktop intention, as most students will use desktop to learn instead of smaller devices. On this note, the site is still mobile responsive and can be used any way.

## Technologies Used
The following programming languages and tools were used to build the website:

- HTML 5
- CSS
- JavaScript
- Bootstrap v4.4
- jQuery library for DOM manipulation
- Python
- Django framework
- Heroku for Deployment
- PostgreSQL database
- Gitpod and Visual Studio Codefor the writing of codes and testing of website
- W3C Markup Validation Service for HTML and CSS validation
- GitHub for repository hosting

### Database
The deployed web application uses SQL database to store its data.
- The entities are all inter-related, hence a relational database was required
- SQL was selected instead of MongoDb which stores data in JSON format

Entity Relationship Diagram:<br>
<img src="/static/img/readme/erd-diagram.png" alt="Devices Mockup">
    
**To experience different user perspective**:
- Public User: [Mainpage](https://aceacademy.herokuapp.com)
- Authenticated User: [Register as one!](https://aceacademy.herokuapp.com/accounts/signup)
- Admin User: 
-- username/email: alexiahsu/hsu.enyang@gmail.com
-- password: tgc123456

## Testing

The website has been tested for viewing and responsiveness on various screen sizes, including but not limited to the following web browsers and devices:

- Apple Safari Web Browser
  1. macOS
  2. Windows 10
  3. iOS
  4. iPadOS
- Mozilla Firefox Web Browser
  1. macOS
  2. Windows 10
  3. Android 10
- Microsoft Edge (Chromium) Web Browser
  1. macOS
  2. Windows 10
  3. Android 10
- Google Chrome Web Browser
  1. macOS
  2. Windows 10
  3. Android 10

* HTML, CSS validated by W3C Markup Validation

1. Page by page testing was completed for each of the users perspective
2. Each CRUD was referenced to database
3. Upon deployment to Heroku, database was replaced with PostgreSQL where checking was completed again
4. External pages like allauth or stripe were tested as well
5. UI/UX feedback were given by Code Institute changes were made accordingly

## Roadblocks
- Unable to have cloudinary instance in the lessons and instructor updates
- Not enough time to apply page concept to this project
- Did not implement filter function beyond search bar
- Countup JS is not working

## Hypothetical future plans
- Expand to other subjects
- Introduce page, cloudinary instance and filter function as per roadblocks

***

## Deployment

The website is deployed on Heroku, using GitHub to host the project repository. The website can be found at this [link](http://aceacademy.herokuapp.com).<br>
The deployment process is as such:
1. Code was written on gitpod using Code Institute's template. Heroku was installed in gitpod and setup using an existing account.
2. An application was created on heroku using an unique name and environment variables such as passwords and session keys were added to the application settings.
3. Database was switched over to PostgreSQL as Heroku did not support SQLite.
4. Content was populated again using interface as part of application testing.
5. Deployed website was provided to testers for testing purposes, afterwhich adjustments were made.
6. Code was pushed onto Heroku again after changes were done, and final testing was conducted to check the UI/UX elements and processes.
7. Final adjustments were made and pushed onto Heroku for submission.

***

## Credits
This website was built using tools and data from various sources, including but not limited to the following:

- [Heroku](https://www.heroku.com) for the hosting of the web application.
- [Unsplash](https://unsplash.com/) for the images of humans page.
- [Vecteezy](vecteezy.com) for the vector images
- [Placeitnet](https://placeit.net/) for designing logo for free
- [CSS Template](https://colorlib.com/) for css template
- [Stripe](https://stripe.com/en-sg) for payment platform
- [Allauth](https://django-allauth.readthedocs.io/en/latest/) for user authentication routes
- [jQuery script.net](https://www.jqueryscript.net/slider/responsive-bootstrap-carousel-multiple-items.html) for the multi-item responsive carousel sample
- [favicon.io](https://favicon.io/favicon-converter) for the favicon generator 
- [Trent Global](https://www.trentglobal.edu.sg/diplomainsoftwaredevelopment/?gclid=EAIaIQobChMI8M3ezf6t6QIV2BwrCh2R6A44EAAYASAAEgL6__D_BwE) and [Code Institute](https://codeinstitute.net) for the teachings and support to have made this project possible.**
