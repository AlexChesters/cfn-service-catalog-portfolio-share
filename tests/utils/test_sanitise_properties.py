import unittest

from cfn_service_catalog_portfolio_share.utils.sanitise_properties import sanitise_properties

class SanitisePropertiesTests(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_invalid_accept_language_raises_value_error(self):
        with self.assertRaises(ValueError):
            sanitise_properties({
                "AcceptLanguage": "gb"
            })

    def test_missing_portfolio_id_raises_value_error(self):
        with self.assertRaises(ValueError):
            sanitise_properties({
                "PortfolioId": "abc-123"
            })

    def test_providing_account_id_and_organisation_node_raises_value_error(self):
        with self.assertRaises(ValueError):
            sanitise_properties({
                "PortfolioId": "abc-123",
                "AccountId": "111111111111",
                "OrganizationNode": {
                    "Type": "ORGANIZATION",
                    "Value": "o-abcdef"
                }
            })

    def test_not_providing_account_id_and_organisation_node_raises_value_error(self):
        with self.assertRaises(ValueError):
            sanitise_properties({
                "PortfolioId": "abc-123"
            })

    def test_properties_are_correctly_sanitised(self):
        result = sanitise_properties({
            "PortfolioId": "abc-123",
            "OrganizationNode": {
                "Type": "ORGANIZATION",
                "Value": "o-abcdef"
            },
            "SharePrincipals": "true"
        })
        expected = {
            "PortfolioId": "abc-123",
            "OrganizationNode": {
                "Type": "ORGANIZATION",
                "Value": "o-abcdef"
            },
            "SharePrincipals": True,
            "ShareTagOptions": False
        }

        self.assertEqual(result, expected)
