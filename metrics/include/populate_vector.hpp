#pragma once

#include <iostream>
#include <string>
#include <vector>
#include <fstream>
#include <stdexcept>

inline void populate_vector(
    const ::std::string name,
    const ::std::string fw,
    const ::std::string file,
    const ::std::vector<std::string> config,
    std::vector<std::vector<double>> &app_vector)
{

    std::cout << "\n" << fw << " ########## POPULATE VECTOR [ " << name << " ] ##########" << std::endl;
    std::string line;

    for (size_t i = 0; i < config.size(); ++i)
    {
        // std::cout << file << name << "-" << config[i] << "-throughput.txt" << std::endl;
        std::ifstream read(file + name + "-" + config[i] + "-throughput.txt");

        std::vector<double> temp;
        std::cout << "Config: " << i+1 << std::endl;

        if (!read.is_open())
                throw std::runtime_error("Error opening input file");

        for (size_t j = 0; j < 10; ++j)
        {
            std::getline(read, line);

            temp.push_back(std::stod(line));
            std::cout << "Value: " << line << std::endl;
        }
        app_vector.push_back(temp);
        std::cout << "#######################################################" << std::endl;
    }
}
