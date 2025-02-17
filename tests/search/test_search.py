from tests.graph_case import GraphTestCase

class TestSearchOneDrive(GraphTestCase):
    @classmethod
    def setUpClass(cls):
        super(TestSearchOneDrive, cls).setUpClass()

    @classmethod
    def tearDownClass(cls):
        pass

    def test1_search_files(self):
        """
        Test searching for files in OneDrive using the search API.
        """
        result = self.client.search.query_drive_items("Guide.docx").execute_query()
        self.assertIsNotNone(result.value, "Search for 'Guide.docx' returned no results.")
        self.assertGreater(len(result.value), 0, "Search returned no items for 'Guide.docx'.")

    def test2_search_messages(self):
        """
        Test searching for messages in Microsoft Graph.
        """
        result = self.client.search.query_messages("Jon Doe").execute_query()
        self.assertIsNotNone(result.value, "Search for 'Jon Doe' returned no results.")
        self.assertGreater(len(result.value), 0, "Search returned no messages for 'Jon Doe'.")

    def test3_search_events(self):
        """
        Test searching for events in Microsoft Graph.
        """
        result = self.client.search.query_events("Meeting").execute_query()
        self.assertIsNotNone(result.value, "Search for events with 'Meeting' returned no results.")
        self.assertGreater(len(result.value), 0, "Search returned no events for 'Meeting'.")

    def test4_search_files_no_results(self):
        """
        Test searching for files that do not exist to ensure correct behavior.
        """
        result = self.client.search.query_drive_items("NonExistentFile.xyz").execute_query()
        self.assertEqual(len(result.value), 0, "Search for a non-existent file should return no results.")

    def test5_search_messages_no_results(self):
        """
        Test searching for messages with a query that should return no results.
        """
        result = self.client.search.query_messages("NonExistentUser").execute_query()
        self.assertEqual(len(result.value), 0, "Search for messages with 'NonExistentUser' should return no results.")

    def test6_search_events_no_results(self):
        """
        Test searching for events that do not exist.
        """
        result = self.client.search.query_events("NonExistentEvent").execute_query()
        self.assertEqual(len(result.value), 0, "Search for a non-existent event should return no results.")

    def test7_search_multiple_terms(self):
        """
        Test searching for multiple terms (e.g., files containing both 'Guide' and 'docx').
        """
        result = self.client.search.query_drive_items("Guide docx").execute_query()
        self.assertIsNotNone(result.value, "Search for 'Guide docx' returned no results.")
        self.assertGreater(len(result.value), 0, "Search returned no items for 'Guide docx'.")
    
    # You can add more test cases as needed, for example, testing search filters or sorting.

