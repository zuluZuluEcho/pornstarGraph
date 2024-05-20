#ifndef FREQUENCY_H
#define FREQUENCY_H


#include <iostream>
#include <string>
#include <map>
#include <unordered_map>
#include <vector>


std::map<std::string, unsigned int> count_frequency_pornstars(const std::vector<std::string>& pornstars, const std::vector<std::string>& filenames);
std::unordered_map<std::string, unsigned int> count_frequency_pornstar_pairs(const std::vector<std::string>& pornstar_pairs,
                                                                             const std::unordered_map<std::string, std::vector<std::string>>& appearances_pornstars);


#endif
