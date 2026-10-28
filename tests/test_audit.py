import unittest
from depsaudit import audit

class RequirementsTests(unittest.TestCase):
    def test_identifies_pinned_unpinned_and_skipped(self):
        findings = audit('requests==2.32.3\nhttpx>=0.27\n-r extra.txt\n# comment\n')
        self.assertEqual(findings, [(2, 'unpinned'), (3, 'unsupported')])

    def test_environment_markers_and_inline_comments(self):
        findings = audit('foo==1.2; python_version < "3.12" # comment\nbar==1.*\n')
        self.assertEqual(findings, [(2, 'unpinned')])

    def test_sensitive_url_is_not_output(self):
        findings = audit('https://user:secret@example.com/pkg.whl\n')
        self.assertEqual(findings, [(1, 'unsupported')])
