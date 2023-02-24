from xmlunittest import XmlTestCase


class CustomTestCase(XmlTestCase):

    def test_my_custom_test(self):
        # In a real case, data come from a call to your function/method.
        data = """<?xml version="1.0" encoding="UTF-8" ?>
        <root xmlns:ns="uri">
            <leaf id="1" active="on" />
            <leaf id="2" active="on" />
            <leaf id="3" active="off" />
        </root>"""

        # Everything starts with `assertXmlDocument`
        root = self.assertXmlDocument(data.encode())

        # Check namespace
        self.assertXmlNamespace(root, 'ns', 'uri')
        # Check
        self.assertXpathsUniqueValue(root, ('./leaf/@id', ))
        self.assertXpathValues(root, './leaf/@active', ('on', 'off'))
