#pragma once

#include <vector>
#include <limits>
#include <iostream>
#include <string>
#include <iomanip>

inline double best_mean(const std::vector<double>& means)
{
    double best = std::numeric_limits<double>::lowest();

    for (double n : means)
    {
        if (n > best)
        {
            best = n;
        }
    }
    return best;
}

inline double relative_difference(
    const std::string name,
    const std::string fw_ref,
    const std::string fw_cmp,
    const std::vector<double> ref,
    const std::vector<double> cmp)
{
    std::cout << std::fixed << std::setprecision(8);

    double best_ref = best_mean(ref);
    double best_cmp = best_mean(cmp);

    if (best_ref == 0.0)
        throw std::runtime_error("Reference value is zero in relative_difference");

    double dr = (best_cmp - best_ref) / best_ref * 100;

    std::cout << "\n########## RELATIVE DIFFERENCE [ " << name << " ] ##########\n";
    std::cout << fw_ref << " (best): " << best_ref << "\n";
    std::cout << fw_cmp << " (best): " << best_cmp << "\n";
    std::cout << "Relative Diff (" << fw_cmp << " vs " << fw_ref << "): " << dr << "%\n";

    return dr;
}