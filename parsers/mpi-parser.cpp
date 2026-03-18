#include <iostream>
#include <string>
#include <vector>
#include <fstream>

void save_throughput(
    const::std::string write_name,
    const std::string name,
    const std::string read_file,
    const std::string write_file,
    const std::vector<std::string> config)
{
    std::string line;

    for (size_t i = 0; i < config.size(); ++i)
    {
        std::ofstream write(write_file + write_name + "-" + config[i] + "-throughput.txt");

        std::ifstream read(read_file + name + "_" + config[i] + ".txt");
        std::cout << read_file << name << "_" << config[i] << ".txt" << std::endl;
        if (!read.is_open()) throw std::runtime_error("Error opening input file");

        while (std::getline(read, line))
        {
            if (line.find("Throughput") != std::string::npos)
            {
                size_t position = line.find(":");
                std::string throughput = line.substr(position + 1);

                throughput.erase(0, throughput.find_first_not_of(" \t"));

                throughput = throughput.substr(0, throughput.find(" "));
                write << throughput << std::endl;
            }
        }
    }
}

int main(void)
{
    std::string read_file = "../MPI/execution/";
    std::string write_file = "../MPI/mpi_throughput/";

    std::vector<std::string> three_operator_config = {"111", "121", "131", "141", "161", "181"};
    std::vector<std::string> four_operator_config = {"1111", "1221", "1331", "1441", "1641", "1861"};

    save_throughput("FD" ,"fd_demand", read_file, write_file, three_operator_config);
    save_throughput("SA", "sa_demand", read_file, write_file, three_operator_config);
    save_throughput("SD", "sd_demand", read_file, write_file, four_operator_config);
    save_throughput("TM", "tm_demand", read_file, write_file, four_operator_config);

    return 0;
}