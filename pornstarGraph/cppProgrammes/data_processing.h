#ifndef DATAVERWERKING_H
#define DATAVERWERKING_H


# include <iostream>
#include <fstream>
#include<vector>
#include <map>
#include <unordered_map>


const std::string PATH_FREQUENCIES_PORNSTARS = "<YOUR PATH>/pornstarGraph/data/frequencyPerPornstar.txt";
const std::string PATH_FREQUENCIES_PORNSTAR_PAIRS = "<YOUR PATH>/pornstarGraph/data/frequencyPerPornstarPair.txt";


std::vector<std::string> read_file(const std::string& file_path);
void save_frequencies_pornstars(const std::map<std::string, unsigned int>& frequencies_pornstars);
void save_frequencies_pornstar_pairs(const std::unordered_map<std::string, unsigned int>& frequencies_pornstar_pairs);


#endif