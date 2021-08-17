# Licensed under the MIT License
# https://github.com/craigahobbs/python-build/blob/main/LICENSE

# pylint: disable=missing-class-docstring, missing-function-docstring, missing-module-docstring

import filecmp
import os
import shutil
import subprocess
import unittest
import unittest.mock


class PythonPackageTemplateTest(unittest.TestCase):

    def assert_dcmp(self, dcmp):
        self.assertListEqual(dcmp.diff_files, [])
        self.assertListEqual(dcmp.left_only, [])
        self.assertListEqual(dcmp.right_only, [])
        for subdir_dcmp in dcmp.subdirs.values():
            self.assert_dcmp(subdir_dcmp)

    def test_required(self):

        # Ensure the actual directory is non-existent
        expected_dir = os.path.join('test_expected', 'test_required')
        actual_root = 'test_actual'
        actual_dir = os.path.join(actual_root, 'test_required')
        if os.path.exists(actual_dir):
            shutil.rmtree(actual_root)

        # Render the template
        output = subprocess.check_output(
            [
                'build/venv/bin/template-specialize', 'template/', actual_dir,
                '-k', 'package', 'package-name',
                '-k', 'name', 'John Doe',
                '-k', 'email', 'johndoe@gmail.com',
                '-k', 'github', 'johndoe'
            ],
            env={},
            stderr=subprocess.STDOUT,
            encoding='utf-8'
        )
        self.assertEqual(output, '')

        # Compare the rendered template to the expected
        self.assert_dcmp(filecmp.dircmp(expected_dir, actual_dir))

        # Run "make commit" on rendered template
        actual_make = subprocess.check_output(
            ['make', '-C', actual_dir, 'commit'],
            env={'PATH': os.getenv('PATH')},
            stderr=subprocess.STDOUT,
            encoding='utf-8'
        )
        self.assertNotEqual(actual_make, '')

        # Delete the actual directory
        shutil.rmtree(actual_root)
