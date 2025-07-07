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
"""The Python implementation of the GRPC helloworld.Greeter server."""

from concurrent import futures
import logging

import grpc
import variable_test_pb2
import variable_test_pb2_grpc


class Transfer(variable_test_pb2_grpc.Transfer):
    def TransferFloat(self, request, context):
        input_double = request.double_val
        input_float = request.float_val
        print(f"clinet input double : {input_double}, input float : {input_float}")
        return variable_test_pb2.FloatVariable(double_val=request.double_val,float_val=request.float_val)
    
    def TransferInt(self, request, context):
        input_int32 = request.int32_val
        input_int64 = request.int64_val
        input_uint32 = request.uint32_val
        input_uint64 = request.uint64_val
        input_sint32 = request.sint32_val
        input_sint64 = request.sint64_val
        input_fixed32 = request.fixed32_val
        input_fixed64 = request.fixed64_val
        input_sfixed32 = request.sfixed32_val
        input_sfixed64 = request.sfixed64_val
        
        print(f"clinet \
            input int32 : {input_int32}, \
            input int64 : {input_int64}, \
            input uint32 : {input_uint32}, \
            input uint64 : {input_uint64}, \
            input sint32 : {input_sint32}, \
            input sint64 : {input_sint64}, \
            input fixed32 : {input_fixed32}, \
            input fixed64 : {input_fixed64}, \
            input sfixed32 : {input_sfixed32}, \
            input sfixed64 : {input_sfixed64}")
        
        return variable_test_pb2.IntVariable(int32_val=input_int32, \
                                             int64_val=input_int64, \
                                             uint32_val=input_uint32, \
                                             uint64_val=input_uint64, \
                                             sint32_val=input_sint32, \
                                             sint64_val=input_sint64, \
                                             fixed32_val=input_fixed32, \
                                             fixed64_val=input_fixed64, \
                                             sfixed32_val=input_sfixed32, \
                                             sfixed64_val=input_sfixed64)
    
    def TransferOther(self, request, context):
        input_bool = request.bool_val
        input_string = request.string_val
        input_bytes = request.bytes_val
        
        print(f"clinet input bool : {input_bool}, \
            input string : {input_string}, \
            input bytes : {input_bytes} ")
        with open("test_image.jpg", "rb") as f:
            image_bytes = f.read()

        return variable_test_pb2.OtherVariable(bool_val=request.bool_val, \
                                            string_val=request.string_val, \
                                            bytes_val=request.bytes_val,)
      
def serve():
    port = "50051"
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    variable_test_pb2_grpc.add_TransferServicer_to_server(Transfer(), server)
    server.add_insecure_port("[::]:" + port)
    server.start()
    print("Server started, listening on " + port)
    server.wait_for_termination()

if __name__ == "__main__":
    logging.basicConfig()
    serve()
