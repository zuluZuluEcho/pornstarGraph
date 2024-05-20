#ifndef SUPPORT_H
#define SUPPORT_H


#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <chrono>
#include <unordered_map>


bool is_in(const std::string& substring, const std::string& string_);
std::vector<std::string> find_actual_pornstars(const std::map<std::string, unsigned int>& pornstar_frequencies);
std::vector<std::string> find_actual_files(const std::vector<std::string>& filenames, const std::vector<std::string>& actual_pornstars);
std::vector<std::string> make_pairs(const std::vector<std::string>& pornstars);
std::unordered_map<std::string, std::vector<std::string>> give_appearances_pornstars(const std::vector<std::string>& pornstars, const std::vector<std::string>& filenames);
void clear_terminal();
void print_progress(const unsigned long int& processed_files, const unsigned long long& total_amount_of_loops);
std::vector<std::string> split(const std::string& string_, const char& separator);
std::string format_duration(std::chrono::duration<double>& duration);


#endif
