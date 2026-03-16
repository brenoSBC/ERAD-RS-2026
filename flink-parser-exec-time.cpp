#include <iostream>
#include <string>
#include <vector>
#include <fstream>

/*
 * This parser reads execution times from the "execution_times" directory
 * and calculates the application throughput.
 *
 * The timestamps in this directory correspond to the machine time when
 * the job was submitted and when it finished. Therefore, the calculated
 * throughput includes the submission time overhead.
 *
 * Because of this, the results may vary depending on the machine and
 * execution environment.
 *
 * The throughput values used in the paper are obtained with
 * "flink-parser-stream.cpp", which uses a more precise measurement method.
 */

double to_seconds(std::string time)
{

    double hour = std::stod(time.substr(0, 2)) * 3600;
    double minute = std::stod(time.substr(3, 2)) * 60;
    double second = std::stod(time.substr(6, 2));
    double micro = std::stod(time.substr(9, 6)) / 1000000.0;

    return hour + minute + second + micro;
}

void calculate_throughput(
    const std::string name,
    const std::string read_file,
    const std::string write_file,
    const std::vector<std::string> config,
    size_t workload)
{
    std::string line;

    for (int i = 0; i < config.size(); ++i)
    {
        std::ofstream write(write_file + name + "-" + config[i] + "-throughput.txt");

        for (int j = 1; j <= 10; ++j)
        {
            std::ifstream read(read_file + std::to_string(j) + "-" + config[i] + ".txt");

            if (!read.is_open()) throw std::runtime_error("Error opening input file");

            std::getline(read, line);

            std::string start_time = line.substr(11, 15);
            std::string end_time = line.substr(40);

            double start_in_seconds = to_seconds(start_time);
            double end_in_seconds = to_seconds(end_time);

            double exec_time = (end_in_seconds - start_in_seconds);

            double throughput = workload / exec_time;

            write << throughput << std::endl;

            read.close();
        }
        write.close();
    }
}

int main(void)
{
    size_t fd_workload = 925000;
    size_t sa_workload = 80000;
    size_t sd_workload = 80000;
    size_t tm_workload = 75000;

    std::string fd_read_file = "./FLINK/execution_times/frauddetection-";
    std::string sa_read_file = "./FLINK/execution_times/sentimentanalysis-";
    std::string sd_read_file = "./FLINK/execution_times/spikedetection-";
    std::string tm_read_file = "./FLINK/execution_times/trafficmonitoring-";

    std::string write_file = "./FLINK/flink_throughput_exec_time/";

    std::vector<std::string> three_operator_config = {"111", "121", "131", "141", "161", "181"};
    std::vector<std::string> four_operator_config = {"1111", "1221", "1331", "1441", "1641", "1861"};

    calculate_throughput("FD", fd_read_file, write_file, three_operator_config, fd_workload);
    calculate_throughput("SA", sa_read_file, write_file, three_operator_config, sa_workload);
    calculate_throughput("SD", sd_read_file, write_file, four_operator_config, sd_workload);
    calculate_throughput("TM", tm_read_file, write_file, four_operator_config, tm_workload);

    return 0;
}