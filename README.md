# Delicious recipes
(Developer: Bilan Mykhailo)

[Live webpage](https://cookingblognew-0b91b3c6b01a.herokuapp.com/)

![Mockup image](docs/mockup.jpg)

## Table of Content
1. [About Project](#about-project)
2. [Project Goals](#project-goals)
    1. [User Goals](#user-goals)
    2. [Site Owner Goals](#site-owner-goals)
3. [User Experience](#user-experience)
    1. [Target Audience](#target-audience)
    2. [User Requrements and Expectations](#user-requrements-and-expectations)
    3. [User Stories](#user-stories)
    4. [Site Owner Stories](#site-owner-stories)
4. [Design](#design)
    1. [Design Choices](#design-choices)
    2. [Colors](#colors)
    3. [Fonts](#fonts)
    4. [Structure](#structure)
       1. [Home Page](#home-page)
       2. [Create Post Page](#create-post-page)
       3. [Post Detail Page](#post-detail-page)
       4. [Update Post Detail Page](#update-post-detail-page)
       5. [Delete Post Detail Page](#delete-post-detail-page)
       6. [Categories Page](#categories-page)
       7. [Profile Page](#profile-page)
       8. [Update Profile Page](#update-profile-page)
       9. [Create Profile Page](#create-profile-page)
       10. [Contact Page](#contact-page)
       11. [Thanks Page](#thanks-page)
       12. [SignUp Page](#signup-page)
       13. [LogIn Page](#login-page)
       14. [LogOut Page](#logout-page)
    5. [Wireframes](#wireframes)
5. [Database](#database)
    1. [Models Used](#models-used)
       1. [User](#user)
       2. [CookingRecipePost](#cookingrecipepost)
       3. [Comment](#comment)
       4. [Category](#category)
       5. [Profile](#profile)
       6. [Contact](#contact)
6. [Agile](#agile)
7. [Features](#features)
    1. [Blocks are typical for all pages](#blocks-are-typical-for-all-pages)
        1. [Logo and Navbar](#logo-and-navbar)
        2. [Footer](#footer)
    2. [Blocks are not typical for all pages](#blocks-are-not-typical-for-all-pages)
        1. [Home Page (Features)](#home-page-features)
        2. [Create Post Page (Features)](#create-post-page-features)
        3. [Detail Post Page (Features)](#delete-post-page-features)
        4. [Update Post Page (Features)](#update-post-page-features)
        5. [Delete Post Page (Features)](#delete-post-page-features)
        6. [Categories Page (Features)](#categories-page-features)
        7. [Create Profile Page (Features)](#create-post-page-features)
        8. [Profile Page (Features)](#profile-page-features)
        9. [Update Profile Page (Features)](#update-post-page-features)
        10. [Contact Page (Features)](#contact-page-features)
        11. [Thanks Page (Features)](#thanks-page-features)
        12. [SignUp Page (Features)](#signup-page-features)
        13. [LogIn Page (Features)](#login-page-features)
        14. [LogOut Page (Features)](#logout-page-features)
8. [Technologies Used](#technologies-used)
    1. [Languages & Frameworks](#languages--frameworks)
    2. [Libraries & Tools](#libraries--tools)
9. [Validation](#validation)
    1. [HTML](#html)
    2. [CSS](#css)
    3. [JS](#js)
    4. [Python](#python)
        1. [Cookingproject](#cookingproject)
        2. [Cookingblock](#cookingblock)
        3. [Customactions](#customactions)
10. [Testing]
    1. [User Story Testing](#user-story-testing)
    2. [Site Owner Stories Testing](#site-owner-stories-testing)
    3. [Device testing](#device-testing)
    4. [Browser compatibility](#browser-compatibility)
11. [Bugs](#bugs)
12. [Deployment](#deployment)
    1. [Workspace](#workspace)
    2. [Heroku](#heroku)
    3. [PostgreSQL](#postgresql)
    4. [Cloudinary](#cloudinary)
    5. [Last Deployment Steps](#last-deployment-steps)
    6. [Cloning the repository](#cloning-the-repository)
    7. [Forking the GitHub Repository](#forking-the-github-repository)
13. [Credits](#credits)
    1. [Content](#content)
    2. [Media](#media)
    3. [Code](#code)
14. [Acknowledgements](#acknowledgements)




## About Project
A simple, colorful and interesting website with delicious culinary recipes, where anyone can post a recipe for their favorite dishes or watch, comment and rate recipes posted by other users

## Project Goals

### User Goals

 - Create your own culinary blog
 - View interesting recipes for various dishes
 - Rate and comment on interesting recipes for various dishes


### Site Owner Goals

  - Provide the opportunity for various users to post recipes for their favorite dishes
  - Create a beautiful, easy-to-use website with rich functionality (registration, comments, updates, etc.)

## User Experience

### Target Audience

- People of different ages who want to post a recipe for their favorite dishes or watch, comment and rate recipes posted by other users

### User Requrements and Expectations

- Simple and user-friendly to use
- Interactive interaction with the user (reaction to user actions)
- Fully adaptive and beautiful design
- Accessible navigation, links working as expected

### User Stories 

1. As User I can use navigation bar so that I can easy to navigate the site.
2. As a site user, I want to be able to see a list of all site posts on the main page
3. As a user of the site, I want to be able to view my posts as well as the posts of other users
4. As a site user, I want the post to contain a photo of the dish and a description of the cooking process
5. As a registered user of the site, I want to be able to post, update and delete posts in which I am the author
6. As a registered user of the site, I want to be able to rate posts
7. As a registered user of the site, I want to be able to comment on posts, as well as the ability to delete comments
8. As a site user, I want to see all possible categories of site posts on the main page
9. As a site user, I can select a specific category of posts that are interesting to me
10. As a registered user of the site I can create and update profile page
11. As a registered user of the site, I can see all my published posts on the portfolio page
12. As a user of the site I can see interesting quotes and aphorisms about food
13. As a user of the site, I would like to receive notifications about my actions


### Site Owner Stories

1. As the owner of the site, I want only authorized users to have access to all the functionality of the site
2. As the owner of the site, I want the registered user to be able to update and delete posts only if he is the author
3. As a site owner, I want to be able to pre-approve user posts and comments to avoid publishing inappropriate content
4. As the owner of the site, I want the post to contain a photo of the dish and a description of the cooking process
5. As the owner of the site I can receive feedback from registered users
6. As the owner of the site, I can place links to the project’s social pages on every page of the site

## Design

### Design Choices

The site was created in such a way as to maximize the interest of users and provide the opportunity to easily and simply use the functionality of the site.

### Colors

The main color palette was chosen in accordance with the basic colors of the bootstrap framework. The dark background includes contrasting white font. To draw attention to certain content on the site, two bright accent colors are used

<details><summary>Colour pallet</summary>
<img src="docs/colors.png">
</details>

### Fonts

For plain text, the Mulish font is used, connected using google fonts. For headings, Young Serif font was used. Inter font used for other text. Used fonts are well combined with each other


### Structure

The site structure is designed to ensure maximum ease of use. Also, much attention is paid to the stylistic beauty of the site. All pages of the site have the same header with a navigation menu and a footer containing links to social networks

#### Home Page

- The home page consists of three sections: navigation menu, main section, right additional section and footer.

- The main section displays posts published by site users (main picture, short description of the recipe, date of creation, author and number of likes)

- Right-side section contains a list of post categories, as well as a block with quotes about food.

#### Create Post Page

- The page consists of three sections: header, main section and footer. The footer and header sections are standard for the entire site.

- The main section of the page displays a form with various fields for updating the post.

#### Post Detail Page

- The page consists of three sections: header, main section and footer. The footer and header sections are standard for the entire site

- The main section displays the full text of the post with a cover image on the left and a description on the right. Below is a block with the date the post was created and the author. Below is a block with comments and a comment form for authorized users.

#### Update Post Page

- The page consists of three sections: header, main section and footer. The footer and header sections are standard for the entire site.

- The main section of the page displays a form with various fields for updating the post.

#### Delete Post Page

- The page consists of three sections: header, main section and footer. The footer and header sections are standard for the entire site.

- The main section of the page is a warning about deleting a post and buttons for deleting and canceling

#### Categories Page

- This page uses the home page template, but only displays posts from a specific category

#### Profile Page

- The page consists of three sections: header, main section and footer. The footer and header sections are standard for the entire site.

- The main page is conditionally divided into two parts. The first part contains the user's avatar and brief information about him. The second part contains a list of the user’s posts with a picture and a brief description or, if the user has no posts display a message about the presence and a button to add a post.

#### Update Profile Page

- The page consists of three sections: header, main section and footer. The footer and header sections are standard for the entire site.

- The main section of the page displays a form with various fields for updating the profile.

#### Create Profile Page

- The page consists of three sections: header, main section and footer. The footer and header sections are standard for the entire site.

- The main section of the page displays a form with various fields for creating profile.

#### Contact Page

- The page consists of three sections: header, main section and footer. The footer and header sections are standard for the entire site.

- The main section of the page displays a form with various fields for creating message.

#### Thanks Page

- The page consists of three sections: header, main section and footer. The footer and header sections are standard for the entire site.

- The main section of the page is notification of sending a message and buttons to return to the main page and to write a new message

#### SignUp Page

- The page consists of three sections: header, main section and footer. The footer and header sections are standard for the entire site.

- The main section of the page displays a form with various fields for registrate on the site.

#### LogIn Page

- The page consists of three sections: header, main section and footer. The footer and header sections are standard for the entire site.

- The main section of the page displays a form with various fields for log in on the site.

#### LogOut Page

- The page consists of three sections: header, main section and footer. The footer and header sections are standard for the entire site.

- The main section of the page is notification of leaving the site and button for confirmation 

### Wireframes

<details><summary>Home Page Wireframes</summary>

<details><summary>Home Page Fullscreen</summary>
<img src="docs/wireframe-images/home-page.png">
</details>

<details><summary>Home Page Ipad</summary>
<img src="docs/wireframe-images/home-page-ipad.png">
</details>

<details><summary>Home Page Mobile</summary>
<img src="docs/wireframe-images/home-page-iphone.png">
</details>
</details>

<details><summary>Detail Page Wireframes</summary>

<details><summary>Detail Page Fullscreen</summary>
<img src="docs/wireframe-images/detail-page.png">
</details>

<details><summary>Deatail Page Ipad</summary>
<img src="docs/wireframe-images/detail-page-ipad.png">
</details>

<details><summary>Detail Page Mobile</summary>
<img src="docs/wireframe-images/detail-page-iphone.png">
</details>
</details>

<details><summary>Add Post Page Wireframes</summary>

<details><summary>Add Post Page Fullscreen</summary>
<img src="docs/wireframe-images/add-post-page.png">
</details>

<details><summary>Add Post Page Ipad</summary>
<img src="docs/wireframe-images/add-post-page-ipad.png">
</details>

<details><summary>Add Post Page Mobile</summary>
<img src="docs/wireframe-images/add-post-page-iphone.png">
</details>
</details>

<details><summary>Update Post Page Wireframes</summary>

<details><summary>Update Post Page Fullscreen</summary>
<img src="docs/wireframe-images/update-post-page.png">
</details>

<details><summary>Update Post Page Ipad</summary>
<img src="docs/wireframe-images/update-post-page-ipad.png">
</details>

<details><summary>Update Post Page Mobile</summary>
<img src="docs/wireframe-images/update-post-page-iphone.png">
</details>
</details>

<details><summary>Delete Post Page Wireframes</summary>

<details><summary>Delete Post Page Fullscreen</summary>
<img src="docs/wireframe-images/delete-post-page.png">
</details>

<details><summary>Delete Post Page Ipad</summary>
<img src="docs/wireframe-images/delete-post-page-ipad.png">
</details>

<details><summary>Delete Post Page Mobile</summary>
<img src="docs/wireframe-images/delete-post-page-iphone.png">
</details>
</details>

<details><summary>Profile Page Wireframes</summary>

<details><summary>Profile Page Fullscreen</summary>
<img src="docs/wireframe-images/profile-page.png">
</details>

<details><summary>Profile Page Ipad</summary>
<img src="docs/wireframe-images/profile-page-ipad.png">
</details>

<details><summary>Profile Page Mobile</summary>
<img src="docs/wireframe-images/profile-page-iphone.png">
</details>
</details>

<details><summary>Update Profile Page Wireframes</summary>

<details><summary>Update Profile Page Fullscreen</summary>
<img src="docs/wireframe-images/update-profile-page.png">
</details>

<details><summary>Update Profile Page Ipad</summary>
<img src="docs/wireframe-images/update-profile-page-ipad.png">
</details>

<details><summary>Update Profile Page Mobile</summary>
<img src="docs/wireframe-images/update-profile-page-iphone.png">
</details>
</details>

<details><summary>Contact Page Wireframes</summary>

<details><summary>Contact Page Fullscreen</summary>
<img src="docs/wireframe-images/contact-page.png">
</details>

<details><summary>Contact Page Ipad</summary>
<img src="docs/wireframe-images/contact-page-ipad.png">
</details>

<details><summary>Contact Page Mobile</summary>
<img src="docs/wireframe-images/contact-page-iphone.png">
</details>
</details>

<details><summary>Thanks Page Wireframes</summary>

<details><summary>Thanks Page Fullscreen</summary>
<img src="docs/wireframe-images/thanks-page.png">
</details>

<details><summary>Thanks Page Ipad</summary>
<img src="docs/wireframe-images/thanks-page-ipad.png">
</details>

<details><summary>Thanks Page Mobile</summary>
<img src="docs/wireframe-images/thanks-page-iphone.png">
</details>
</details>

<details><summary>SignUp Page Wireframes</summary>

<details><summary>SignUp Page Fullscreen</summary>
<img src="docs/wireframe-images/signup-page.png">
</details>

<details><summary>SignUp Page Ipad</summary>
<img src="docs/wireframe-images/signup-page-ipad.png">
</details>

<details><summary>SignUp Page Mobile</summary>
<img src="docs/wireframe-images/signup-page-iphone.png">
</details>
</details>

<details><summary>Login Page Wireframes</summary>

<details><summary>Login Page Fullscreen</summary>
<img src="docs/wireframe-images/login-page.png">
</details>

<details><summary>Login Page Ipad</summary>
<img src="docs/wireframe-images/login-page-ipad.png">
</details>

<details><summary>Login Page Mobile</summary>
<img src="docs/wireframe-images/login-page-iphone.png">
</details>
</details>

<details><summary>Logout Page Wireframes</summary>

<details><summary>Logout Page Fullscreen</summary>
<img src="docs/wireframe-images/logout-page.png">
</details>

<details><summary>Logout Page Ipad</summary>
<img src="docs/wireframe-images/logout-page-ipad.png">
</details>

<details><summary>Logout Page Mobile</summary>
<img src="docs/wireframe-images/logout-page-iphone.png">
</details>
</details>


## Database

- For this Django app I ve used PostgreSQL relational database management system.

<details><summary>Database model</summary>
<img src="docs/db-diagram.jpg">
</details>

### Models Used

#### User

- standard Django user model which contains username, password and email fields

#### CookingRecipePost

- The model was created to provide the user with the ability to create, view, edit and delete posts on the site. this model contains the following fields

- cooking_recipe_title
   - type: CharField
   - validation: max_length=200, unique=True

- slug
   - type: SlugField
   - validation: max_length=200, unique=True 

- cooking_recipe_author
    - type: ForeignKey
    - validation: User, on_delete=models.CASCADE,

- cooking_recipe_image
   - type: CloudinaryField
   - validation: 'image', default='placeholder' 

- excerpt
   - type: TextField
   - validation: blank=True 

- cooking_recipe_body
   - type: TextField
   - validation: -

- updated_on
   - type: DateTimeField
   - validation: auto_now=True 

- created_on
   - type: DateTimeField
   - validation: auto_now_add=True 

- status
   - type: IntegerField
   - validation: auto_now_add=True 

- likes
   - type: ManyToManyField
   - validation: User, blank=True

- cat
   - type: ForeignKey
   - validation: 'Category', on_delete=models.PROTECT

#### Comment

- The model was created to allow user interaction with comments on posts. this model contains the following fields

- cooking_recipe_post
   - type: ForeignKey
   - validation: CookingRecipePost, on_delete=models.CASCADE,

- name
   - type: CharField
   - validation: max_length=80 

- email
    - type: EmailField
    - validation: -

- body
   - type: TextField
   - validation: max_length=500 

- created_on
   - type: DateTimeField
   - validation: auto_now_add=True 

- approved
   - type: BooleanField
   - validation: default=False


#### Category

- The model was created to provide the ability to define categories of posts for their subsequent filtering. this model contains the following fields

- name
   - type: CharField
   - validation: max_length=100, db_index=True

- slug
   - type: SlugField
   - validation: max_length=255, unique=True, db_index=True

#### Profile

- The model was created to allow the user to create a profile with personal information and an avatar, which improves the quality of the user’s interaction with the site. this model contains the following fields

- user
   - type: OneToOneField
   - validation: User, on_delete=models.CASCADE

- nickname
   - type: CharField
   - validation: blank=True, max_length=50

- avatars
   - type: CloudinaryField
   - validation: 'image', default='placeholder'

- bio
   - type: TextField
   - validation: max_length=500, blank=True

- birth_date
   - type: DateField
   - validation: null=True, blank=True

- region
   - type: CharField
   - validation: blank=True, max_length=50

- occupation
   - type: CharField
   - validation: blank=True, max_length=50

#### Contact

- The model was created to allow user interaction with comments on posts. this model contains the following fields

- name
   - type: CharField
   - validation: max_length=120 

- email
    - type: EmailField
    - validation: -

- message
   - type: TextField
   - validation: max_length=1000 

## Agile 

- steps taken:
   1. created User Story Template
   <details><summary>User story template</summary>
   <img src="docs/agile/user-story-template.jpg">
   </details>
   2. project created [Link to project](https://github.com/users/Belan-Mihail/projects/5/)
   3. based on the user story template, issues were created. A total of 41 issues were created the main part of which was created at the very beginning of the project development process, others during the development process (which corresponds to the principles of agile development)
   <details><summary>Issues</summary>
   <img src="docs/agile/issues.jpg">
   </details>
   4. main labels have been created for marking issues and marked issues in accordance with Moscow Prioritisation
   5. Kanban Board was created to visualize the process of completing tasks
   <details><summary>Kanban Board</summary>
   <img src="docs/agile/kanban-board.jpg">
   </details>


- This project was the first time I used agile development methods. The importance of these principles is beyond doubt. There may have been certain inaccuracies in the use of all the principles of this methodology.


## Features

### Blocks are typical for all pages

#### Logo and Navbar

- A navigation bar is displayed on all pages for easy navigation around the site.
- The navigation bar consists of the site logo (which is a link to the main page) and a drop-down link containing links to the login and registration pages.
- An authenticated user (without a profile) sees other links in the drop-down link block:
      - Profile creation page
      - Link to the exit page from the site
      - Add post page
- Additionally, for an authorized user, a link to the contact page appears
- An authenticated user (having a profile), instead of a link to the profile creation page, sees a link to the profile page in the drop-down link block
- The navigation bar is adaptive and turns into a “hamburger menu” on small screens.

- User Story covered with this feature: 1, 5, 10
- Site Owner Story covered with this feature: 1, 5


![Logo an Navbar](docs/features/navbars/logo-and-navigation-1.jpg)
![Logo an Navbar](docs/features/navbars/logo-and-navigation-2.jpg)
![Logo an Navbar](docs/features/navbars/logo-and-navigation-3.jpg)
![Logo an Navbar](docs/features/navbars/logo-and-navigation-4.jpg)

#### Footer

- The footer is displayed on all pages of the site

- The footer contains links to social networks that open in a new tab.

- Site Owner Story covered with this feature: 6

![Footer](docs/features/footer/footer.jpg)

### Blocks are not typical for all pages

#### Home Page (Features)

- The main page consists of three sections: navigation menu, main section, right additional section and footer.

- The main section displays posts published by site users (main picture, short description of the recipe, date of creation, author and number of likes)

- Right-side section contains a list of post categories, as well as a block with quotes about food.

- For authorized users, a stick notification about authorization is displayed in the right corner

- When the user performs authorization and other actions as a result of which he is redirected to the main page, a notification appears about the implementation of the corresponding actions by the user

- If the number of posts on the main page exceeds 5, the page pagination function is triggered

- User Story covered with this feature: 2, 4, 8, 10, 12,

![Home page](docs/features/home-page/home-page-1.jpg)
![Home page](docs/features/home-page/home-page-2.jpg)
![Home page](docs/features/home-page/home-page-3.jpg)
![Home page](docs/features/home-page/home-page-4.jpg)


#### Create Post Page (Features)

- The page consists of three sections: header, main section and footer. The footer and header sections are standard for the entire site.

- The main section of the page displays a form with various fields for updating the post.

- This page is available only to authorized site users

- After creation, the post is initially submitted for approval to the administration (about which a notification is displayed to the user) and the user is redirected to the main page of the site


- User Story covered with this feature: 1, 5, 10
- Site Owner Story covered with this feature: 1, 3


![Create Post Page](docs/features/create-post/create-post-1.jpg)
![Create Post Page](docs/features/create-post/create-post-2.jpg)
![Create Post Page](docs/features/create-post/create-post-3.jpg)
![Create Post Page](docs/features/create-post/create-post-4.jpg)


#### Detail Post Page (Features)

- The page consists of three sections: header, main section and footer. The footer and header sections are standard for the entire site.

- The main section displays the full text of the publication with a cover image on the left and a description on the right. Below is a block with the date the post was created and the author, as well as the number of likes the user received. A block with comments is displayed even lower. The likes function is not available for non-authorized users.

- An authorized user who is not the author of the post also sees the comment form. The likes function is available for such a user

- For an authorized user who is the author of the post, buttons to update the recipe and delete the recipe are additionally displayed.

- For the user who is the author of the comment, a button to delete the comment is additionally displayed.

- After adding a comment, the comment requires approval by the administrator (about which a notification is displayed to the user)

- User Story covered with this feature: 3, 4, 5, 6, 7, 13
- Site Owner Story covered with this feature: 1, 2, 3, 4

![Detail Post Page](docs/features/detail-post/detail-post-1.jpg)
![Detail Post Page](docs/features/detail-post/detail-post-2.jpg)
![Detail Post Page](docs/features/detail-post/detail-post-3.jpg)
![Detail Post Page](docs/features/detail-post/detail-post-4.jpg)
![Detail Post Page](docs/features/detail-post/detail-post-5.jpg)
![Detail Post Page](docs/features/detail-post/detail-post-6.jpg)


#### Update Post Page (Features)

- The page consists of three sections: header, main section and footer. The footer and header sections are standard throughout the site.

- The main section of the page displays a form with various fields for updating the publication.

- This page is available only to authorized users of the site who are the authors of the post

- After updating, the post is initially submitted for approval to the administration (about which the user is notified) and the user is redirected to the main page of the site.

- User history covered by this feature: 5, 13.
- History of the site owner covered by this function: 1, 3.


![Update Post Page](docs/features/update-post/update-post-1.jpg)
![Update Post Page](docs/features/update-post/update-post-2.jpg)
![Update Post Page](docs/features/update-post/update-post-3.jpg)
![Update Post Page](docs/features/detail-post/detail-post-4.jpg)
![Update Post Page](docs/features/detail-post/detail-post-5.jpg)


#### Delete Post Page (Features)

- The page consists of three sections: header, main section and footer. The footer and header sections are standard throughout the site.

- The main section of the page is a warning about deleting a post and buttons for deleting and canceling

- This page is available only to authorized users of the site who are the authors of the post


- User history covered by this feature: 5, 13.
- History of the site owner covered by this function: 1, 3.


![Delete Post Page](docs/features/delete-post/delete-post-1.jpg)
![Delete Post Page](docs/features/delete-post/delete-post-2.jpg)
![Delete Post Page](docs/features/detail-post/detail-post-4.jpg)
![Delete Post Page](docs/features/detail-post/detail-post-5.jpg)



#### Categories Page (Features)

- This page uses the home page template, but only displays posts from a specific category


- User history covered by this feature: 9


![Categories Page](docs/features/categories/categories-1.jpg)
![Categories Page](docs/features/categories/categories-2.jpg)


#### Create Profile Page (Features)

- The page consists of three sections: header, main section and footer. The footer and header sections are standard for the entire site.

- The main section of the page displays a form with various fields for creating profile.

- The page is only available to registered users without a profile


- User history covered by this feature: 10, 11
- History of the site owner covered by this function: 1,


![Logo an Navbar](docs/features/navbars/logo-and-navigation-2.jpg)
![Create Profile Page](docs/features/create-profile/create-profile-1.jpg)
![Create Profile Page](docs/features/create-profile/create-profile-2.jpg)


#### Profile Page (Features)

- The page consists of three sections: header, main section and footer. The footer and header sections are standard for the entire site.

- - The main page is conditionally divided into two parts. The first part contains the user's avatar and brief information about him. The second part contains a list of the user’s posts with a picture and a brief description or, if the user has no posts display a message about the presence and a button to add a post.

- The page is only available to registered users with a created profile


- User history covered by this feature: 10, 11
- History of the site owner covered by this function: 1,


![Logo an Navbar](docs/features/navbars/logo-and-navigation-3.jpg)
![Profile Page](docs/features/profile/profile-1.jpg)
![Profile Page](docs/features/profile/profile-2.jpg)
![Profile Page](docs/features/profile/profile-3.jpg)



#### Update Profile Page (Features)

- The page consists of three sections: header, main section and footer. The footer and header sections are standard for the entire site.

- The main section of the page displays a form with various fields for updating the profile.

- Due to the fact that the link to the page button is located on the profile page, access to the page is possible only for an authorized user who is the owner of the profile


- User history covered by this feature: 10
- History of the site owner covered by this function: 1,


![Update Profile Page](docs/features/update-profile/update-profile-1.jpg)
![Update Profile Page](docs/features/update-profile/update-profile-2.jpg)
![Update Profile Page](docs/features/update-profile/update-profile-3.jpg)


#### Contact Page (Features)

- The page consists of three sections: header, main section and footer. The footer and header sections are standard for the entire site.

- The main section of the page displays a form with various fields for creating message.

- The page is only available to registered users

- After sending the message the user is taken to the thanks page


- History of the site owner covered by this function: 5


![Contact Page](docs/features/contact-page/contact-page-1.jpg)
![Contact Page](docs/features/contact-page/contact-page-2.jpg)
![Contact Page](docs/features/contact-page/contact-page-3.jpg)


#### Thanks Page (Features)

- The page consists of three sections: header, main section and footer. The footer and header sections are standard for the entire site.

- The main section of the page is notification of sending a message and buttons to return to the main page and to write a new message

- The page is only available to registered users


- User history covered by this feature: 13
- History of the site owner covered by this function: 1, 5


![Thanks Page](docs/features/thanks-page/thanks-page-1.jpg)
![Thanks Page](docs/features/thanks-page/thanks-page-2.jpg)
![Thanks Page](docs/features/thanks-page/thanks-page-3.jpg)



#### SignUp Page (Features)

- The page consists of three sections: header, main section and footer. The footer and header sections are standard for the entire site.

- The main section of the page displays a form with various fields for registrate on the site.


- History of the site owner covered by this function: 1


![Thanks Page](docs/features/signup-page/signup-page-1.jpg)
![Thanks Page](docs/features/signup-page/signup-page-2.jpg)
![Thanks Page](docs/features/signup-page/signup-page-3.jpg)


#### LogIn Page (Features)

- The page consists of three sections: header, main section and footer. The footer and header sections are standard for the entire site.

- The main section of the page displays a form with various fields for registrate on the site.


- History of the site owner covered by this function: 1


![Login Page](docs/features/login-page/login-page-1.jpg)
![Login Page](docs/features/login-page/login-page-2.jpg)
![Login Page](docs/features/login-page/login-page-3.jpg)


#### LogOut Page (Features)

- The page consists of three sections: header, main section and footer. The footer and header sections are standard for the entire site.

- The main section of the page displays a notification of leaving the site as well as the corresponding button.


- History of the site owner covered by this function: 1


![Thanks Page](docs/features/logout-page/logout-page-1.jpg)
![Thanks Page](docs/features/logout-page/logout-page-2.jpg)
![Thanks Page](docs/features/logout-page/logout-page-3.jpg)


## Technologies Used

### Languages & Frameworks

- HTML
- CSS
- Javascript
- JQuery
- Boostrap 5
- Python 3.12.0
- Django 3.2

### Libraries & Tools

- [Am I Responsive](http://ami.responsivedesign.is/) was usedfor creating mock-up 
- [Cloudinary](https://cloudinary.com/) to store static images files
- [Summernote](https://summernote.org/) to style the admin page 
- [Balsamiq](https://balsamiq.com/) to create the projects wireframes
- [Bootstrap 5](https://getbootstrap.com/). to style various website components
- [Api Ninjas](https://api-ninjas.com/) to displaying food quotes on the home page
- [Favicon.io](https://favicon.io) for site favicon
- [Chrome dev tools](https://developers.google.com/web/tools/chrome-devtools/) was used for checking sites components styles 
- [GitPod](https://www.gitpod.io/) was used for writing code.
- [GitHub](https://github.com/) was used as a remote repository to store project code
- [Google Fonts](https://fonts.google.com/) - for typography in project
- [Fontawesome](https://fontawesome.com/) - for displaying beautiful icons on the site (for example, like hearts)
- [Coolors](https://coolors.co/) - to create a color palette for the site
- [Paint.NET](https://getpaint.net/) - Used to process screenshots and pictures.
- [CI Python Linter](https://pep8ci.herokuapp.com/) - Used to test Python code;
- [JSHint](https://jshint.com/) - Used to test JS code;
- [Lighthouse](https://main--developer-chrome-com.netlify.app/docs/devtools/lighthouse/) - Used to test Perfomance;
- [W3C Markup validation service](https://validator.w3.org/) - Used to test HTML code
- [W3C Jigsaw CSS validation service](https://jigsaw.w3.org/css-validator/)  Used to test css;
- [WAVE WebAIM web accessibility evaluation tool](https://wave.webaim.org/) - Used to test accessibility

## Validation

### HTML

The W3C Markup Validation Service was used to validate the HTML of the website.

**Note**: ***According to the results of the code check, there were no errors directly in the HTML code. errors associated with the use of template tags and URL-links in HTML files are hidden by filtering***

<details><summary>Base</summary>
<img src="docs/validation/html-validation/validation-base-html.jpg">
</details>

<details><summary>Home</summary>
<img src="docs/validation/html-validation/validation-home-html.jpg">
</details>

<details><summary>Post Detail</summary>
<img src="docs/validation/html-validation/validation-post-detail-html.jpg">
</details>

<details><summary>Recipe Create</summary>
<img src="docs/validation/html-validation/validation-recipe-create-html.jpg">
</details>

<details><summary>Recipe Delete</summary>
<img src="docs/validation/html-validation/validation-recipe-delete-html.jpg">
</details>

<details><summary>Recipe Update</summary>
<img src="docs/validation/html-validation/validation-recipe-update-html.jpg">
</details>

<details><summary>500</summary>
<img src="docs/validation/html-validation/validation-500-html.jpg">
</details>

<details><summary>404</summary>
<img src="docs/validation/html-validation/validation-404-html.jpg">
</details>

<details><summary>LogIn</summary>
<img src="docs/validation/html-validation/validation-login-html.jpg">
</details>

<details><summary>LogOut</summary>
<img src="docs/validation/html-validation/validation-logout-html.jpg">
</details>

<details><summary>SignUp</summary>
<img src="docs/validation/html-validation/validation-signup-html.jpg">
</details>

<details><summary>Create Profile</summary>
<img src="docs/validation/html-validation/validation-create-profile-html.jpg">
</details>

<details><summary>Profile Page</summary>
<img src="docs/validation/html-validation/validation-profile-page-html.jpg">
</details>

<details><summary>Update Profile</summary>
<img src="docs/validation/html-validation/validation-update-profile-html.jpg">
</details>

<details><summary>Thanks</summary>
<img src="docs/validation/html-validation/validation-thanks-html.jpg">
</details>

<details><summary>Contact</summary>
<img src="docs/validation/html-validation/validation-contact-html.jpg">
</details>

### CSS

Jigsaw W3 Validator was used to validate the css in the project. Validator with no errors.

<details><summary>CSS</summary>
<img src="docs/validation/css-validation/validation-style-css.jpg">
</details>

### JS

JShint Validator was used to validate the js and jquery in the project. Validator with no errors.

Note: in file main.js one undefined variable "bootstrap" is an external library used

<details><summary>JS</summary>
<img src="docs/validation/js-validation/validation-main-js.jpg">
</details>

Note: in file myscript.js one undefined variable "$" which is jQuery selectors

<details><summary>jQuery</summary>
<img src="docs/validation/js-validation/validation-myscript-js.jpg">
</details>

### Python

CI Python Linter was used for validation of python files.

#### Cookingproject

<details><summary>settings.py</summary>
Note: Lines 132, 135, 138, 141, 164 contain important settings data that cannot be changed, therefore exceeding the line limit is justified 
<img src="docs/validation/python-validation/cookingproject/settings-py.jpg">
</details>

<details><summary>urls.py</summary>
<img src="docs/validation/python-validation/cookingproject/urls-py.jpg">
</details>

<details><summary>views.py</summary>
<img src="docs/validation/python-validation/cookingproject/views-py.jpg">
</details>

#### Cookingblock

<details><summary>admin.py</summary>
<img src="docs/validation/python-validation/cookingblog/admin-py.jpg">
</details>

<details><summary>forms.py</summary>
<img src="docs/validation/python-validation/cookingblog/forms-py.jpg">
</details>

<details><summary>models.py</summary>
<img src="docs/validation/python-validation/cookingblog/models-py.jpg">
</details>

<details><summary>urls.py</summary>
<img src="docs/validation/python-validation/cookingblog/urls-py.jpg">
</details>

<details><summary>views.py</summary>
<img src="docs/validation/python-validation/cookingblog/views-py.jpg">
</details>

<details><summary>test_form.py</summary>
<img src="docs/validation/python-validation/cookingblog/test-form-py.jpg">
</details>

<details><summary>test_models.py</summary>
<img src="docs/validation/python-validation/cookingblog/test-models-py.jpg">
</details>

<details><summary>test_view.py</summary>
<img src="docs/validation/python-validation/cookingblog/test-view-py.jpg">
</details>

#### Customactions

<details><summary>admin.py</summary>
<img src="docs/validation/python-validation/customactions/admin-py.jpg">
</details>

<details><summary>forms.py</summary>
<img src="docs/validation/python-validation/customactions/forms-py.jpg">
</details>

<details><summary>models.py</summary>
<img src="docs/validation/python-validation/customactions/models-py.jpg">
</details>

<details><summary>urls.py</summary>
<img src="docs/validation/python-validation/customactions/urls-py.jpg">
</details>

<details><summary>views.py</summary>
<img src="docs/validation/python-validation/customactions/views-py.jpg">
</details>

<details><summary>test_form.py</summary>
<img src="docs/validation/python-validation/customactions/test-form-py.jpg">
</details>

<details><summary>test_models.py</summary>
<img src="docs/validation/python-validation/customactions/test-models-py.jpg">
</details>

<details><summary>test_view.py</summary>
<img src="docs/validation/python-validation/customactions/test-view-py.jpg">
</details>


## Testing

### User Story Testing


   1. As User I can use navigation bar so that I can easy to navigate the site

   **Action** | **Result** 
 -----------| ----------  
 1.Being on the any site pages, on the top of the page you can see navbars. | By clicking on the buttons you can easily navigate the site 

<details><summary>Screenshot evidences</summary>
<img src="docs/user-stories/first-user-story-evidence-1.jpg">
</details> 

---

   2. As a site user, I want to be able to see a list of all site posts on the main page


   **Action** | **Result** 
 -----------| ----------  
 While on any page of the site, go to the main page and click on the logo located in the right-left corner of the page. | The main page of the site displays a list of all posts with pagination every 5 posts 

<details><summary>Screenshot evidences</summary>
<img src="docs/user-stories/second-user-story-evidence-1.jpg">
<img src="docs/user-stories/second-user-story-evidence-2.jpg">
</details>

---

   3. As a user of the site, I want to be able to view my posts as well as the posts of other users


   **Action** | **Result** 
   -----------| ----------  
 While on the main page of the site, you can select any post that interests you. | Click on the corresponding picture and you will be taken to the corresponding post page

<details><summary>Screenshot evidences</summary>
<img src="docs/user-stories/third-user-story-evidence-1.jpg">
<img src="docs/user-stories/third-user-story-evidence-2.jpg">
</details>

---

   4. As a site user, I want the post to contain a photo of the dish and a description of the cooking process


   **Action** | **Result** 
   -----------| ----------  
 While on the main page of the site, you can select any post that interests you and click. | On the post detail page you will see a picture of the recipe and a description of the recipe

<details><summary>Screenshot evidences</summary>
<img src="docs/user-stories/fourth-user-story-evidence-1.jpg">
<img src="docs/user-stories/fourth-user-story-evidence-2.jpg">
</details>

---

   5. As a registered user of the site, I want to be able to post, update and delete posts in which I am the author


   **Action** | **Result** 
   -----------| ----------  
 While on any page of the site, click on the login or register button in the navigation menu and fill out the appropriate form | A button for adding a post will become available in the navigation menu 
 Go to the page of the corresponding post | The delete and update post buttons will be available
 Click on the button you are interested in. |Depending on what you have chosen, you will be taken to the post deletion page or the post update page |
 When on the post update page, fill out the fields you are interested in and click the update post button | You will be redirected to the main page of the site, where you will receive a notification that your updated post has been sent to the administrator for approval | 
 When you are on the post deletion page, click on the button to confirm the deletion | Your post will be deleted

<details><summary>Screenshot evidences</summary>
<img src="docs/user-stories/fifth-user-story-evidence-1.jpg">
<img src="docs/user-stories/fifth-user-story-evidence-2.jpg">
<img src="docs/user-stories/fifth-user-story-evidence-3.jpg">
<img src="docs/user-stories/fifth-user-story-evidence-4.jpg">
<img src="docs/user-stories/fifth-user-story-evidence-5.jpg">
<img src="docs/user-stories/fifth-user-story-evidence-6.jpg">
<img src="docs/user-stories/fifth-user-story-evidence-7.jpg">
<img src="docs/user-stories/fifth-user-story-evidence-8.jpg">
</details>

---

   6. As a registered user of the site, I want to be able to rate posts


   **Action** | **Result** 
   -----------| ----------  
 While on any page of the site, click on the login or register button in the navigation menu and fill out the appropriate form | A button for adding a post will become available in the navigation menu 
 Go to the page of the corresponding post | To rate a post, click on the heart icon.

<details><summary>Screenshot evidences</summary>
<img src="docs/user-stories/sixth-user-story-evidence-1.jpg">
<img src="docs/user-stories/sixth-user-story-evidence-2.jpg">
<img src="docs/user-stories/sixth-user-story-evidence-3.jpg">
<img src="docs/user-stories/sixth-user-story-evidence-4.jpg">
<img src="docs/user-stories/sixth-user-story-evidence-5.jpg">
<img src="docs/user-stories/sixth-user-story-evidence-6.jpg">
</details>


---

   7. As a registered user of the site, I want to be able to comment on posts, as well as the ability to delete comments


   **Action** | **Result** 
   -----------| ----------  
 While on any page of the site, click on the login or register button in the navigation menu and fill out the appropriate form | A button for adding a post will become available in the navigation menu 
 Go to the page of the corresponding post | To add a comment, fill out the form and click the add comment button. You will receive notifications that your comment must be approved. after approval, the comment will appear on the site
 While on the page of a previously commented post, click on the delete comment button | Your comment will be deleted


<details><summary>Screenshot evidences</summary>
<img src="docs/user-stories/seventh-user-story-evidence-1.jpg">
<img src="docs/user-stories/seventh-user-story-evidence-2.jpg">
<img src="docs/user-stories/seventh-user-story-evidence-3.jpg">
<img src="docs/user-stories/seventh-user-story-evidence-4.jpg">
<img src="docs/user-stories/seventh-user-story-evidence-5.jpg">
<img src="docs/user-stories/seventh-user-story-evidence-6.jpg">
<img src="docs/user-stories/seventh-user-story-evidence-7.jpg">
</details>

---

   8. As a site user, I want to see all possible categories of site posts on the main page


   **Action** | **Result** 
   -----------| ----------  
 While on any page of the site, go to the main page and click on the logo located in the right-left corner of the page. | Possible categories of posts are displayed on the right side of the page 

<details><summary>Screenshot evidences</summary>
<img src="docs/user-stories/eighth-user-story-evidence-1.jpg">
<img src="docs/user-stories/eighth-user-story-evidence-2.jpg">
</details>

---


   9. As a site user, I can select a specific category of posts that are interesting to me


   **Action** | **Result** 
   -----------| ----------  
 While on any page of the site, go to the main page and click on the logo located in the right-left corner of the page. | Possible categories of posts are displayed on the right side of the page
 Click on the post category you are interested in  | Posts in this category will be displayed 

<details><summary>Screenshot evidences</summary>
<img src="docs/user-stories/ninth-user-story-evidence-1.jpg">
<img src="docs/user-stories/ninth-user-story-evidence-2.jpg">
<img src="docs/user-stories/ninth-user-story-evidence-3.jpg">
</details>

---


   10. As a registered user of the site I can create and update profile page


   **Action** | **Result** 
   -----------| ----------  
 As a user who does not have a profile, go to the profile creation page | You will be taken to the profile creation page
 Fill out the profile form and click on the create profile button  | Your profile will be created
 To update your profile, go to your profile page | Your profile will be shown
 While on the profile page, click on the update profile button  | The profile update page will open
 Fill out the profile update form and click on the update button | Your profile will be updated

<details><summary>Screenshot evidences</summary>
<img src="docs/user-stories/tenth-user-story-evidence-1.jpg">
<img src="docs/user-stories/tenth-user-story-evidence-2.jpg">
<img src="docs/user-stories/tenth-user-story-evidence-3.jpg">
<img src="docs/user-stories/tenth-user-story-evidence-4.jpg">
<img src="docs/user-stories/tenth-user-story-evidence-5.jpg">
</details>

---



   11. As a registered user of the site I can create and update profile page


   **Action** | **Result** 
   -----------| ----------  
 As a registered user with a profile, go to the profile page | If you have posts, they will be displayed under the profile information, if you do not have aposts yet, then a corresponding message will be displayed
 

<details><summary>Screenshot evidences</summary>
<img src="docs/user-stories/eleventh-user-story-evidence-1.jpg">
<img src="docs/user-stories/eleventh-user-story-evidence-2.jpg">
<img src="docs/user-stories/eleventh-user-story-evidence-3.jpg">
</details>

---



   12. As a site user, I can select a specific category of posts that are interesting to me


   **Action** | **Result** 
   -----------| ----------  
 While on any page of the site, go to the main page and click on the logo located in the right-left corner of the page. | On the right side of the site you will see quotes about food
 

<details><summary>Screenshot evidences</summary>
<img src="docs/user-stories/twelfth-user-story-evidence-1.jpg">
<img src="docs/user-stories/twelfth-user-story-evidence-2.jpg">
</details>

---


   13. As a user of the site, I would like to receive notifications about my actions


   **Action** | **Result** 
   -----------| ----------  
 You can perform any registration action | Based on the results, a corresponding notification will be displayed
 

<details><summary>Screenshot evidences</summary>
<img src="docs/user-stories/thirteenth-user-story-evidence-1.jpg">
</details>

---

### Site Owner Stories Testing


   1. As the owner of the site, I want only authorized users to have access to all the functionality of the site


   **Action** | **Result** 
   -----------| ----------  
 Register or log in to the site | As a registered user you will have access to the functions create a profile, contact administration, create a post, add a comment or rate a post
 

<details><summary>Screenshot evidences</summary>
<img src="docs/site-owner-stories/first-site-owner-story-evidence-1.jpg">
<img src="docs/site-owner-stories/first-site-owner-story-evidence-2.jpg">
</details>

---


   2. As the owner of the site, I want the registered user to be able to update and delete posts only if he is the author


   **Action** | **Result** 
   -----------| ----------  
 Register or log in to the site | You can delete or update a post but only if you are the author of the post
 

<details><summary>Screenshot evidences</summary>
<img src="docs/site-owner-stories/second-site-owner-story-evidence-1.jpg">
<img src="docs/site-owner-stories/second-site-owner-story-evidence-2.jpg">
</details>

---

   3. As a site owner, I want to be able to pre-approve user posts and comments to avoid publishing inappropriate content


   **Action** | **Result** 
   -----------| ----------  
 Create a post as a registered user | Your post will appear on the site only after approval by the administrator
 Create a comment as a registered user | Your comment will appear on the site only after approval by the administrator
 

<details><summary>Screenshot evidences</summary>
<img src="docs/site-owner-stories/third-site-owner-story-evidence-1.jpg">
<img src="docs/site-owner-stories/third-site-owner-story-evidence-2.jpg">
<img src="docs/site-owner-stories/third-site-owner-story-evidence-3.jpg">
<img src="docs/site-owner-stories/third-site-owner-story-evidence-4.jpg">
</details>

---

4. As the owner of the site, I want the post to contain a photo of the dish and a description of the cooking process


   **Action** | **Result** 
   -----------| ----------  
 As a registered user, go to the post creation page | The post creation form allows you to add a recipe picture and description
 Go to the user's post page. | The user's post will have a picture and description of the recipe. If the user does not select an image, the default image will be used
 

<details><summary>Screenshot evidences</summary>
<img src="docs/site-owner-stories/fourth-site-owner-story-evidence-1.jpg">
<img src="docs/site-owner-stories/fourth-site-owner-story-evidence-2.jpg">
<img src="docs/site-owner-stories/fourth-site-owner-story-evidence-3.jpg">
</details>

---



   5. As the owner of the site I can receive feedback from registered users


   **Action** | **Result** 
   -----------| ----------  
 Register or log in to the site | You get the opportunity to send a message
 

<details><summary>Screenshot evidences</summary>
<img src="docs/site-owner-stories/fifth-site-owner-story-evidence-1.jpg">
<img src="docs/site-owner-stories/fifth-site-owner-story-evidence-2.jpg">
</details>

---


   6. As the owner of the site, I can place links to the project’s social pages on every page of the site


   **Action** | **Result** 
   -----------| ----------  
 On any page of the site, scroll down to the footer | The site footer contains links to social networks.
 

<details><summary>Screenshot evidences</summary>
<img src="docs/site-owner-stories/sixth-site-owner-story-evidence-1.jpg">
</details>

---

### Device testing

The website was tested on the following devices:

   - Iphone 7;
   - Iphone 12 Pro;


In addition, the website was tested using Google Chrome Developer Tools Device Toggeling option for all available device options.

### Browser compatibility

The website was tested on the following browsers:

   - Google Chrome;
   - Yandex Browser;
   - Mozilla Firefox;


## Bugs

  - In the model CookingRecipePost lacked a method for creating slugs for new posts, which caused an error when adding posts to the site

   **Actions**: a method for creating slugs for new posts was added to the model (method save);


   **Result**: automatic slug began to appear for new posts in accordance with the title of the post;

   **Status**: bug fixed;


  - When updating posts, an old slug remained, which could lead to bugs

   **Actions**: in the CookingRecipePostUpdateView the form_valid method was changed with the addition of slug cleaning;


   **Result**: automatic slug began to appear for updated posts in accordance with the title of the post;

   **Status**: bug fixed;


  - In the profilefor form widget, the nickname field was specified twice, which led to a crash

   **Actions**: Removed extra nickname field.


   **Result**: the error stopped appearing;


   **Status**: bug fixed;


  - based on the educational project, a model named in the educational project was added without updating the name in accordance with the current project

   **Actions**: this model has been renamed, other models have been checked for correct naming


   **Result**: the error stopped appearing;


   **Status**: bug fixed;


  - Based on the tutorial project and the tutor's comments to the project volume in the settings. py was accidentally added as an application 'crispy_bootstrap4', which caused the main project to crash (ModuleNotFoundError: No module named 'crispy_bootstrap4')

   **Actions**: accidentally added as an application 'crispy_bootstrap4' was deleted


   **Result**: the error stopped appearing;


   **Status**: bug fixed;


  - There was no closing article tag in the post detail file, which led to a violation of semantics rules

   **Actions**: a closing article tag has been added to the file. 


   **Result**: violations of the rules of semantics ceased to exist


   **Status**: bug fixed;


  - when creating tests for views, the primary test was copied several times, which led to the presence of identical and inaccurate comments for a number of tests

   **Actions**: comments on the presentation have been clarified. 


   **Result**: the inaccuracy in the comments has been corrected


   **Status**: bug fixed;


  - supporting comments were not added to many functions, loops and conditional objections in various project files, which would make the code difficult to understand

   **Actions**: supporting comments have been added in the appropriate places. 


   **Result**: the code has become easier to understand 


   **Status**: bug fixed;

  - base.html metadata lacked description tags and keywords, which was incorrect from the point of view of semantic markup rules

   **Actions**: Description tags and keywords have been added to the file metadata.

   **Result**:  semantic markup errors fixed  


   **Status**: bug fixed;


  - all views, models, and forms files for both applications in the project had lines longer than 79 characters, causing code review to fail

   **Actions**: implemented views, models and forms of both project applications in places where there were lines longer than 79 characters. 

   **Result**:  All files have been validated


   **Status**: bug fixed;


  - there was no alt argument in the image tags in the page profile.html, which led to violations of markup rules

   **Actions**: added alt argument to image tags in the page profile file. 

   **Result**:  HTML markup rules are not violated


   **Status**: bug fixed;


  - there was no alt argument in the image tags in the page profile.html, which led to violations of markup rules

   **Actions**: added alt argument to image tags in the page profile file. 

   **Result**:  HTML markup rules are not violated


   **Status**: bug fixed;


  - the notification that your comment is being approved by the administrator did not disappear after a while

   **Actions**: Added afdi message to the markup that displays the notification, which is tracked by the javascript function 

   **Result**:  comment notifications began to disappear after the timing specified by the js function


   **Status**: bug fixed;


## Deployment 

We assume that the workspace will be located in [Gitpod](https://www.gitpod.io/), the database used will be [PostgreSQL](https://www.postgresql.org/), and the project will be deployed on the server [Heroku](https://heroku.com/)

We have previously created a repository on [GitHub](https://github.com/) and we will use [Cloudinary](https://cloudinary.com/)

### Workspace
1. Install django gunicorn - gunicorn is the server that we're going to use to run Django on Heroku. (pip3 install 'django<4' gunicorn - in Terminal)
2.  Install the supporting libraries:
    1. pip3 install dj_database_url==0.5.0 psycopg2 (for installing PostgreSQL DB)(in Terminal)
    2. pip3 install dj3-cloudinary-storage (for installing cloudinary)(in Terminal)
    3. Create requirements.txt file
    4. pip3 freeze --local > requirements.txt (in Terminal)
3. Create a Django project with command: django-admin startproject <projectname> . (in Terminal)
4. Create a Djsngo app with command: python3 manage.py startapp <blogname> (in Terminal)
5. Add neww app in project app in settings.py
6. Make migrations with command: python manage.py migrate (in Terminal)
7. create a file <env.py>
8. in <env.py> you need import os then:
    1. create variable os.environ["DATABASE_URL"]="<copiedURL>" (URL should be taken from step 11 PostgreSQL section(below))
    2. create variable os.environ["SECRET_KEY"]="<my_super^secret@key>" (you secret key be in the setting.py)
    3. create variable os.environ['CLOUDINARY_URL'] ="<API Environment Varaible>" (<API Environment Varaible> should be taken from step 3 Cloudinary section(below))
    (dont foget remove  "CLOUDINARY_URL =" from the beginning <API Environment Varaible>)
9. add <env.py> to .gitignore file to save confidential data
10. in <settings.py>:
    1. import os
    2. import dj_database_url
    3. Add check: if os.path.isfile('env.py'): import env (it is important to maintain indentation in accordance with Python requirements)
    4. Edit <SECRET_KEY> variable: SECRET_KEY = os.environ.get('SECRET_KEY')
    5. Comment default <DATABASE> varaible
    6. Add new <DATABASE> varaible: DATABASES = { 'default': dj_database_url.parse(os.environ.get("DATABASE_URL")) }
    7. use command "save"
11. Make migrations with command: python manage.py migrate (in Terminal)
12. in settings.py:
    1. Add "cloudinary_storage" and "cloudinary" in project app in settings.py
    2. STATIC_URL = '/static/'
    3. STATICFILES_STORAGE = 'cloudinary_storage.storage.StaticHashedCloudinaryStorage'
    4. STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
    5. STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
    6. MEDIA_URL = '/media/'
    7. DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'
    8. TEMPLATES_DIR = os.path.join(BASE_DIR, 'templates')
    9. in TEMPLATES set value "[TEMPLATES_DIR]" to key "DIRS"
    10. Add Heroku host  name into "ALLOWED_HOSTS" (your Heroku app  name followed by herokuapp.com.)
    11. X_FRAME_OPTIONS = 'SAMEORIGIN'
    12. DEBUG = False
13. Create Procfile(remember the capital P on Procfile) with web: gunicorn <projectname>.wsgi
14. Use commands: "save", "git add .", git commit -m "deploy commit", "git push"


### Heroku

1. Go to [Heroku](https://heroku.com/)
2. Create account or LogIn
3. Create new app (click on the button)
4. Choose a unique name for your app, select region 
5. click on Create App
6. Go back to the Heroku dashboard open the Settings tab
7. Click to "Reveal Config Vars" button
8. Add Config Vars:
   1. <DATABASE_URL> (value: <copiedURL> (URL should be taken from step 11 PostgreSQL))
   2. <SECRET_KEY> (value: <my_super^secret@key>" (you secret key be in the env.py or settings.py))
   3. <PORT> (value: 8000)
   4. <CLOUDINARY_URL> (value: <API Environment Varaible> should be taken from step 8.3 Workspace section(above))

   
### PostgreSQL

1. Go to the ElephantSQL website (https://www.elephantsql.com/) 
2. Create account or LogIn
3. Click "Create new instance" button
4. Edit plan Name 
5. Choose Plan project (the Tiny Turtle (Free) plan)
6. Edit Tags (optionally)
7. Select Region
8. click “Review” button
9. Check your details are correct and then click “Create instance” bitton.
10. Return to the ElephantSQL dashboard and click on the database instance name for this project
11. Find the connection details for your database and  click the copy icon to copy the <database URL>

### Cloudinary
1. [Cloudinary](https://cloudinary.com/)
2. LogIn or Create Account
3. Go to Dashbord and copy <API Environment Varaible>


### Last Deployment Steps 
**NOTE: start here after you have completed all the previous steps**

1. Open Heroku Dashboard
2. Go to Deploy tab
3. Select GitHub deployment method
4. Connect to you Github Account
5. Selecte project repository
6. Click Deploy Branch button
7. Click Open app button


### Cloning the repository
1. On GitHub.com, navigate to the main page of the repository.
2. click "Code" button.
3. Select HTTPS, SSH, or Github CLI.
4. Open Git Bash
5. Change the current working directory to the one where you want the cloned directory
6. Type git clone and paste the URL from the clipboard ($ git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY) 
7. Press Enter to create your local clone. 

steps created using description on [GitHub Docs](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository)

### Forking the GitHub Repository
1. Go to the GitHub repository
2. Click on Fork button

## Credits

### Content
The text content was provided by the site owner.

### Media
The images in the website are taken from [Unsplash](unsplash.com)

### Code

## Acknowledgements

I would like to express my sincere gratitude:

  - My mentor Mo Shami for his advice and support.
  - Tutor support team for help in solving technical problems and advice (especially Joanna)
  - My daughter Alisa and my wife Snizhana for always giving me inspiration and strength to go forward.
  - The government of the city of Hamburg and the employees of the job center Mitti for my opportunity to study at these courses.
  - To all people who are in solidarity and support Ukraine


