#include <iostream>
#include <vector>
#include <tuple>
#include <algorithm>
#include <fstream>
#include <sstream>

struct Event {
    int fromReplicaId;
    int toReplicaId;
    std::string type;
};

std::vector<Event> read_events(const std::string& filename) {
    std::vector<Event> events;
    std::ifstream infile(filename);
    std::string line;

    while (std::getline(infile, line)) {
        std::stringstream ss(line);
        int fromReplicaId, toReplicaId;
        std::string type;
        ss >> fromReplicaId >> toReplicaId >> type;
        events.push_back({fromReplicaId, toReplicaId, type});
    }

    return events;
}

std::vector<std::tuple<Event, Event>> read_specified_groups(const std::string& filename) {
    std::vector<std::tuple<Event, Event>> groups;
    std::ifstream infile(filename);
    std::string line;

    while (std::getline(infile, line)) {
        std::stringstream ss(line);
        int fromReplicaId1, toReplicaId1, fromReplicaId2, toReplicaId2;
        std::string type1, type2;
        ss >> fromReplicaId1 >> toReplicaId1 >> type1;
        ss >> fromReplicaId2 >> toReplicaId2 >> type2;

        groups.push_back({{fromReplicaId1, toReplicaId1, type1}, {fromReplicaId2, toReplicaId2, type2}});
    }

    return groups;
}

std::vector<std::vector<Event>> permute(const std::vector<Event>& events,
                                        const std::vector<std::tuple<Event, Event>>& grouped_events) {
    std::vector<std::vector<Event>> interleavings;
    for (const auto& event : events) {
        interleavings.push_back({event});
    }
    return interleavings;
}

void save_interleavings(const std::vector<std::vector<Event>>& interleavings, const std::string& filename) {
    std::ofstream outfile(filename);

    for (const auto& interleaving : interleavings) {
        for (const auto& event : interleaving) {
            outfile << event.fromReplicaId << " " << event.toReplicaId << " " << event.type << " ";
        }
        outfile << std::endl;
    }
}

int main() {
    std::vector<Event> events = read_events("events.dl"); 
    std::vector<std::tuple<Event, Event>> spec_group = read_specified_groups("groups.dl"); 
    std::vector<std::tuple<Event, Event>> grouped_events;
    std::vector<std::vector<Event>> GI; 

    
    for (const auto& event_i : events) {
        for (const auto& event_j : events) {
            if ((event_i.type == "sync_req" && event_j.type == "exec_sync") ||
                (event_j.type == "sync_req" && event_i.type == "exec_sync")) {

                if (event_i.fromReplicaId == event_j.fromReplicaId &&
                    event_i.toReplicaId == event_j.toReplicaId) {
                    grouped_events.emplace_back(event_i, event_j);
                }
            }
        }
    }

    
    for (const auto& group : spec_group) {
        grouped_events.push_back(group);
    }

    GI = permute(events, grouped_events);

    save_interleavings(GI, "GI.dl");

    return 0;
}
