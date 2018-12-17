# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: object_detection/protos/losses.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='object_detection/protos/losses.proto',
  package='protos',
  syntax='proto2',
  serialized_pb=_b('\n$object_detection/protos/losses.proto\x12\x06protos\"\xec\x01\n\x04Loss\x12\x33\n\x11localization_loss\x18\x01 \x01(\x0b\x32\x18.protos.LocalizationLoss\x12\x37\n\x13\x63lassification_loss\x18\x02 \x01(\x0b\x32\x1a.protos.ClassificationLoss\x12\x34\n\x12hard_example_miner\x18\x03 \x01(\x0b\x32\x18.protos.HardExampleMiner\x12 \n\x15\x63lassification_weight\x18\x04 \x01(\x02:\x01\x31\x12\x1e\n\x13localization_weight\x18\x05 \x01(\x02:\x01\x31\"\xe7\x01\n\x10LocalizationLoss\x12\x39\n\x0bweighted_l2\x18\x01 \x01(\x0b\x32\".protos.WeightedL2LocalizationLossH\x00\x12\x46\n\x12weighted_smooth_l1\x18\x02 \x01(\x0b\x32(.protos.WeightedSmoothL1LocalizationLossH\x00\x12;\n\x0cweighted_iou\x18\x03 \x01(\x0b\x32#.protos.WeightedIOULocalizationLossH\x00\x42\x13\n\x11localization_loss\">\n\x1aWeightedL2LocalizationLoss\x12 \n\x11\x61nchorwise_output\x18\x01 \x01(\x08:\x05\x66\x61lse\"V\n WeightedSmoothL1LocalizationLoss\x12 \n\x11\x61nchorwise_output\x18\x01 \x01(\x08:\x05\x66\x61lse\x12\x10\n\x05\x64\x65lta\x18\x02 \x01(\x02:\x01\x31\"\x1d\n\x1bWeightedIOULocalizationLoss\"\xd2\x02\n\x12\x43lassificationLoss\x12\x45\n\x10weighted_sigmoid\x18\x01 \x01(\x0b\x32).protos.WeightedSigmoidClassificationLossH\x00\x12\x45\n\x10weighted_softmax\x18\x02 \x01(\x0b\x32).protos.WeightedSoftmaxClassificationLossH\x00\x12M\n\x14\x62ootstrapped_sigmoid\x18\x03 \x01(\x0b\x32-.protos.BootstrappedSigmoidClassificationLossH\x00\x12H\n\x16weighted_sigmoid_focal\x18\x04 \x01(\x0b\x32&.protos.SigmoidFocalClassificationLossH\x00\x42\x15\n\x13\x63lassification_loss\"E\n!WeightedSigmoidClassificationLoss\x12 \n\x11\x61nchorwise_output\x18\x01 \x01(\x08:\x05\x66\x61lse\"c\n\x1eSigmoidFocalClassificationLoss\x12 \n\x11\x61nchorwise_output\x18\x01 \x01(\x08:\x05\x66\x61lse\x12\x10\n\x05gamma\x18\x02 \x01(\x02:\x01\x32\x12\r\n\x05\x61lpha\x18\x03 \x01(\x02\"]\n!WeightedSoftmaxClassificationLoss\x12 \n\x11\x61nchorwise_output\x18\x01 \x01(\x08:\x05\x66\x61lse\x12\x16\n\x0blogit_scale\x18\x02 \x01(\x02:\x01\x31\"w\n%BootstrappedSigmoidClassificationLoss\x12\r\n\x05\x61lpha\x18\x01 \x01(\x02\x12\x1d\n\x0ehard_bootstrap\x18\x02 \x01(\x08:\x05\x66\x61lse\x12 \n\x11\x61nchorwise_output\x18\x03 \x01(\x08:\x05\x66\x61lse\"\x90\x02\n\x10HardExampleMiner\x12\x1d\n\x11num_hard_examples\x18\x01 \x01(\x05:\x02\x36\x34\x12\x1a\n\riou_threshold\x18\x02 \x01(\x02:\x03\x30.7\x12:\n\tloss_type\x18\x03 \x01(\x0e\x32!.protos.HardExampleMiner.LossType:\x04\x42OTH\x12%\n\x1amax_negatives_per_positive\x18\x04 \x01(\x05:\x01\x30\x12\"\n\x17min_negatives_per_image\x18\x05 \x01(\x05:\x01\x30\":\n\x08LossType\x12\x08\n\x04\x42OTH\x10\x00\x12\x12\n\x0e\x43LASSIFICATION\x10\x01\x12\x10\n\x0cLOCALIZATION\x10\x02')
)



