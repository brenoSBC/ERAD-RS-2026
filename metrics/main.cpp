#include <iostream>
#include <string>
#include <vector>
#include <fstream>

#include "vectors.hpp"
#include "populate_vector.hpp"
#include "mean.hpp"

int main(void)
{

    std::string file_flink = "./FLINK/flink_throughput_stream/";
    std::string file_mpi = "./MPI/mpi_throughput/";
    std::string file_res = "./RESIPIPE/resipipe_throughput/";

    std::vector<std::string> three_operator_config = {"111", "121", "131", "141", "161", "181"};
    std::vector<std::string> four_operator_config = {"1111", "1221", "1331", "1441", "1641", "1861"};

    populate_vector("FD", "Flink", file_flink, three_operator_config, fd_flink);
    populate_vector("SA", "Flink", file_flink, three_operator_config, sa_flink);
    populate_vector("SD", "Flink", file_flink, four_operator_config, sd_flink);
    populate_vector("TM", "Flink", file_flink, four_operator_config, tm_flink);

    populate_vector("FD", "OpenMPI", file_mpi, three_operator_config, fd_mpi);
    populate_vector("SA", "OpenMPI", file_mpi, three_operator_config, sa_mpi);
    populate_vector("SD", "OpenMPI", file_mpi, four_operator_config, sd_mpi);
    populate_vector("TM", "OpenMPI", file_mpi, four_operator_config, tm_mpi);

    populate_vector("FD", "ResiPipe", file_res, three_operator_config, fd_res);
    populate_vector("SA", "ResiPipe", file_res, three_operator_config, sa_res);
    populate_vector("SD", "ResiPipe", file_res, four_operator_config, sd_res);
    populate_vector("TM", "ResiPipe", file_res, four_operator_config, tm_res);

    fd_flink_mean = mean("FD", "Flink", fd_flink);
    sa_flink_mean = mean("SA", "Flink", sa_flink);
    sd_flink_mean = mean("SD", "Flink", sd_flink);
    tm_flink_mean = mean("TM", "Flink", tm_flink);

    fd_mpi_mean = mean("FD", "OpenMPI",fd_mpi);
    sa_mpi_mean = mean("SA", "OpenMPI",sa_mpi);
    sd_mpi_mean = mean("SD", "OpenMPI",sd_mpi);
    tm_mpi_mean = mean("TM", "OpenMPI",tm_mpi);

    fd_res_mean = mean("FD", "ResiPipe", fd_res);
    sa_res_mean = mean("SA", "ResiPipe", sa_res);
    sd_res_mean = mean("SD", "ResiPipe", sd_res);
    tm_res_mean = mean("TM", "ResiPipe", tm_res);

    return 0;
}