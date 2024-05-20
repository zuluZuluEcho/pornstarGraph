#include "support.h"


bool is_in(const std::string& substring, const std::string& string_)
{
    size_t gevonden = string_.find(substring);
    bool is_bevat = (gevonden != std::string::npos);

    return is_bevat;
}


std::vector<std::string> find_actual_pornstars(const std::map<std::string, unsigned int>& frequencies_pornstars)
{
    std::vector<std::string> actual_pornstars;

    for (const auto& [pornstar, frequency] : frequencies_pornstars)
    {
        if (frequency > 1) // only pornstars that appear several times; half the computation power ...
        {
            actual_pornstars.push_back(pornstar);
        }
    }

    return actual_pornstars;
}


std::vector<std::string> find_actual_files(const std::vector<std::string>& filenames, const std::vector<std::string>& actual_pornstars)
{
    std::vector<std::string> file_in_which_pornstars_appear;

    for (const std::string& pornstar : actual_pornstars)
    {
        for (const std::string& filename : filenames)
        {
            if (is_in(pornstar, filename))
            {
                file_in_which_pornstars_appear.push_back(filename);

                continue;
            }
        }
    }

    return file_in_which_pornstars_appear;
}


std::vector<std::string> make_pairs(const std::vector<std::string>& pornstars)
{
    std::vector<std::string> pornstar_pairs;

    for (unsigned int i = 0; i < pornstars.size(); i++)
    {
        for (unsigned int j = (i + 1); j < pornstars.size(); j++)
        {
            if (pornstars[i] != pornstars[j])
            {
                std::string pair_as_string = pornstars[i] + '|' + pornstars[j];
                pornstar_pairs.push_back(pair_as_string);
            }
        }
    }

    std::cout << "\nThe pornstar pairs have successfully been made ...\n";

    return pornstar_pairs;
}


std::unordered_map<std::string, std::vector<std::string>> give_appearances_pornstars(const std::vector<std::string>& pornstars, const std::vector<std::string>& filenames)
{
    std::unordered_map<std::string, std::vector<std::string>> appearances_pornstars;

    for (const std::string& pornstar : pornstars)
    {
        for (const std::string& filename : filenames)
        {
            if (is_in(pornstar, filename))
            {
                appearances_pornstars[pornstar].push_back(filename);
            }
        }
    }

    return appearances_pornstars;
}


void clear_terminal()
{
    system("clear");
}


void print_progress(const unsigned long int& processed_files, const unsigned long long& total_amount_of_loops)
{
    long double percentage = static_cast<float>(processed_files) / static_cast<float>(total_amount_of_loops) * 100;

    clear_terminal();
    std::cout << "\nProgress: " << percentage << "%.\n";
}




std::vector<std::string> split(const std::string& string_, const char& separator)
{
    std::vector<std::string> string_elements;
    std::string substring;

    for (int i = 0; i < string_.length(); i++)
    {
        char symbol = string_[i];

        if (symbol != separator)
        {
            substring += symbol;
        }
        else
        {
            string_elements.push_back(substring);
            substring = "";
        }
    }

    if (!(substring.empty()))
    {
        string_elements.push_back(substring);
    }

    return string_elements;
}


std::string format_duration(std::chrono::duration<double>& duration)
{
    long long hours = std::chrono::duration_cast<std::chrono::hours>(duration).count();
    duration -= std::chrono::hours(hours);
    long long minutes = std::chrono::duration_cast<std::chrono::minutes>(duration).count();
    duration -= std::chrono::minutes(minutes);
    long long seconds = std::chrono::duration_cast<std::chrono::seconds>(duration).count();

    std::string duration_formatted;

    if (hours != 0)
    {
        duration_formatted += std::to_string(hours) + " h ";
    }
    if ((minutes != 0) || (hours != 0))
    {
        duration_formatted += std::to_string(minutes) + " min ";
    }

    duration_formatted += std::to_string(seconds) + " s";

    return duration_formatted;
}
