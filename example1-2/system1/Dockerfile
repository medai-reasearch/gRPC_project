FROM python:3.10-slim

# 시스템 패키지 설치
RUN apt-get update && apt-get install -y \
    build-essential \
    libglib2.0-0 \
    libsm6 \
    libxrender1 \
    libxext6 \
    git \
    curl \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app
# 4. pip 최신화
RUN pip install --upgrade pip setuptools wheel

# gRPC 관련 라이브러리 설치
COPY requirements-grpc.txt .
RUN pip install --no-cache-dir -r requirements-grpc.txt

# 예제 파일 생성
RUN git clone -b v1.73.0 --depth 1 --shallow-submodules https://github.com/grpc/grpc

# 마이크로 서비스 관련 라이브러리 설치
COPY requirements.txt .
RUN pip install -r requirements.txt

# 쉘 환경으로 진입
CMD ["/bin/bash"]