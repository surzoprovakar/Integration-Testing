#include <iostream>
#include <fstream>
#include <vector>
#include <map>
#include <set>
#include <sstream>
#include <string>
#include <algorithm>

struct Event
{
    int id;
    bool operator<(const Event &other) const
    {
        return id < other.id;
    }
};

std::vector<std::vector<Event>> read_interleavings(const std::string &filename)
{
    std::ifstream file(filename);
    std::vector<std::vector<Event>> interleavings;
    if (!file.is_open())
    {
        throw std::runtime_error("Could not open file for reading.");
    }
    std::string line;
    while (std::getline(file, line))
    {
        std::vector<Event> interleaving;
        std::istringstream ss(line);
        int id;
        while (ss >> id)
        {
            interleaving.push_back(Event{id});
        }
        interleavings.push_back(interleaving);
    }
    file.close();
    return interleavings;
}

std::vector<Event> read_events(const std::string &filename)
{
    std::ifstream file(filename);
    std::vector<Event> events;
    if (!file.is_open())
    {
        throw std::runtime_error("Could not open file for reading.");
    }
    std::string line;
    while (std::getline(file, line))
    {
        std::istringstream ss(line);
        int id;
        while (ss >> id)
        {
            events.push_back(Event{id});
        }
    }
    file.close();
    return events;
}

std::vector<int> find_event_indices(const std::vector<Event> &events, const std::vector<Event> &interleaving)
{
    std::vector<int> indices;
    for (const auto &event : events)
    {
        auto it = std::find(interleaving.begin(), interleaving.end(), event);
        if (it != interleaving.end())
        {
            indices.push_back(std::distance(interleaving.begin(), it));
        }
    }
    return indices;
}

std::vector<int> concat(const std::vector<int> &v1, const std::vector<int> &v2)
{
    std::vector<int> result = v1;
    result.insert(result.end(), v2.begin(), v2.end());
    return result;
}

std::vector<std::vector<Event>> exclude(const std::vector<std::vector<Event>> &ILs,
                                        const std::map<std::vector<int>, std::vector<std::vector<Event>>> &grouped_by_indices)
{
    std::vector<std::vector<Event>> result = ILs;
    for (const auto &pair : grouped_by_indices)
    {
        for (const auto &il : pair.second)
        {
            auto it = std::remove(result.begin(), result.end(), il);
            if (it != result.end())
            {
                result.erase(it, result.end());
            }
        }
    }
    return result;
}

void write_interleavings(const std::string &filename, const std::vector<std::vector<Event>> &interleavings)
{
    std::ofstream file(filename);
    if (!file.is_open())
    {
        throw std::runtime_error("Could not open file for writing.");
    }
    for (const auto &il : interleavings)
    {
        for (const auto &e : il)
        {
            file << e.id << " ";
        }
        file << std::endl;
    }
    file.close();
}

int main()
{
    try
    {
        const std::string interleavings_file = "interleavings.txt";
        const std::string predecessor_events_file = "predecessor_events.txt";
        const std::string successor_events_file = "successor_events.txt";
        const std::string output_file = "failed_ops.dl";

        std::vector<std::vector<Event>> ILs = read_interleavings(interleavings_file);
        std::vector<Event> PEvents = read_events(predecessor_events_file);
        std::vector<Event> SEvents = read_events(successor_events_file);

        std::map<std::vector<int>, std::vector<std::vector<Event>>> grouped_by_indices;

        std::vector<std::vector<Event>> FI;

        for (const auto &il : ILs)
        {
            std::vector<int> pIdx = find_event_indices(PEvents, il);

            std::vector<int> sIdx = find_event_indices(SEvents, il);

            bool valid = true;
            for (const auto &p : pIdx)
            {
                bool found = false;
                for (const auto &s : sIdx)
                {
                    if (p < s)
                    {
                        found = true;
                        break;
                    }
                }
                if (!found)
                {
                    valid = false;
                    break;
                }
            }

            if (valid)
            {
                for (size_t i = 0; i < pIdx.size() - 1; ++i)
                {
                    if (pIdx[i] >= pIdx[i + 1] || sIdx[i] >= sIdx[i + 1])
                    {
                        valid = false;
                        break;
                    }
                }
            }

            if (valid)
            {
                std::vector<int> concatenated = concat(pIdx, sIdx);
                if (grouped_by_indices.find(concatenated) == grouped_by_indices.end())
                {
                    grouped_by_indices[concatenated] = {};
                }
                grouped_by_indices[concatenated].push_back(il);
            }
        }

        FI = exclude(ILs, grouped_by_indices);

        write_interleavings(output_file, FI);
        std::cout << "Failed operations have been written to " << output_file << std::endl;
    }
    catch (const std::exception &e)
    {
        std::cerr << "Error: " << e.what() << std::endl;
        return 1;
    }

    return 0;
}