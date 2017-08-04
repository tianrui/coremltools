# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: Model.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import ArrayFeatureExtractor_pb2 as ArrayFeatureExtractor__pb2
import CategoricalMapping_pb2 as CategoricalMapping__pb2
DataStructures__pb2 = CategoricalMapping__pb2.DataStructures__pb2
FeatureTypes__pb2 = CategoricalMapping__pb2.FeatureTypes__pb2
import DictVectorizer_pb2 as DictVectorizer__pb2
DataStructures__pb2 = DictVectorizer__pb2.DataStructures__pb2
FeatureTypes__pb2 = DictVectorizer__pb2.FeatureTypes__pb2
import FeatureTypes_pb2 as FeatureTypes__pb2
import FeatureVectorizer_pb2 as FeatureVectorizer__pb2
import GLMRegressor_pb2 as GLMRegressor__pb2
import GLMClassifier_pb2 as GLMClassifier__pb2
DataStructures__pb2 = GLMClassifier__pb2.DataStructures__pb2
FeatureTypes__pb2 = GLMClassifier__pb2.FeatureTypes__pb2
import Identity_pb2 as Identity__pb2
import Imputer_pb2 as Imputer__pb2
DataStructures__pb2 = Imputer__pb2.DataStructures__pb2
FeatureTypes__pb2 = Imputer__pb2.FeatureTypes__pb2
import NeuralNetwork_pb2 as NeuralNetwork__pb2
DataStructures__pb2 = NeuralNetwork__pb2.DataStructures__pb2
FeatureTypes__pb2 = NeuralNetwork__pb2.FeatureTypes__pb2
import Normalizer_pb2 as Normalizer__pb2
import OneHotEncoder_pb2 as OneHotEncoder__pb2
DataStructures__pb2 = OneHotEncoder__pb2.DataStructures__pb2
FeatureTypes__pb2 = OneHotEncoder__pb2.FeatureTypes__pb2
import Scaler_pb2 as Scaler__pb2
import SVM_pb2 as SVM__pb2
DataStructures__pb2 = SVM__pb2.DataStructures__pb2
FeatureTypes__pb2 = SVM__pb2.FeatureTypes__pb2
import TreeEnsemble_pb2 as TreeEnsemble__pb2
DataStructures__pb2 = TreeEnsemble__pb2.DataStructures__pb2
FeatureTypes__pb2 = TreeEnsemble__pb2.FeatureTypes__pb2

from ArrayFeatureExtractor_pb2 import *
from CategoricalMapping_pb2 import *
from DictVectorizer_pb2 import *
from FeatureTypes_pb2 import *
from FeatureVectorizer_pb2 import *
from GLMRegressor_pb2 import *
from GLMClassifier_pb2 import *
from Identity_pb2 import *
from Imputer_pb2 import *
from NeuralNetwork_pb2 import *
from Normalizer_pb2 import *
from OneHotEncoder_pb2 import *
from Scaler_pb2 import *
from SVM_pb2 import *
from TreeEnsemble_pb2 import *

