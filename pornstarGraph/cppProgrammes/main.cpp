#include <iostream>
#include <string>
#include <vector>
#include <unordered_map>
#include <map>
#include <chrono>
#include <Windows.h>
#include <mmsystem.h>
#include "support.h"
#include "data_processing.h"
#include "frequency.h"


#pragma comment(lib, "winmm.lib")


const std::string PATH_STAR_FILE = "<YOUR PATH>/pornstarGraph/data/pornstars.txt";
const std::string PATH_FILENAME_FILE = "<YOUR PATH>/pornstarGraph/data/filenamesForCpp.txt";
const CHAR *const PATH_SOUND_FILE = "<YOUR PATH>/pornstarGraph/sounds/bafBrein.wav";


int main()
{
    auto start_time = std::chrono::high_resolution_clock::now();

    const std::vector<std::string> PORNSTARS = read_file(PATH_STAR_FILE);
    const std::vector<std::string> FILENAMES = read_file(PATH_FILENAME_FILE);

    std::cout << "\nThe data of the filenames and pornstars have successfully been read.\n";

    const std::map<std::string, unsigned int> frequencies_pornstars = count_frequency_pornstars(PORNSTARS, FILENAMES);
    save_frequencies_pornstars(frequencies_pornstars);

    const std::vector<std::string> actual_pornstars = find_actual_pornstars(frequencies_pornstars);
    const std::vector<std::string> pornstar_pairs = make_pairs(actual_pornstars);

    std::vector<std::string> file_in_which_pornstars_appear = find_actual_files(FILENAMES, actual_pornstars);
    std::unordered_map<std::string, std::vector<std::string>> pornstar_appearances = give_appearances_pornstars(actual_pornstars, file_in_which_pornstars_appear);

    const std::unordered_map<std::string, unsigned int> frequency_pornstar_pairs = count_frequency_pornstar_pairs(pornstar_pairs, pornstar_appearances);
    save_frequencies_pornstar_pairs(frequency_pornstar_pairs);


    auto end_time = std::chrono::high_resolution_clock::now();
    std::chrono::duration<double> duration = end_time - start_time;

    clear_terminal();
    PlaySound(TEXT(PATH_SOUND_FILE), nullptr, SND_FILENAME | SND_SYNC);
    std::cout << "\nFinished! It took '" << format_duration(duration) << "'.\n";

    return 0;
}
