#!/bin/bash

set -e

mkdir -p FLINK/flink_throughput_stream \
         MPI/mpi_throughput \
         RESIPIPE/resipipe_throughput \
         bin

unzip ./FLINK/stream.zip -d ./FLINK/
unzip ./MPI/execution.zip -d ./MPI/
unzip ./RESIPIPE/execution.zip -d ./RESIPIPE/

g++ parsers/flink-parser-stream.cpp    -Wall -Wextra -o bin/fps
g++ parsers/mpi-parser.cpp             -Wall -Wextra -o bin/mp
g++ parsers/resipipe-parser.cpp        -Wall -Wextra -o bin/rp

./bin/fps
./bin/mp
./bin/rp

python3 plots/plot.py