DESCRIPTOR = _descriptor.FileDescriptor(
  name='Model.proto',
  package='CoreML.Specification',
  syntax='proto3',
  serialized_pb=_b('\n\x0bModel.proto\x12\x14\x43oreML.Specification\x1a\x1b\x41rrayFeatureExtractor.proto\x1a\x18\x43\x61tegoricalMapping.proto\x1a\x14\x44ictVectorizer.proto\x1a\x12\x46\x65\x61tureTypes.proto\x1a\x17\x46\x65\x61tureVectorizer.proto\x1a\x12GLMRegressor.proto\x1a\x13GLMClassifier.proto\x1a\x0eIdentity.proto\x1a\rImputer.proto\x1a\x13NeuralNetwork.proto\x1a\x10Normalizer.proto\x1a\x13OneHotEncoder.proto\x1a\x0cScaler.proto\x1a\tSVM.proto\x1a\x12TreeEnsemble.proto\"7\n\x08Pipeline\x12+\n\x06models\x18\x01 \x03(\x0b\x32\x1b.CoreML.Specification.Model\"F\n\x12PipelineClassifier\x12\x30\n\x08pipeline\x18\x01 \x01(\x0b\x32\x1e.CoreML.Specification.Pipeline\"E\n\x11PipelineRegressor\x12\x30\n\x08pipeline\x18\x01 \x01(\x0b\x32\x1e.CoreML.Specification.Pipeline\"m\n\x12\x46\x65\x61tureDescription\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x18\n\x10shortDescription\x18\x02 \x01(\t\x12/\n\x04type\x18\x03 \x01(\x0b\x32!.CoreML.Specification.FeatureType\"\xd6\x01\n\x08Metadata\x12\x18\n\x10shortDescription\x18\x01 \x01(\t\x12\x15\n\rversionString\x18\x02 \x01(\t\x12\x0e\n\x06\x61uthor\x18\x03 \x01(\t\x12\x0f\n\x07license\x18\x04 \x01(\t\x12\x44\n\x0buserDefined\x18\x64 \x03(\x0b\x32/.CoreML.Specification.Metadata.UserDefinedEntry\x1a\x32\n\x10UserDefinedEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\xf9\x01\n\x10ModelDescription\x12\x37\n\x05input\x18\x01 \x03(\x0b\x32(.CoreML.Specification.FeatureDescription\x12\x38\n\x06output\x18\n \x03(\x0b\x32(.CoreML.Specification.FeatureDescription\x12\x1c\n\x14predictedFeatureName\x18\x0b \x01(\t\x12\"\n\x1apredictedProbabilitiesName\x18\x0c \x01(\t\x12\x30\n\x08metadata\x18\x64 \x01(\x0b\x32\x1e.CoreML.Specification.Metadata\"\x83\x0c\n\x05Model\x12\x1c\n\x14specificationVersion\x18\x01 \x01(\x05\x12;\n\x0b\x64\x65scription\x18\x02 \x01(\x0b\x32&.CoreML.Specification.ModelDescription\x12G\n\x12pipelineClassifier\x18\xc8\x01 \x01(\x0b\x32(.CoreML.Specification.PipelineClassifierH\x00\x12\x45\n\x11pipelineRegressor\x18\xc9\x01 \x01(\x0b\x32\'.CoreML.Specification.PipelineRegressorH\x00\x12\x33\n\x08pipeline\x18\xca\x01 \x01(\x0b\x32\x1e.CoreML.Specification.PipelineH\x00\x12;\n\x0cglmRegressor\x18\xac\x02 \x01(\x0b\x32\".CoreML.Specification.GLMRegressorH\x00\x12O\n\x16supportVectorRegressor\x18\xad\x02 \x01(\x0b\x32,.CoreML.Specification.SupportVectorRegressorH\x00\x12M\n\x15treeEnsembleRegressor\x18\xae\x02 \x01(\x0b\x32+.CoreML.Specification.TreeEnsembleRegressorH\x00\x12O\n\x16neuralNetworkRegressor\x18\xaf\x02 \x01(\x0b\x32,.CoreML.Specification.NeuralNetworkRegressorH\x00\x12=\n\rglmClassifier\x18\x90\x03 \x01(\x0b\x32#.CoreML.Specification.GLMClassifierH\x00\x12Q\n\x17supportVectorClassifier\x18\x91\x03 \x01(\x0b\x32-.CoreML.Specification.SupportVectorClassifierH\x00\x12O\n\x16treeEnsembleClassifier\x18\x92\x03 \x01(\x0b\x32,.CoreML.Specification.TreeEnsembleClassifierH\x00\x12Q\n\x17neuralNetworkClassifier\x18\x93\x03 \x01(\x0b\x32-.CoreML.Specification.NeuralNetworkClassifierH\x00\x12=\n\rneuralNetwork\x18\xf4\x03 \x01(\x0b\x32#.CoreML.Specification.NeuralNetworkH\x00\x12=\n\roneHotEncoder\x18\xd8\x04 \x01(\x0b\x32#.CoreML.Specification.OneHotEncoderH\x00\x12\x31\n\x07imputer\x18\xd9\x04 \x01(\x0b\x32\x1d.CoreML.Specification.ImputerH\x00\x12\x45\n\x11\x66\x65\x61tureVectorizer\x18\xda\x04 \x01(\x0b\x32\'.CoreML.Specification.FeatureVectorizerH\x00\x12?\n\x0e\x64ictVectorizer\x18\xdb\x04 \x01(\x0b\x32$.CoreML.Specification.DictVectorizerH\x00\x12/\n\x06scaler\x18\xdc\x04 \x01(\x0b\x32\x1c.CoreML.Specification.ScalerH\x00\x12G\n\x12\x63\x61tegoricalMapping\x18\xde\x04 \x01(\x0b\x32(.CoreML.Specification.CategoricalMappingH\x00\x12\x37\n\nnormalizer\x18\xdf\x04 \x01(\x0b\x32 .CoreML.Specification.NormalizerH\x00\x12M\n\x15\x61rrayFeatureExtractor\x18\xe1\x04 \x01(\x0b\x32+.CoreML.Specification.ArrayFeatureExtractorH\x00\x12\x33\n\x08identity\x18\x84\x07 \x01(\x0b\x32\x1e.CoreML.Specification.IdentityH\x00\x42\x06\n\x04TypeB\x02H\x03P\x00P\x01P\x02P\x03P\x04P\x05P\x06P\x07P\x08P\tP\nP\x0bP\x0cP\rP\x0e\x62\x06proto3')
  ,
  dependencies=[ArrayFeatureExtractor__pb2.DESCRIPTOR,CategoricalMapping__pb2.DESCRIPTOR,DictVectorizer__pb2.DESCRIPTOR,FeatureTypes__pb2.DESCRIPTOR,FeatureVectorizer__pb2.DESCRIPTOR,GLMRegressor__pb2.DESCRIPTOR,GLMClassifier__pb2.DESCRIPTOR,Identity__pb2.DESCRIPTOR,Imputer__pb2.DESCRIPTOR,NeuralNetwork__pb2.DESCRIPTOR,Normalizer__pb2.DESCRIPTOR,OneHotEncoder__pb2.DESCRIPTOR,Scaler__pb2.DESCRIPTOR,SVM__pb2.DESCRIPTOR,TreeEnsemble__pb2.DESCRIPTOR,],
  public_dependencies=[ArrayFeatureExtractor__pb2.DESCRIPTOR,CategoricalMapping__pb2.DESCRIPTOR,DictVectorizer__pb2.DESCRIPTOR,FeatureTypes__pb2.DESCRIPTOR,FeatureVectorizer__pb2.DESCRIPTOR,GLMRegressor__pb2.DESCRIPTOR,GLMClassifier__pb2.DESCRIPTOR,Identity__pb2.DESCRIPTOR,Imputer__pb2.DESCRIPTOR,NeuralNetwork__pb2.DESCRIPTOR,Normalizer__pb2.DESCRIPTOR,OneHotEncoder__pb2.DESCRIPTOR,Scaler__pb2.DESCRIPTOR,SVM__pb2.DESCRIPTOR,TreeEnsemble__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_PIPELINE = _descriptor.Descriptor(
  name='Pipeline',
  full_name='CoreML.Specification.Pipeline',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='models', full_name='CoreML.Specification.Pipeline.models', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=336,
  serialized_end=391,
)


_PIPELINECLASSIFIER = _descriptor.Descriptor(
  name='PipelineClassifier',
  full_name='CoreML.Specification.PipelineClassifier',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='pipeline', full_name='CoreML.Specification.PipelineClassifier.pipeline', index=0,
      number=1, type=11, cpp_type=10, label=1,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=393,
  serialized_end=463,
)


_PIPELINEREGRESSOR = _descriptor.Descriptor(
  name='PipelineRegressor',
  full_name='CoreML.Specification.PipelineRegressor',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='pipeline', full_name='CoreML.Specification.PipelineRegressor.pipeline', index=0,
      number=1, type=11, cpp_type=10, label=1,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=465,
  serialized_end=534,
)


_FEATUREDESCRIPTION = _descriptor.Descriptor(
  name='FeatureDescription',
  full_name='CoreML.Specification.FeatureDescription',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='CoreML.Specification.FeatureDescription.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='shortDescription', full_name='CoreML.Specification.FeatureDescription.shortDescription', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='type', full_name='CoreML.Specification.FeatureDescription.type', index=2,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=536,
  serialized_end=645,
)


_METADATA_USERDEFINEDENTRY = _descriptor.Descriptor(
  name='UserDefinedEntry',
  full_name='CoreML.Specification.Metadata.UserDefinedEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='CoreML.Specification.Metadata.UserDefinedEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='value', full_name='CoreML.Specification.Metadata.UserDefinedEntry.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=_descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001')),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=812,
  serialized_end=862,
)

