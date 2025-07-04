# gRPC HelloWorld Example (Python)

이 예제는 `helloworld.proto` 파일을 기반으로 gRPC 서버(`greeter_server.py`)와 클라이언트(`greeter_client.py`)가 Docker Network로 연결된 다른 Container끼리 통신하는 기본적인 구조를 보여줍니다.

---

## 📦 사전 준비

### 환경

```bash
pip install grpcio grpcio-tools
```

### Docker Network 구성
각각의 Docker Image 및 Container의 이름이 system1, system2로 구성되어있음을 가정합니다.

## 🛠️ 1. proto 파일 컴파일
다음 명령어를 통해 helloworld.proto를 Python 코드로 컴파일합니다:

```bash
python -m grpc_tools.protoc \
  -I. \
  --python_out=. \
  --grpc_python_out=. \
  helloworld.proto
```

이 명령은 현재 디렉토리에 helloworld.proto가 존재한다고 가정합니다.

이를 실행할 시 .proto 파일을 컴파일함으로써, 아래와 같은 파이썬 파일이 자동 생성됩니다.

```bash
helloworld_pb2.py : 메시지 클래스 자동 생성

helloworld_pb2_grpc.py : gRPC 서비스 Stub 자동 생성

```

## 🚀 2. gRPC 서버 실행 (System 2)
system2/greeter_server.py에서 서버를 실행합니다:

```bash
python greeter_server.py
```
서버는 기본적으로 포트 50051에서 대기합니다.

## 💬 3. gRPC 클라이언트 실행 (System 1)
system1/greeter_client.py를 실행하여 서버에 요청을 보냅니다:

```bash
python greeter_client.py
```
클라이언트가 서버로 메시지를 보내면, 서버가 응답을 반환합니다.

📁 디렉토리 구조 예시
```bash
.
├── helloworld.proto
├── helloworld_pb2.py           # ← protoc로 생성됨
├── helloworld_pb2_grpc.py      # ← protoc로 생성됨
├── system1/
│   └── greeter_client.py
└── system2/
    └── greeter_server.py
```

✅ 참고 사항
서버와 클라이언트는 동일 도커 네트워크 상에 있어야 하며, 포트 50051 접근이 가능해야 합니다.

.proto를 수정한 경우, 다시 컴파일해야 합니다.

🙋‍♂️ 문의
해당 예제는 gRPC 공식 문서를 기반으로 제작되었습니다.
자세한 문법은 https://protobuf.dev 및 https://grpc.io/docs를 참고하세요.

