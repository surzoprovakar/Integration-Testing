#include <iostream>
#include <vector>
#include <map>
#include <tuple>
#include <fstream>
#include <sstream>


struct Event {
    int replicaId;
    std::string type;
};

std::vector<std::vector<Event>> read_interleavings(const std::string& filename) {
    std::vector<std::vector<Event>> interleavings;
    std::ifstream infile(filename);
    std::string line;

    while (std::getline(infile, line)) {
        std::vector<Event> interleaving;
        std::stringstream ss(line);
        int replicaId;
        std::string type;

        while (ss >> replicaId >> type) {
            interleaving.push_back({replicaId, type});
        }

        interleavings.push_back(interleaving);
    }

    return interleavings;
}

std::vector<int> index_in_interleaving(int rID, const std::vector<Event>& il) {
    std::vector<int> indices;
    for (int i = 0; i < il.size(); ++i) {
        if (il[i].replicaId == rID) {
            indices.push_back(i);
        }
    }
    return indices;
}

std::vector<Event> events_after_indices(const std::vector<Event>& il, const std::vector<int>& idx) {
    std::vector<Event> remaining_events;
    for (int i : idx) {
        for (int j = i + 1; j < il.size(); ++j) {
            remaining_events.push_back(il[j]);
        }
    }
    return remaining_events;
}

std::vector<std::vector<Event>> exclude(const std::vector<std::vector<Event>>& ils,
                                        const std::vector<std::vector<Event>>& grouped_events) {
    std::vector<std::vector<Event>> pruned_interleavings;
    for (const auto& il : ils) {
        bool include = true;
        for (const auto& ge : grouped_events) {
            if (std::includes(il.begin(), il.end(), ge.begin(), ge.end())) {
                include = false;
                break;
            }
        }
        if (include) {
            pruned_interleavings.push_back(il);
        }
    }
    return pruned_interleavings;
}

void save_interleavings(const std::vector<std::vector<Event>>& interleavings, const std::string& filename) {
    std::ofstream outfile(filename);

    for (const auto& il : interleavings) {
        for (const auto& event : il) {
            outfile << event.replicaId << " " << event.type << " ";
        }
        outfile << std::endl;
    }
}

int main() {
    int rID;
    std::cin >> rID; 
    std::vector<std::vector<Event>> ILs = read_interleavings("interleavings.dl"); 
    std::map<std::vector<int>, std::vector<std::vector<Event>>> grouped_by_indices;
    std::vector<std::vector<Event>> grouped_events;
    std::vector<std::vector<Event>> RI; 

    for (const auto& il : ILs) {
        std::vector<int> indices = index_in_interleaving(rID, il);

        
        if (grouped_by_indices.find(indices) == grouped_by_indices.end()) {
            grouped_by_indices[indices] = {};
        }
        grouped_by_indices[indices].push_back(il);
    }

    
    for (const auto& [idx, ils] : grouped_by_indices) {
        std::vector<Event> evs = events_after_indices(ils[0], idx);
        grouped_events.push_back(evs);
    }

    
    RI = exclude(ILs, grouped_events);

    save_interleavings(RI, "RI.dl");

    return 0;
}
