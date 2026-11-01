import unittest
from pathlib import Path
from tempfile import TemporaryDirectory
from validate_research import Document, local_link_exists, validate_source_ids

class PublicationTests(unittest.TestCase):
    def test_duplicate_sources_rejected(self):
        self.assertFalse(validate_source_ids([{'id':'S01'},{'id':'S01'}]))
        self.assertTrue(validate_source_ids([{'id':'S01'},{'id':'S02'}]))
    def test_invalid_source_id(self):
        self.assertFalse(validate_source_ids([{'id':'source'}]))
    def test_missing_links(self):
        with TemporaryDirectory() as d:
            root=Path(d);(root/'file.md').write_text('x')
            self.assertTrue(local_link_exists(root,'file.md#section',root))
            self.assertFalse(local_link_exists(root,'missing.md',root))
    def test_links_cannot_escape_root(self):
        with TemporaryDirectory() as d:
            root=Path(d)
            self.assertFalse(local_link_exists(root,'../',root))
    def test_url_and_fragment(self):
        root=Path.cwd()
        self.assertTrue(local_link_exists(root,'https://example.org/a',root))
        self.assertTrue(local_link_exists(root,'#section',root))
    def test_html_assets_and_anchor_collection(self):
        doc=Document();doc.feed('<h1 id="a">A</h1><a href="#a">go</a><script src="bad.js"></script>')
        self.assertEqual(doc.ids,['a']);self.assertEqual(doc.links,['#a'])
        self.assertEqual(len(doc.assets),1)
