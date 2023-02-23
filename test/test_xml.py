import pytest
from xmlunittest import XmlTestCase


class CustomTestCase(XmlTestCase):

    def test_good_xml(self):
        fc = open('good.xsd')
        data = fc.read().encode()
        root = self.assertXmlDocument(data)

    def test_bad_xml(self):
        fc = open('bad.xsd')
        data = fc.read().encode()
        with pytest.raises(AssertionError):
            self.assertXmlDocument(data)

