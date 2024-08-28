#include <iostream>
#include <vector>
#include <map>
#include <tuple>
#include <set>
#include <algorithm>
#include <fstream>
#include <sstream>

struct Event {
    int id;
    std::string type;

    bool operator<(const Event& other) const {
        return std::tie(id, type) < std::tie(other.id, other.type);
    }

    bool operator==(const Event& other) const {
        return std::tie(id, type) == std::tie(other.id, other.type);
    }
};

std::vector<std::vector<Event>> read_interleavings(const std::string& filename) {
    std::vector<std::vector<Event>> interleavings;
    std::ifstream file(filename);
    std::string line;
    while (std::getline(file, line)) {
        std::vector<Event> interleaving;
        std::istringstream iss(line);
        int id;
        std::string type;
        while (iss >> id >> type) {
            interleaving.push_back({id, type});
        }
        interleavings.push_back(interleaving);
    }
    return interleavings;
}

std::set<Event> read_independent_events(const std::string& filename) {
    std::set<Event> independent_events;
    std::ifstream file(filename);
    int id;
    std::string type;
    while (file >> id >> type) {
        independent_events.insert({id, type});
    }
    return independent_events;
}

std::vector<int> independent_events_indices(const std::set<Event>& independent_events, const std::vector<Event>& interleaving) {
    std::vector<int> indices;
    for (size_t i = 0; i < interleaving.size(); ++i) {
        if (independent_events.find(interleaving[i]) != independent_events.end()) {
            indices.push_back(static_cast<int>(i));
        }
    }
    return indices;
}

std::vector<std::vector<Event>> exclude(const std::vector<std::vector<Event>>& interleavings, const std::vector<std::vector<Event>>& to_exclude) {
    std::vector<std::vector<Event>> result;
    for (const auto& il : interleavings) {
        if (std::find(to_exclude.begin(), to_exclude.end(), il) == to_exclude.end()) {
            result.push_back(il);
        }
    }
    return result;
}

int main() {
    std::vector<std::vector<Event>> ILs = read_interleavings("interleavings.dl");

    std::set<Event> IEvs = read_independent_events("independent_events.dl");

    std::vector<std::vector<Event>> grouped_interleavings;
    std::map<std::vector<int>, std::vector<std::vector<Event>>> grouped_by_indices;

    std::vector<std::vector<Event>> EI;

    for (const auto& il : ILs) {
        std::vector<int> indices = independent_events_indices(IEvs, il);
        if (grouped_by_indices.find(indices) == grouped_by_indices.end()) {
            grouped_by_indices[indices] = {};
        }
        grouped_by_indices[indices].push_back(il);
    }

    for (const auto& [idx, interleavings] : grouped_by_indices) {
        int index_first = idx[0];
        int index_last = idx.back();

        for (const auto& il : interleavings) {
            std::vector<Event> Evs(il.begin() + index_first, il.begin() + index_last + 1);

            bool all_independent = true;
            for (const auto& ev : Evs) {
                for (const auto& iev : IEvs) {
                    if (!(ev == iev)) {
                        all_independent = false;
                        break;
                    }
                }
                if (!all_independent) break;
            }

            if (all_independent) {
                grouped_interleavings.push_back(il);
            }
        }
    }

    EI = exclude(ILs, grouped_interleavings);

    std::ofstream outfile("independent_interleavings.dl");
    for (const auto& il : EI) {
        for (const auto& event : il) {
            outfile << event.id << " " << event.type << " ";
        }
        outfile << "\n";
    }
    outfile.close();

    return 0;
}
