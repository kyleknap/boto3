# Copyright 2015 Amazon.com, Inc. or its affiliates. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License"). You
# may not use this file except in compliance with the License. A copy of
# the License is located at
#
# http://aws.amazon.com/apache2.0/
#
# or in the "license" file accompanying this file. This file is
# distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF
# ANY KIND, either express or implied. See the License for the specific
# language governing permissions and limitations under the License.
import mock
from botocore.compat import six

from tests.unit.docs import BaseDocsTest


class TestResourceDocstrings(BaseDocsTest):
    def test_action_help(self):
        with mock.patch('sys.stdout', six.StringIO()) as mock_stdout:
            help(self.resource.sample_operation)
        action_docstring = mock_stdout.getvalue()
        self.assert_contains_lines_in_order([
            '  **Request Syntax**',
            '  ::',
            '    response = myservice.sample_operation(',
            '        Foo=\'string\',',
            '        Bar=\'string\'',
            '    )',
            '  :type Foo: string',
            '  :param Foo: Documents Foo',
            '  :type Bar: string',
            '  :param Bar: Documents Bar',
            '  :rtype: dict',
            '  :returns:',
            '    **Response Syntax**',
            '    ::',
            '      {',
            '          \'Foo\': \'string\',',
            '          \'Bar\': \'string\'',
            '      }',
            '    **Response Structure**',
            '    - *(dict) --*',
            '      - **Foo** *(string) --* Documents Foo',
            '      - **Bar** *(string) --* Documents Bar'
        ], action_docstring)

    def test_load_help(self):
        sub_resource = self.resource.Sample('Id')
        with mock.patch('sys.stdout', six.StringIO()) as mock_stdout:
            help(sub_resource.load)
        load_docstring = mock_stdout.getvalue()
        self.assert_contains_lines_in_order([
            ('  Calls :py:meth:`MyService.Client.sample_operation` to update '
             'the attributes of the Sample resource'),
            '  **Request Syntax** ',
            '  ::',
            '    sample.load()',
            '  :returns: None',
        ], load_docstring)

    def test_sub_resource_help(self):
        with mock.patch('sys.stdout', six.StringIO()) as mock_stdout:
            help(self.resource.Sample)
        sub_resource_docstring = mock_stdout.getvalue()
        self.assert_contains_lines_in_order([
            '  Creates a Sample resource.::',
            "    sample = myservice.Sample('name')",
            '  :type name: string',
            "  :param name: The Sample's name identifier.",
            '  :rtype: :py:class:`MyService.Sample`',
            '  :returns: A Sample resource',
        ], sub_resource_docstring)

    def test_attribute_help(self):
        with mock.patch('sys.stdout', six.StringIO()) as mock_stdout:
            help(self.resource.Sample('id').__class__.foo)
        attribute_docstring = mock_stdout.getvalue()
        self.assert_contains_lines_in_order([
            '    *(string)* Documents Foo'
        ], attribute_docstring)

    def test_identifier_help(self):
        with mock.patch('sys.stdout', six.StringIO()) as mock_stdout:
            help(self.resource.Sample('id').__class__.name)
        identifier_docstring = mock_stdout.getvalue()
        self.assert_contains_lines_in_order([
            "    *(string)* The Sample's name identifier. This "
            "**must** be set."
        ], identifier_docstring)

    def test_reference_help(self):
        sample_resource = self.resource.Sample('id')
        with mock.patch('sys.stdout', six.StringIO()) as mock_stdout:
            help(sample_resource.__class__.related_sample)
        reference_docstring = mock_stdout.getvalue()
        self.assert_contains_lines_in_order([
            "    (:py:class:`Sample`) The related related_sample "
            "if set, otherwise ``None``."
        ], reference_docstring)
