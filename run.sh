#!/bin/bash
set -e

export PGPASSWORD="$DB_PASSWORD"

echo "wait db..."
until pg_isready -h "$DB_HOST" -U "$DB_USER" -d "$DB_NAME" >/dev/null 2>&1
do
  sleep 1
done

echo "build..."
g++ my_gemm_float.cpp -O2 -pthread -o my_gemm_float
g++ my_gemm_double.cpp -O2 -pthread -o my_gemm_double
g++ test_gemm_openblas_float.cpp -O2 -lopenblas -o test_gemm_openblas_float
g++ test_gemm_openblas_double.cpp -O2 -lopenblas -o test_gemm_openblas_double

echo "create table..."
psql -h "$DB_HOST" -U "$DB_USER" -d "$DB_NAME" -c "CREATE TABLE IF NOT EXISTS results (id SERIAL PRIMARY KEY, program TEXT, output TEXT, created_at TIMESTAMP DEFAULT NOW());"

save_result() {
  name="$1"
  file="$2"
  text=$(cat "$file" | sed "s/'/''/g")
  psql -h "$DB_HOST" -U "$DB_USER" -d "$DB_NAME" -c "INSERT INTO results (program, output) VALUES ('$name', '$text');"
}

echo "run tests..."
./my_gemm_float > my_gemm_float.txt
save_result "my_gemm_float" "my_gemm_float.txt"

./my_gemm_double > my_gemm_double.txt
save_result "my_gemm_double" "my_gemm_double.txt"

./test_gemm_openblas_float > test_gemm_openblas_float.txt
save_result "test_gemm_openblas_float" "test_gemm_openblas_float.txt"

./test_gemm_openblas_double > test_gemm_openblas_double.txt
save_result "test_gemm_openblas_double" "test_gemm_openblas_double.txt"

echo "done"
psql -h "$DB_HOST" -U "$DB_USER" -d "$DB_NAME" -c "SELECT id, program, created_at FROM results ORDER BY id;"
