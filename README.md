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
