from scheduler.base_scheduler import Scheduler
from utils.energy_model import calculate_energy

class EnergyAwareScheduler(Scheduler):
    def run(self):
        tasks = sorted(self.tasks, key=lambda x: (x['priority'], x['arrival']))
        time = 0
        schedule = []
        total_energy = 0

        for task in tasks:
            if time < task['arrival']:
                time = task['arrival']
            task_start = time
            task_end = time + task['burst']
            energy = calculate_energy(task['burst'], task['freq'])
            total_energy += energy
            schedule.append((task['name'], task_start, task_end, energy))
            time = task_end

        return schedule, total_energy