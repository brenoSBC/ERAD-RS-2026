#!/bin/bash

set -e

mkdir -p FLINK/flink_throughput \
         MPI/mpi_throughput \
         RESIPIPE/resipipe_throughput \
         bin

unzip ./FLINK/stream.zip
unzip ./FLINK/execution.zip
unzip ./MPI/execution.zip
unzip ./RESIPIPE/execution.zip

g++ parsers/flink-parser-stream.cpp    -Wall -Wextra -o bin/fps
g++ parsers/flink-parser-exec-time.cpp -Wall -Wextra -o bin/fpet
g++ parsers/mpi-parser.cpp             -Wall -Wextra -o bin/mp
g++ parsers/resipipe-parser.cpp        -Wall -Wextra -o bin/rp

./bin/fps
./binfpet
./bin/mp
./bin/rp
