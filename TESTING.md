# Testing

> [!NOTE]  
> Return back to the [README.md](README.md) file.

## Code Validation

### HTML

I have used the recommended [HTML W3C Validator](https://validator.w3.org) to validate all of my HTML files.

| Directory               | File                                                                                                                          | URL                                                                 | Screenshot                                                                 | Notes                                                                                                                                                                                                               |
| ----------------------- | ----------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------- | -------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Home                    | [index.html](https://github.com/EllisBale/stay_hollow/blob/main/home/templates/home/index.html)                               | [Link](https://stay-hollow-9b3793ea0059.herokuapp.com/)             | ![screenshot](docs/testing_imgs/html_valid/valid_html_home.png)            | No Issues                                                                                                                                                                                                           |
| Listings                | [property_list.html](https://github.com/EllisBale/stay_hollow/blob/main/listings/templates/listings/property_list.html)       | [Link](https://stay-hollow-9b3793ea0059.herokuapp.com/listings/)    | ![screenshot](docs/testing_imgs/html_valid/valid_html_listing.png)         | No Issues                                                                                                                                                                                                           |
| Listing Details         | [property_detail.html](https://github.com/EllisBale/stay_hollow/blob/main/listings/templates/listings/property_detail.html)   | [Link](https://stay-hollow-9b3793ea0059.herokuapp.com/listings/16/) | ![screenshot](docs/testing_imgs/html_valid/valid_html_listing_details.png) | No Issues                                                                                                                                                                                                           |
| Contact                 | [contact.html](https://github.com/EllisBale/stay_hollow/blob/main/home/templates/home/contact.html)                           | [Link](https://stay-hollow-9b3793ea0059.herokuapp.com/contact/)     | ![screenshot](docs/testing_imgs/html_valid/valid_html_contact.png)         | No Issues                                                                                                                                                                                                           |
| About                   | [about.html](https://github.com/EllisBale/stay_hollow/blob/main/home/templates/home/about.html)                               | [Link](https://stay-hollow-9b3793ea0059.herokuapp.com/about/)       | ![screenshot](docs/testing_imgs/html_valid/valid_html_about.png)           | Only one issue with the footer heading structure. I can't change the footer heading because it's in my base.html and it will effect other pages.                                                                    |
| Order History           | [index.html](https://github.com/EllisBale/stay_hollow/blob/main/user_account/templates/user_account/order_history.html)       | No Link                                                             | ![screenshot](docs/testing_imgs/html_valid/valid_html_order_history.png)   | No Issues                                                                                                                                                                                                           |
| Booking Create Date     | [booking.html](https://github.com/EllisBale/stay_hollow/blob/main/bookings/templates/bookings/booking.html)                   | No Link                                                             | ![screenshot](docs/testing_imgs/html_valid/valid_html_booking.png)         | Only one issue with the footer heading structure. I can't change the footer heading because it's in my base.html and it will effect other pages.                                                                    |
| Checkout                | [checkout.html](https://github.com/EllisBale/stay_hollow/blob/main/checkout/templates/checkout/checkout.html)                 | No Link                                                             | ![screenshot](docs/testing_imgs/html_valid/valid_html_checkout.png)        | Only one issue with the footer heading structure. I can't change the footer heading because it's in my base.html and it will effect other pages.                                                                    |
| Checkout Success        | [checkout_success.html](https://github.com/EllisBale/stay_hollow/blob/main/checkout/templates/checkout/checkout_success.html) | No Link                                                             | ![screenshot](docs/testing_imgs/html_valid/valid_html_success.png)         | No Issues                                                                                                                                                                                                           |
| Management              | [management.html](https://github.com/EllisBale/stay_hollow/blob/main/management/templates/management/management.html)         | No Link                                                             | ![screenshot](docs/testing_imgs/html_valid/valid_html_management.png)      | No Issues                                                                                                                                                                                                           |
| Management Listing list | [listings_list.html](https://github.com/EllisBale/stay_hollow/blob/main/management/templates/management/listings_list.html)   | No Link                                                             | ![screenshot](docs/testing_imgs/html_valid/valid_html_manage_listing.png)  | Issue with the footer heading structure. I can't change the footer heading because it's in my base.html and it will effect other pages. I have another issue with the pagination which I tried to fix but couldn't. |
| Management Booking list | [booking_list.html](https://github.com/EllisBale/stay_hollow/blob/main/management/templates/management/booking_list.html)     | No Link                                                             | ![screenshot](docs/testing_imgs/html_valid/valid_html_manage_bookings.png) | Issue with the footer heading structure. I can't change the footer heading because it's in my base.html and it will effect other pages. I have another issue with the pagination which I tried to fix but couldn't. |
| Management User list    | [user_list.html](https://github.com/EllisBale/stay_hollow/blob/main/management/templates/management/user_list.html)           | No Link                                                             | ![screenshot](docs/testing_imgs/html_valid/valid_html_manage_users.png)    | Issue with the footer heading structure. I can't change the footer heading because it's in my base.html and it will effect other pages. I have another issue with the pagination which I tried to fix but couldn't. |
| Management Review list  | [reviews_list.html](https://github.com/EllisBale/stay_hollow/blob/main/management/templates/management/reviews_list.html)     | No Link                                                             | ![screenshot](docs/testing_imgs/html_valid/valid_html_manage_reviews.png)  | Issue with the footer heading structure. I can't change the footer heading because it's in my base.html and it will effect other pages. I have another issue with the pagination which I tried to fix but couldn't. |
| All Manage forms        |                                                                                                                               | No Link                                                             |                                                                            | No Issues on all forms.                                                                                                                                                                                             |

### CSS

I have used the recommended [CSS Jigsaw Validator](https://jigsaw.w3.org/css-validator) to validate all of my CSS files.

| Directory        | File                                                                                                                         | URL                                                                                             | Screenshot                                                      | Notes     |
| ---------------- | ---------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- | --------------------------------------------------------------- | --------- |
| base.css         | [base.css](https://github.com/EllisBale/stay_hollow/blob/main/static/css/base.css)                                           | [Link](https://stay-hollow-9b3793ea0059.herokuapp.com/static/css/base.css)                      | ![screenshot](docs/testing_imgs/css_valid/css_base.png)         | No Issues |
| home.css         | [home.css](https://github.com/EllisBale/stay_hollow/blob/main/home/static/home/css/home.css)                                 | [Link](https://stay-hollow-9b3793ea0059.herokuapp.com/static/home/css/home.css)                 | ![screenshot](docs/testing_imgs/css_valid/css_home.png)         | No Issues |
| listings.css     | [listings.css](https://github.com/EllisBale/stay_hollow/blob/main/listings/static/listings/css/listings.css)                 | [Link](https://stay-hollow-9b3793ea0059.herokuapp.com/static/listings/css/listings.css)         | ![screenshot](docs/testing_imgs/css_valid/css_listing.png)      | No Issues |
| manage.css       | [manage.css](https://github.com/EllisBale/stay_hollow/blob/main/management/static/management/css/manage.css)                 | [Link](https://stay-hollow-9b3793ea0059.herokuapp.com/static/management/css/manage.css)         | ![screenshot](docs/testing_imgs/css_valid/css_manage.png)       | No Issues |
| user_account.css | [user_account.css](https://github.com/EllisBale/stay_hollow/blob/main/user_account/static/user_account/css/user_account.css) | [Link](https://stay-hollow-9b3793ea0059.herokuapp.com/static/user_account/css/user_account.css) | ![screenshot](docs/testing_imgs/css_valid/css_user_account.png) | No Issues |

### JavaScript

I have used the recommended [JShint Validator](https://jshint.com) to validate all of my JS files.

| Directory          | File                                                                                                                    | URL                                                                                          | Screenshot                                                     | Notes     |
| ------------------ | ----------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------- | --------- |
| stripe_elements.js | [stripe_elements.js](https://github.com/EllisBale/stay_hollow/blob/main/checkout/static/checkout/js/stripe_elements.js) | [Link](https://stay-hollow-9b3793ea0059.herokuapp.com/static/checkout/js/stripe_elements.js) | ![screenshot](docs/testing_imgs/js_valid/js_valid_stripe.png)  | No Issues |
| home.js            | [home.js](https://github.com/EllisBale/stay_hollow/blob/main/home/static/home/js/home.js)                               | [Link](https://stay-hollow-9b3793ea0059.herokuapp.com/static/home/js/home.js)                | ![screenshot](docs/testing_imgs/js_valid/js_valid_home.png)    | No Issues |
| listings.js        | [listings.js](https://github.com/EllisBale/stay_hollow/blob/main/listings/static/listings/js/listings.js)               | [Link](https://stay-hollow-9b3793ea0059.herokuapp.com/static/listings/js/listings.js)        | ![screenshot](docs/testing_imgs/js_valid/js_valid_listing.png) | No Issues |
| manage.js          | [manage.js](https://github.com/EllisBale/stay_hollow/blob/main/management/static/management/js/manage.js)               | [Link](https://stay-hollow-9b3793ea0059.herokuapp.com/static/management/js/manage.js)        | ![screenshot](docs/testing_imgs/js_valid/js_valid_manage.png)  | No Issues |
| base.js            | [base.js](https://github.com/EllisBale/stay_hollow/blob/main/static/js/base.js)                                         | [Link](https://stay-hollow-9b3793ea0059.herokuapp.com/static/js/base.js)                     | ![screenshot](docs/testing_imgs/js_valid/js_valid_base.png)    | No Issues |

### Python

⚠️ INSTRUCTIONS ⚠️

The [CI Python Linter](https://pep8ci.herokuapp.com) can be used two different ways.

- Copy/Paste your Python code directly into the linter.
- As an API, using the "raw" URL appended to the linter URL.
  - To find the "raw" URL, navigate to your file directly on the GitHub repo.
  - On that page, GitHub provides a button on the right called "Raw" that you can click.
  - From that new page, copy the full URL, and paste it after the CI Python Linter URL (with a `/` separator).

It's recommended to validate each file using the API URL. This will give you a custom URL which you can use on your testing documentation. It makes it easier to return back to a file for validating it again in the future. Use the steps above to generate your own custom URLs for each Python file.

**IMPORTANT**: `E501 line too long` errors

You must strive to fix all Python lines that are too long (>80 characters). In rare cases where you cannot break the lines [*without breaking the functionality*], adding "`  # noqa`" (_NO Quality Assurance_) to the end of those lines will ignore linting validation. Do not use "`  # noqa`" all over your project just to clear down validation errors! This can still cause a project to fail, for failing to fix actual PEP8 validation errors.

Sometimes variables can get too long, or excessive `if/else` conditional statements. These are acceptable instances to use the "`  # noqa`" comment.

When trying to fix "line too long" errors, try to avoid using `/` to split lines. A better approach would be to use any type of opening bracket, and hit `<Enter>` just after that. Any opening bracket type will work: `(`, `[`, `{`. By using an opening bracket, Python knows where to appropriately indent the next line of code, without having to _guess_ for yourself and attempt to "tab" to the correct indentation level.

⚠️ --- END --- ⚠️

🛑 IMPORTANT 🛑

**IMPORTANT**: Django settings

The Django `settings.py` file comes with 4 lines that are quite long, and will throw the `E501 line too long` error. This is default behavior, but can be fixed by adding the "`  # noqa`" comment at the end of those lines.

```python
AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",  # noqa
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",  # noqa
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",  # noqa
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",  # noqa
    },
]
```

**IMPORTANT**: _migration_ and _pycache_ files

You do not have to validate files from the `migrations/` or `pycache/` folders! Ignore these `.py` files, and validate just the files that you've created or modified.

🛑 --- END --- 🛑

I have used the recommended [PEP8 CI Python Linter](https://pep8ci.herokuapp.com) to validate all of my Python files.

| Directory   | File                                                                                      | URL                                                                                                                               | Screenshot                                                          | Notes                    |
| ----------- | ----------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------ |
| accounts    | [admin.py](https://github.com/EllisBale/stay_hollow/blob/main/accounts/admin.py)          | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/EllisBale/stay_hollow/main/accounts/admin.py)       | ![screenshot](documentation/validation/py-accounts-admin.png)       | ⚠️ Notes (if applicable) |
| accounts    | [models.py](https://github.com/EllisBale/stay_hollow/blob/main/accounts/models.py)        | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/EllisBale/stay_hollow/main/accounts/models.py)      | ![screenshot](documentation/validation/py-accounts-models.png)      | ⚠️ Notes (if applicable) |
| accounts    | [tests.py](https://github.com/EllisBale/stay_hollow/blob/main/accounts/tests.py)          | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/EllisBale/stay_hollow/main/accounts/tests.py)       | ![screenshot](documentation/validation/py-accounts-tests.png)       | ⚠️ Notes (if applicable) |
| accounts    | [views.py](https://github.com/EllisBale/stay_hollow/blob/main/accounts/views.py)          | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/EllisBale/stay_hollow/main/accounts/views.py)       | ![screenshot](documentation/validation/py-accounts-views.png)       | ⚠️ Notes (if applicable) |
| bookings    | [admin.py](https://github.com/EllisBale/stay_hollow/blob/main/bookings/admin.py)          | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/EllisBale/stay_hollow/main/bookings/admin.py)       | ![screenshot](documentation/validation/py-bookings-admin.png)       | ⚠️ Notes (if applicable) |
| bookings    | [models.py](https://github.com/EllisBale/stay_hollow/blob/main/bookings/models.py)        | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/EllisBale/stay_hollow/main/bookings/models.py)      | ![screenshot](documentation/validation/py-bookings-models.png)      | ⚠️ Notes (if applicable) |
| bookings    | [tests.py](https://github.com/EllisBale/stay_hollow/blob/main/bookings/tests.py)          | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/EllisBale/stay_hollow/main/bookings/tests.py)       | ![screenshot](documentation/validation/py-bookings-tests.png)       | ⚠️ Notes (if applicable) |
| bookings    | [views.py](https://github.com/EllisBale/stay_hollow/blob/main/bookings/views.py)          | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/EllisBale/stay_hollow/main/bookings/views.py)       | ![screenshot](documentation/validation/py-bookings-views.png)       | ⚠️ Notes (if applicable) |
| checkout    | [admin.py](https://github.com/EllisBale/stay_hollow/blob/main/checkout/admin.py)          | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/EllisBale/stay_hollow/main/checkout/admin.py)       | ![screenshot](documentation/validation/py-checkout-admin.png)       | ⚠️ Notes (if applicable) |
| checkout    | [models.py](https://github.com/EllisBale/stay_hollow/blob/main/checkout/models.py)        | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/EllisBale/stay_hollow/main/checkout/models.py)      | ![screenshot](documentation/validation/py-checkout-models.png)      | ⚠️ Notes (if applicable) |
| checkout    | [tests.py](https://github.com/EllisBale/stay_hollow/blob/main/checkout/tests.py)          | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/EllisBale/stay_hollow/main/checkout/tests.py)       | ![screenshot](documentation/validation/py-checkout-tests.png)       | ⚠️ Notes (if applicable) |
| checkout    | [views.py](https://github.com/EllisBale/stay_hollow/blob/main/checkout/views.py)          | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/EllisBale/stay_hollow/main/checkout/views.py)       | ![screenshot](documentation/validation/py-checkout-views.png)       | ⚠️ Notes (if applicable) |
| home        | [admin.py](https://github.com/EllisBale/stay_hollow/blob/main/home/admin.py)              | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/EllisBale/stay_hollow/main/home/admin.py)           | ![screenshot](documentation/validation/py-home-admin.png)           | ⚠️ Notes (if applicable) |
| home        | [models.py](https://github.com/EllisBale/stay_hollow/blob/main/home/models.py)            | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/EllisBale/stay_hollow/main/home/models.py)          | ![screenshot](documentation/validation/py-home-models.png)          | ⚠️ Notes (if applicable) |
| home        | [tests.py](https://github.com/EllisBale/stay_hollow/blob/main/home/tests.py)              | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/EllisBale/stay_hollow/main/home/tests.py)           | ![screenshot](documentation/validation/py-home-tests.png)           | ⚠️ Notes (if applicable) |
| home        | [urls.py](https://github.com/EllisBale/stay_hollow/blob/main/home/urls.py)                | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/EllisBale/stay_hollow/main/home/urls.py)            | ![screenshot](documentation/validation/py-home-urls.png)            | ⚠️ Notes (if applicable) |
| home        | [views.py](https://github.com/EllisBale/stay_hollow/blob/main/home/views.py)              | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/EllisBale/stay_hollow/main/home/views.py)           | ![screenshot](documentation/validation/py-home-views.png)           | ⚠️ Notes (if applicable) |
| listings    | [admin.py](https://github.com/EllisBale/stay_hollow/blob/main/listings/admin.py)          | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/EllisBale/stay_hollow/main/listings/admin.py)       | ![screenshot](documentation/validation/py-listings-admin.png)       | ⚠️ Notes (if applicable) |
| listings    | [models.py](https://github.com/EllisBale/stay_hollow/blob/main/listings/models.py)        | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/EllisBale/stay_hollow/main/listings/models.py)      | ![screenshot](documentation/validation/py-listings-models.png)      | ⚠️ Notes (if applicable) |
| listings    | [tests.py](https://github.com/EllisBale/stay_hollow/blob/main/listings/tests.py)          | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/EllisBale/stay_hollow/main/listings/tests.py)       | ![screenshot](documentation/validation/py-listings-tests.png)       | ⚠️ Notes (if applicable) |
| listings    | [views.py](https://github.com/EllisBale/stay_hollow/blob/main/listings/views.py)          | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/EllisBale/stay_hollow/main/listings/views.py)       | ![screenshot](documentation/validation/py-listings-views.png)       | ⚠️ Notes (if applicable) |
|             | [manage.py](https://github.com/EllisBale/stay_hollow/blob/main/manage.py)                 | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/EllisBale/stay_hollow/main/manage.py)               | ![screenshot](documentation/validation/py--manage.png)              | ⚠️ Notes (if applicable) |
| reviews     | [admin.py](https://github.com/EllisBale/stay_hollow/blob/main/reviews/admin.py)           | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/EllisBale/stay_hollow/main/reviews/admin.py)        | ![screenshot](documentation/validation/py-reviews-admin.png)        | ⚠️ Notes (if applicable) |
| reviews     | [models.py](https://github.com/EllisBale/stay_hollow/blob/main/reviews/models.py)         | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/EllisBale/stay_hollow/main/reviews/models.py)       | ![screenshot](documentation/validation/py-reviews-models.png)       | ⚠️ Notes (if applicable) |
| reviews     | [tests.py](https://github.com/EllisBale/stay_hollow/blob/main/reviews/tests.py)           | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/EllisBale/stay_hollow/main/reviews/tests.py)        | ![screenshot](documentation/validation/py-reviews-tests.png)        | ⚠️ Notes (if applicable) |
| reviews     | [views.py](https://github.com/EllisBale/stay_hollow/blob/main/reviews/views.py)           | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/EllisBale/stay_hollow/main/reviews/views.py)        | ![screenshot](documentation/validation/py-reviews-views.png)        | ⚠️ Notes (if applicable) |
| stay_hollow | [settings.py](https://github.com/EllisBale/stay_hollow/blob/main/stay_hollow/settings.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/EllisBale/stay_hollow/main/stay_hollow/settings.py) | ![screenshot](documentation/validation/py-stay_hollow-settings.png) | ⚠️ Notes (if applicable) |
| stay_hollow | [urls.py](https://github.com/EllisBale/stay_hollow/blob/main/stay_hollow/urls.py)         | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/EllisBale/stay_hollow/main/stay_hollow/urls.py)     | ![screenshot](documentation/validation/py-stay_hollow-urls.png)     | ⚠️ Notes (if applicable) |

## Responsiveness

⚠️ INSTRUCTIONS ⚠️

Use this space to discuss testing the live/deployed site on various device sizes.

The minimum requirement is to test the following 3 sizes:

- Mobile
- Tablet
- Desktop

**IMPORTANT**: You must provide screenshots of your results, to "prove" that you've actually tested them.

Using the [amiresponsive](http://ami.responsivedesign.is) mockup images (_or similar_) does not meet the requirements. Consider using some of the built-in device sizes from the Developer Tools.

If you have tested the project on your actual mobile phone or tablet, consider also including screenshots of these as well. It showcases a higher level of manual tests, and can be seen as a positive inclusion!

⚠️ --- END --- ⚠️

I've tested my deployed project to check for responsiveness issues.

| Page             | Mobile                                                                  | Tablet                                                                  | Desktop                                                                  | Notes             |
| ---------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ------------------------------------------------------------------------ | ----------------- |
| Register         | ![screenshot](documentation/responsiveness/mobile-register.png)         | ![screenshot](documentation/responsiveness/tablet-register.png)         | ![screenshot](documentation/responsiveness/desktop-register.png)         | Works as expected |
| Login            | ![screenshot](documentation/responsiveness/mobile-login.png)            | ![screenshot](documentation/responsiveness/tablet-login.png)            | ![screenshot](documentation/responsiveness/desktop-login.png)            | Works as expected |
| Profile          | ![screenshot](documentation/responsiveness/mobile-profile.png)          | ![screenshot](documentation/responsiveness/tablet-profile.png)          | ![screenshot](documentation/responsiveness/desktop-profile.png)          | Works as expected |
| Home             | ![screenshot](documentation/responsiveness/mobile-home.png)             | ![screenshot](documentation/responsiveness/tablet-home.png)             | ![screenshot](documentation/responsiveness/desktop-home.png)             | Works as expected |
| Products         | ![screenshot](documentation/responsiveness/mobile-products.png)         | ![screenshot](documentation/responsiveness/tablet-products.png)         | ![screenshot](documentation/responsiveness/desktop-products.png)         | Works as expected |
| Product Details  | ![screenshot](documentation/responsiveness/mobile-product-details.png)  | ![screenshot](documentation/responsiveness/tablet-product-details.png)  | ![screenshot](documentation/responsiveness/desktop-product-details.png)  | Works as expected |
| Bag              | ![screenshot](documentation/responsiveness/mobile-bag.png)              | ![screenshot](documentation/responsiveness/tablet-bag.png)              | ![screenshot](documentation/responsiveness/desktop-bag.png)              | Works as expected |
| Checkout         | ![screenshot](documentation/responsiveness/mobile-checkout.png)         | ![screenshot](documentation/responsiveness/tablet-checkout.png)         | ![screenshot](documentation/responsiveness/desktop-checkout.png)         | Works as expected |
| Checkout Success | ![screenshot](documentation/responsiveness/mobile-checkout-success.png) | ![screenshot](documentation/responsiveness/tablet-checkout-success.png) | ![screenshot](documentation/responsiveness/desktop-checkout-success.png) | Works as expected |
| Add Product      | ![screenshot](documentation/responsiveness/mobile-add-product.png)      | ![screenshot](documentation/responsiveness/tablet-add-product.png)      | ![screenshot](documentation/responsiveness/desktop-add-product.png)      | Works as expected |
| Edit Product     | ![screenshot](documentation/responsiveness/mobile-edit-product.png)     | ![screenshot](documentation/responsiveness/tablet-edit-product.png)     | ![screenshot](documentation/responsiveness/desktop-edit-product.png)     | Works as expected |
| Newsletter       | ![screenshot](documentation/responsiveness/mobile-newsletter.png)       | ![screenshot](documentation/responsiveness/tablet-newsletter.png)       | ![screenshot](documentation/responsiveness/desktop-newsletter.png)       | Works as expected |
| Contact          | ![screenshot](documentation/responsiveness/mobile-contact.png)          | ![screenshot](documentation/responsiveness/tablet-contact.png)          | ![screenshot](documentation/responsiveness/desktop-contact.png)          | Works as expected |
| 404              | ![screenshot](documentation/responsiveness/mobile-404.png)              | ![screenshot](documentation/responsiveness/tablet-404.png)              | ![screenshot](documentation/responsiveness/desktop-404.png)              | Works as expected |

## Browser Compatibility

⚠️ INSTRUCTIONS ⚠️

Use this space to discuss testing the live/deployed site on various browsers. Consider testing at least 3 different browsers, if available on your system. You DO NOT need to use all of the browsers below, just pick any 3 (minimum).

Recommended browsers to consider:

- [Chrome](https://www.google.com/chrome)
- [Firefox (Developer Edition)](https://www.mozilla.org/firefox/developer)
- [Edge](https://www.microsoft.com/edge)

**IMPORTANT**: You must provide screenshots of the browsers you've tested, to "prove" that you've actually tested them.

Please note, there are services out there that can test multiple browser compatibilities at the same time. Some of these are paid services, but some are free. If you use these, you must provide a link to the source used for attribution, and multiple screenshots of the results.

⚠️ --- END --- ⚠️

I've tested my deployed project on multiple browsers to check for compatibility issues.

| Page             | Chrome                                                            | Firefox                                                            | Safari                                                            | Notes             |
| ---------------- | ----------------------------------------------------------------- | ------------------------------------------------------------------ | ----------------------------------------------------------------- | ----------------- |
| Register         | ![screenshot](documentation/browsers/chrome-register.png)         | ![screenshot](documentation/browsers/firefox-register.png)         | ![screenshot](documentation/browsers/safari-register.png)         | Works as expected |
| Login            | ![screenshot](documentation/browsers/chrome-login.png)            | ![screenshot](documentation/browsers/firefox-login.png)            | ![screenshot](documentation/browsers/safari-login.png)            | Works as expected |
| Profile          | ![screenshot](documentation/browsers/chrome-profile.png)          | ![screenshot](documentation/browsers/firefox-profile.png)          | ![screenshot](documentation/browsers/safari-profile.png)          | Works as expected |
| Home             | ![screenshot](documentation/browsers/chrome-home.png)             | ![screenshot](documentation/browsers/firefox-home.png)             | ![screenshot](documentation/browsers/safari-home.png)             | Works as expected |
| Products         | ![screenshot](documentation/browsers/chrome-products.png)         | ![screenshot](documentation/browsers/firefox-products.png)         | ![screenshot](documentation/browsers/safari-products.png)         | Works as expected |
| Product Details  | ![screenshot](documentation/browsers/chrome-product-details.png)  | ![screenshot](documentation/browsers/firefox-product-details.png)  | ![screenshot](documentation/browsers/safari-product-details.png)  | Works as expected |
| Bag              | ![screenshot](documentation/browsers/chrome-bag.png)              | ![screenshot](documentation/browsers/firefox-bag.png)              | ![screenshot](documentation/browsers/safari-bag.png)              | Works as expected |
| Checkout         | ![screenshot](documentation/browsers/chrome-checkout.png)         | ![screenshot](documentation/browsers/firefox-checkout.png)         | ![screenshot](documentation/browsers/safari-checkout.png)         | Works as expected |
| Checkout Success | ![screenshot](documentation/browsers/chrome-checkout-success.png) | ![screenshot](documentation/browsers/firefox-checkout-success.png) | ![screenshot](documentation/browsers/safari-checkout-success.png) | Works as expected |
| Add Product      | ![screenshot](documentation/browsers/chrome-add-product.png)      | ![screenshot](documentation/browsers/firefox-add-product.png)      | ![screenshot](documentation/browsers/safari-add-product.png)      | Works as expected |
| Edit Product     | ![screenshot](documentation/browsers/chrome-edit-product.png)     | ![screenshot](documentation/browsers/firefox-edit-product.png)     | ![screenshot](documentation/browsers/safari-edit-product.png)     | Works as expected |
| Newsletter       | ![screenshot](documentation/browsers/chrome-newsletter.png)       | ![screenshot](documentation/browsers/firefox-newsletter.png)       | ![screenshot](documentation/browsers/safari-newsletter.png)       | Works as expected |
| Contact          | ![screenshot](documentation/browsers/chrome-contact.png)          | ![screenshot](documentation/browsers/firefox-contact.png)          | ![screenshot](documentation/browsers/safari-contact.png)          | Works as expected |
| 404              | ![screenshot](documentation/browsers/chrome-404.png)              | ![screenshot](documentation/browsers/firefox-404.png)              | ![screenshot](documentation/browsers/safari-404.png)              | Works as expected |

## Lighthouse Audit

⚠️ INSTRUCTIONS ⚠️

Use this space to discuss testing the live/deployed site's Lighthouse Audit reports. Avoid testing the local version (Gitpod/VSCode/etc.), as this can have knock-on effects for performance. If you don't have "Lighthouse" in your Developer Tools, it can be added as an [extension](https://chrome.google.com/webstore/detail/lighthouse/blipmdconlkpinefehnmjammfjpmpbjk).

Unless your project is a single-page application (SPA), you should test Lighthouse Audit results for all of your pages, for both _mobile_ and _desktop_.

**IMPORTANT**: You must provide screenshots of the results, to "prove" that you've actually tested them.

⚠️ --- END --- ⚠️

I've tested my deployed project using the Lighthouse Audit tool to check for any major issues. Some warnings are outside of my control, and mobile results tend to be lower than desktop.

| Page             | Mobile                                                              | Desktop                                                              |
| ---------------- | ------------------------------------------------------------------- | -------------------------------------------------------------------- |
| Register         | ![screenshot](documentation/lighthouse/mobile-register.png)         | ![screenshot](documentation/lighthouse/desktop-register.png)         |
| Login            | ![screenshot](documentation/lighthouse/mobile-login.png)            | ![screenshot](documentation/lighthouse/desktop-login.png)            |
| Profile          | ![screenshot](documentation/lighthouse/mobile-profile.png)          | ![screenshot](documentation/lighthouse/desktop-profile.png)          |
| Home             | ![screenshot](documentation/lighthouse/mobile-home.png)             | ![screenshot](documentation/lighthouse/desktop-home.png)             |
| Products         | ![screenshot](documentation/lighthouse/mobile-products.png)         | ![screenshot](documentation/lighthouse/desktop-products.png)         |
| Product Details  | ![screenshot](documentation/lighthouse/mobile-product-details.png)  | ![screenshot](documentation/lighthouse/desktop-product-details.png)  |
| Bag              | ![screenshot](documentation/lighthouse/mobile-bag.png)              | ![screenshot](documentation/lighthouse/desktop-bag.png)              |
| Checkout         | ![screenshot](documentation/lighthouse/mobile-checkout.png)         | ![screenshot](documentation/lighthouse/desktop-checkout.png)         |
| Checkout Success | ![screenshot](documentation/lighthouse/mobile-checkout-success.png) | ![screenshot](documentation/lighthouse/desktop-checkout-success.png) |
| Add Product      | ![screenshot](documentation/lighthouse/mobile-add-product.png)      | ![screenshot](documentation/lighthouse/desktop-add-product.png)      |
| Edit Product     | ![screenshot](documentation/lighthouse/mobile-edit-product.png)     | ![screenshot](documentation/lighthouse/desktop-edit-product.png)     |
| Newsletter       | ![screenshot](documentation/lighthouse/mobile-newsletter.png)       | ![screenshot](documentation/lighthouse/desktop-newsletter.png)       |
| Contact          | ![screenshot](documentation/lighthouse/mobile-contact.png)          | ![screenshot](documentation/lighthouse/desktop-contact.png)          |
| 404              | ![screenshot](documentation/lighthouse/mobile-404.png)              | ![screenshot](documentation/lighthouse/desktop-404.png)              |

## Defensive Programming

Defensive programming was manually tested with the below user acceptance testing:

| Page/Feature        | Expectation                                                                                                                                   | Test                                                                                                                                                                                                                   | Result                                                                                                                                | Screenshot                                                    |
| ------------------- | --------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------- |
| Booking Date        | Feature is expected to allow logged-in users to pick a date.                                                                                  | Click the "Book Now" button on listing details page and pick guests, check-in, and check-out date.                                                                                                                     | Logged-in users can select dates and guests successfully and proceed to checkout page if the dates are available.                     | ![screenshot](documentation/defensive/products.png)           |
|                     | Feature is expected to redirect guest users to the login page.                                                                                | Go to listing details page as a guest user and click "Book Now".                                                                                                                                                       | Guest users get redirected to login page successfully.                                                                                | ![screenshot](documentation/defensive/sorting.png)            |
|                     | Feature is expected show error message for already booked dates.                                                                              | Book a date that has already been booked.                                                                                                                                                                              | Error message appears successfully and remains on the booking date page.                                                              | ![screenshot](documentation/defensive/filtering.png)          |
| Checkout            | Feature is expected to allow logged-in users that have picked a valid date to fill in checkout information and proceed onto checkout success. | Fill in all form information to proceed onto checkout success page.                                                                                                                                                    | Users can proceed to checkout success page successfully when all information is entered.                                              | ![screenshot](documentation/defensive/add-to-cart.png)        |
|                     | Feature is expected to restrict checkout to booking owner only.                                                                               | Have multiple logged-in accounts in the browser (Make sure one account is in incognito). Get to the checkout page on one of the accounts and copy the URL onto the other account.                                      | The user gets redirect to a 404 page successfully.                                                                                    | ![screenshot](documentation/defensive/manage-cart.png)        |
|                     | Feature is expected to only proceed once all required payment information is entered.                                                         | Fill in each required form field one by one and complete payment after form field is filled.                                                                                                                           | The form will alert the user for required form fields to be filled in if left empty.                                                  | ![screenshot](documentation/defensive/checkout.png)           |
|                     | Feature is expected to send a confirmation email after purchase.                                                                              | Completed a purchase and checked email inbox.                                                                                                                                                                          | Confirmation email was received with order details.                                                                                   | ![screenshot](documentation/defensive/confirmation-email.png) |
| Searchbar           | Feature is expected to allow users to search property names.                                                                                  | Go to homepage or listing page and search for a property name.                                                                                                                                                         | Users can see relevant property results based on search.                                                                              | ![screenshot](documentation/defensive/order-history.png)      |
|                     | Feature is expected to allow users to search location name.                                                                                   | Go to homepage or listing page and search for an existing location. names.                                                                                                                                             | Users can see relevant location results based on search.                                                                              | ![screenshot](documentation/defensive/order-history.png)      |
|                     | Feature is expected to allow users to search property description keyword.                                                                    | Go to homepage or listing page and search for a word from a property description keywords.                                                                                                                             | Users can see relevant results based on description keywords.                                                                         | ![screenshot](documentation/defensive/order-history.png)      |
| Sortby              | Feature is expected to allow users to filter properties by low to high price, high to low, and newest.                                        | Go to the listing page and click "Sort By" button to filter properties.                                                                                                                                                | Properties where filtered as expected.                                                                                                | ![screenshot](documentation/defensive/order-history.png)      |
| Reviews             | Feature is expected to allow users to review properties that have been booked by them.                                                        | Book a property and checkout, then go to the property that has been booked and add review. Fill in required form information and click "Complete Review" button.                                                       | Review works as expected.                                                                                                             | ![screenshot](documentation/defensive/order-history.png)      |
|                     | Feature is expected to prevent users from reviewing again on the same property.                                                               | After adding a review, try and add another review to the same property.                                                                                                                                                | Users can't add another review as expected.                                                                                           | ![screenshot](documentation/defensive/order-history.png)      |
|                     | Feature is expected to prevent users from adding reviews to properties they haven't booked.                                                   | Go to a property listing that you haven't booked and try to add a review.                                                                                                                                              | Users can't add review as expected.                                                                                                   | ![screenshot](documentation/defensive/order-history.png)      |
| Pagination          | Feature is expected to load 12 properties per page and provide navigation for additional pages.                                               | Navigate to the listings page and verify that exactly 12 properties are displayed.                                                                                                                                     | The first page loads with exactly 12 properties, and users can navigate to the next page through the arrows or numbers on pagination. | ![screenshot](documentation/defensive/order-history.png)      |
| Account Management  | Feature is expected to allow returning customers to log in and view past orders.                                                              | Logged in as a returning customer and accessed order history.                                                                                                                                                          | Past orders were displayed correctly on the account page.                                                                             | ![screenshot](documentation/defensive/order-history.png)      |
| User Management     | Feature is expected to allow staff/admin to Edit users.                                                                                       | Log in as a staff/admin member, then click the "Edit" button on the User List Management page. Change any of the information of the user and click "Save Changes" button.                                              | User updated successfully.                                                                                                            | ![screenshot](documentation/defensive/create-product.png)     |
|                     | Feature is expected to allow staff/admin to delete users.                                                                                     | Log in as an admin account and remove user by clicking "Delete" button.                                                                                                                                                | User deleted successfully.                                                                                                            | ![screenshot](documentation/defensive/update-product.png)     |
|                     | Feature is expected to prevent staff users from deleting or editing superusers.                                                               | Log in as a staff user and edit and delete super user.                                                                                                                                                                 | Staff users can't edit or delete super users.                                                                                         | ![screenshot](documentation/defensive/delete-product.png)     |
| Listings Management | Feature is expected to allow staff/admin users to add properties.                                                                             | Log in as a staff/admin member, then click the "add property" button to open the add property form on the Listings Management page. Fill in the required information on the form, then click "create Property" button. | Staff/Admin users can add properties successfully.                                                                                    | ![screenshot](documentation/defensive/view-orders.png)        |
|                     | Feature is expected to allow staff/admin users to edit a property.                                                                            | Log in as staff/admin, then click "Edit" button to open update property form on the Listing Mangement page. Edit the information in the form and click "Save Changes" button.                                          | Staff/Admin can successfully edit properties.                                                                                         | ![screenshot](documentation/defensive/newsletter.png)         |
|                     | Feature is expected to allow staff/admin to delete properties.                                                                                | Log in as staff/admin and click the "delete" button on the Listings Management page.                                                                                                                                   | Staff/Admin can successfully delete property.                                                                                         | ![screenshot](documentation/defensive/404.png)                |
| Booking Management  | Feature is expected to allow staff/admin users to edit booking.                                                                               | Log in as a staff member, then click the "Edit" button to open update booking form on the Booking Management page. Edit the information in the form and click "save Changes" button.                                   | Staff/Admin can edit bookings successfully.                                                                                           | ![screenshot](documentation/defensive/404.png)                |
|                     | Feature is expected to allow staff/admin to delete bookings.                                                                                  | Log in as staff/admin and click the "delete" button on the Booking Management page.                                                                                                                                    | Staff/Admin can successfully delete booking.                                                                                          | ![screenshot](documentation/defensive/404.png)                |
| Review Management   | Feature is expected to allow staff/admin users to delete reviews.                                                                             | Log in as staff/admin and click the "delete" button on the Reviews Management page.                                                                                                                                    | Staff/Admin can successfully delete review.                                                                                           | ![screenshot](documentation/defensive/404.png)                |
| Authentication      | Users should be able to register an account.                                                                                                  | Go to register page and make an account, then verify email.                                                                                                                                                            | Registration was successful and user has to log in.                                                                                   | ![screenshot](documentation/defensive/404.png)                |
|                     | Feature is expected to allow users to log in securely.                                                                                        | Log in with valid credentials.                                                                                                                                                                                         | Login was successful.                                                                                                                 | ![screenshot](documentation/defensive/404.png)                |
|                     | Feature is expected to allow users to be able to logout securely.                                                                             | Logged out after login and try to access pages that require account sign in.                                                                                                                                           | User has to login to access these pages as expected.                                                                                  | ![screenshot](documentation/defensive/404.png)                |
| Security            | Feature is expected to redirect non-admin users to home page when they attempt access admin pages.                                            | Log in as a user and try to access all admin pages by copying URL.                                                                                                                                                     | Users are redirected to home page as expected.                                                                                        | ![screenshot](documentation/defensive/404.png)                |
| 404 Error Page      | Feature is expected to display a 404 error page for non-existent pages.                                                                       | Navigated to an invalid URL (e.g., `/test`).                                                                                                                                                                           | A custom 404 error page was displayed as expected.                                                                                    | ![screenshot](documentation/defensive/404.png)                |

## User Story Testing

| Target               | Expectation                                                                    | Outcome                                                                    | Screenshot                                          |
| -------------------- | ------------------------------------------------------------------------------ | -------------------------------------------------------------------------- | --------------------------------------------------- |
| As a Logged-in user  | I want to book a holiday property for specific dates,                          | so I can secure my stay and complete my reservation online.                | ![screenshot](documentation/features/feature01.png) |
| As a Logged-in user, | I want to view an order booking confirmation after checkout.                   | so I can verify that my payment and booking were successful.               | ![screenshot](documentation/features/feature02.png) |
| As a Logged-in user, | I want to make secure online payments for my bookings                          | so my financial details are protected.                                     | ![screenshot](documentation/features/feature03.png) |
| As a Logged-in user, | I want to be able to receive a confirmation through email after checkout       | so I have a confirmation for my records.                                   | ![screenshot](documentation/features/feature04.png) |
| As a Site User,      | I want to search for properties directly from the homepage                     | so I can start finding places immediately.                                 | ![screenshot](documentation/features/feature05.png) |
| As a Site User,      | I want to be able to browse all available holiday properties                   | so I can explore my options.                                               | ![screenshot](documentation/features/feature06.png) |
| As a Site User,      | I want to view detailed property pages with photos, descriptions and amenities | so I can make an informed choice.                                          | ![screenshot](documentation/features/feature07.png) |
| As a Site User,      | I want to filter properties by location, price and number of guests            | so I can find suitable accommodation.                                      | ![screenshot](documentation/features/feature08.png) |
| As a Site User,      | I want to create an account and log in                                         | so I can manage bookings and preferences.                                  | ![screenshot](documentation/features/feature09.png) |
| As a Site User,      | I want to see featured or popular properties on the landing page,              | so I can quickly explore attractive options.                               | ![screenshot](documentation/features/feature10.png) |
| As a Site User,      | I want to be able to see reviews and ratings for each property,                | so that I can decide where to stay.                                        | ![screenshot](documentation/features/feature11.png) |
| As a Site User,      | I want to see reasons to book on this website and what the benefits are,       | so that I can be assured that using this website to book will be worth it. | ![screenshot](documentation/features/feature12.png) |
| As a Site User,      | I want to see footer details like contact info, social links, and copyright,   | so I can learn more about the company.                                     | ![screenshot](documentation/features/feature13.png) |
| As a Site User,      | I want to see a list of popular destinations on the homepage                   | so I can quickly discover places that are trending or highly recommended.  | ![screenshot](documentation/features/feature14.png) |
| As an Admin,         | I want to add, edit, or remove property listings                               | so I can control what’s shown on the website.                              | ![screenshot](documentation/features/feature15.png) |
| As an Admin,         | I want to view and manage user accounts                                        | so I can assist customers when needed.                                     | ![screenshot](documentation/features/feature16.png) |
| As an Admin,         | I want to moderate or remove inappropriate reviews,                            | so that I can maintain the platform’s reputation.                          | ![screenshot](documentation/features/feature17.png) |
| As an Admin,         | I want to view and manage user bookings                                        | so I can assist customers when needed.                                     | ![screenshot](documentation/features/feature18.png) |

## Automated Testing

I have conducted a series of automated tests on my application.

> [!NOTE]  
> I fully acknowledge and understand that, in a real-world scenario, an extensive set of additional tests would be more comprehensive.

### Python (Unit Testing)

⚠️ INSTRUCTIONS ⚠️

Adjust the code below (file names, function names, etc.) to match your own project files/folders. Use these notes loosely when documenting your own Python Unit tests, and remove/adjust where applicable.

⚠️ SAMPLE ⚠️

I have used Django's built-in unit testing framework to test the application functionality. In order to run the tests, I ran the following command in the terminal each time:

- `python3 manage.py test name-of-app`

To create the coverage report, I would then run the following commands:

- `pip3 install coverage`
- `pip3 freeze --local > requirements.txt`
- `coverage run --omit="*/site-packages/*,*/migrations/*,*/__init__.py,env.py,.env" manage.py test`
- `coverage report`

To see the HTML version of the reports, and find out whether some pieces of code were missing, I ran the following commands:

- `coverage html`
- `python3 -m http.server`

Below are the results from the full coverage report on my application that I've tested:

![screenshot](documentation/automation/html-coverage.png)

#### Unit Test Issues

⚠️ INSTRUCTIONS ⚠️

Use this section to list any known issues you ran into while writing your Python unit tests. Remember to include screenshots (where possible), and a solution to the issue (if known). This can be used for both "fixed" and "unresolved" issues. Remove this sub-section entirely if you somehow didn't run into any issues while working with your tests.

⚠️ --- END --- ⚠️

## Bugs

⚠️ INSTRUCTIONS ⚠️

Nobody likes bugs,... except the assessors! Projects seem more suspicious if a student doesn't properly track their bugs. If you're about to submit your project without any bugs listed below, you should ask yourself why you're doing this course in the first place, if you're able to build this entire application without running into any bugs. The best thing you can do for any project is to document your bugs! Not only does it show the true stages of development, but think of it as breadcrumbs for yourself in the future, should you encounter the same/similar bug again, it acts as a gentle reminder on what you did to fix the bug.

If/when you encounter bugs during the development stages of your project, you should document them here, ideally with a screenshot explaining what the issue was, and what you did to fix the bug.

Alternatively, an improved way to manage bugs is to use the built-in **[Issues](https://www.github.com/EllisBale/stay_hollow/issues)** tracker on your GitHub repository. This can be found at the top of your repository, the tab called "Issues".

If using the Issues tracker for bug management, you can simplify the documentation process for testing. Issues allow you to directly paste screenshots into the issue page without having to first save the screenshot locally. You can add labels to your issues (e.g. `bug`), assign yourself as the owner, and add comments/updates as you progress with fixing the issue(s). Once you've solved the issue/bug, you should then "Close" it.

When showcasing your bug tracking for assessment, you can use the following examples below.

⚠️ --- END --- ⚠️

### Fixed Bugs

[![GitHub issue custom search](https://img.shields.io/github/issues-search/EllisBale/stay_hollow?query=is%3Aissue%20is%3Aclosed%20label%3Abug&label=Fixed%20Bugs&color=green)](https://www.github.com/EllisBale/stay_hollow/issues?q=is%3Aissue+is%3Aclosed+label%3Abug)

I've used [GitHub Issues](https://www.github.com/EllisBale/stay_hollow/issues) to track and manage bugs and issues during the development stages of my project.

All previously closed/fixed bugs can be tracked [here](https://www.github.com/EllisBale/stay_hollow/issues?q=is%3Aissue+is%3Aclosed+label%3Abug).

![screenshot](documentation/bugs/gh-issues-closed.png)

### Unfixed Bugs

⚠️ INSTRUCTIONS ⚠️

You will need to mention any unfixed bugs and why they are not fixed upon submission of your project. This section should include shortcomings of the frameworks or technologies used. Although time can be a big variable to consider, paucity of time and difficulty understanding implementation is not a valid reason to leave bugs unfixed. Where possible, you must fix all outstanding bugs, unless outside of your control.

If you've identified any unfixed bugs, no matter how small, be sure to list them here! It's better to be honest and list them, because if it's not documented and an assessor finds the issue, they need to know whether or not you're aware of them as well, and why you've not corrected/fixed them.

⚠️ --- END --- ⚠️

[![GitHub issue custom search](https://img.shields.io/github/issues-search/EllisBale/stay_hollow?query=is%3Aissue%2Bis%3Aopen%2Blabel%3Abug&label=Unfixed%20Bugs&color=red)](https://www.github.com/EllisBale/stay_hollow/issues?q=is%3Aissue+is%3Aopen+label%3Abug)

Any remaining open issues can be tracked [here](https://www.github.com/EllisBale/stay_hollow/issues?q=is%3Aissue+is%3Aopen+label%3Abug).

![screenshot](documentation/bugs/gh-issues-open.png)

### Known Issues

| Issue                                                                                                                                                                                                                                                                                                                                                               | Screenshot                                                  |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------- |
| The project is designed to be responsive from `375px` and upwards, in line with the material taught on the course LMS. Minor layout inconsistencies may occur on extra-wide (e.g. 4k/8k monitors), or smart-display devices (e.g. Nest Hub, Smart Watches, Gameboy Color, etc.), as these resolutions are outside the project’s scope, as taught by Code Institute. | ![screenshot](documentation/issues/poor-responsiveness.png) |
| When validating HTML with a semantic `<section>` element, the validator warns about lacking a header `h2-h6`. This is acceptable.                                                                                                                                                                                                                                   | ![screenshot](documentation/issues/section-header.png)      |
| Validation errors on "signup.html" coming from the Django Allauth package.                                                                                                                                                                                                                                                                                          | ![screenshot](documentation/issues/allauth.png)             |
| With a known order-number, users can brute-force "checkout_success.html" and see potentially sensitive information.                                                                                                                                                                                                                                                 | ![screenshot](documentation/issues/checkout-success.png)    |
| If a product is in your bag/cart, but then gets deleted from the database, it throws errors from the session storage memory.                                                                                                                                                                                                                                        | ![screenshot](documentation/issues/session-storage.png)     |
| The `-`/`+` quantity buttons work well on "product_details.html", but not on "bag.html".                                                                                                                                                                                                                                                                            | ![screenshot](documentation/issues/quantity-buttons.png)    |

> [!IMPORTANT]  
> There are no remaining bugs that I am aware of, though, even after thorough testing, I cannot rule out the possibility.
