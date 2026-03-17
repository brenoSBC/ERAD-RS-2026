#include <iostream>
#include <string>
#include <vector>
#include <fstream>

void save_throughput(
    const std::string name,
    const std::string read_file,
    const std::string write_file,
    const std::vector<std::string> config)
{
    std::string line;

    for (int i = 0; i < config.size(); ++i)
    {
        std::ofstream write(write_file + name + "-" + config[i] + "-throughput.txt");
        std::ifstream read(read_file + "-" + config[i] + ".txt");

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
    std::string read_file = "./MPI/executions/";
    std::string write_file = "./MPI/mpi_throughput/";

    std::vector<std::string> three_operator_config = {"111", "121", "131", "141", "161", "181"};
    std::vector<std::string> four_operator_config = {"1111", "1221", "1331", "1441", "1641", "1861"};

    save_throughput("FD", read_file, write_file, three_operator_config);

    return 0;
}