_METADATA = _descriptor.Descriptor(
  name='Metadata',
  full_name='CoreML.Specification.Metadata',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='shortDescription', full_name='CoreML.Specification.Metadata.shortDescription', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='versionString', full_name='CoreML.Specification.Metadata.versionString', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='author', full_name='CoreML.Specification.Metadata.author', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='license', full_name='CoreML.Specification.Metadata.license', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='userDefined', full_name='CoreML.Specification.Metadata.userDefined', index=4,
      number=100, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_METADATA_USERDEFINEDENTRY, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=648,
  serialized_end=862,
)


_MODELDESCRIPTION = _descriptor.Descriptor(
  name='ModelDescription',
  full_name='CoreML.Specification.ModelDescription',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='input', full_name='CoreML.Specification.ModelDescription.input', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='output', full_name='CoreML.Specification.ModelDescription.output', index=1,
      number=10, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='predictedFeatureName', full_name='CoreML.Specification.ModelDescription.predictedFeatureName', index=2,
      number=11, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='predictedProbabilitiesName', full_name='CoreML.Specification.ModelDescription.predictedProbabilitiesName', index=3,
      number=12, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='metadata', full_name='CoreML.Specification.ModelDescription.metadata', index=4,
      number=100, type=11, cpp_type=10, label=1,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=865,
  serialized_end=1114,
)


