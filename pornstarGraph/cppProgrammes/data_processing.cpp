#include "data_processing.h"
#include "support.h"


std::vector<std::string> read_file(const std::string& file_path)
{
    std::fstream file(file_path);
    std::string line;
    std::vector<std::string> file_lines;

    if (file.is_open())
    {
        while (std::getline(file, line))
        {
            file_lines.push_back(line);
        }
    }
    else
    {
        std::cout << "\nUnable to read file.\n";

        return {};
    }

    return file_lines;
}


void save_frequencies_pornstars(const std::map<std::string, unsigned int>& pornstar_frequencies)
{
    std::ofstream frequency_file_pornstars(PATH_FREQUENCIES_PORNSTARS);

    if (frequency_file_pornstars.is_open())
    {
        for (const auto& [pornstar, frequency] : pornstar_frequencies)
        {
            frequency_file_pornstars << pornstar << "," << frequency << "\n";
        }

        frequency_file_pornstars.close();

        std::cout << "\nThe pornstar frequencies have successfully been saved.\n";
    }
    else
    {
        std::cout << "\nUnable to write to pornstar file.\n";

        return;
    }
}


void save_frequencies_pornstar_pairs(const std::unordered_map<std::string, unsigned int>& frequencies_pornstar_pairs)
{
    std::ofstream file_frequencies_pornstar_pairs(PATH_FREQUENCIES_PORNSTAR_PAIRS);

    if (file_frequencies_pornstar_pairs.is_open())
    {
        for (const auto& [pair_concatenated, frequency] : frequencies_pornstar_pairs)
        {
            const std::vector<std::string> pornstars_seperated = split(pair_concatenated, '|');
            const std::string& pornstar1 = pornstars_seperated[0];
            const std::string& pornstar2 = pornstars_seperated[1];

            file_frequencies_pornstar_pairs << pornstar1 << ',' << pornstar2 << ',' << frequency << "\n";

            std::cout << "\nThe pornstar pair frequencies have successfully been saved.\n";
        }
    }
    else
    {
        std::cout << "\nUnable to write to pornstar pairs file.\n";

        return;
    }
}
