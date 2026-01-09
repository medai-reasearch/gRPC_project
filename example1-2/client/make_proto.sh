python -m grpc_tools.protoc \
  -I. \
  --python_out=. \
  --grpc_python_out=. \
  variable_test.proto