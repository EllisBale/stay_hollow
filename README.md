# [stay_hollow](https://stay-hollow-9b3793ea0059.herokuapp.com)

Developer: ([EllisBale](https://www.github.com/EllisBale))

[![GitHub commit activity](https://img.shields.io/github/commit-activity/t/EllisBale/stay_hollow)](https://www.github.com/EllisBale/stay_hollow/commits/main)
[![GitHub last commit](https://img.shields.io/github/last-commit/EllisBale/stay_hollow)](https://www.github.com/EllisBale/stay_hollow/commits/main)
[![GitHub repo size](https://img.shields.io/github/repo-size/EllisBale/stay_hollow)](https://www.github.com/EllisBale/stay_hollow)
[![badge](https://img.shields.io/badge/deployment-Heroku-purple)](https://stay-hollow-9b3793ea0059.herokuapp.com)

![screenshot](documentation/mockup.png)

source: [stay_hollow amiresponsive](https://ui.dev/amiresponsive?url=https://stay-hollow-9b3793ea0059.herokuapp.com)

## Project Overview

**Stay Hollow** is a centralised holiday letting booking website that allows users to **explore a range of holiday properties** across the UK. The platform enables users to **browse available properties**, **view detailed information**, and make **secure online bookings with ease**.

The platform is designed to be **simple**, **intuitive**, and **streamlined**, providing users with a **smooth** and **reliable booking experience**. Its **clean layout** and **straightforward navigation** helps users find **suitable accommodation** without confusion or unnecssary steps.

The website provides admins with **effcient tools** to **manage property listings**, **user accounts**, and **bookings**. This allows for **easier maintenance** of **property information** and **user management**, ensuring that availability and bookings remain **accurate** and **up to date**.

The primary target audience for this platform would be **holiday travellers** and **local visitors** looking for **comfortable**, **reliable**, and **enjoyable short-term accommodation**. Users benfit from a **simple**, **centralised booking experience** that brings everything they need into one place.

I chose to develop a holiday letting booking system because I wanted to try something that is both **challenging** and **practical** in a **real-world** use. I aim to make this website **simple** for the users because many people struggle with **complicated interfaces**. Booking a holiday should feel **exciting** and **not stressful**, so making the booking process and property listings **simple** and **enjoyable** for the user.

For this project, I researched popular UK-based holiday letting websites to understand their **layouts**, **features** and **purpose**, allowing me to **implement effective design choices and functionality** to my own website. All of the websites I visited featured a **landing page** containing a **hero image** and **search bar** to help users search immediately. It would benefit my website to have a **search bar** on the **landing page** so that users can find suitable properties based on their chosen location and requirements without unnecessary navigation.

**Websites Visited:**

[Luxury Cottages](https://luxurycottages.com/)

[Ivy](https://www.ivylettings.com/)

[The Landmark Trust](https://www.landmarktrust.org.uk/)

[Holiday Cottages](https://www.holidaycottages.co.uk/)

[Cottages](https://www.cottages.com/)

[Airbnb](https://www.airbnb.co.uk/)

## UX

### The 5 Planes of UX

#### 1. Strategy

**Purpose**

The project's purpose is to provide a seamless and intuitive e-commerce experience for users to browse, filter, search, and book properties around the UK. The website is designed to deliver users an easy-to-navigate, informative platform with secure transactions that supports users decision-making and straightforward bookings.

**Admin/Managers purpose**

The platform provides an admin interface that allows administrators and managers to:

- Create new property listings and add information for the property.
- Update existing property information, including overview, images, amenities, and location.
- Delete property listings that are no longer available.
- Manage user accounts.

**Primary User Needs**

- Guest users need to browse property listings.
- Registered users need to be able to book a date for holiday booking with secure transactions, and view order history.
- Admin/Managers users need tools for order management, user management, and property listing management.

**Business Goals**

- Drive sales by providing a user-friendly booking experience.
- Encourage repeat visits by allowing users to browse and discover new properties and locations.
- Improve property management for admin/managers to maintain an up-to-date listings.
- Increase customer trust by providing users with secure transactions, clear pricing, and up-to-date property information.
- Enhance reputation by enabling users reviews and ratings.

#### 2. Scope

**[Features](#features)** (see below)

**Content Requirements**

##### All Users

- View property details
- View destinations
- Filter listings by price, location, property name, guests, bedrooms, and description
- Search property information
- Sort listings price and newest
- 404 page for lost users

##### Registered Users

- Register and login
- Logout
- Book property dates
- Secure payments
- View current and past bookings
- Leave reviews after a stay
- Receive booking confirmation in email

##### Admin/Manager Users

- User Management
- Add properties
- Delete properties
- Edit Existing properties
- Manage reviews

#### 3. Structure

**Information Architecture**

- **Navigation Menu**:

  - User (Guest)
    - Links to Home, Listings, Destination, Contact, About, Login and Signup.
  - User (Logged-in)
    - Links to Home, Listings, Destinations, Contact, Account, About and Logout.
  - User (Admin)
    - Links to Home, Listings, Destinations, Contact, Account, About, Manage and Logout.

- **Hierarchy**:
  - Well-structured holiday categories and filters for seamless browsing.

**User Flow**

1. Guest user browses the homepage → View hero banner with searchbar, featured properties and why book with us section.
2. Guest user explore listings page → Searchbar, sortby, View listings → View property listing details.
3. Guest user creates an account → log in to make bookings.
4. Logged-in user views property detail → Choose a date → Checkout → Receive confirmation.
5. Logged-in user views past bookings.
6. Admin access manage panel → add, edit, or delete user, listings, reviews and bookings.

#### 4. Skeleton

**[Wireframes](#wireframes)** (see below)

#### 5. Surface

**Visual Design Elements**

- **[Colours](#colour-scheme)** (see below)
- **[Typography](#typography)** (see below)

### Colour Scheme

The website primarily uses light colours, mainly shade of white with slightly darker accents. For the navigation bar, I chose `#2F6F3E`, a type of green that is associated with nature and relaxation and complements well with a holiday letting website. The navbar button background colours include `#ffffff` and transparent, helping maintain a clean and simple design. The text colours on the page are mainly black to maintain a good contrast ratio with the background and ensure readability.

I used [coolors.co](https://coolors.co/2f6f3e-f3f1f1-1f2f24-245a32-e8e7e7) to generate my colour palette.

- `#0a0a0a` primary text and headings.
- `#f3f1f1` body background.
- `#2F6F3E` Navbar and transparent button background.
- `#245A32` Book Now button.
- `#E8E7E7` Light gray background for some sections.
- `#1f2f24` Dark green for footer background colour.

![screenshot](docs/readme_imgs/colours.png)

### Typography

I used three types of fonts for this website. I imported fonts from Google Fonts. I felt the fonts worked well for each other as they give optimal readability for the types of content on the website.

I use icons from [Font Awesome](https://fontawesome.com/). These icons allow users to understand information without having to read text. For example, I use icons in my property card listings so users can quickly see how many guests and beds are available on the property. Using Font Awesome icons gives the site a professional apperance.

- [Google Fonts](https://fonts.google.com/) Fonts were used for all text such as buttons, headings and paragraphs.
  - [Playfair Display](https://fonts.google.com/specimen/Playfair+Display) Used for headings.
  - [Inter](https://fonts.google.com/specimen/Inter) Used for paragraphs.
  - [Montserrat](https://fonts.google.com/specimen/Montserrat) Used for buttons and call to actions.
- [Font Awesome](https://fontawesome.com) icons were used throughout the site, such as the social media icons in the footer and amenities.

## Wireframes

To follow best practice, wireframes were developed for mobile, tablet, and desktop sizes.
I've used [Balsamiq](https://balsamiq.com/wireframes) to design my site wireframes.

| Page                  | Mobile/Tablet/Deskop                                                       |
| --------------------- | -------------------------------------------------------------------------- |
| Home                  | ![screenshot](docs/wireframes/stay_hollow_home_wireframes.png)             |
| Login                 | ![screenshot](docs/wireframes/stay_hollow_login_wireframes.png)            |
| Sign up               | ![screenshot](docs/wireframes/stay_hollow_signup_wireframes.png)           |
| Listings              | ![screenshot](docs/wireframes/stay_hollow_listings_wireframes.png)         |
| Listing Details       | ![screenshot](docs/wireframes/stay_hollow_listings_details_wireframes.png) |
| Account Order History | ![screenshot](docs/wireframes/stay_hollow_order_history_wireframes.png)    |
| Management            | ![screenshot](docs/wireframes/stay_hollow_admin_wireframes.png)            |
| Checkout              | ![screenshot](docs/wireframes/stay_hollow_checkout_wireframes.png)         |
| Checkout Success      | ![screenshot](docs/wireframes/stay_hollow_checkout_success_wireframes.png) |
| About                 | ![screenshot](docs/wireframes/stay_hollow_about_wireframes.png)            |
| Contact               | ![screenshot](docs/wireframes/stay_hollow_contact_wireframes.png)          |
| 404                   | ![screenshot](docs/wireframes/stay_hollow_404_wireframes.png)              |

## User Stories

| Target               | Expectation                                                                    | Outcome                                                                    |
| -------------------- | ------------------------------------------------------------------------------ | -------------------------------------------------------------------------- |
| As a Logged-in user, | I want to book a holiday property for specific dates,                          | so I can secure my stay and complete my reservation online.                |
| As a Logged-in user, | I want to view an order booking confirmation after checkout.                   | so I can verify that my payment and booking were successful.               |
| As a Logged-in user, | I want to make secure online payments for my bookings                          | so my financial details are protected.                                     |
| As a Logged-in user, | I want to be able to receive a confirmation through email after checkout       | so I have a confirmation for my records.                                   |
| As a Site User,      | I want to search for properties directly from the homepage                     | so I can start finding places immediately.                                 |
| As a Site User,      | I want to be able to browse all available holiday properties                   | so I can explore my options.                                               |
| As a Site User,      | I want to view detailed property pages with photos, descriptions and amenities | so I can make an informed choice.                                          |
| As a Site User,      | I want to filter properties by location, price and number of guests            | so I can find suitable accommodation.                                      |
| As a Site User,      | I want to create an account and log in                                         | so I can manage bookings and preferences.                                  |
| As a Site User,      | I want to see featured or popular properties on the landing page,              | so I can quickly explore attractive options.                               |
| As a Site User,      | I want to be able to see reviews and ratings for each property,                | so that I can decide where to stay.                                        |
| As a Site User,      | I want to see reasons to book on this website and what the benefits are,       | so that I can be assured that using this website to book will be worth it. |
| As a Site User,      | I want to see footer details like contact info, social links, and copyright,   | so I can learn more about the company.                                     |
| As a Site User,      | I want to see a list of popular destinations on the homepage                   | so I can quickly discover places that are trending or highly recommended.  |
| As an Admin,         | I want to add, edit, or remove property listings                               | so I can control what’s shown on the website.                              |
| As an Admin,         | I want to view and manage user accounts                                        | so I can assist customers when needed.                                     |
| As an Admin,         | I want to moderate or remove inappropriate reviews,                            | so that I can maintain the platform’s reputation.                          |
| As an Admin,         | I want to view and manage user bookings                                        | so I can assist customers when needed.                                     |

## Features

### Existing Features

| Feature                         | Notes                                                                                                                                                                                                                                                    | Screenshot                                                      |
| ------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------- |
| Register                        | Authentication is handled by allauth, allowing users to register accounts. I have added a custom form so that users are required to give first name and last name when registering an account.                                                           | ![screenshot](docs/readme_imgs/features/signup.png)             |
| Login                           | Authentication is handled by allauth, allowing users to log in to their existing accounts.                                                                                                                                                               | ![screenshot](docs/readme_imgs/features/login.png)              |
| Logout                          | Authentication is handled by allauth, allowing users to log out of their accounts.                                                                                                                                                                       | ![screenshot](docs/readme_imgs/features/logout.png)             |
| Hero Section                    | The homepage displays a large hero image containing a search bar to immediately engage users and communicate the purpose of the website.                                                                                                                 | ![screenshot](docs/readme_imgs/features/hero.png)               |
| Property Search Bar             | Allows users to search properties that are available. The search bar requests queries for property name, bedrooms, guests, description and destinations.                                                                                                 | ![screenshot](docs/readme_imgs/features/searchbar.png)          |
| Featured Properties             | Home page contains featured properties to encourage users to explore directly from the homepage.                                                                                                                                                         | ![screenshot](docs/readme_imgs/features/featured.png)           |
| Property Listings               | Displays a list of all available properties from the database which users can click on for more details.                                                                                                                                                 | ![screenshot](docs/readme_imgs/features/property_list.png)      |
| Property Sort By                | Allows users to filter properties by low to high price, high to low, and newest properties.                                                                                                                                                              | ![screenshot](docs/readme_imgs/features/sortby.png)             |
| Property Details Display        | Displays full property information including description, price, max-guests, bedrooms, images and location. Having these on the page allows the user to understand what the property has to offer. This allows users to make informed booking decisions. | ![screenshot](docs/readme_imgs/features/property_details.png)   |
| Property Location Map           | Provides an interactive map showing the property's location. This helps users understand the surrounding area and what attractions and transport links are near by.                                                                                      | ![screenshot](docs/readme_imgs/features/location.png)           |
| Book Now Button                 | Allows users to begin the booking process directly from the property details page, allowing them to secure accommodation quickly and efficiently.                                                                                                        | ![screenshot](docs/readme_imgs/features/book_now.png)           |
| Property Review                 | Displays customer reviews that have previously stayed at the property, helping users assess the quality and reliability of a property and increase user trust in their booking decision.                                                                 | ![screenshot](docs/readme_imgs/features/reviews.png)            |
| Amenities Display               | Shows a clear list of amenities for each property, allowing users to confirm that the property meets their specific requirements.                                                                                                                        | ![screenshot](docs/readme_imgs/features/amenities.png)          |
| Destination Navigation Dropdown | Users can navigate destination locations on the navigation dropdown, allowing users to explore properties on chosen location.                                                                                                                            | ![screenshot](docs/readme_imgs/features/destination.png)        |
| Order History                   | Allows Logged-in users to see their recent orders details. This helps users keep track of past bookings and easily reference booking information when needed.                                                                                            | ![screenshot](documentation/features/faqs.png)                  |
| User Feedback                   | Clear and concise Django messages are used to provide feedback to users when interacting with various features.                                                                                                                                          | ![screenshot](docs/readme_imgs/features/messages.png)           |
| Pagination                      | Splits pages including properties page and admin pages to improve usability and performance.                                                                                                                                                             | ![screenshot](docs/readme_imgs/features/pagination.png)         |
| Booking Date                    | Allows users to pick a check-in and check-out date as well as number of guests staying. Dates that have been previously booked will be invalid and a error message will show. If dates are valid it will move onto the checkout page.                    | ![screenshot](docs/readme_imgs/features/booking_date.png)       |
| Checkout                        | Users can proceed to checkout, where they provide their delivery details and payment information using Stripe integration.                                                                                                                               | ![screenshot](documentation/features/heroku.png)                |
| Order Confirmation              | Users receive an on-screen and email confirmation with details of their purchase. users.                                                                                                                                                                 | ![screenshot](docs/readme_imgs/features/email_confirmaiton.png) |
| Admin Overview                  | Allows admin users to view a summary of total listings, total bookings, total users and total reviews. This provides admin to see platform activity, helping them monitor performance and to make informed decisions to manage and improve the system.   | ![screenshot](docs/readme_imgs/features/overview.png)           |
| Heroku Deployment               | The site is deployed to Heroku, making it accessible online for users.                                                                                                                                                                                   | ![screenshot](docs/readme_imgs/features/heroku.png)             |
| Admin CRUD - Listings           | Allows admin users to create, read, update, and delete property listings.This enables admin to manage available properties, ensuring the platform always displays accurate and up-to-date information about the properties for users.                    | ![screenshot](docs/readme_imgs/features/manage_listings.png)    |
| Admin CRUD - Users              | Allows admin users to manage user accounts, including updating and removing users. This ensures users have the right access control and helps maintain safe, organised user database.                                                                    | ![screenshot](docs/readme_imgs/features/manage_users.png)       |
| Admin CRUD - Bookings           | Allows admin users to view and manage user bookings, including editing and deleting bookings. This enables admins to support users with their bookings.                                                                                                  | ![screenshot](docs/readme_imgs/features/manage_bookings.png)    |
| Admin CRUD - Reviews            | Allows admin users to manage user-submitted reviews, including editing or deleting them. This helps maintain content quality and ensures the reviews are appropriate and accurate.                                                                       | ![screenshot](docs/readme_imgs/features/manage_reviews.png)     |
| 404                             | The 404 error page will indicate when a user has navigated to a page that doesn't exist, replacing the default Heroku 404 page with one that ties into the site's look and feel.                                                                         | ![screenshot](docs/readme_imgs/features/404.png)                |

### Future Features

- **Product Reviews & Ratings**: Allow customers to leave reviews and rate products, with admin moderation. Display average ratings and review counts on product pages.
- **Wishlist Functionality**: Enable users to save products to a personal wishlist for future purchases. Notify users if wishlist items go on sale or are back in stock.
- **Product Recommendations**: Implement a "Customers who bought this also bought" or "You might also like" feature to suggest related products.
- **Live Chat Support**: Provide real-time customer support through an integrated live chat or chatbot.
- **Abandoned Cart Recovery**: Automatically send emails to users who add items to their cart but don't complete the purchase, offering discounts or reminders.
- **Discount Codes and Vouchers**: Allow the admin to create discount codes or vouchers for promotions and marketing campaigns.
- **Loyalty Program**: Introduce a points-based loyalty system where customers earn points for purchases, which can be redeemed for discounts.
- **Product Inventory Alerts**: Notify customers when out-of-stock items are back in stock, or when low inventory is approaching.
- **Multi-Currency and Multi-Language Support**: Expand the application to support multiple currencies and languages to reach a global audience.
- **Product Bundles**: Offer discounted product bundles (e.g., buy 3 for the price of 2) or custom product kits.
- **Social Media Integration**: Enable users to share products directly to social media platforms or implement a social login for quick account creation.
- **Shipping Tracking Integration**: Provide real-time shipping updates and tracking information directly within the user’s order history.
- **Advanced Analytics Dashboard for Admin**: Offer an in-depth dashboard that displays sales trends, popular products, customer behavior, and more.
- **Subscription-Based Products**: Allow users to subscribe to certain products (e.g., monthly deliveries of consumables like coffee or skincare products).
- **Product Video Demos**: Support product videos to better showcase features, especially for high-tech or complex items.
- **Mobile App**: Develop a mobile app for iOS and Android, providing users with a more optimized shopping experience on mobile devices.

## Tools & Technologies

| Tool / Tech                                                                                                                | Use                                                                               |
| -------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- |
| [![badge](https://img.shields.io/badge/Markdown_Builder-grey?logo=markdown&logoColor=000000)](https://markdown.2bn.dev)    | Generate README and TESTING templates.                                            |
| [![badge](https://img.shields.io/badge/Git-grey?logo=git&logoColor=F05032)](https://git-scm.com)                           | Version control. (`git add`, `git commit`, `git push`)                            |
| [![badge](https://img.shields.io/badge/GitHub-grey?logo=github&logoColor=181717)](https://github.com)                      | Secure online code storage.                                                       |
| [![badge](https://img.shields.io/badge/VSCode-grey?logo=htmx&logoColor=007ACC)](https://code.visualstudio.com)             | Local IDE for development.                                                        |
| [![badge](https://img.shields.io/badge/HTML-grey?logo=html5&logoColor=E34F26)](https://en.wikipedia.org/wiki/HTML)         | Main site content and layout.                                                     |
| [![badge](https://img.shields.io/badge/CSS-grey?logo=css&logoColor=1572B6)](https://en.wikipedia.org/wiki/CSS)             | Design and layout.                                                                |
| [![badge](https://img.shields.io/badge/JavaScript-grey?logo=javascript&logoColor=F7DF1E)](https://www.javascript.com)      | User interaction on the site.                                                     |
| [![badge](https://img.shields.io/badge/Python-grey?logo=python&logoColor=3776AB)](https://www.python.org)                  | Back-end programming language.                                                    |
| [![badge](https://img.shields.io/badge/jQuery-grey?logo=jquery&logoColor=3776AB)](https://jquery.com/)                     | JavaScript library.                                                               |
| [![badge](https://img.shields.io/badge/Heroku-grey?logo=heroku&logoColor=430098)](https://www.heroku.com)                  | Hosting the deployed back-end site.                                               |
| [![badge](https://img.shields.io/badge/Bootstrap-grey?logo=bootstrap&logoColor=7952B3)](https://getbootstrap.com)          | Front-end CSS framework for modern responsiveness and pre-built components.       |
| [![badge](https://img.shields.io/badge/Django-grey?logo=django&logoColor=092E20)](https://www.djangoproject.com)           | Python framework for the site.                                                    |
| [![badge](https://img.shields.io/badge/PostgreSQL-grey?logo=postgresql&logoColor=4169E1)](https://www.postgresql.org)      | Relational database management.                                                   |
| [![badge](https://img.shields.io/badge/Cloudinary-grey?logo=cloudinary&logoColor=3448C5)](https://cloudinary.com)          | Online static file storage.                                                       |
| [![badge](https://img.shields.io/badge/WhiteNoise-grey?logo=python&logoColor=FFFFFF)](https://whitenoise.readthedocs.io)   | Serving static files with Heroku.                                                 |
| [![badge](https://img.shields.io/badge/Stripe-grey?logo=stripe&logoColor=008CDD)](https://stripe.com)                      | Online secure payments of e-commerce products/services.                           |
| [![badge](https://img.shields.io/badge/Gmail_API-grey?logo=gmail&logoColor=EA4335)](https://mail.google.com)               | Sending emails in my application.                                                 |
| [![badge](https://img.shields.io/badge/Balsamiq-grey?logo=barmenia&logoColor=CE0908)](https://balsamiq.com/wireframes)     | Creating wireframes.                                                              |
| [![badge](https://img.shields.io/badge/Leaflet-grey?logo=leaflet&logoColor=199900)](https://leafletjs.com/)                | Interactive map on my site.                                                       |
| [![badge](https://img.shields.io/badge/Font_Awesome-grey?logo=fontawesome&logoColor=528DD7)](https://fontawesome.com)      | Icons.                                                                            |
| [![badge](https://img.shields.io/badge/ChatGPT-grey?logo=openai&logoColor=75A99C)](https://chat.openai.com)                | Help debug, troubleshoot, and explain things as well as for property information. |
| [![badge](https://img.shields.io/badge/Mermaid-grey?logo=mermaid&logoColor=FF3670)](https://mermaid.live)                  | Generate an interactive diagram for the data/schema.                              |
| [![badge](https://img.shields.io/badge/W3Schools-grey?logo=w3schools&logoColor=04AA6D)](https://www.w3schools.com)         | Tutorials/Reference Guide                                                         |
| [![badge](https://img.shields.io/badge/MDN-grey?logo=mdnwebdocs&logoColor=000000)](https://developer.mozilla.org/en-US/)   | Tutorials/Reference Guide                                                         |
| [![badge](https://img.shields.io/badge/StackOverflow-grey?logo=stackoverflow&logoColor=F58025)](https://stackoverflow.com) | Troubleshooting and Debugging                                                     |
| [![badge](https://img.shields.io/badge/GoogleFonts-grey?logo=googlefonts&logoColor=4285F4)](https://fonts.google.com/)     | Font Styles                                                                       |

## Database Design

### Data Model

Entity Relationship Diagrams (ERD) help to visualize database architecture before creating models. Understanding the relationships between different tables can save time later in the project.

![screenshot](docs/readme_imgs/erd.svg)

I have used `Mermaid` to generate an interactive ERD of my project.

```mermaid
erDiagram
    %% USERS
    USER ||--o{ BOOKING : makes
    USER ||--o{ ORDER : places
    USER ||--o{ REVIEW : writes

    %% LISTINGS
    PROPERTY ||--o{ BOOKING : booked_in
    PROPERTY ||--o{ PROPERTY_IMAGE : has
    PROPERTY ||--o{ AMENITY : includes
    DESTINATION ||--o{ PROPERTY : contains
    DESTINATION ||--o{ DESTINATION : parent_of

    %% BOOKINGS AND ORDERS
    BOOKING ||--o| ORDER : generates
    BOOKING ||--o| REVIEW : has

    %% ENTITIES
    USER {
        int id PK
        string username
        string email
        string password
    }

    BOOKING {
        int id PK
        int property_id FK
        int user_id FK
        date check_in
        date check_out
        int guests
        decimal total_price
        datetime created_at
        boolean is_paid
    }

    ORDER {
        int id PK
        string order_number
        int user_id FK
        int booking_id FK
        string first_name
        string last_name
        string email
        string phone_number
        string postcode
        string town_or_city
        string street_address1
        string street_address2
        string country
        string county
        decimal order_total
        string stripe_payment_intent
        datetime date
    }

    PROPERTY {
        int id PK
        string property_name
        int destinations_id FK
        decimal price_per_night
        int bedrooms
        int guests
        string main_image
        string description
        decimal latitude
        decimal longitude
        boolean is_featured
        datetime created_at
    }

    PROPERTY_IMAGE {
        int id PK
        int property_id FK
        string image
    }

    AMENITY {
        int id PK
        string name
        string icon_class
    }

    DESTINATION {
        int id PK
        string name
        int parent_destination_id FK
        string slug
        text area_description
    }

    REVIEW {
        int id PK
        int booking_id FK
        int user_id FK
        int rating
        text comment
        datetime created_at
    }
```

source: [Mermaid](https://mermaid.live/edit#pako:eNqdVm1vmzAQ_ivIUr-1FaQhS_mWLaxCXZMqyTZtioRccIgVsJFt1GZp__vOvJUCaaPyBfve7567gwMKeEiQg4iYUhwJnKyZAc_ZmfFz6S6WxU0fjefniwt-ML7O57fe7MZwjATviOwKzBdTuDhGGuOgj79wf3nubxB4FFRpgdrjD2-5AtOl0_vF_N5drP50HT9wviOhT1m_YHX3vbvJjQvyWyz7JSd37syDq2NQFsRZWIU7dXUgk5U3n7WNgmzAmcKUHZdtkqAOWBCmfL5pZFrmsjQms2lRsDLpKsnc0nNdy4gwIrCq4mtJ1RXNE62duLOVt_LcJoaH4qwfypRBQ-P-9pUklaAsMjJJBMMJ6TBIgmncoaZYykcuwoLxUgVQxfi-S01KBU-JUHsfeN9bPB1Lmx5CIYxgS4Jd3QItMs_UWzNRRqSSDVkS0ATHhuIKx34qaEDeGlI0AWOCwDH0ccMa9F5MMDOo9FNM20kXeJ1UZagYpMay5IGIj3PWdN32oNlmlfY2VEjl9-IW42OcI4huOSOd0Coml0rvjA5D8Ufmc-EHVO07THgRonwchoJIaX3AH3T4Ac-YEvt--r4LbFHdHN4-XzQlAN8-0YMJpYVXD_z60MK33gInQVw39tvaawVYNYoyrChnstPfZQ55W_qp7hIabVsd_UBCwXki3-_zMhBAmflgM-qiBoEEUA4dSDeCGAJUWRPrmsNZ1GI1JmMDc5MJEp4wU53Sllv782ujTKyRbu2j2vcnodc7MBSWvx_AQMmW6ebO_4T5PKHiQ9FojSOpyTiLXomKPCkDVLHfwbKOrvxCfFzUIzvmvbUE3yXQaMUT8CTpn6pOA6BzFAkaIkeJjJyjhAhoV7iiPNo1UlsClUIOHEMsdmu0ZlonxewvDEClJngWbZGzwbGEW5Zqf-UfTS1CGCyFb3pjIMeyTTs3gpwDekLOxcC8HI9t2xxdDa-G46H55RztgTw2L0embY1Gw8HIHI6tl3P0L3drXQ6vx5ZpX1v20DKtgQ0KOFN8uWdB4fHlP4pb0Bg)

## Agile Development Process

### GitHub Projects

[GitHub Projects](https://www.github.com/EllisBale/stay_hollow/projects) served as an Agile tool for this project. Through it, EPICs, User Stories, issues/bugs, and Milestone tasks were planned, then subsequently tracked on a regular basis using the Kanban project board.

![screenshot](docs/readme_imgs/github_project.png)

### GitHub Issues

[GitHub Issues](https://www.github.com/EllisBale/stay_hollow/issues) served as an another Agile tool. There, I managed my User Stories and Milestone tasks, and tracked any issues/bugs.

| Link                                                                                                                                                                                                                                                                        | Screenshot                                              |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------- |
| [![GitHub issues](https://img.shields.io/github/issues-search/EllisBale/stay_hollow?query=is%3Aissue%20is%3Aopen%20-label%3Abug&label=Open%20Issues&color=yellow)](https://www.github.com/EllisBale/stay_hollow/issues?q=is%3Aissue%20is%3Aopen%20-label%3Abug)             | ![screenshot](docs/readme_imgs/close_github_issues.png) |
| [![GitHub closed issues](https://img.shields.io/github/issues-search/EllisBale/stay_hollow?query=is%3Aissue%20is%3Aclosed%20-label%3Abug&label=Closed%20Issues&color=green)](https://www.github.com/EllisBale/stay_hollow/issues?q=is%3Aissue%20is%3Aclosed%20-label%3Abug) | ![screenshot](docs/readme_imgs/github_issues.png)       |

### MoSCoW Prioritization

I've decomposed my Epics into User Stories for prioritizing and implementing them. Using this approach, I was able to apply "MoSCoW" prioritization and labels to my User Stories within the Issues tab.

- **Must Have**: guaranteed to be delivered - required to Pass the project (_max ~60% of stories_)
- **Should Have**: adds significant value, but not vital (_~20% of stories_)
- **Could Have**: has small impact if left out (_the rest ~20% of stories_)
- **Won't Have**: not a priority for this iteration - future features

## Testing

> [!NOTE]  
> For all testing, please refer to the [TESTING.md](TESTING.md) file.

## Deployment

The live deployed application can be found deployed on [Heroku](https://stay-hollow-9b3793ea0059.herokuapp.com).

### Heroku Deployment

This project uses [Heroku](https://www.heroku.com), a platform as a service (PaaS) that enables developers to build, run, and operate applications entirely in the cloud.

Deployment steps are as follows, after account setup:

- Select **New** in the top-right corner of your Heroku Dashboard, and select **Create new app** from the dropdown menu.
- Your app name must be unique, and then choose a region closest to you (EU or USA), then finally, click **Create App**.
- From the new app **Settings**, click **Reveal Config Vars**, and set your environment variables to match your private `env.py` file.

> [!IMPORTANT]  
> This is a sample only; you would replace the values with your own if cloning/forking my repository.

| Key                     | Value                                                                |
| ----------------------- | -------------------------------------------------------------------- |
| `CLOUDINARY_URL`        | user-inserts-own-cloudinary-url                                      |
| `DATABASE_URL`          | user-inserts-own-postgres-database-url                               |
| `DISABLE_COLLECTSTATIC` | 1 (_this is temporary, and can be removed for the final deployment_) |
| `EMAIL_HOST_PASS`       | user-inserts-own-gmail-api-key                                       |
| `EMAIL_HOST_USER`       | user-inserts-own-gmail-email-address                                 |
| `SECRET_KEY`            | any-random-secret-key                                                |
| `HOST`                  | your-heroku-app-name.herokuapp.com                                   |
| `STRIPE_PUBLIC_KEY`     | user-inserts-own-stripe-public-key                                   |
| `STRIPE_SECRET_KEY`     | user-inserts-own-stripe-secret-key                                   |
| `STRIPE_WH_SECRET`      | user-inserts-own-stripe-webhook-secret                               |

Heroku needs some additional files in order to deploy properly.

- [requirements.txt](requirements.txt)
- [Procfile](Procfile)
- [.python-version](.python-version)

You can install this project's **[requirements.txt](requirements.txt)** (_where applicable_) using:

- `pip3 install -r requirements.txt`

If you have your own packages that have been installed, then the requirements file needs updated using:

- `pip3 freeze --local > requirements.txt`

The **[Procfile](Procfile)** can be created with the following command:

- `echo web: gunicorn app_name.wsgi > Procfile`
- _replace `app_name` with the name of your primary Django app name; the folder where `settings.py` is located_

The **[.python-version](.python-version)** file tells Heroku the specific version of Python to use when running your application.

- `3.12` (or similar)

For Heroku deployment, follow these steps to connect your own GitHub repository to the newly created app:

Either (_recommended_):

- Select **Automatic Deployment** from the Heroku app.

Or:

- In the Terminal/CLI, connect to Heroku using this command: `heroku login -i`
- Set the remote for Heroku: `heroku git:remote -a app_name` (_replace `app_name` with your app name_)
- After performing the standard Git `add`, `commit`, and `push` to GitHub, you can now type:
  - `git push heroku main`

The project should now be connected and deployed to Heroku!

### Cloudinary API

This project uses the [Cloudinary API](https://cloudinary.com) to store media assets online, due to the fact that Heroku doesn't persist this type of data.

To obtain your own Cloudinary API key, create an account and log in.

- For "Primary Interest", you can choose **Programmable Media for image and video API**.
- _Optional_: edit your assigned cloud name to something more memorable.
- On your Cloudinary Dashboard, you can copy your **API Environment Variable**.
- Be sure to remove the leading `CLOUDINARY_URL=` as part of the API **value**; this is the **key**.
  - `cloudinary://123456789012345:AbCdEfGhIjKlMnOpQrStuVwXyZa@1a2b3c4d5)`
- This will go into your own `env.py` file, and Heroku Config Vars, using the **key** of `CLOUDINARY_URL`.

### PostgreSQL

This project uses a [Code Institute PostgreSQL Database](https://dbs.ci-dbs.net) for the Relational Database with Django.

> [!CAUTION]
>
> - PostgreSQL databases by Code Institute are only available to CI Students.
> - You must acquire your own PostgreSQL database through some other method if you plan to clone/fork this repository.
> - Code Institute students are allowed a maximum of 8 databases.
> - Databases are subject to deletion after 18 months.

To obtain my own Postgres Database from Code Institute, I followed these steps:

- Submitted my email address to the CI PostgreSQL Database link above.
- An email was sent to me with my new Postgres Database.
- The Database connection string will resemble something like this:
  - `postgres://<db_username>:<db_password>@<db_host_url>/<db_name>`
- You can use the above URL with Django; simply paste it into your `env.py` file and Heroku Config Vars as `DATABASE_URL`.

### Stripe API

This project uses [Stripe](https://stripe.com) to handle the ecommerce payments.

Once you've created a Stripe account and logged-in, follow these series of steps to get your project connected.

- From your Stripe dashboard, click to expand the "Get your test API keys".
- You'll have two keys here:
  - `STRIPE_PUBLIC_KEY` = Publishable Key (starts with **pk**)
  - `STRIPE_SECRET_KEY` = Secret Key (starts with **sk**)

As a backup, in case users prematurely close the purchase-order page during payment, we can include Stripe Webhooks.

- From your Stripe dashboard, click **Developers**, and select **Webhooks**.
- From there, click **Add Endpoint**.
  - `https://stay-hollow-9b3793ea0059.herokuapp.com/checkout/wh/`
- Click **receive all events**.
- Click **Add Endpoint** to complete the process.
- You'll have a new key here:
  - `STRIPE_WH_SECRET` = Signing Secret (Wehbook) Key (starts with **wh**)

### Gmail API

This project uses [Gmail](https://mail.google.com) to handle sending emails to users for purchase order confirmations.

Once you've created a Gmail (Google) account and logged-in, follow these series of steps to get your project connected.

- Click on the **Account Settings** (cog icon) in the top-right corner of Gmail.
- Click on the **Accounts and Import** tab.
- Within the section called "Change account settings", click on the link for **Other Google Account settings**.
- From this new page, select **Security** on the left.
- Select **2-Step Verification** to turn it on. (_verify your password and account_)
- Once verified, select **Turn On** for 2FA.
- Navigate back to the **Security** page, and you'll see a new option called **App passwords** (_search for it at the top, if not_).
- This might prompt you once again to confirm your password and account.
- Select **Mail** for the app type.
- Select **Other (Custom name)** for the device type.
  - Any custom name, such as "Django" or `stay_hollow`
- You'll be provided with a 16-character password (API key).
  - Save this somewhere locally, as you cannot access this key again later!
  - If your 16-character password contains _spaces_, make sure to remove them entirely.
  - `EMAIL_HOST_PASS` = user's 16-character API key
  - `EMAIL_HOST_USER` = user's own personal Gmail email address

### WhiteNoise

This project uses the [WhiteNoise](https://whitenoise.readthedocs.io/en/latest/) to aid with static files temporarily hosted on the live Heroku site.

To include WhiteNoise in your own projects:

- Install the latest WhiteNoise package:
  - `pip install whitenoise`
- Update the `requirements.txt` file with the newly installed package:
  - `pip freeze --local > requirements.txt`
- Edit your `settings.py` file and add WhiteNoise to the `MIDDLEWARE` list, above all other middleware (apart from Django’s "SecurityMiddleware"):

```python
# settings.py

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    # any additional middleware
]
```

### Local Development

This project can be cloned or forked in order to make a local copy on your own system.

For either method, you will need to install any applicable packages found within the [requirements.txt](requirements.txt) file.

- `pip3 install -r requirements.txt`.

You will need to create a new file called `env.py` at the root-level, and include the same environment variables listed above from the Heroku deployment steps.

> [!IMPORTANT]  
> This is a sample only; you would replace the values with your own if cloning/forking my repository.

Sample `env.py` file:

```python
import os

os.environ.setdefault("DATABASE_URL", "user-inserts-own-postgres-database-url")
os.environ.setdefault("HOST", "127.0.0.1")
os.environ.setdefault("EMAIL_HOST_PASS", "user-inserts-own-gmail-host-api-key")
os.environ.setdefault("EMAIL_HOST_USER", "user-inserts-own-gmail-email-address")
os.environ.setdefault("CLOUDINARY_URL", "user-inserts-own-cloudinary-url")
os.environ.setdefault("SECRET_KEY", "any-random-secret-key")
os.environ.setdefault("STRIPE_PUBLIC_KEY", "user-inserts-own-stripe-public-key")
os.environ.setdefault("STRIPE_SECRET_KEY", "user-inserts-own-stripe-secret-key")
os.environ.setdefault("STRIPE_WH_SECRET", "user-inserts-own-stripe-webhook-secret")  # only if using Stripe Webhooks

# local environment only (do not include these in production/deployment!)
os.environ.setdefault("DEBUG", "True")
os.environ.setdefault("DEVELOPMENT", "1")
```

Once the project is cloned or forked, in order to run it locally, you'll need to follow these steps:

- Start the Django app: `python3 manage.py runserver`
- Stop the app once it's loaded: `CTRL+C` (_Windows/Linux_) or `⌘+C` (_Mac_)
- Make any necessary migrations: `python3 manage.py makemigrations --dry-run` then `python3 manage.py makemigrations`
- Migrate the data to the database: `python3 manage.py migrate --plan` then `python3 manage.py migrate`
- Create a superuser: `python3 manage.py createsuperuser`
- Load fixtures (_if applicable_): `python3 manage.py loaddata file-name.json` (_repeat for each file_)
- Everything should be ready now, so run the Django app again: `python3 manage.py runserver`

If you'd like to backup your database models, use the following command for each model you'd like to create a fixture for:

- `python3 manage.py dumpdata your-model > your-model.json`
- _repeat this action for each model you wish to backup_
- **NOTE**: You should never make a backup of the default _admin_ or _users_ data with confidential information.

#### Cloning

You can clone the repository by following these steps:

1. Go to the [GitHub repository](https://www.github.com/EllisBale/stay_hollow).
2. Locate and click on the green "Code" button at the very top, above the commits and files.
3. Select whether you prefer to clone using "HTTPS", "SSH", or "GitHub CLI", and click the "copy" button to copy the URL to your clipboard.
4. Open "Git Bash" or "Terminal".
5. Change the current working directory to the location where you want the cloned directory.
6. In your IDE Terminal, type the following command to clone the repository:
   - `git clone https://www.github.com/EllisBale/stay_hollow.git`
7. Press "Enter" to create your local clone.

Alternatively, if using Ona (formerly Gitpod), you can click below to create your own workspace using this repository.

[![Open in Ona-Gitpod](https://ona.com/run-in-ona.svg)](https://gitpod.io/#https://www.github.com/EllisBale/stay_hollow)

**Please Note**: in order to directly open the project in Ona (Gitpod), you should have the browser extension installed. A tutorial on how to do that can be found [here](https://www.gitpod.io/docs/configure/user-settings/browser-extension).

#### Forking

By forking the GitHub Repository, you make a copy of the original repository on our GitHub account to view and/or make changes without affecting the original owner's repository. You can fork this repository by using the following steps:

1. Log in to GitHub and locate the [GitHub Repository](https://www.github.com/EllisBale/stay_hollow).
2. At the top of the Repository, just below the "Settings" button on the menu, locate and click the "Fork" Button.
3. Once clicked, you should now have a copy of the original repository in your own GitHub account!

### Local VS Deployment

There are no remaining major differences between the local version when compared to the deployed version online.

## Credits

### Content

| Source                                                                                                                        | Notes                                               |
| ----------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------- |
| [Markdown Builder](https://markdown.2bn.dev)                                                                                  | Help generating Markdown files                      |
| [Boutique Ado](https://codeinstitute.net)                                                                                     | Code Institute walkthrough project inspiration      |
| [Bootstrap](https://getbootstrap.com)                                                                                         | Various components / responsive front-end framework |
| [Whitenoise](https://whitenoise.readthedocs.io)                                                                               | Static file service                                 |
| [Stripe](https://docs.stripe.com/payments/elements)                                                                           | Online payment services                             |
| [Gmail API](https://developers.google.com/gmail/api/guides)                                                                   | Sending payment confirmation emails                 |
| [Python Tutor](https://pythontutor.com)                                                                                       | Additional Python help                              |
| [ChatGPT](https://chatgpt.com)                                                                                                | Help with code logic and explanations               |
| [Leaflet](https://leafletjs.com)                                                                                              | Interactive map                                     |
| [Pixabay](https://pixabay.com)                                                                                                | Copyright free images for properties                |
| [Unsplash](https://unsplash.com)                                                                                              | Copyright free images for properties                |
| [pxhere](https://pxhere.com)                                                                                                  | Copyright free images for properties                |
| [TempMail](https://temp-mail.org/en)                                                                                          | Help with testing accounts with temporary emails    |
| [CSS Box Shadow](https://www.w3schools.com/css/css3_shadows_box.asp)                                                          | Box shadow for property cards                       |
| [Pagination](https://docs.djangoproject.com/en/5.2/topics/pagination)                                                         | Pagination for admin pages and properties           |
| [Window: innerWidth property](https://developer.mozilla.org/en-US/docs/Web/API/Window/innerWidth)                             | Back to top button                                  |
| [Built-in template tags and filters](https://docs.djangoproject.com/en/6.0/ref/templates/builtins/)                           | forloop.counter for review rating                   |
| [QuerySet API reference](https://docs.djangoproject.com/en/6.0/ref/models/querysets/#django.db.models.query.QuerySet.exclude) | .exclude() and .first() used for add review view.   |

### Media

#### Listing images used:

- [Hero Image](https://pixabay.com/photos/building-interior-design-furnitures-8484196/) by 23555986

- [England Destination Image](https://pixabay.com/photos/lake-district-england-countryside-4098349/) by Northern_Punkie

- [Scotland Destination Image](https://pixabay.com/photos/scotland-mountains-road-lonely-4276144/) by McRonny

- [Wales Destination Image ](https://pixabay.com/photos/coast-ocean-cliffs-beach-wales-4537432/) by diego_torres

- [Edinburgh Destination Image](https://pixabay.com/photos/edinburgh-castle-edinburgh-castle-997077/) by Walkerssk

- [Dorset Destination Image](https://pixabay.com/photos/bay-ship-ocean-dorset-england-1787065/) by diego_torres

- [Cornwall Destination Image](https://pixabay.com/id/photos/cornwall-lanskap-pesisir-2391906/) by Kathy_Büscher

- [Whitwave House](https://pixabay.com/photos/architecture-render-external-design-1477101/) by Giovanni_cg

  - [Room](https://pixabay.com/photos/architecture-render-external-design-1477100/) by Giovanni_cg

- [Saltwood Retreat](https://unsplash.com/photos/white-and-grey-concrete-building-near-swimming-pool-under-clear-sky-during-daytime-2d4lAQAlbDA) by Frames For Your Heart

  - [Room](https://unsplash.com/photos/a-house-with-a-glass-front-HOCxqM8z4LY) by Woody Kelly

- [Seafoam House](https://unsplash.com/photos/white-and-brown-concrete-house-near-body-of-water-during-daytime-htIxmylBznU) by Eilis Garvey

- [Glenpine Lodge](https://pixabay.com/tr/photos/eve-giri%c5%9f-yapmak-kay%c4%b1t-ev-k%c4%b1rsal-2225433/) by user32212

  - [Kitchen](https://pixabay.com/photos/hdr-logs-log-home-log-cabin-2244067/) by user32212
  - [Bedroom](https://pixabay.com/photos/log-home-log-home-bedroom-rustic-2225414/) by user32212

- [Brambleroom House](https://pixabay.com/photos/house-cottage-rural-building-home-4020575/) by dimitrisvetsikas1969

- [Cwmleaf Cottage](https://unsplash.com/photos/a-couple-of-wooden-chairs-sitting-on-top-of-a-wooden-deck-MvBf0e0mVjw) by Jonathan Ardila

- [The Driftpine](https://unsplash.com/photos/a-stone-house-with-purple-flowers-on-the-side-of-the-road-mc146Wabe9Y) by Benjamin Elliott

  - [Kitchen](https://unsplash.com/photos/green-indoor-plant-near-brown-wooden-table-Ihh0nT34AJs) by Seiji Seiji
  - [Bedroom](https://unsplash.com/photos/white-bed-linen-on-bed-H87P_izw84s) by Ashley Byrd

- [Maplehurst House](https://pixabay.com/photos/eagla-rock-way-montclair-867216/) by WikimediaImages

  - [Room](https://unsplash.com/photos/a-chandelier-hanging-from-a-wooden-ceiling-in-a-library-DAE--I2sJQI) by Daniil Smetanin

- [Heatherwood](https://pixabay.com/photos/farmhouse-woodhouse-house-usa-8482881/) by Tho-Ge

  - [Bathroom](https://pixabay.com/photos/bathroom-toilet-wooden-wood-retro-4787940/) by Engin_Akyurt
  - [Bedroom](https://unsplash.com/photos/empty-bed-beside-closed-window-b-HIPPuBgeM) by Sam McNamara

- [Thistlewood House](https://unsplash.com/photos/old-stone-house-with-four-windows-and-a-dark-door-BNnDVC52Hrg) by Annie Spratt

- [Branwen Cottage](https://unsplash.com/photos/brown-and-white-concrete-house-8NmXsNGwKWE) by Charles Lamb

- [Bramblewood Cottage](https://pixabay.com/photos/cottage-trees-path-trail-house-2955582/) by Stanly8853

  - [Room](https://unsplash.com/photos/a-dining-room-with-a-wooden-table-and-a-chandelier-KLPARZr59Vs) by Clay Banks

- [Trevellan Manor](https://pixabay.com/photos/mansion-england-estate-3431460/) by GregMontani

  - [Bedroom](https://pixabay.com/photos/bedroom-fireplace-double-bedroom-1706801/) by joseclaudioguima

- [Glenhaven](https://unsplash.com/photos/a-house-with-a-large-garden-of-flowers-in-front-of-it-e3Ujhjjr1Fs) by Kevin Krüger

  - [Kitchen](https://pixabay.com/photos/home-interiors-kitchen-2486092/) by user32212

- [Willowbrook House](https://unsplash.com/photos/black-city-bike-parked-beside-white-and-brown-house-during-daytime-4aVF-MMbu_M) by May Gauthier
  - [Kitchen](https://pixabay.com/photos/garlic-cactus-window-green-house-2556022/) by TheVirtualDenise

### Acknowledgements

- I would like to thank my Code Institute mentor, [Tim Nelson](https://www.github.com/TravelTimN) for the support throughout the development of this project.
- I would like to thank the [Code Institute Slack community](https://code-institute-room.slack.com) and [Code Institute Discord community](https://discord-portal.codeinstitute.net) for the moral support; it kept me going during periods of self doubt and impostor syndrome.
