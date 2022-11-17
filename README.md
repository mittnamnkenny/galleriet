# Galleriet - Buy original paintings online

This is my fifth and final project with Code Institute. Galleriet is a B2C (Business to Customer) e-commerce application which sells paintings online. This application has been created using the Django framework. It is targeted towards individual customers that are interested in art and want to purchase original paintings from the best emerging artists around the world.

This project is for educational purposes only!

[View the live project here.](https://galleriet-mittnamnkenny.herokuapp.com/)

![Mockup](documentation/amiresponsive.png)

## Index – Table of Contents
* [User Experience (UX)](#user-experience-ux)
  * [Project Goals:](#project-goals)
  * [Strategy:](#strategy)
  * [User stories:](#user-stories)
* [Features](#features)
  * [Existing Features](#existing-features)

## User Experience (UX)

### Project Goals:

The primary goal for this project is to create a fully functional and easy-to-use e-commerce store that allow users to browse a number of different products to add to their shopping bag, so that they can checkout securely using Stripe online payment processing system and complete a purchase.

**Stripe test card:**
  - test card number 4242 4242 4242 4242, 
  - a random three-digit CVC number, 
  - and any expiration date in the future.

Please note: The website is for educational purposes only and uses Stripe test mode to simulate payments.

A user should be able to register to the site and store their personal information, such as default delivery information and view their past order history. They should also be presented with the option to contact store admin, subscribe to a newsletter provided by Mailchimp, and visit Galleriet's Facebook business page so that they can stay up to date with all the latest news.

Site administrator should have full CRUD functionality over available products directly from the site, so that they can Create, Read, Update and Delete products without any delays, and that any changes made on the site are directly reflected to the user.

A full description of all available functionality is included in this file.

### Strategy:

An Agile methodology was used to plan this project. This was implemented using a Kanban board in GitHub Project with linked Issues. To cover the goals of this project, a total of 6 Epics where created, which were then further developed into 26 User Stories, each with their own acceptance criterias and tasks to complete. Labels where then used to prioritize the importance of each User Story.

The following labels were used in this project and the distribution of user stories by label are:

  - Must-Have: 14/26
  - Should-Have: 9/26
  - Could-Have: 3/26

For more information: [View the Kanban Board here.](https://github.com/users/mittnamnkenny/projects/2/views/1)

### User stories:

  - #### EPIC Admin and Store management
    - US1. Add products:
      - As a **Site Admin** I can **add products directly from the site** so that **I can add new items to my store**
    - US2. Update products:
      - As a **Site Admin** I can **update products directly from the site** so that **I can change product prices, descriptions, images, and other product criteria**
    - US3. Delete products:
      - As a **Site Admin** I can **delete products directly from the site** so that **I remove items that are no longer for sale**
  
  - #### Registration and User accounts
    - US4. Account registration:
      - As a **Site User** I can **register an account** so that **I can have a personal account and be able to view my profile**
    - US5. Login/Logout:
      - As a **Site User** I can **login or logout** so that **I can access my personal account information**
    - US6. Password reset:
      - As a **Site User** I can **easily reset my password in case I forget it** so that **I can recover access to my account**
    - US7. Personalized profile:
      - As a **Site User** I can **have a personalized profile** so that **I can view my personal order history and order confirmations, and save my payment information**

  - #### Navigation and Interaction
    - US8. View products:
      - As a **Site Shopper** I can **view a list of products** so that **I can select some to purchase**
    - US9. Product detail:
      - As a **Site Shopper** I can **view individual product details** so that **I can identify the price, description, product image etc**
    - US10. View total:
      - As a **Site Shopper** I can **easily view the total of my purchase at any time** so that **I can avoid spending too much**
    - US11. Sort list:
      - As a **Site Shopper** I can **sort the list of available products** so that **I can easily identify the best priced and categorically sorted products**
    - US12. Search product:
      - As a **Site Shopper** I can **search for a product** so that **I can find a specific product I’d like to purchase**
    - US13. System messages:
      - As a **Site User** I will **get system messages when I interact with the site** so that **I get feedback when certain actions are completed**

  - #### Purchasing and Checkout
    - US14. Product purchase:
      - As a **Site Shopper** I can **easily select a product to purchase** so that **I can continue browsing the site and viewing more products**
    - US15. Shopping bag:
      - As a **Site Shopper** I can **view items in my bag to be purchased** so that **I can identify the total cost of my purchase and all items I will receive**
    - US16. Payment:
      - As a **Site Shopper** I can **easily enter my payment information** so that **I can check out quickly with no hassles, and feel that my personal and payment information is safe and secure**
    - US17. Order confirmation:
      - As a **Site Shopper** I can **view an order confirmation after checkout** so that **I can verify that my purchase was successful and I haven’t made any mistakes**

  - #### Contact, Web Marketing and SEO
    - US18. Contact page:
      - As a **Site User** I can **contact site admin** so that **I can get my questions answered or provide feedback**
    - US19. Newsletter:
      - As a **Site User** I can **subscribe to a newsletter** so that **I can get email informing me about new products and any changes made to the site**
    - US20. Facebook page:
      - As a **Site User** I can **access the store’s Facebook business page** so that **I can view posts and updates made on Facebook and interact**
    - US21. SEO:
      - As a **Site User** I can **easily find the site using popular search engines** so that **I can take advantage of what the site has to offer**

  - #### UX, UI, ETC
    - US22. Responsive:
      - As a **Site User** I can **use the site on the following platforms: desktop, laptop, tablet and smartphone** so that **I can access all functionality**
    - US23. Design:
      - As a **Site User** I can **get an overall positive impression based on the principles of user experience design, accessibility and responsivity** so that **I can quickly determine the purpose of the site and enjoy using it**
    - US24. Favicon:
      - As a **Site User** I am **presented with a favicon** so that **I can get a better experience when browsing with multiple tabs**
    - US25. GitHub:
      - As a **Site User** I am **presented with a link to mittnamnkenny’s GitHub** so that **I can view more repositories**
    - US26. 404 page:
      - As a **Site User** I am **presented with a custom 404 page when trying to access a URL that does not exist** so that **I can get an proper error page and easily return to the home page**

## Features

### Existing Features

#### Header:

The header is present on all pages of the site. It uses bootstrap's built-in class fixed-top, so when the user scrolls, it will remain fixed to the top of the browser's viewport and always visible to the user.

On the left-hand side of the header the user is presented with the logo; Galleriet with a styled Font Awesome icon (fa-solid fa-g), which when clicked will redirect the user to the home page. On mobile devices, the logo is centered.

![Header](documentation/features-header.png)

The main navigation is featured in the header with the following links to: Home, Products, Categories, and Contact. Using request path and highlighting the current page in bold text.

My account and the Shopping bag is always visible to the user. The shopping bag will display the number of products added and the total price, automatically updating when new products added. Depending on your login status, the following links can be accessed using a drop-down menu under My account:

  - Not logged in: Register, Login
  - Logged in: My Profile, Logout and (if superuser) Product management

![Header Account](documentation/features-headeraccount.png)

The header also features a search bar that allows the user to search for products and a delivery banner displaying the free delivery message. 

The header is fully responsive, so when on smaller devices the header will collapse and the main navigation links are accessed using a ”hamburger menu”.

<details>
<summary>View collapsed navbar:</summary>

![Header Collapse](documentation/features-headercollapse.png)
</details>

#### Home page:

##### Home page - Callout:

Positioned at the top of the home page, this is first presented to the user as they visit the site. It includes a background image featuring an abstract painting photo.

![Callout](documentation/features-callout.png)

A large text overlay; Buy original paintings online Galleriet, Sweden with an included link that will redirect the user to the products page.

On smaller screen sizes a dark background colour is positioned above the image so the text will stand out more and be easier to read. The text is also centered.

![Callout Small](documentation/features-calloutsmall.png)

When the user visits the site for the first time, they will clearly see that this site is selling paintings.

##### Home page - Latest products:

Positioned below the callout, the user can view the most recent products available for purchase. This is featured on the home page so that the user can quickly see any product updates.

The user can view the latest products with information including: Product image, name, price, category, and artist.

![Latest Products](documentation/features-latestproducts.png)

By clicking on the product image, the user is redirected to the product detail page. The user can also click on the artist name or category to find matching products.

#### Products page:

The Products page will present a paginated list of all products on the site, limited to a maximum of eight products per page. The Products page can easily be accessed using the provided link on the Home page or in the main navigation; Products and Categories, alternatively by searching for a product name or description using the search bar.

The user will be able to view the number of products and sort products by price, name or category using the included drop-down field; Sort by.

![Products](documentation/features-products.png)

Category buttons will be presented at the top of the page when the user chooses Categories in the main navigation. This will allow the user to easily switch between certain categories.

![Products Small](documentation/features-productssmall.png)

For each product the following information is presented to the user: Product image, name, price, category, and artist.

By clicking on the product image, the user is redirected to the product detail page. The user can also click on the artist name or category to find matching products.

#### Product detail page:

When a user chooses to click on a product, they are brought to the Product detail page. The user is shown the entirety of the product. The following information will be presented to the user: Product image, name, price, category, artist, description, medium, height and, width.

![Product Details](documentation/features-productdetails.png)

The user will be able to add the product to the shopping bag or return to the Products page using the clearly labeled buttons. The user can also click on the artist name or category to find matching products.


#### Shopping bag:

A user can easily access the Shopping bag by clicking on the shopping bag icon in the header section or when adding a new product using the; Go to secure checkout button in the success message displayed to the user.

On the Shopping bag page the user is presented with a summary of all products added for purchase and the grand total price. As new products are added to the shopping bag, the grand total is automatically updated, taking into consideration any delivery costs.

![Shoppingbag](documentation/features-shoppingbag.png)

The user will be able to remove unwanted products from their shopping bag by clicking on Remove, before proceeding to the checkout page.

From this page the user can also choose to return to the Products page by clicking on the Keep shopping button.

<details>
<summary>Shopping bag on mobile devices:</summary>

![Shoppingbag Small](documentation/features-shoppingbagsmall.png)
</details>

#### Checkout page:

When a user clicks on Secure checkout on the Shopping bag page, the user is redirected to the Checkout page; this is the last step before completing a purchase. On the Checkout page the user is presented with an Order Summary and the user is required to enter their details, delivery information and payment credit card number. 

The option to Save this delivery information to my profile is presented to logged-in users; this allows the delivery form fields to be pre-populated on future purchases, which results in a faster checkout process.

From this page the user can also choose to return to the Shopping bag page by clicking on the Adjust bag button.

![Checkout](documentation/features-checkout.png)

<details>
<summary>Checkout page on mobile devices:</summary>

![Checkout Small](documentation/features-checkoutsmall.png)
</details>

All payments are handled by Stripe online payment processing system, and webhooks are implemented to ensure that all transactions are handled correctly in case of any problems during the payment process.

**Stripe test card:**
  - test card number 4242 4242 4242 4242, 
  - a random three-digit CVC number, 
  - and any expiration date in the future.

Please note: The website is for educational purposes only and uses Stripe test mode to simulate payments.

Stripe events example:

![Stripe Events](documentation/features-stripe.png)

Stripe webhooks example:

![Stripe Webhooks](documentation/features-stripewh.png)

#### Checkout success page:

The user is redirected to the Checkout success page when a purchase is completed, here the user is presented with a confirmation message and order information.

![Checkout Success](documentation/features-checkoutsuccess.png)

The user will receive an order confirmation email.

temp-mail.org was used when completing this purchase:

![Checkout Mail](documentation/features-checkoutsuccessmail.png)

#### Profile page:

A user can easily access the Profile page from the header section using the drop-down menu under my account name. It is required that the user is registered and logged in.

The Profile page contains the users Default Delivery Information. A user can easily update their details by changing the pre-populated form fields and clicking on the Update Information button.

Order history is also presented to the user, here the user can view all their past orders and will be able to click on order number and check individual orders for full order information.

![Profile](documentation/features-profile.png)

<details>
<summary>Profile page on mobile devices:</summary>

![Profile Small](documentation/features-profilesmall.png)
</details>

#### Register / Sign up page:

Unregistered users will be able to access the Register page by navigating to the header section and using the drop-down menu under My account. A new account can easily be created on the register page; the user needs to provide the following information: email, username and password.

![Register](documentation/features-register.png)

The user is required to verify their email address after clicking on the Sign up button; an email will be automatically sent to the users email address.

![Register Verify](documentation/features-registerverify.png)

temp-mail.org was used when registering this user:

![Register Mail](documentation/features-registermail.png)

Confirm Email address:

![Register Confirm](documentation/features-registerconfirm.png)

#### Login / Sign in page:

When a user has completed the registration process, they can easily login to the site using the Sign in page. The Sign in page can be accessed in the header section using the drop-down menu under My account. To login the user is required to enter their username or email and the correct password.

![Login](documentation/features-login.png)

A user can also reset their password in case they forget it, using the link Forgot Password?

![Login Reset](documentation/features-loginreset.png)

After clicking on Reset my password:

![Login Resetmail](documentation/features-loginresetmail.png)

temp-mail.org was used when resetting the password for this user:

![Login Mail](documentation/features-loginmail.png)

Enter new password:

![Login Change](documentation/features-loginchange.png)

Password change confirmation:

![Login Changed](documentation/features-loginchanged.png)

#### Logout / Sign out page:

The Sign out page can be accessed in the header section using the drop-down menu under My account name.

The user will have to confirm before singing out. When the user clicks on Sign out, they are directly logged out of their account and redirected to the Home page. If the user chooses to click the Cancel button instead, the user will be redirected to the Home page.

![Logout](documentation/features-logout.png)

#### Contact page:

The Contact page allows a user to send a message to a site administrator directly from the site using the contact form. The user is required to enter their name, email and message. The user is also able to choose a subject; Customer service (default) or Technical assistance.

The Contact page can be accessed using the provided link in the main navigation header or at the bottom of the page in the footer section. 

![Contact](documentation/features-contact.png)

#### Django Admin page:

To manage the site, a superuser account was created. The Admin page can be accessed by logging in to the /admin URL with the superuser account. From the admin panel, the superuser will have full control, and be able to manage all products on the site, view any new contact inquiries, etc.

![Admin](documentation/features-admin.png)

#### Product management:

For full CRUD functionality, the superuser can Create, Update, and Delete products directly from the site to manage products available for purchase. Any changes made on the site will be directly reflected to the user without having to use the Django admin panel.

##### Add product:

The Product management / Add product page can be accessed in the header section using the drop-down menu under My account name. The superuser will be able to add a new product to the site by filling in the Add a product form. If no image is selected here, a placeholder image will be displayed instead.

![Management Add](documentation/features-managementadd.png)

##### Edit product:

If the superuser wants to edit a specific product the Edit product page can be accessed using the Edit button on the Products or Product detail page. On the Edit a product page, the superuser will be able to update all product information including the image.

Products (superuser):

![Management](documentation/features-management.png)

Product detail (superuser):

![Management Detail](documentation/features-managementdetail.png)

Edit product:

![Management Edit](documentation/features-managementedit.png)

##### Delete product:

The Delete button is also displayed on the Products and Product detail page for each product.
If the superuser wants to delete a specific product they will have to confirm the deletion before the product is removed; a pop-up modal is displayed to the superuser with the option to Delete or Close.

Delete product modal:

![Management Delete](documentation/features-managementdelete.png)

#### System Messages:

System / Flash messages are present throughout the site and will be displayed to the user as feedback. The message will appear at the top right of the screen when certain actions are completed and can easily be removed by manually clicking on the close x button.

System message when product added to bag:

![Message Add](documentation/features-messageadd.png)

Alert message:

![Message Alert](documentation/features-messagealert.png)

#### Featurette:

Positioned above the footer, the user is presented with three styled Font Awesome icons with text included; this will help the user to identify the purpose of the site and some of it’s features. The featurette is available on all pages of the site; on smaller devices the number of icons is reduced to two.

![Featurette](documentation/features-featurette.png)

#### Footer:

The Footer is present on all pages of the site, featured at the absolute bottom. The footer contains links to Galleriet’s Facebook page, mittnamnkenny’s GitHub page, the Contact page, and the Privacy policy page. All External links open in a new tab.

An embedded Mailchimp newsletter form is also available in the footer. This will encourage users to subscribe to Galleriet’s newsletter.

![Footer](documentation/features-footer.png)

<details>
<summary>Footer on mobile devices:</summary>

![Footer Small](documentation/features-footersmall.png)
</details>

#### Web marketing:

##### Newsletter:

A user will be able to subscribe to Galleriet’s newsletter. The user is required to enter their email address and click on the Subscribe button to sign up. This will automatically add their email address to Galleriet’s subscription list. Newsletters can be sent out when new products are added to the store, as a part of the web marketing strategy for this project.

This service is handled by MailChimp.

[Mailchimp Website.](https://mailchimp.com/)

MailChimp Audience:

![Mailchimp](documentation/features-mailchimp.png)

##### Facebook business page:

A Facebook business page was created for the purpose of web marketing. The footer contains a link to Galleriet’s Facebook page; Visit our Facebook page; this link will open in a new tab.

[Galleriet’s Facebook page.](https://www.facebook.com/people/Galleriet/100086925295277/)

Screenshot Galleriet’s Facebook page:

![Facebook](documentation/features-facebook.png)

#### Privacy Policy:

A Privacy policy page was created and can be accessed by the link in the footer. The Privacy policy will show the user that this site is trustworthy and that Galleriet takes privacy seriously.

The privacy policy was created using:

[Privacy Policy Generator.](https://www.privacypolicygenerator.info/)

![Privacy](documentation/features-privacy.png)

#### SEO:

To increase brand reach and make the site search-engine friendly, the following Search Engine Optimization (SEO) techniques were used:

##### Keyword research:

Keywords and phrases were identified using the site [Wordtracker](https://www.wordtracker.com/). I have also used the auto-complete feature of Google to get keyword ideas for my project.

A list of relevant keywords for my project: gallery, paintings, paintings online, artists, art, unique art, original paintings, art store.

I have used the following Keywords:

  - Home Callout h1: Buy original <strong>paintings</strong> online
  - Featurette h3: Quality paintings
  - Featurette p: From the best emerging artists around the world
  - Footer p: Keep up to date with all our latest paintings
  - Title tag: Galleriet - Buy original paintings online
  - Meta description: Galleriet, Buy original paintings online
  - Meta keywords: galleriet, gallery, paintings, paintings online, artists, art, unique art, original paintings, art store

Images on the site have descriptive alternative text 

A sitemap.xml file was created to allow search engine bot crawling

A robots.txt file was created to control search engine bot crawling

#### Additional features:

Favicon.

![Favicon](documentation/features-favicon.png)

Most links and buttons will change colour when hovered over.

![Buttons](documentation/features-buttons.png)

404 response page.

![Error](documentation/features-error.png)

### Features that could be implemented in the future:

#### Product inventory:

This website is for educational purposes only, and currently a user will be able to purchase the same painting multiple times without it being removed from the list of available products.
This will guarantee that products are always available for test purchase to the user.

To solve this the following could be done in the future:

In the products app:
Update the product model and add a new field named available (IntegerField), that defaults to 1.
Update the all_products view to filter Product by available=1 instead of all.

In the checkout app:
Update the checkout view to first check if product is still available for purchase and when order form is valid, set product available to 0 and save.

## Design

### Wireframes

At the beginning of this project and as a part of the planning phase wireframes were created using [Balsamiq](https://balsamiq.com/). The wireframes were used to get a basic idea on how the site might look when finished, both on desktop and mobile devices.

Wireframes were created for the following pages and features:

#### Home page:

![Wireframes Home](documentation/wireframes-home.png)

#### Products page:

![Wireframes Products](documentation/wireframes-products.png)

#### Product detail page:

![Wireframes Detail](documentation/wireframes-productdetail.png)

#### Shopping bag:

![Wireframes Bag](documentation/wireframes-shoppingbag.png)

#### Checkout page:

![Wireframes Checkout](documentation/wireframes-checkout.png)

#### Profile page:

![Wireframes Profile](documentation/wireframes-profile.png)

#### Contact page:

![Wireframes Contact](documentation/wireframes-contact.png)

#### Mobile devices:

![Wireframes Mobile](documentation/wireframes-mobile.png)

### Data Model

This project is hosted on [Heroku](https://www.heroku.com/) and the database used is Heroku PostgreSQL. 
[Amazon Web Services (AWS)](https://aws.amazon.com) is used to store all static files and images. 
This project is based on Code Institute's walkthrough project Boutique Ado, Building an E-Commerce Platform. 

Four custom models were created for this project; Product, Artist, Contact and OrderLineItem.

Entity Relationship Diagram - Product:

![ERD Product](documentation/erd-product.png)

Entity Relationship Diagram - Artist:

![ERD Artist](documentation/erd-artist.png)

Entity Relationship Diagram - Contact:

![ERD Contact](documentation/erd-contact.png)

Entity Relationship Diagram - OrderLineItem:

![ERD OrderLineItem](documentation/erd-orderlineitem.png)

### Site map

To explain the structure of the site and how to navigate it, I created a site map using [Lucidchart](https://www.lucidchart.com/pages/):

![Site Map](documentation/site-map.png)

### Colours

To match the background image featuring an abstract painting photo, red was chosen as the main colour to use throughout the site. The idea is to create a minimalist look and with a different colour scheme compared to my previous projects with Code Institute. [Google Materialize](https://materializecss.com/color.html) color palette was used to select the hex colour codes.

With a focus on accessibility and contrast, the following main colours were chosen:

![Design Palette](documentation/design-palette.png)

### Typography

I have used font-family "Helvetica Neue", Helvetica, Arial, sans-serif for all of the text throughout the site. This is Bootstrap's default font, and this was chosen because it both looks good and is easy to read.

To make text catch the users attention and improve SEO, strong tags were used in the callout header.

### Imagery

Background image used in this project:

  - [Unsplash:](https://unsplash.com/photos/0YZekL_Kp2E) Abstract painting photo, Steve Johnson

Photoshop was used to adjust the brightness and add a gradient overlay, this will make the callout text stand out and more visible to the user.

All product images used in this project are real paintings created by mittnamnkenny’s family and friend. mittnamnkenny have full permission to use their paintings in this project.

  - [Tomas K:](https://galleri.black/flyfishing/) Tomas K Galleri

## Technologies Used

### Languages Used:

  - HTML5
  - CSS3
  - JavaScript
  - Python

### Python packages Used:

    asgiref==3.5.2
    boto3==1.24.96
    botocore==1.27.96
    dj-database-url==0.5.0
    Django==3.2
    django-allauth==0.41.0
    django-countries==7.2.1
    django-crispy-forms==1.14.0
    django-storages==1.9.1
    gunicorn==20.0.4
    jmespath==1.0.1
    oauthlib==3.2.1
    Pillow==9.2.0
    psycopg2-binary==2.8.6
    python3-openid==3.2.0
    pytz==2022.2.1
    requests-oauthlib==1.3.1
    s3transfer==0.6.0
    sqlparse==0.4.3
    stripe==4.2.0

### Frameworks, Libraries and Software Used:

  - [Am I Responsive:](http://ami.responsivedesign.is) Checking the responsive.
  - [Amazon Web Services (AWS)](https://aws.amazon.com) Used to store all static files and images.
  - [Balsamiq:](https://balsamiq.com/) Used to create the wireframes.  
  - [Bootstrap:](https://getbootstrap.com/) Bootstrap CSS Framework used for styling and to build responsive web pages.
  - [Chrome DevTools:](https://developer.chrome.com/docs/devtools/) Used to test the response on different screen sizes, debugging and to generate a Lighthouse report to analyze page load.  
  - [Django:](https://www.djangoproject.com/) Main Python framework used in the development.
  - [Font Awesome:](https://fontawesome.com/) Used throughout the site to add icons for aesthetic and UX purposes.
  - [Git:](https://git-scm.com/) Git was used for version control by utilizing the Gitpod terminal to commit to Git and Push to GitHub.
  - [GitHub:](https://github.com/) GitHub is used to store the projects code after being pushed from Git and to create the Kanban board used for this project.
  - [Gmail:](https://www.google.com/intl/sv/gmail/about/) Galleriet's main mail account.
  - [Heroku:](https://www.heroku.com/) For deployment and hosting of the application.
  - [Heroku PostgreSQL:](https://www.heroku.com/postgres) The database used for this application.
  - [HTML Validator:](https://validator.w3.org/) Check your code for HTML validation.
  - [JSHint:](https://jshint.com/) Check code for JavaScript validation.
  - [jQuery:](https://jquery.com/) JavaScript library.  
  - [Lucidchart:](https://www.lucidchart.com/pages/) Used to create the site map.
  - [Mailchimp:](https://mailchimp.com/) Newsletter service.
  - [Materialize Colors:](https://materializecss.com/color.html) Used to create the main colour palette.
  - [Photoshop:](https://www.adobe.com/se/products/photoshop.html) Used to customize the callout image, adjust brightness and add gradient overlay.
  - [Stripe:](https://stripe.com/se) Online payment processing system.
  - [Temp Mail:](https://temp-mail.org/en/) Used for account registration, newsletter sign up and test purchases.
  - [Tiny PNG:](https://tinypng.com/) Compressing images to smaller sizes.
  - [Unsplash:](https://unsplash.com/photos/0YZekL_Kp2E) Abstract painting photo, Steve Johnson
  - [W3 CSS Validator:](https://jigsaw.w3.org/css-validator/) Check your code for CSS validation.
  - [Writer:](https://writer.com/grammar-checker/) Free Grammar Check.

## Testing

### Browser Testing

I have tested that this application works using Macbook Air (Retina, 13-inch, 2018), with macOS Ventura 13.0.1 installed, using the following browsers:

  - Safari Version 16.1
  - Google Chrome Version 107.0.5304.110 
  - Firefox Browser 106.0.5

I have tested this application works on the following iOS devices using Safari Version 16.1 browser:

  - iPhone X, with iOS 16.1.1 installed
  - iPad Air 3, with iPadOS 16.1.1 installed

### Responsiveness

Chrome developer tool have been used to check the responsiveness.

  - I have tested that this application works on different screen sizes from iPhone 5 (320px wide) and very large screens like 5K iMac Pro (5120 x 2880 px).

### Validator Testing

The W3C Markup Validator were used to validate the HTML on all pages of the project to ensure there were no syntax errors in there. To validate the HTML files all Django template tags were manually removed with the HTML code copied and inserted to the base template.

Index page:

![HTML Index](documentation/testing/htmlchecker-index.png)

Products page:

![HTML Products](documentation/testing/htmlchecker-products.png)

Product detail page:

![HTML Detail](documentation/testing/htmlchecker-productdetail.png)

Shopping bag:

![HTML Bag](documentation/testing/htmlchecker-bag.png)

Checkout page:

![HTML Checkout](documentation/testing/htmlchecker-checkout.png)

Checkout success page:

![HTML Success](documentation/testing/htmlchecker-checkoutsuccess.png)

Profile page:

![HTML Profile](documentation/testing/htmlchecker-profile.png)

Register / Sign up page:

![HTML Register](documentation/testing/htmlchecker-signup.png)

Login / Sign in page:

![HTML Login](documentation/testing/htmlchecker-login.png)

Logout / Sign out page:

![HTML Logout](documentation/testing/htmlchecker-logout.png)

Contact page:

![HTML Contact](documentation/testing/htmlchecker-contact.png)

Add product page:

![HTML Add](documentation/testing/htmlchecker-addproduct.png)

Edit product page:

![HTML Edit](documentation/testing/htmlchecker-editproduct.png)

Privacy policy page:

![HTML Privacy](documentation/testing/htmlchecker-privacypolicy.png)

404 page:

![HTML 404](documentation/testing/htmlchecker-404.png)

#### W3C CSS Validator:

The W3C CSS Validator Services were used to validate the CSS to ensure there were no errors in there.

![W3C CSS](documentation/testing/w3ccssvalidator.png)

#### JSHint:

JSHint was used to validate the JavaScript with no errors highlighted.

Bag JS:

![JSHint Bag](documentation/testing/jshint-bag.png)

Countryfield JS:

![JSHint Countryfield](documentation/testing/jshint-countryfield.png)

Product JS:

![JSHint product](documentation/testing/jshint-product.png)

Stripeelements JS:

![JSHint stripeelements](documentation/testing/jshint-stripeelements.png)

#### Python Validation:

To validate Python files the following command was used: python3 -m flake8.
Flake8 will inspects code for errors, including failing to comply with PEP8 standards. No serious errors listed on all files tested:

![Flake8](documentation/testing/flake8.png)

#### Lighthouse:

I have confirmed that the colours and fonts chosen are easy to read and accessible by running it through lighthouse in Chrome developer tools on the following pages:

Home page:

![Lighthouse Home](documentation/testing/lighthouse-home.png)

Products page:

![Lighthouse Products](documentation/testing/lighthouse-products.png)

Product detail page:

![Lighthouse Detail](documentation/testing/lighthouse-productdetail.png)

Shopping bag:

![Lighthouse Bag](documentation/testing/lighthouse-bag.png)

Checkout page:

![Lighthouse Checkout](documentation/testing/lighthouse-checkout.png)

Checkout success page:

![Lighthouse Success](documentation/testing/lighthouse-checkoutsuccess.png)

Profile page:

![Lighthouse Profile](documentation/testing/lighthouse-profile.png)

Register / Sign up page:

![Lighthouse Register](documentation/testing/lighthouse-signup.png)

Login / Sign in page:

![Lighthouse Login](documentation/testing/lighthouse-login.png)

Logout / Sign out page:

![Lighthouse Logout](documentation/testing/lighthouse-logout.png)

Contact page:

![Lighthouse Contact](documentation/testing/lighthouse-contact.png)

Add product page:

![Lighthouse Add](documentation/testing/lighthouse-addproduct.png)

Edit product page:

![Lighthouse Edit](documentation/testing/lighthouse-editproduct.png)

Privacy policy page:

![Lighthouse Privacy](documentation/testing/lighthouse-privacypolicy.png)

### User Stories testing

To further ensure this application is working correctly and functions as expected, manual testing was performed. User Stories were tested successfully to verify that all acceptance criteria was met. 


  - US1. Add products:
    - As a **Site Admin** I can **add products directly from the site** so that **I can add new items to my store**

    - Acceptance Criteria:
      - Site admin can add products directly from the site
      - Site admin can upload a product image

    - I have tested:
      - Adding products directly from the site using the superuser account.
      - That the add product page is restricted to superuser only. With the following response: Sorry, only store owners can do that.
      - That a superuser can select a product image to upload and if none is provided a placeholder image is displayed instead.


  - US2. Update products:
    - As a **Site Admin** I can **update products directly from the site** so that **I can change product prices, descriptions, images, and other product criteria**

    - Acceptance Criteria:
      - Site admin can update products directly from the site
      - Site admin can upload and update a product image

    - I have tested:
      - That the Edit link on the products and product detail page will redirect the superuser to the edit a product page.
      - That the correct product information is displayed and that all fields are loaded pre-populated on the edit a product page
      - Updating a product and image on the edit a product page works as expected.
      - That the edit a product page and links to access it, is restricted to superuser only.

  - US3. Delete products:
    - As a **Site Admin** I can **delete products directly from the site** so that **I remove items that are no longer for sale**

    - Acceptance Criteria:
      - Site admin can delete products directly from the site
      - Site admin should have to confirm before deleting a product
    
    - I have tested:
      - That the delete link on the products and product detail page will display the delete modal with correct product information to the superuser.
      - That the delete button in the modal and that deleting a product works as expected.
      - That the delete a product modal and links to access it, is restricted to superuser only.

  - US4. Account registration:
    - As a **Site User** I can **register an account** so that **I can have a personal account and be able to view my profile**

    - Acceptance Criteria:
      - To register a user must enter username, email and password
      - User should not be able to register the same username more than once
    
    - I have tested:
      - That username, email and password is required.
      - That registering with an already created username will generate the following response: A user with that username already exists. I will not be able to register the same username more than once.

  - US5. Login/Logout:
    - As a **Site User** I can **login or logout** so that **I can access my personal account information**

    - Acceptance Criteria:
      - To login a user must enter correct username (or email) and password
      - User should have to confirm before logging out of their account

    - I have tested:
      - That a user can login with their username of email, and that correct password is required.
      - That the user is presented with a sign out page with the following text: Are you sure you want to sign out?
      - That a user can sign out with the included sign out link.

  - US6. Password reset:
    - As a **Site User** I can **easily reset my password in case I forget it** so that **I can recover access to my account**

    - Acceptance Criteria:
      - A Forgot password link should be available on the login page
      - User should have to enter their registered email address
      - User should receive an password reset email

    - I have tested:
      - That a user is required to enter a correct email adress assigned to any user account.
      - That a user will ba able to reset their password using the forgot password link on the sign in page. Temp mail was used to test the reset password feature.

  - US7. Personalized profile:
    - As a **Site User** I can **have a personalized profile** so that **I can view my personal order history and order confirmations, and save my payment information**

    - Acceptance Criteria:
      - My Profile link is easily accessible to the user
      - User should be able to update and save their default delivery information
      - User should be able to view their order history

    - I have tested:
      - That signed in users are presented with the my profile link in the header section under my account name and that the link works as expected.
      - That the default delivery information form will display the correct information to the user and that all form fields are loaded pre-populated if previously saved.
      - That a user can update their default delivery information using the update information link.
      - That order history is displayed to the user and that the user can click on order number for full order information.

  - US8. View products:
    - As a **Site Shopper** I can **view a list of products** so that **I can select some to purchase**

    - Acceptance Criteria:
      - User is presented with a list of products for sale
      - Correct image and information for each product

    - I have tested:
      - That all products are presented on the products page and if the number of total products exceeds eight, a paginated view is presented to the user.
      - That the correct information is presented to the user for each product.
      - That the Next and Prev links work as expected.

  - US9. Product detail:
    - As a **Site Shopper** I can **view individual product details** so that **I can identify the price, description, product image etc**

    - Acceptance Criteria:
      - User should be able to click on a product for full information
      - Correct image and information is presented to the user

    - I have tested:
      - That all products on the products and home page can be clicked and opened for full detail view.  
      - That the correct information is presented to the user.

  - US10. View total:
    - As a **Site Shopper** I can **easily view the total of my purchase at any time** so that **I can avoid spending too much**

    - Acceptance Criteria:
      - Grand Total is always visible to the user
      - Grand Total is automatically updated when adding new products to the bag

    - I have tested:
      - That the shopping bag is always visable to the user in the header section, and that adding new products will automatically update the grand total.

  - US11. Sort list:
    - As a **Site Shopper** I can **sort the list of available products** so that **I can easily identify the best priced and categorically sorted products**

    - Acceptance Criteria:
      - User should be able to sort by price
      - User should be able to sort by category
      - User should be able to sort by name

    - I have tested:
      - That a user can sort products by price, name or category on the products page using the included drop-down field; Sort by.

  - US12. Search product:
    - As a **Site Shopper** I can **search for a product** so that **I can find a specific product I’d like to purchase**

    - Acceptance Criteria:
      - The search field is easily accessible to the user
      - User can search for products by name and description
      - User can easily see what they’ve searched for and the number of results

    - I have tested:
      - That searching for products by name or description works as expected and that the user will be presented with the total number of results found on the products page.
      - Searching for an empty string of text will result in the following message to the user: You didn't enter any search criteria.

  - US13. System messages:
    - As a **Site User** I will **get system messages when I interact with the site** so that **I get feedback when certain actions are completed**

    - Acceptance Criteria:
      - User should get feedback through pop-up messages with relevant information
      - The pop-up message should include a close button

    - I have tested:
      - That system / flash messages will appear correctly when performing certain actions on the site.
      - That the system / flash message can be removed manually by clicking on the close x button.

  - US14. Product purchase:
    - As a **Site Shopper** I can **easily select a product to purchase** so that **I can continue browsing the site and viewing more products**

    - Acceptance Criteria:
      - User should be able to add a product to the shopping bag on the product details page
      - Adding a product will automatically update the shopping bag and grand total

    - I have tested:
      - That the user is presented with the add to bag option on the product detail page, and by clicking on add to bag the product is automatically added to the shopping bag and the grand total is updated.
    
  - US15. Shopping bag:
    - As a **Site Shopper** I can **view items in my bag to be purchased** so that **I can identify the total cost of my purchase and all items I will receive**

    - Acceptance Criteria:
      - User should be able to view the shopping bag and all products added
      - User should be able to remove products and update their shopping bag
      - User should be able to view the grand total before proceeding to the checkout page

    - I have tested:
      - That a user can access the shopping bag page by clicking on the shopping bag icon in the header section.
      - That the shopping bag page will display all products added to the shopping bag and the grand total cost.
      - That a user can remove a specific product from the shopping bag by clicking on the remove link.

  - US16. Payment:
    - As a **Site Shopper** I can **easily enter my payment information** so that **I can check out quickly with no hassles, and feel that my personal and payment information is safe and secure**

    - Acceptance Criteria:
      - An order summary is presented to the user with grand total
      - Stripe is used for safe and secure payments

    - I have tested:
      - That an order summary is presented on the checkout page.
      - That the user is required to fill out the checkout form to complete their order.
      - That a signed in user will be able to save or not save the checkout delivery information to their profile.
      - That a signed in user will have the checkout form fields pre-populated, if previously saved profile. 
      - Using the stripe test card to complete an order, and signing in to stripe to verify that the payment has been successfully processed.

  - US17. Order confirmation:
    - As a **Site Shopper** I can **view an order confirmation after checkout** so that **I can verify that my purchase was successful and I haven’t made any mistakes**

    - Acceptance Criteria:
      - User is presented with full order information after checkout
      - User should receive an confirmation email including full order information

    - I have tested:
      - That a user is redirected to the checkout success page after completing a purchase.
      - That the correct order information is displayed on the checkout success page.
      - That the user will receive an order confirmation to their registered email account, temp mail was used to test this feature.

  - US18. Contact page:
    - As a **Site User** I can **contact site admin** so that **I can get my questions answered or provide feedback**

    - Acceptance Criteria:
      - User should easily be able to contact store admin
      - User should be presented with an contact form

    - I have tested:
      - That a user can access the contact page using the provided link in the header or footer section.
      - That all form fields are required on the contact form and that subject default is Customer service. 
      - That site admin can log in to the /admin URL with a superuser account to view any new contact inquiries.

  - US19. Newsletter:
    - As a **Site User** I can **subscribe to a newsletter** so that **I can get email informing me about new products and any changes made to the site**

    - Acceptance Criteria:
      - User should be able to subscribe to a newsletter
      - Should be easily accessible to the user

    - I have tested:
      - That a user is presented with an embedded Mailchimp newsletter form in the footer section.
      - That a user is required to enter an email addess and click on the Subscribe button to sign up, temp mail was used to test this feature.
      - That email addresses can be managed under Mailchimp audience.

  - US20. Facebook page:
    - As a **Site User** I can **access the store’s Facebook business page** so that **I can view posts and updates made on Facebook and interact**

    - Acceptance Criteria:
      - Provide a link in the footer using matching Font Awesome Facebook icon
      - The link should open in a new tab

    - I have tested:
      - That a user is presented with a link to Galleriet's facebook page in the footer section.
      - That the link address is correct and that it opens in a new tab.

  - US21. SEO:
    - As a **Site User** I can **easily find the site using popular search engines** so that **I can take advantage of what the site has to offer**

    - Acceptance Criteria:
      - Implement Keywords and descriptive meta tags
      - robots.txt file
      - sitemap.xml file

    - I have tested:
      - Acceptance criteria is met and all files are present.
      - SEO lighthouse testing.  

  - US22. Responsive:
    - As a **Site User** I can **use the site on the following platforms: desktop, laptop, tablet and smartphone** so that **I can access all functionality**

    - Acceptance Criteria:
      - Suitable graphics on different screen sizes
      - User should be able to use the site successfully on small devices (320px wide)

    - I have tested:
      - Browser testing.
      - Responsiveness.

  - US23. Design:
    - As a **Site User** I can **get an overall positive impression based on the principles of user experience design, accessibility and responsivity** so that **I can quickly determine the purpose of the site and enjoy using it**

    - Acceptance Criteria:
      - The user is presented with an easy to use navigation
      - The site meets accessibility guidelines
      - The user is presented with graphics that are consistent in style and colour

    - I have tested:
      - Browser testing.
      - Responsiveness.
      - Lighthouse.

  - US24. Favicon:
    - As a **Site User** I am **presented with a favicon** so that **I can get a better experience when browsing with multiple tabs**

    - Acceptance Criteria:
      - The user is presented with a favicon
      - The favicon is matching the overall design of the site

    - I have tested:
      - That the user is presented with a favicon that is reflecting the purpose of this project.

  - US25. GitHub:
    - As a **Site User** I am **presented with a link to mittnamnkenny’s GitHub** so that **I can view more repositories**

    - Acceptance Criteria:
      - Provide a link in the footer using matching Font Awesome GitHub icon
      - The link should open in a new tab

    - I have tested:
      - That the link address is correct and that it opens in a new tab.  

  - US26. 404 page:
    - As a **Site User** I am **presented with a custom 404 page when trying to access a URL that does not exist** so that **I can get an proper error page and easily return to the home page**

    - Acceptance Criteria:
      - The custom 404 page should be matching the overall design of the site
      - User should be provided a link to the home page

    - I have tested:
      - That the 404 page will display when changing the URL to a broken URL path. For example: /test.
      - That the return to shop link works.

#### Testing which features support which stories

User stories have been tested and below you can see which features support which stories:

User stories are numbered 1 to 26 and the features are:

1. Header
2. Home page
3. Products page
4. Product detail page
5. Shopping bag
6. Checkout page
7. Checkout success page
8. Profile page
9. Register page
10. Login page
11. Logout page
12. Contact page
13. Django Admin page
14. Product management
15. System messages
16. Featurette
17. Footer
18. Web marketing
19. Privacy Policy
20. SEO
21. Additional features


| ID | User Stories                            | Features                |
|----|---------------------------------------- |-------------------------|
|  1 | Add products                            | 14                      |
|  2 | Update products                         | 14                      |
|  3 | Delete products                         | 14                      |
|  4 | Account registration                    | 9                       |
|  5 | Login/Logout                            | 10, 11                  |
|  6 | Password reset                          | 10                      |
|  7 | Personalized profile                    | 8                       |
|  8 | View products                           | 2, 3                    |
|  9 | Product detail                          | 4                       |
| 10 | View total                              | 1                       |
| 11 | Sort list                               | 3                       |
| 12 | Search product                          | 1                       |
| 13 | System messages                         | 21                      |
| 14 | Product purchase                        | 4                       |
| 15 | Shopping bag                            | 5                       |
| 16 | Payment                                 | 6                       |
| 17 | Order confirmation                      | 7                       |
| 18 | Contact page                            | 12                      |
| 19 | Newsletter                              | 17, 18                  |
| 20 | Facebook page                           | 17, 18                  |
| 21 | SEO                                     | 20                      |
| 22 | Responsive                              | OK *                    |
| 23 | Design                                  | OK *                    |
| 24 | Favicon                                 | 21                      |
| 25 | GitHub                                  | 17                      |
| 26 | 404 page                                | 21                      |

  - OK - Tested and verifed ok in Browser Testing and Responsiveness

### Further Testing

  - I have tested that the hover effect on all buttons and links works as expected.
  - I have tested that all animations work correctly.

### Known bugs

  - Currently no known bugs.
