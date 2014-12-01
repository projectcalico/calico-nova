#    Copyright 2013 IBM Corp.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

import mock

from nova import test
from nova.virt import images


class QemuTestCase(test.NoDBTestCase):
    def test_qemu_info_with_bad_path(self):
        image_info = images.qemu_img_info("/path/that/does/not/exist")
        self.assertTrue(image_info)
        self.assertTrue(str(image_info))


class FetchImagesTestCase(test.NoDBTestCase):

    @mock.patch('nova.image.glance.get_remote_image_service')
    @mock.patch('nova.openstack.common.fileutils.remove_path_on_error')
    def test_fetch(self, mock_fileutils, mock_glance):
        mock_image_service = mock.Mock()
        mock_glance.return_value = [mock_image_service, 'image_id']

        images.fetch('context', None, 'path', None, None)

        mock_image_service.download.assert_called_with(
                'context', 'image_id', dst_path='path')

    @mock.patch('nova.image.glance.get_remote_image_service')
    def test_direct_fetch(self, mock_glance):
        mock_image_service = mock.Mock()
        mock_glance.return_value = [mock_image_service, 'image_id']
        mock_image_service._get_locations.return_value = 'locations'
        mock_image_service.show.return_value = 'image_meta'
        mock_backend = mock.Mock()

        images.direct_fetch('context', 'image_href', mock_backend)

        mock_backend.direct_fetch.assert_called_with(
                'image_id', 'image_meta', 'locations')

    @mock.patch('nova.virt.images.direct_fetch')
    def test_fetch_to_raw_direct_fetch(self, mock_direct_fetch):
        images.fetch_to_raw('context', 'image', None, None, None,
                            backend='backend')
        mock_direct_fetch.assert_called_with('context', 'image', 'backend')
