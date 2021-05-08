# coding=utf-8
# Copyright 2021 The TensorFlow Datasets Authors.
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

"""schema_guided_dialogue dataset."""

import tensorflow_datasets.public_api as tfds
from tensorflow_datasets.text.schema_guided_dialogue import schema_guided_dialogue


class SchemaGuidedDialogueTest(tfds.testing.DatasetBuilderTestCase):
  """Tests for schema_guided_dialogue dataset."""
  DATASET_CLASS = schema_guided_dialogue.SchemaGuidedDialogue
  SPLITS = {
      'train': 3,  # Number of fake train example
      'dev': 2,  # Number of fake train example
      'test': 1,  # Number of fake test example
  }

if __name__ == '__main__':
  tfds.testing.test_main()
