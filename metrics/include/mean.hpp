#pragma once

#include <iostream>
#include <string>
#include <vector>

inline double mean(const::std::string name, const::std::string fw, std::vector<double> &app_vector)
{
    double total = 0;
    for(double n : app_vector) {
        total += n;
    }
    double mean = total / app_vector.size();

    std::cout << "\n" << fw << " ########## MEAN [ " << name << " ] ##########" << std::endl;
    std::cout << mean << std::endl;

    return mean;
}





