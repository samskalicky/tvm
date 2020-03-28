# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.
# pylint: disable=unused-import
"""Common data structures across all IR variants."""
from .base import SourceName, Span, Node, EnvFunc, load_json, save_json
from .base import structural_equal, assert_structural_equal, structural_hash
from .type import Type, TypeKind, PrimType, PointerType, TypeVar, GlobalTypeVar, TupleType
from .type import TypeConstraint, FuncType, IncompleteType, RelayRefType
from .tensor_type import TensorType
from .type_relation import TypeCall, TypeRelation
from .expr import BaseExpr, PrimExpr, RelayExpr, GlobalVar, Range
from .function import BaseFunc
from .adt import Constructor, TypeData
from .module import IRModule
from .attrs import Attrs, DictAttrs, make_node
from .container import Array, Map

from . import transform