_HARDEXAMPLEMINER_LOSSTYPE = _descriptor.EnumDescriptor(
  name='LossType',
  full_name='protos.HardExampleMiner.LossType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='BOTH', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CLASSIFICATION', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LOCALIZATION', index=2, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=1648,
  serialized_end=1706,
)
_sym_db.RegisterEnumDescriptor(_HARDEXAMPLEMINER_LOSSTYPE)


_LOSS = _descriptor.Descriptor(
  name='Loss',
  full_name='protos.Loss',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='localization_loss', full_name='protos.Loss.localization_loss', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='classification_loss', full_name='protos.Loss.classification_loss', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='hard_example_miner', full_name='protos.Loss.hard_example_miner', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='classification_weight', full_name='protos.Loss.classification_weight', index=3,
      number=4, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=float(1),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='localization_weight', full_name='protos.Loss.localization_weight', index=4,
      number=5, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=float(1),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=49,
  serialized_end=285,
)


_LOCALIZATIONLOSS = _descriptor.Descriptor(
  name='LocalizationLoss',
  full_name='protos.LocalizationLoss',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='weighted_l2', full_name='protos.LocalizationLoss.weighted_l2', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='weighted_smooth_l1', full_name='protos.LocalizationLoss.weighted_smooth_l1', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='weighted_iou', full_name='protos.LocalizationLoss.weighted_iou', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='localization_loss', full_name='protos.LocalizationLoss.localization_loss',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=288,
  serialized_end=519,
)


_WEIGHTEDL2LOCALIZATIONLOSS = _descriptor.Descriptor(
  name='WeightedL2LocalizationLoss',
  full_name='protos.WeightedL2LocalizationLoss',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='anchorwise_output', full_name='protos.WeightedL2LocalizationLoss.anchorwise_output', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=521,
  serialized_end=583,
)


_WEIGHTEDSMOOTHL1LOCALIZATIONLOSS = _descriptor.Descriptor(
  name='WeightedSmoothL1LocalizationLoss',
  full_name='protos.WeightedSmoothL1LocalizationLoss',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='anchorwise_output', full_name='protos.WeightedSmoothL1LocalizationLoss.anchorwise_output', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='delta', full_name='protos.WeightedSmoothL1LocalizationLoss.delta', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=float(1),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=585,
  serialized_end=671,
)


_WEIGHTEDIOULOCALIZATIONLOSS = _descriptor.Descriptor(
  name='WeightedIOULocalizationLoss',
  full_name='protos.WeightedIOULocalizationLoss',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=673,
  serialized_end=702,
)


_CLASSIFICATIONLOSS = _descriptor.Descriptor(
  name='ClassificationLoss',
  full_name='protos.ClassificationLoss',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='weighted_sigmoid', full_name='protos.ClassificationLoss.weighted_sigmoid', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='weighted_softmax', full_name='protos.ClassificationLoss.weighted_softmax', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='bootstrapped_sigmoid', full_name='protos.ClassificationLoss.bootstrapped_sigmoid', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='weighted_sigmoid_focal', full_name='protos.ClassificationLoss.weighted_sigmoid_focal', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='classification_loss', full_name='protos.ClassificationLoss.classification_loss',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=705,
  serialized_end=1043,
)


_WEIGHTEDSIGMOIDCLASSIFICATIONLOSS = _descriptor.Descriptor(
  name='WeightedSigmoidClassificationLoss',
  full_name='protos.WeightedSigmoidClassificationLoss',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='anchorwise_output', full_name='protos.WeightedSigmoidClassificationLoss.anchorwise_output', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1045,
  serialized_end=1114,
)


_SIGMOIDFOCALCLASSIFICATIONLOSS = _descriptor.Descriptor(
  name='SigmoidFocalClassificationLoss',
  full_name='protos.SigmoidFocalClassificationLoss',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='anchorwise_output', full_name='protos.SigmoidFocalClassificationLoss.anchorwise_output', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='gamma', full_name='protos.SigmoidFocalClassificationLoss.gamma', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=float(2),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='alpha', full_name='protos.SigmoidFocalClassificationLoss.alpha', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1116,
  serialized_end=1215,
)


