#include <iostream>
#include <string>
#include <vector>
#include <ctime>
#include <fstream>
#include <sstream>
#include <iomanip>

// %Y -> ano
// %m -> mês
// %d -> dia
// %H -> hora
// %M -> minuto
// %S -> segundo

void calculate_throughput(std::string app_name, std::string read_file_name, std::string write_file_name, size_t app_workload, std::vector<std::string> app_config) {

    std::string line;
    
    for(int i = 0; i < app_config.size(); ++i) {
        
        std::ofstream write_file(write_file_name + app_name + "-" + app_config[i] + "-throughput.txt");
        
        for(int j = 1; j <= 10 ; ++j) {

            std::tm tm1 = {};
            std::tm tm2 = {};

            std::ifstream read_file(read_file_name + std::to_string(j) + "-" + app_config[i] + ".txt");

            if (!read_file.is_open()) {
                std::cout << "\nErro ao abrir algum arquivo\n";
                exit(0);
            }       
            
            std::getline(read_file, line);

            std::string s_time_1 = line.substr(0, 19);
            std::string s_time_2 = line.substr(29, 19);


            std::cout << "TEMPO EM STRING 1: " << s_time_1 << std::endl;
            std::cout << "TEMPO EM STRING 2: " << s_time_2 << std::endl;


            std::istringstream ss1(s_time_1.substr(0,19));
            std::istringstream ss2(s_time_2.substr(0,19));


            std::cout << "TEMPO EM SS 1: " << ss1.str() << std::endl;
            std::cout << "TEMPO EM SS 2: " << ss2.str() << std::endl;


            ss1 >> std::get_time(&tm1, "%Y-%m-%d %H:%M:%S");
            ss2 >> std::get_time(&tm2, "%Y-%m-%d %H:%M:%S");

            time_t convert_time_1 = mktime(&tm1);
            time_t convert_time_2 = mktime(&tm2);

            double exec_time = difftime(convert_time_2, convert_time_1);

            double throughput = app_workload / exec_time;

            write_file << throughput << std::endl;

            read_file.close();        
        }
        write_file.close();
    }
}

int main(void) {

    size_t fd_workload = 925000;
    size_t sa_workload = 80000;
    size_t sd_workload = 80000;
    size_t tm_workload = 75000;

    std::string fd_read_file_name = "./FLINK/execution_times/frauddetection-";
    std::string sa_read_file_name = "./FLINK/execution_times/sentimentanalysis-";
    std::string sd_read_file_name = "./FLINK/execution_times/spikedetection-";
    std::string tm_read_file_name = "./FLINK/execution_times/trafficmonitoring-";

    std::string write_file_name = "./FLINK/flink_throughput/";
    
    std::vector<std::string> three_operator_config = {"111", "121", "131", "141", "161", "181"};
    std::vector<std::string> four_operator_config  = {"1111", "1221", "1331", "1441", "1641", "1861"};

    calculate_throughput("fd", fd_read_file_name, write_file_name, fd_workload, three_operator_config);
    // calculate_throughput("sa", sa_read_file_name, write_file_name, sa_workload, three_operator_config);
    // calculate_throughput("sd", sd_read_file_name, write_file_name, sd_workload, four_operator_config);
    // calculate_throughput("tm", tm_read_file_name, write_file_name, tm_workload, four_operator_config);

    return 0;
}