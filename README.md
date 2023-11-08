# Delicious recipes
(Developer: Bilan Mykhailo)

[Live webpage](add)

![Mockup image](add)

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
    6. [Models Used](#models-used)
      1. [User](#user)
      2. [CookingRecipePost](#cookingrecipepost)
      3. [Comment](#comment)
      4. [Category](#category)
      5. [Profile](#profile)
      6. [Contact](#contact)



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

- The main section of the page displays a form with various fields for creating post.

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

- The main section of the page is notification of leaving the site and buttons for confirmation and cancellation

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

### Agile 

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

<!-- #### Home Page




#### Delete Post Detail Page

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

- The main section of the page displays a form with various fields for creating post.

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

- The main section of the page is notification of leaving the site and buttons for confirmation and cancellation -->