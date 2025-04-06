#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>

using namespace std;

// Structure to hold process details
struct Process {
    int pid, arrival_time, burst_time, priority, completion_time, waiting_time, turnaround_time;
    float energy_consumption;
};

class EnergyEfficientScheduler {
private:
    vector<Process> processes; // List of processes
    float total_energy_consumption; // Total energy consumption counter

public:
    // Constructor to initialize the scheduler with processes
    EnergyEfficientScheduler(vector<Process> proc) : processes(proc), total_energy_consumption(0) {}

    // Function to schedule processes based on priority scheduling
    void schedule() {
        auto cmp = [](Process a, Process b) { return a.priority > b.priority; };
        priority_queue<Process, vector<Process>, decltype(cmp)> ready_queue(cmp);
        int time = 0, index = 0, n = processes.size();

        // Sorting processes by arrival time
        sort(processes.begin(), processes.end(), [](Process a, Process b) {
            return a.arrival_time < b.arrival_time;
        });





        while (index < n || !ready_queue.empty()) {
            // Adding processes to the queue based on arrival time
            while (index < n && processes[index].arrival_time <= time) {
                ready_queue.push(processes[index]);
                index++;
            }

            if (!ready_queue.empty()) {
                Process process = ready_queue.top();
                ready_queue.pop();
                time += process.burst_time;
                process.completion_time = time;
                process.turnaround_time = process.completion_time - process.arrival_time;
                process.waiting_time = process.turnaround_time - process.burst_time;
                process.energy_consumption = process.burst_time * 0.5f; // Simulated energy consumption factor
                total_energy_consumption += process.energy_consumption;

                // Update process in original list
                for (auto &p : processes) {
                    if (p.pid == process.pid) {
                        p = process;
                        break;
                    }
                }
            } else {
                time++;
            }
        }
    }

    // Function to display scheduling results
    void display_results() {
        cout << "\nPID\tAT\tBT\tCT\tTAT\tWT\tEnergy\n";
        for (const auto &process : processes) {
            cout << process.pid << "\t" << process.arrival_time << "\t" << process.burst_time << "\t";
            cout << process.completion_time << "\t" << process.turnaround_time << "\t";
            cout << process.waiting_time << "\t" << process.energy_consumption << "\n";
        }
        cout << "\n\nTotal Energy Consumption: " << total_energy_consumption << "\n";
    }
};

int main() {
    int n;
    cout << "Enter the number of processes: ";
    cin >> n;

    vector<Process> process_list;

    // Taking input for each process
    for (int i = 0; i < n; i++) {
        Process p;
        cout << "\nEnter details for Process " << i + 1 << ":\n";
        p.pid = i + 1;
        cout << "Arrival Time: ";
        cin >> p.arrival_time;
        cout << "Burst Time: ";
        cin >> p.burst_time;
        cout << "Priority (Lower number = Higher Priority): ";
        cin >> p.priority;
        p.completion_time = p.waiting_time = p.turnaround_time = 0;
        p.energy_consumption = 0.0f;
        process_list.push_back(p);
    }

    // Creating scheduler and executing scheduling
    EnergyEfficientScheduler scheduler(process_list);
    scheduler.schedule();
    scheduler.display_results();

    return 0;
}
//Average waiting & Turnaround  time
