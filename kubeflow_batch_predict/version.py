# Copyright 2018 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Kubeflow Batch Predict version constants.
"""

# Google Cloud Machine Learning Prediction Engine Version info.
__version__ = '0.1-alpha'

required_install_packages = [
    'oauth2client >= 2.2.0',
    'six == 1.10.0',
    'bs4 >= 0.0.1, < 1.0',
    'numpy >= 1.10.4',  # Don't pin numpy, as it requires a recompile.
    'crcmod >= 1.7, < 2.0',
    'nltk >= 3.2.1, < 4.0',
    'pyyaml >= 3.11, < 4.0',
    'protobuf >= 3.1.0, < 4.0',
    'enum34 >= 1.1',
    'tensorflow >= 1.0.0',
]

required_install_packages_with_batch_prediction = required_install_packages + [
    'apache-beam[gcp] >= 2.5.0',
]

