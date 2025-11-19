from django.test import TestCase
from .forms import CollaborateForm


class TestCollaborateForm(TestCase):

    def test_form_is_valid(self):
        """ Test for all fields"""
        form = CollaborateForm({
            'name': 'Test',
            'email': 'test@test.com',
            'message': 'Hello!'
        })
        self.assertTrue(form.is_valid(), msg="Form is not valid")
    
    def test_form_name_field_is_required(self):
        """ Test for 'name' field"""
        form = CollaborateForm({
            'name': '',
            'email': 'testname@testname.com',
            'message': 'Hello! Name field'
        })
        self.assertFalse(form.is_valid(), msg="Form is valid, but name was not provided.")

    def test_form_email_field_is_required(self):
        """ Test for 'email' field"""
        form = CollaborateForm({
            'name': 'Test Email field',
            'email': '',
            'message': 'Hello! Email field'
        })
        self.assertFalse(form.is_valid(), msg="Form is valid, but email was not provided.")
    
    def test_form_message_field_is_required(self):
        """ Test for 'message' field"""
        form = CollaborateForm({
            'name': 'Test message field',
            'email': 'testmsg@testmsg.com',
            'message': ''
        })
        self.assertFalse(form.is_valid(), msg="Form is valid, but message was not provided.")
