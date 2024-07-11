import pytest 
from ..models import NewsLetterEmail,Post

"""NEWSLETTEREMAIL"""
@pytest.mark.django_db
class TestNewsLetterEmail():

    def setup_method(self):

        self.email =  NewsLetterEmail.objects.create(
            id=100,
            email="email@proveedor.com",
        )

    def test_attributes(self):

        assert self.email.id    == 100
        assert self.email.email == "email@proveedor.com"

    def test_str(self):

        expected_result = self.email.__str__()

        assert expected_result == "email@proveedor.com"

"""POST"""
@pytest.mark.django_db
class TestPost():

    def setup_method(self):

        self.post =  Post.objects.create(
            id=1000,
            title="Health insurance title",
            content_text = "orem ipsum dolor sit amet, consectetur adipiscing elit. Sed sit amet nibh quis justo tincidunt vulputate. Fusce non dolor pharetra, blandit neque ut, fermentum ex. Ut scelerisque risus et ultricies congue. Duis quis ex dui. Phasellus luctus justo at cursus fringilla. Vestibulum lobortis ipsum vel metus faucibus, pellentesque mollis ligula ornare. Nulla vehicula, nisi eget efficitur ultricies, est nibh finibus elit, et efficitur erat odio sit amet lorem. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae; Curabitur egestas a lacus in molestie. Ut lacinia sed leo id tempus. Suspendisse potenti.",
            content_media = "path/path/file.ext",
        )

    def test_attributes(self):

        assert self.post.id == 1000
        assert self.post.title == "Health insurance title"
        assert self.post.content_text == "orem ipsum dolor sit amet, consectetur adipiscing elit. Sed sit amet nibh quis justo tincidunt vulputate. Fusce non dolor pharetra, blandit neque ut, fermentum ex. Ut scelerisque risus et ultricies congue. Duis quis ex dui. Phasellus luctus justo at cursus fringilla. Vestibulum lobortis ipsum vel metus faucibus, pellentesque mollis ligula ornare. Nulla vehicula, nisi eget efficitur ultricies, est nibh finibus elit, et efficitur erat odio sit amet lorem. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae; Curabitur egestas a lacus in molestie. Ut lacinia sed leo id tempus. Suspendisse potenti."
        assert self.post.content_media == "path/path/file.ext"

    def test_str(self):

        expected_result = self.post.__str__()

        assert expected_result == "Health insurance title"
