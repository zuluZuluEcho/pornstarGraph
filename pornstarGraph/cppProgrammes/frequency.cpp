#include "frequency.h"
#include "support.h"


std::map<std::string, unsigned int> count_frequency_pornstars(const std::vector<std::string>& pornstars, const std::vector<std::string>& filenames)
{
    std::map<std::string, unsigned int> frequency_pornstars;

    std::cout << "\nThe pornstar frequencies are being counted ...\n";

    for (const std::string& pornstar : pornstars)
    {
        for (const std::string& filename : filenames)
        {
            if (is_in(pornstar, filename))
            {
                frequency_pornstars[pornstar] += 1;
            }
        }
    }

    return frequency_pornstars;
}


std::unordered_map<std::string, unsigned int> count_frequency_pornstar_pairs(const std::vector<std::string>& pornstar_pairs,
                                                                    const std::unordered_map<std::string, std::vector<std::string>>& appearances_pornstars)
{
    const unsigned long long TOTAL_AMOUNT_OF_PAIRS = pornstar_pairs.size();

    unsigned long int count_processed_files = 0;

    std::unordered_map<std::string, unsigned int> frequency_pornstar_pairs;

    std::cout << "\nThe pornstar pair frequencies are being counted ...\n";

    for (const auto& pornstars_concatenated : pornstar_pairs)
    {
        const std::vector<std::string> pornstar_pairs_separated = split(pornstars_concatenated, '|');
        const std::string& pornstar1 = pornstar_pairs_separated[0];
        const std::string& pornstar2 = pornstar_pairs_separated[1];

        const std::vector<std::string>& appearances_pornstar1 = appearances_pornstars.at(pornstar1);  // voor de const

        for (const std::string& filename : appearances_pornstar1)
        {
            if (is_in(pornstar2, filename))
            {
                frequency_pornstar_pairs[pornstars_concatenated]++;
            }
        }

        count_processed_files++;

        print_progress(count_processed_files, TOTAL_AMOUNT_OF_PAIRS);
    }

    return frequency_pornstar_pairs;
}
