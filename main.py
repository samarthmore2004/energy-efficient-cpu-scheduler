from scheduler.energy_aware import EnergyAwareScheduler
from utils.task_generator import load_tasks
from visualizer.gantt_chart import draw_gantt

if __name__ == '__main__':
    tasks = load_tasks()
    scheduler = EnergyAwareScheduler(tasks)
    schedule, total_energy = scheduler.run()

    for entry in schedule:
        print(f"Task: {entry[0]} | Start: {entry[1]} | End: {entry[2]} | Energy: {entry[3]}")

    print(f"\nTotal Energy Consumed: {total_energy}")
    draw_gantt(schedule)