_WEIGHTEDSOFTMAXCLASSIFICATIONLOSS = _descriptor.Descriptor(
  name='WeightedSoftmaxClassificationLoss',
  full_name='protos.WeightedSoftmaxClassificationLoss',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='anchorwise_output', full_name='protos.WeightedSoftmaxClassificationLoss.anchorwise_output', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='logit_scale', full_name='protos.WeightedSoftmaxClassificationLoss.logit_scale', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=float(1),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1217,
  serialized_end=1310,
)


_BOOTSTRAPPEDSIGMOIDCLASSIFICATIONLOSS = _descriptor.Descriptor(
  name='BootstrappedSigmoidClassificationLoss',
  full_name='protos.BootstrappedSigmoidClassificationLoss',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='alpha', full_name='protos.BootstrappedSigmoidClassificationLoss.alpha', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='hard_bootstrap', full_name='protos.BootstrappedSigmoidClassificationLoss.hard_bootstrap', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='anchorwise_output', full_name='protos.BootstrappedSigmoidClassificationLoss.anchorwise_output', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1312,
  serialized_end=1431,
)


_HARDEXAMPLEMINER = _descriptor.Descriptor(
  name='HardExampleMiner',
  full_name='protos.HardExampleMiner',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='num_hard_examples', full_name='protos.HardExampleMiner.num_hard_examples', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=64,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='iou_threshold', full_name='protos.HardExampleMiner.iou_threshold', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=float(0.7),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='loss_type', full_name='protos.HardExampleMiner.loss_type', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='max_negatives_per_positive', full_name='protos.HardExampleMiner.max_negatives_per_positive', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='min_negatives_per_image', full_name='protos.HardExampleMiner.min_negatives_per_image', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _HARDEXAMPLEMINER_LOSSTYPE,
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1434,
  serialized_end=1706,
)

_LOSS.fields_by_name['localization_loss'].message_type = _LOCALIZATIONLOSS
_LOSS.fields_by_name['classification_loss'].message_type = _CLASSIFICATIONLOSS
_LOSS.fields_by_name['hard_example_miner'].message_type = _HARDEXAMPLEMINER
_LOCALIZATIONLOSS.fields_by_name['weighted_l2'].message_type = _WEIGHTEDL2LOCALIZATIONLOSS
_LOCALIZATIONLOSS.fields_by_name['weighted_smooth_l1'].message_type = _WEIGHTEDSMOOTHL1LOCALIZATIONLOSS
_LOCALIZATIONLOSS.fields_by_name['weighted_iou'].message_type = _WEIGHTEDIOULOCALIZATIONLOSS
_LOCALIZATIONLOSS.oneofs_by_name['localization_loss'].fields.append(
  _LOCALIZATIONLOSS.fields_by_name['weighted_l2'])
_LOCALIZATIONLOSS.fields_by_name['weighted_l2'].containing_oneof = _LOCALIZATIONLOSS.oneofs_by_name['localization_loss']
_LOCALIZATIONLOSS.oneofs_by_name['localization_loss'].fields.append(
  _LOCALIZATIONLOSS.fields_by_name['weighted_smooth_l1'])
_LOCALIZATIONLOSS.fields_by_name['weighted_smooth_l1'].containing_oneof = _LOCALIZATIONLOSS.oneofs_by_name['localization_loss']
_LOCALIZATIONLOSS.oneofs_by_name['localization_loss'].fields.append(
  _LOCALIZATIONLOSS.fields_by_name['weighted_iou'])
_LOCALIZATIONLOSS.fields_by_name['weighted_iou'].containing_oneof = _LOCALIZATIONLOSS.oneofs_by_name['localization_loss']
_CLASSIFICATIONLOSS.fields_by_name['weighted_sigmoid'].message_type = _WEIGHTEDSIGMOIDCLASSIFICATIONLOSS
_CLASSIFICATIONLOSS.fields_by_name['weighted_softmax'].message_type = _WEIGHTEDSOFTMAXCLASSIFICATIONLOSS
_CLASSIFICATIONLOSS.fields_by_name['bootstrapped_sigmoid'].message_type = _BOOTSTRAPPEDSIGMOIDCLASSIFICATIONLOSS
_CLASSIFICATIONLOSS.fields_by_name['weighted_sigmoid_focal'].message_type = _SIGMOIDFOCALCLASSIFICATIONLOSS
_CLASSIFICATIONLOSS.oneofs_by_name['classification_loss'].fields.append(
  _CLASSIFICATIONLOSS.fields_by_name['weighted_sigmoid'])
