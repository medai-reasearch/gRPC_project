# Copyright 2015 gRPC authors.
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
"""The Python implementation of the GRPC helloworld.Greeter client."""

from __future__ import print_function

import logging

import grpc
import variable_test_pb2
import variable_test_pb2_grpc

class request_float:
    def __init__(
        self,
        double_val=None,
        float_val=None
    ):
        self.double_val: float = double_val
        self.float_val: float = float_val ## float 범위를 초과한 값인 double의 영역을 전송하면

class request_int:
    def __init__(self,
                 int32_val: int = None,
                 int64_val: int = None,
                 uint32_val: int = None,
                 uint64_val: int = None,
                 sint32_val: int = None,
                 sint64_val: int = None,
                 fixed32_val: int = None,
                 fixed64_val: int = None,
                 sfixed32_val: int = None,
                 sfixed64_val: int = None):
        self.int32_val = int32_val
        self.int64_val = int64_val
        self.uint32_val = uint32_val
        self.uint64_val = uint64_val
        self.sint32_val = sint32_val
        self.sint64_val = sint64_val
        self.fixed32_val = fixed32_val
        self.fixed64_val = fixed64_val
        self.sfixed32_val = sfixed32_val
        self.sfixed64_val = sfixed64_val
    
class request_other:
    def __init__(self,
                 bool_val: bool = None,
                 string_val: str = None,
                 bytes_val: bytes = None):
        self.bool_val = bool_val
        self.string_val = string_val
        self.bytes_val = bytes_val

def print_request_fields(obj):
    if hasattr(obj, 'ListFields'):
        # proto 메시지인 경우
        for field_desc, value in obj.ListFields():
            print(f"{field_desc.name} : {value}")
    else:
        # 일반 클래스
        for key, value in vars(obj).items():
            print(f"{key} : {value}")

def normal_run():
    ## 모든 입력값들이 해당 전송 포맷에 알맞게
    rf = request_float(
        double_val=0.8282,
        float_val=0.1357
    )

    ri = request_int(
        int32_val=1,
        int64_val=2,
        uint32_val=3,
        uint64_val=4,
        sint32_val=5,
        sint64_val=6,
        fixed32_val=7,
        fixed64_val=8,
        sfixed32_val=9,
        sfixed64_val=10
    )

    ro = request_other(
        bool_val=True,
        string_val="안녕하세요. 감사해요. 잘있어요. 다시만나요.",
        bytes_val=b"And I say hey I'm gonna make it smile smile smile away"
    )
        
    print("Start to send our data!")
    with grpc.insecure_channel("server:50051") as channel:
        stub = variable_test_pb2_grpc.TransferStub(channel)
        response_rf = stub.TransferFloat(variable_test_pb2.FloatVariable(**vars(rf)))
        response_ri = stub.TransferInt(variable_test_pb2.IntVariable(**vars(ri)))
        response_ro = stub.TransferOther(variable_test_pb2.OtherVariable(**vars(ro)))
    print("float 형식에 다시 돌아온 respone! 입력한 입력값과 동일해야 합니다!")
    print_request_fields(response_rf)
    print("int 형식에 다시 돌아온 respone! 입력한 입력값과 동일해야 합니다!")
    print_request_fields(response_ri)
    print("other 형식에 다시 돌아온 respone! 입력한 입력값과 동일해야 합니다!")
    print_request_fields(response_ro)

def image_run():
    # 이미지 읽기
    with open("test_image.jpg", "rb") as f:
        image_bytes = f.read()

    ro = request_other(
        bool_val=True,
        string_val="deemo",
        bytes_val=image_bytes
    )
        
    print("Start to send our data!")
    with grpc.insecure_channel("server:50051") as channel:
        stub = variable_test_pb2_grpc.TransferStub(channel)
        
        response_ro = stub.TransferOther(variable_test_pb2.OtherVariable(**vars(ro)))
    
    with open(f"response_{response_ro.string_val}.jpg", "wb") as f:
        f.write(response_ro.bytes_val)
        
if __name__ == "__main__":
    logging.basicConfig()
    image_run()
