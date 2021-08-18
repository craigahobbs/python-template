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

    LEFT_ONLY_EXCLUDE = ['.coverage', '.docker', 'Makefile.base', 'build', 'pylintrc']
    LEFT_ONLY_EXCLUDE_EXT = ['.egg-info']

    def assert_dcmp(self, dcmp):
        self.assertListEqual(dcmp.diff_files, [])
        self.assertListEqual(
            [
                file_ for file_ in dcmp.left_only if
                (file_ not in self.LEFT_ONLY_EXCLUDE and
                 not any(file_.endswith(ext) for ext in self.LEFT_ONLY_EXCLUDE_EXT))
            ],
            []
        )
        self.assertListEqual(dcmp.right_only, [])
        for subdir_dcmp in dcmp.subdirs.values():
            self.assert_dcmp(subdir_dcmp)

    def _test_template(self, test_name, template_args):

        # Ensure the actual directory is non-existent
        expected_dir = os.path.join('test_expected', test_name)
        actual_dir = os.path.join('test_actual', test_name)
        if os.path.exists(actual_dir):
            shutil.rmtree(actual_dir)

        # Render the template
        render_output = subprocess.check_output(
            ['build/venv/bin/template-specialize', 'template/', actual_dir, *template_args],
            env={},
            stderr=subprocess.STDOUT,
            encoding='utf-8'
        )
        self.assertEqual(render_output, '')

        # Compare the rendered template to the expected
        self.assert_dcmp(filecmp.dircmp(expected_dir, actual_dir))

        # Run "make commit" on rendered template
        compile_output = subprocess.check_output(
            ['make', '-C', expected_dir, 'commit'],
            env={'PATH': os.getenv('PATH')},
            stderr=subprocess.STDOUT,
            encoding='utf-8'
        )
        self.assertNotEqual(compile_output, '')

        # Delete the actual directory
        shutil.rmtree(actual_dir)

    def test_required(self):
        self._test_template(
            'test_required',
            [
                '-k', 'package', 'package-name',
                '-k', 'name', 'John Doe',
                '-k', 'email', 'johndoe@gmail.com',
                '-k', 'github', 'johndoe'
            ]
        )

    def test_nodoc(self):
        self._test_template(
            'test_nodoc',
            [
                '-k', 'package', 'package-name',
                '-k', 'name', 'John Doe',
                '-k', 'email', 'johndoe@gmail.com',
                '-k', 'github', 'johndoe',
                '-k', 'nodoc', '1'
            ]
        )

    def test_nomain(self):
        self._test_template(
            'test_nomain',
            [
                '-k', 'package', 'package-name',
                '-k', 'name', 'John Doe',
                '-k', 'email', 'johndoe@gmail.com',
                '-k', 'github', 'johndoe',
                '-k', 'nomain', '1'
            ]
        )

    def test_nodoc_nomain(self):
        self._test_template(
            'test_nodoc_nomain',
            [
                '-k', 'package', 'package-name',
                '-k', 'name', 'John Doe',
                '-k', 'email', 'johndoe@gmail.com',
                '-k', 'github', 'johndoe',
                '-k', 'nodoc', '1',
                '-k', 'nomain', '1'
            ]
        )

    def test_nodoc_0_nomain_0(self):
        self._test_template(
            'test_nodoc_0_nomain_0',
            [
                '-k', 'package', 'package-name',
                '-k', 'name', 'John Doe',
                '-k', 'email', 'johndoe@gmail.com',
                '-k', 'github', 'johndoe',
                '-k', 'nodoc', '0',
                '-k', 'nomain', '0'
            ]
        )