_MODEL = _descriptor.Descriptor(
  name='Model',
  full_name='CoreML.Specification.Model',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='specificationVersion', full_name='CoreML.Specification.Model.specificationVersion', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='description', full_name='CoreML.Specification.Model.description', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='pipelineClassifier', full_name='CoreML.Specification.Model.pipelineClassifier', index=2,
      number=200, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='pipelineRegressor', full_name='CoreML.Specification.Model.pipelineRegressor', index=3,
      number=201, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='pipeline', full_name='CoreML.Specification.Model.pipeline', index=4,
      number=202, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='glmRegressor', full_name='CoreML.Specification.Model.glmRegressor', index=5,
      number=300, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='supportVectorRegressor', full_name='CoreML.Specification.Model.supportVectorRegressor', index=6,
      number=301, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='treeEnsembleRegressor', full_name='CoreML.Specification.Model.treeEnsembleRegressor', index=7,
      number=302, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='neuralNetworkRegressor', full_name='CoreML.Specification.Model.neuralNetworkRegressor', index=8,
      number=303, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='glmClassifier', full_name='CoreML.Specification.Model.glmClassifier', index=9,
      number=400, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='supportVectorClassifier', full_name='CoreML.Specification.Model.supportVectorClassifier', index=10,
      number=401, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='treeEnsembleClassifier', full_name='CoreML.Specification.Model.treeEnsembleClassifier', index=11,
      number=402, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='neuralNetworkClassifier', full_name='CoreML.Specification.Model.neuralNetworkClassifier', index=12,
      number=403, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='neuralNetwork', full_name='CoreML.Specification.Model.neuralNetwork', index=13,
      number=500, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='oneHotEncoder', full_name='CoreML.Specification.Model.oneHotEncoder', index=14,
      number=600, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='imputer', full_name='CoreML.Specification.Model.imputer', index=15,
      number=601, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='featureVectorizer', full_name='CoreML.Specification.Model.featureVectorizer', index=16,
      number=602, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='dictVectorizer', full_name='CoreML.Specification.Model.dictVectorizer', index=17,
      number=603, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='scaler', full_name='CoreML.Specification.Model.scaler', index=18,
      number=604, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='categoricalMapping', full_name='CoreML.Specification.Model.categoricalMapping', index=19,
      number=606, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='normalizer', full_name='CoreML.Specification.Model.normalizer', index=20,
      number=607, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='arrayFeatureExtractor', full_name='CoreML.Specification.Model.arrayFeatureExtractor', index=21,
      number=609, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='identity', full_name='CoreML.Specification.Model.identity', index=22,
      number=900, type=11, cpp_type=10, label=1,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='Type', full_name='CoreML.Specification.Model.Type',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=1117,
  serialized_end=2656,
)

