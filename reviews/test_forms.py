from django.test import TestCase
from reviews.forms import ReviewForm


class ReviewFormTest(TestCase):

    def test_review_form_is_valid(self):
        """
        Test if review form is valid
        """
        form = ReviewForm(data={
            "rating" : 5,
            "comment": "Great property!"
        })

        self.assertTrue(form.is_valid(), form.errors)

    def test_review_form_is_valid_without_comment(self):
        """
        Test review is valid without comment
        """
        form = ReviewForm(data={
            "rating": 4,
            "comment": ""
        })
        self.assertTrue(form.is_valid(), form.errors)