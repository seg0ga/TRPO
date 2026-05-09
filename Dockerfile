FROM ubuntu:22.04

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y \
    g++ \
    make \
    libopenblas-dev \
    postgresql-client \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY my_gemm_float.cpp .
COPY my_gemm_double.cpp .
COPY test_gemm_openblas_float.cpp .
COPY test_gemm_openblas_double.cpp .
COPY run.sh .

RUN chmod +x run.sh

CMD ["./run.sh"]