_CLASSIFICATIONLOSS.fields_by_name['weighted_sigmoid'].containing_oneof = _CLASSIFICATIONLOSS.oneofs_by_name['classification_loss']
_CLASSIFICATIONLOSS.oneofs_by_name['classification_loss'].fields.append(
  _CLASSIFICATIONLOSS.fields_by_name['weighted_softmax'])
_CLASSIFICATIONLOSS.fields_by_name['weighted_softmax'].containing_oneof = _CLASSIFICATIONLOSS.oneofs_by_name['classification_loss']
_CLASSIFICATIONLOSS.oneofs_by_name['classification_loss'].fields.append(
  _CLASSIFICATIONLOSS.fields_by_name['bootstrapped_sigmoid'])
_CLASSIFICATIONLOSS.fields_by_name['bootstrapped_sigmoid'].containing_oneof = _CLASSIFICATIONLOSS.oneofs_by_name['classification_loss']
_CLASSIFICATIONLOSS.oneofs_by_name['classification_loss'].fields.append(
  _CLASSIFICATIONLOSS.fields_by_name['weighted_sigmoid_focal'])
_CLASSIFICATIONLOSS.fields_by_name['weighted_sigmoid_focal'].containing_oneof = _CLASSIFICATIONLOSS.oneofs_by_name['classification_loss']
_HARDEXAMPLEMINER.fields_by_name['loss_type'].enum_type = _HARDEXAMPLEMINER_LOSSTYPE
_HARDEXAMPLEMINER_LOSSTYPE.containing_type = _HARDEXAMPLEMINER
DESCRIPTOR.message_types_by_name['Loss'] = _LOSS
DESCRIPTOR.message_types_by_name['LocalizationLoss'] = _LOCALIZATIONLOSS
DESCRIPTOR.message_types_by_name['WeightedL2LocalizationLoss'] = _WEIGHTEDL2LOCALIZATIONLOSS
DESCRIPTOR.message_types_by_name['WeightedSmoothL1LocalizationLoss'] = _WEIGHTEDSMOOTHL1LOCALIZATIONLOSS
DESCRIPTOR.message_types_by_name['WeightedIOULocalizationLoss'] = _WEIGHTEDIOULOCALIZATIONLOSS
DESCRIPTOR.message_types_by_name['ClassificationLoss'] = _CLASSIFICATIONLOSS
DESCRIPTOR.message_types_by_name['WeightedSigmoidClassificationLoss'] = _WEIGHTEDSIGMOIDCLASSIFICATIONLOSS
DESCRIPTOR.message_types_by_name['SigmoidFocalClassificationLoss'] = _SIGMOIDFOCALCLASSIFICATIONLOSS
DESCRIPTOR.message_types_by_name['WeightedSoftmaxClassificationLoss'] = _WEIGHTEDSOFTMAXCLASSIFICATIONLOSS
DESCRIPTOR.message_types_by_name['BootstrappedSigmoidClassificationLoss'] = _BOOTSTRAPPEDSIGMOIDCLASSIFICATIONLOSS
DESCRIPTOR.message_types_by_name['HardExampleMiner'] = _HARDEXAMPLEMINER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Loss = _reflection.GeneratedProtocolMessageType('Loss', (_message.Message,), dict(
  DESCRIPTOR = _LOSS,
  __module__ = 'protos.losses_pb2'
  # @@protoc_insertion_point(class_scope:protos.Loss)
  ))
_sym_db.RegisterMessage(Loss)

LocalizationLoss = _reflection.GeneratedProtocolMessageType('LocalizationLoss', (_message.Message,), dict(
  DESCRIPTOR = _LOCALIZATIONLOSS,
  __module__ = 'protos.losses_pb2'
  # @@protoc_insertion_point(class_scope:protos.LocalizationLoss)
  ))
_sym_db.RegisterMessage(LocalizationLoss)

