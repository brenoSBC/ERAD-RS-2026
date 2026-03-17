#include <iostream>
#include <string>
#include <vector>
#include <fstream>

/*
 * This parser reads timestamps from the "stream" directory and calculates
 * the application throughput.
 *
 * The timestamps correspond to when an event is emitted at the beginning
 * of the pipeline (TransactionParser) and when it is received at the end
 * of the pipeline (ConsoleSink).
 *
 * The total processing time is computed as the difference between the
 * earliest emitted event timestamp and the latest received event timestamp.
 * 
 * This method measures the end-to-end processing time of the streaming
 * pipeline and does not include job submission or deployment overheads,
 * providing a more accurate throughput measurement compared to the other
 * parser, which includes job submission time and related overhead.
 */

double extract_timestamp(const std::string &line)
{
    size_t position = line.find(',');
    return std::stod(line.substr(0, position));
}

double get_max_timestamp(const std::string &filename)
{

    std::ifstream file(filename);
    if (!file) throw std::runtime_error("Error opening: " + filename);

    std::string line;
    double max = 0;

    while (std::getline(file, line))
    {
        double timestamp = extract_timestamp(line);
        if (timestamp > max)
            max = timestamp;
    }
    return max;
}

double get_min_timestamp(const std::string &filename)
{

    std::ifstream file(filename);
    if (!file) throw std::runtime_error("Error opening: " + filename);

    std::string line;
    double min = 1e18;

    while (std::getline(file, line))
    {
        double timestamp = extract_timestamp(line);
        if (timestamp < min)
            min = timestamp;
    }
    return min;
}

void calculate_throughput(
    const std::string name,
    const std::string read_file,
    const std::string write_file,
    const std::string sink_csv,
    const std::string source_csv,
    const std::vector<std::string> config,
    size_t workload)

{
    std::string line;

    for (int i = 0; i < config.size(); ++i)
    {
        std::string base_dir = read_file + name + config[i] + "/";
        std::ofstream write(write_file + name + "-" + config[i] + "-throughput.txt");

        for (int j = 1; j <= 10; ++j)
        {
            std::string dir = base_dir + std::to_string(j) + "/";

            double max_sink = get_max_timestamp(dir + sink_csv);
            double min_source = get_min_timestamp(dir + source_csv);

            double time = max_sink - min_source;
            double throughput = workload / time;

            write << throughput << std::endl;
        }
    }
}

int main(void)
{
    size_t fd_workload = 925000;
    size_t sa_workload = 80000;
    size_t sd_workload = 80000;
    size_t tm_workload = 75000;

    std::string read_file = "./FLINK/stream/";
    std::string write_file = "./FLINK/flink_throughput_stream/";

    std::string sink_csv = "ConsoleSink-received.csv";

    std::string fd_source_csv = "TransactionParser-emitted.csv";
    std::string sa_source_csv = "JsonTweetParser-emitted.csv";
    std::string sd_source_csv = "SensorParser-emitted.csv";
    std::string tm_source_csv = "BeijingTaxiParser-emitted.csv";

    std::vector<std::string> three_operator_config = {"111", "121", "131", "141", "161", "181"};
    std::vector<std::string> four_operator_config = {"1111", "1221", "1331", "1441", "1641", "1861"};

    calculate_throughput("FD", read_file, write_file, sink_csv, fd_source_csv, three_operator_config, fd_workload);
    calculate_throughput("SA", read_file, write_file, sink_csv, sa_source_csv, three_operator_config, sa_workload);
    calculate_throughput("SD", read_file, write_file, sink_csv, sd_source_csv, four_operator_config, sd_workload);
    calculate_throughput("TM", read_file, write_file, sink_csv, tm_source_csv, four_operator_config, tm_workload);

    return 0;
}