_PIPELINE.fields_by_name['models'].message_type = _MODEL
_PIPELINECLASSIFIER.fields_by_name['pipeline'].message_type = _PIPELINE
_PIPELINEREGRESSOR.fields_by_name['pipeline'].message_type = _PIPELINE
_FEATUREDESCRIPTION.fields_by_name['type'].message_type = FeatureTypes__pb2._FEATURETYPE
_METADATA_USERDEFINEDENTRY.containing_type = _METADATA
_METADATA.fields_by_name['userDefined'].message_type = _METADATA_USERDEFINEDENTRY
_MODELDESCRIPTION.fields_by_name['input'].message_type = _FEATUREDESCRIPTION
_MODELDESCRIPTION.fields_by_name['output'].message_type = _FEATUREDESCRIPTION
_MODELDESCRIPTION.fields_by_name['metadata'].message_type = _METADATA
_MODEL.fields_by_name['description'].message_type = _MODELDESCRIPTION
_MODEL.fields_by_name['pipelineClassifier'].message_type = _PIPELINECLASSIFIER
_MODEL.fields_by_name['pipelineRegressor'].message_type = _PIPELINEREGRESSOR
_MODEL.fields_by_name['pipeline'].message_type = _PIPELINE
_MODEL.fields_by_name['glmRegressor'].message_type = GLMRegressor__pb2._GLMREGRESSOR
_MODEL.fields_by_name['supportVectorRegressor'].message_type = SVM__pb2._SUPPORTVECTORREGRESSOR
_MODEL.fields_by_name['treeEnsembleRegressor'].message_type = TreeEnsemble__pb2._TREEENSEMBLEREGRESSOR
_MODEL.fields_by_name['neuralNetworkRegressor'].message_type = NeuralNetwork__pb2._NEURALNETWORKREGRESSOR
_MODEL.fields_by_name['glmClassifier'].message_type = GLMClassifier__pb2._GLMCLASSIFIER
_MODEL.fields_by_name['supportVectorClassifier'].message_type = SVM__pb2._SUPPORTVECTORCLASSIFIER
_MODEL.fields_by_name['treeEnsembleClassifier'].message_type = TreeEnsemble__pb2._TREEENSEMBLECLASSIFIER
_MODEL.fields_by_name['neuralNetworkClassifier'].message_type = NeuralNetwork__pb2._NEURALNETWORKCLASSIFIER
_MODEL.fields_by_name['neuralNetwork'].message_type = NeuralNetwork__pb2._NEURALNETWORK
_MODEL.fields_by_name['oneHotEncoder'].message_type = OneHotEncoder__pb2._ONEHOTENCODER
_MODEL.fields_by_name['imputer'].message_type = Imputer__pb2._IMPUTER
_MODEL.fields_by_name['featureVectorizer'].message_type = FeatureVectorizer__pb2._FEATUREVECTORIZER
_MODEL.fields_by_name['dictVectorizer'].message_type = DictVectorizer__pb2._DICTVECTORIZER
_MODEL.fields_by_name['scaler'].message_type = Scaler__pb2._SCALER
_MODEL.fields_by_name['categoricalMapping'].message_type = CategoricalMapping__pb2._CATEGORICALMAPPING
_MODEL.fields_by_name['normalizer'].message_type = Normalizer__pb2._NORMALIZER
_MODEL.fields_by_name['arrayFeatureExtractor'].message_type = ArrayFeatureExtractor__pb2._ARRAYFEATUREEXTRACTOR
_MODEL.fields_by_name['identity'].message_type = Identity__pb2._IDENTITY
_MODEL.oneofs_by_name['Type'].fields.append(
  _MODEL.fields_by_name['pipelineClassifier'])
_MODEL.fields_by_name['pipelineClassifier'].containing_oneof = _MODEL.oneofs_by_name['Type']
_MODEL.oneofs_by_name['Type'].fields.append(
  _MODEL.fields_by_name['pipelineRegressor'])
_MODEL.fields_by_name['pipelineRegressor'].containing_oneof = _MODEL.oneofs_by_name['Type']
_MODEL.oneofs_by_name['Type'].fields.append(
  _MODEL.fields_by_name['pipeline'])