WeightedL2LocalizationLoss = _reflection.GeneratedProtocolMessageType('WeightedL2LocalizationLoss', (_message.Message,), dict(
  DESCRIPTOR = _WEIGHTEDL2LOCALIZATIONLOSS,
  __module__ = 'protos.losses_pb2'
  # @@protoc_insertion_point(class_scope:protos.WeightedL2LocalizationLoss)
  ))
_sym_db.RegisterMessage(WeightedL2LocalizationLoss)

WeightedSmoothL1LocalizationLoss = _reflection.GeneratedProtocolMessageType('WeightedSmoothL1LocalizationLoss', (_message.Message,), dict(
  DESCRIPTOR = _WEIGHTEDSMOOTHL1LOCALIZATIONLOSS,
  __module__ = 'protos.losses_pb2'
  # @@protoc_insertion_point(class_scope:protos.WeightedSmoothL1LocalizationLoss)
  ))
_sym_db.RegisterMessage(WeightedSmoothL1LocalizationLoss)

WeightedIOULocalizationLoss = _reflection.GeneratedProtocolMessageType('WeightedIOULocalizationLoss', (_message.Message,), dict(
  DESCRIPTOR = _WEIGHTEDIOULOCALIZATIONLOSS,
  __module__ = 'protos.losses_pb2'
  # @@protoc_insertion_point(class_scope:protos.WeightedIOULocalizationLoss)
  ))
_sym_db.RegisterMessage(WeightedIOULocalizationLoss)

ClassificationLoss = _reflection.GeneratedProtocolMessageType('ClassificationLoss', (_message.Message,), dict(
  DESCRIPTOR = _CLASSIFICATIONLOSS,
  __module__ = 'protos.losses_pb2'
  # @@protoc_insertion_point(class_scope:protos.ClassificationLoss)
  ))
_sym_db.RegisterMessage(ClassificationLoss)

WeightedSigmoidClassificationLoss = _reflection.GeneratedProtocolMessageType('WeightedSigmoidClassificationLoss', (_message.Message,), dict(
  DESCRIPTOR = _WEIGHTEDSIGMOIDCLASSIFICATIONLOSS,
  __module__ = 'protos.losses_pb2'
  # @@protoc_insertion_point(class_scope:protos.WeightedSigmoidClassificationLoss)
  ))
_sym_db.RegisterMessage(WeightedSigmoidClassificationLoss)

SigmoidFocalClassificationLoss = _reflection.GeneratedProtocolMessageType('SigmoidFocalClassificationLoss', (_message.Message,), dict(
  DESCRIPTOR = _SIGMOIDFOCALCLASSIFICATIONLOSS,
  __module__ = 'protos.losses_pb2'
  # @@protoc_insertion_point(class_scope:protos.SigmoidFocalClassificationLoss)
  ))
_sym_db.RegisterMessage(SigmoidFocalClassificationLoss)

WeightedSoftmaxClassificationLoss = _reflection.GeneratedProtocolMessageType('WeightedSoftmaxClassificationLoss', (_message.Message,), dict(
  DESCRIPTOR = _WEIGHTEDSOFTMAXCLASSIFICATIONLOSS,
  __module__ = 'protos.losses_pb2'
  # @@protoc_insertion_point(class_scope:protos.WeightedSoftmaxClassificationLoss)
  ))
_sym_db.RegisterMessage(WeightedSoftmaxClassificationLoss)

BootstrappedSigmoidClassificationLoss = _reflection.GeneratedProtocolMessageType('BootstrappedSigmoidClassificationLoss', (_message.Message,), dict(
  DESCRIPTOR = _BOOTSTRAPPEDSIGMOIDCLASSIFICATIONLOSS,
  __module__ = 'protos.losses_pb2'
  # @@protoc_insertion_point(class_scope:protos.BootstrappedSigmoidClassificationLoss)
  ))
_sym_db.RegisterMessage(BootstrappedSigmoidClassificationLoss)

HardExampleMiner = _reflection.GeneratedProtocolMessageType('HardExampleMiner', (_message.Message,), dict(
  DESCRIPTOR = _HARDEXAMPLEMINER,
  __module__ = 'protos.losses_pb2'
  # @@protoc_insertion_point(class_scope:protos.HardExampleMiner)
  ))
_sym_db.RegisterMessage(HardExampleMiner)


# @@protoc_insertion_point(module_scope)
