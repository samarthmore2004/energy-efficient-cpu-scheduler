import streamlit as st
from scheduler.energy_aware import EnergyAwareScheduler
from utils.energy_model import calculate_energy
import pandas as pd
import matplotlib.pyplot as plt
from visualizer.gantt_chart import draw_gantt

def main():
    st.title("Energy-Efficient CPU Scheduling Simulator")

    st.sidebar.header("Task Parameters")
    num_tasks = st.sidebar.slider("Number of Tasks", 1, 10, 3)
    
    task_list = []
    for i in range(num_tasks):
        st.sidebar.subheader(f"Task {i+1}")
        name = f"T{i+1}"
        arrival = st.sidebar.number_input(f"Arrival Time T{i+1}", min_value=0, value=i*2)
        burst = st.sidebar.number_input(f"Burst Time T{i+1}", min_value=1, value=3)
        priority = st.sidebar.slider(f"Priority T{i+1}", 1, 5, 3)
        freq = st.sidebar.selectbox(f"Frequency T{i+1}", ['low', 'medium', 'high'], index=1)
        task_list.append({'name': name, 'arrival': arrival, 'burst': burst, 'priority': priority, 'freq': freq})

    if st.button("Run Scheduler"):
        scheduler = EnergyAwareScheduler(task_list)
        schedule, total_energy = scheduler.run()

        df = pd.DataFrame(schedule, columns=['Task', 'Start Time', 'End Time', 'Energy'])
        st.subheader("Scheduling Result")
        st.dataframe(df)

        st.write(f"### Total Energy Consumed: {total_energy}")
        st.subheader("Gantt Chart")
        draw_gantt(schedule, streamlit_mode=True)

if __name__ == "__main__":
    main()