_MODEL.fields_by_name['pipeline'].containing_oneof = _MODEL.oneofs_by_name['Type']
_MODEL.oneofs_by_name['Type'].fields.append(
  _MODEL.fields_by_name['glmRegressor'])
_MODEL.fields_by_name['glmRegressor'].containing_oneof = _MODEL.oneofs_by_name['Type']
_MODEL.oneofs_by_name['Type'].fields.append(
  _MODEL.fields_by_name['supportVectorRegressor'])
_MODEL.fields_by_name['supportVectorRegressor'].containing_oneof = _MODEL.oneofs_by_name['Type']
_MODEL.oneofs_by_name['Type'].fields.append(
  _MODEL.fields_by_name['treeEnsembleRegressor'])
_MODEL.fields_by_name['treeEnsembleRegressor'].containing_oneof = _MODEL.oneofs_by_name['Type']
_MODEL.oneofs_by_name['Type'].fields.append(
  _MODEL.fields_by_name['neuralNetworkRegressor'])
_MODEL.fields_by_name['neuralNetworkRegressor'].containing_oneof = _MODEL.oneofs_by_name['Type']
_MODEL.oneofs_by_name['Type'].fields.append(
  _MODEL.fields_by_name['glmClassifier'])
_MODEL.fields_by_name['glmClassifier'].containing_oneof = _MODEL.oneofs_by_name['Type']
_MODEL.oneofs_by_name['Type'].fields.append(
  _MODEL.fields_by_name['supportVectorClassifier'])
_MODEL.fields_by_name['supportVectorClassifier'].containing_oneof = _MODEL.oneofs_by_name['Type']
_MODEL.oneofs_by_name['Type'].fields.append(
  _MODEL.fields_by_name['treeEnsembleClassifier'])
_MODEL.fields_by_name['treeEnsembleClassifier'].containing_oneof = _MODEL.oneofs_by_name['Type']
_MODEL.oneofs_by_name['Type'].fields.append(
  _MODEL.fields_by_name['neuralNetworkClassifier'])
_MODEL.fields_by_name['neuralNetworkClassifier'].containing_oneof = _MODEL.oneofs_by_name['Type']
_MODEL.oneofs_by_name['Type'].fields.append(
  _MODEL.fields_by_name['neuralNetwork'])
_MODEL.fields_by_name['neuralNetwork'].containing_oneof = _MODEL.oneofs_by_name['Type']
_MODEL.oneofs_by_name['Type'].fields.append(
  _MODEL.fields_by_name['oneHotEncoder'])
_MODEL.fields_by_name['oneHotEncoder'].containing_oneof = _MODEL.oneofs_by_name['Type']
_MODEL.oneofs_by_name['Type'].fields.append(
  _MODEL.fields_by_name['imputer'])
_MODEL.fields_by_name['imputer'].containing_oneof = _MODEL.oneofs_by_name['Type']
_MODEL.oneofs_by_name['Type'].fields.append(
  _MODEL.fields_by_name['featureVectorizer'])
_MODEL.fields_by_name['featureVectorizer'].containing_oneof = _MODEL.oneofs_by_name['Type']
_MODEL.oneofs_by_name['Type'].fields.append(
  _MODEL.fields_by_name['dictVectorizer'])
_MODEL.fields_by_name['dictVectorizer'].containing_oneof = _MODEL.oneofs_by_name['Type']
_MODEL.oneofs_by_name['Type'].fields.append(
  _MODEL.fields_by_name['scaler'])
_MODEL.fields_by_name['scaler'].containing_oneof = _MODEL.oneofs_by_name['Type']
_MODEL.oneofs_by_name['Type'].fields.append(
  _MODEL.fields_by_name['categoricalMapping'])
_MODEL.fields_by_name['categoricalMapping'].containing_oneof = _MODEL.oneofs_by_name['Type']
_MODEL.oneofs_by_name['Type'].fields.append(
  _MODEL.fields_by_name['normalizer'])
_MODEL.fields_by_name['normalizer'].containing_oneof = _MODEL.oneofs_by_name['Type']
_MODEL.oneofs_by_name['Type'].fields.append(
  _MODEL.fields_by_name['arrayFeatureExtractor'])
