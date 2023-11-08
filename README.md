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

<details><summary>Add</summary>
<img src="add">
</details>

### Fonts

For plain text, the Mulish font is used, connected using google fonts. For headings, Young Serif font was used. Inter font used for other text. Used fonts are well combined with each other


### Structure

The site structure is designed to ensure maximum ease of use. Also, much attention is paid to the stylistic beauty of the site. All pages of the site have the same header with a navigation menu and a footer containing links to social networks

#### Home Page

- The main page consists of three sections: navigation menu, main section, right additional section and footer.

- The main section displays posts published by site users (main picture, short description of the recipe, date of creation, author and number of likes)

- Additional rights section contains a list of post categories, as well as a block with quotes about food.

#### Create Post Page

- The page consists of three sections: header, main section and footer. The footer and header sections are standard for the entire site.

- The main section of the page displays a form with various fields for updating the post.

#### Post Detail Page

- The page consists of three sections: header, main section and footer. The footer and header sections are standard for the entire site

- The main section displays the full text of the post with a cover image on the left and a description on the right. Below is a block with the date the post was created and the author. Below is a block with comments and a comment form for authorized users.

#### Update Post Detail Page

- The page consists of three sections: header, main section and footer. The footer and header sections are standard for the entire site.

- The main section of the page displays a form with various fields for updating the post.

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
