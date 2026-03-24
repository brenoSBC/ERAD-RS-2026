#pragma once

#include <iostream>
#include <string>
#include <vector>
#include <iomanip>

inline std::vector<double> mean(
    const std::string name,
    const std::string fw,
    const std::vector<std::vector<double>> &app_vector)
{
    std::cout << std::fixed << std::setprecision(8);
    
    std::vector<double> means;

    std::cout << "\n" << fw << " ########## MEAN PER CONFIG [ " << name << " ] ##########" << std::endl;

    for (size_t i = 0; i < app_vector.size(); ++i)
    {
        double total = 0;

       for (size_t j = 0; j < app_vector[i].size(); ++j)
        {
            total += app_vector[i][j];
        }

        double m = total / app_vector[i].size();

        means.push_back(m);

        std::cout << "Config " << i + 1 << ": " << m << std::endl;
    }
    return means;
}