_MODEL.fields_by_name['arrayFeatureExtractor'].containing_oneof = _MODEL.oneofs_by_name['Type']
_MODEL.oneofs_by_name['Type'].fields.append(
  _MODEL.fields_by_name['identity'])
_MODEL.fields_by_name['identity'].containing_oneof = _MODEL.oneofs_by_name['Type']
DESCRIPTOR.message_types_by_name['Pipeline'] = _PIPELINE
DESCRIPTOR.message_types_by_name['PipelineClassifier'] = _PIPELINECLASSIFIER
DESCRIPTOR.message_types_by_name['PipelineRegressor'] = _PIPELINEREGRESSOR
DESCRIPTOR.message_types_by_name['FeatureDescription'] = _FEATUREDESCRIPTION
DESCRIPTOR.message_types_by_name['Metadata'] = _METADATA
DESCRIPTOR.message_types_by_name['ModelDescription'] = _MODELDESCRIPTION
DESCRIPTOR.message_types_by_name['Model'] = _MODEL

Pipeline = _reflection.GeneratedProtocolMessageType('Pipeline', (_message.Message,), dict(
  DESCRIPTOR = _PIPELINE,
  __module__ = 'Model_pb2'
  # @@protoc_insertion_point(class_scope:CoreML.Specification.Pipeline)
  ))
_sym_db.RegisterMessage(Pipeline)

PipelineClassifier = _reflection.GeneratedProtocolMessageType('PipelineClassifier', (_message.Message,), dict(
  DESCRIPTOR = _PIPELINECLASSIFIER,
  __module__ = 'Model_pb2'
  # @@protoc_insertion_point(class_scope:CoreML.Specification.PipelineClassifier)
  ))
_sym_db.RegisterMessage(PipelineClassifier)

PipelineRegressor = _reflection.GeneratedProtocolMessageType('PipelineRegressor', (_message.Message,), dict(
  DESCRIPTOR = _PIPELINEREGRESSOR,
  __module__ = 'Model_pb2'
  # @@protoc_insertion_point(class_scope:CoreML.Specification.PipelineRegressor)
  ))
_sym_db.RegisterMessage(PipelineRegressor)

FeatureDescription = _reflection.GeneratedProtocolMessageType('FeatureDescription', (_message.Message,), dict(
  DESCRIPTOR = _FEATUREDESCRIPTION,
  __module__ = 'Model_pb2'
  # @@protoc_insertion_point(class_scope:CoreML.Specification.FeatureDescription)
  ))
_sym_db.RegisterMessage(FeatureDescription)

Metadata = _reflection.GeneratedProtocolMessageType('Metadata', (_message.Message,), dict(

  UserDefinedEntry = _reflection.GeneratedProtocolMessageType('UserDefinedEntry', (_message.Message,), dict(
    DESCRIPTOR = _METADATA_USERDEFINEDENTRY,
    __module__ = 'Model_pb2'
    # @@protoc_insertion_point(class_scope:CoreML.Specification.Metadata.UserDefinedEntry)
    ))
  ,
  DESCRIPTOR = _METADATA,
  __module__ = 'Model_pb2'
  # @@protoc_insertion_point(class_scope:CoreML.Specification.Metadata)
  ))
_sym_db.RegisterMessage(Metadata)
_sym_db.RegisterMessage(Metadata.UserDefinedEntry)

ModelDescription = _reflection.GeneratedProtocolMessageType('ModelDescription', (_message.Message,), dict(
  DESCRIPTOR = _MODELDESCRIPTION,
  __module__ = 'Model_pb2'
  # @@protoc_insertion_point(class_scope:CoreML.Specification.ModelDescription)
  ))
_sym_db.RegisterMessage(ModelDescription)

Model = _reflection.GeneratedProtocolMessageType('Model', (_message.Message,), dict(
  DESCRIPTOR = _MODEL,
  __module__ = 'Model_pb2'
  # @@protoc_insertion_point(class_scope:CoreML.Specification.Model)
  ))
_sym_db.RegisterMessage(Model)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('H\003'))
_METADATA_USERDEFINEDENTRY.has_options = True
_METADATA_USERDEFINEDENTRY._options = _descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001'))
# @@protoc_insertion_point(module_scope)
