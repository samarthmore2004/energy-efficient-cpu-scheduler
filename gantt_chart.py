import matplotlib.pyplot as plt
import streamlit as st

def draw_gantt(schedule, streamlit_mode=False):
    fig, gnt = plt.subplots()
    gnt.set_xlabel('Time')
    gnt.set_yticks([15])
    gnt.set_yticklabels(['CPU'])

    for task in schedule:
        gnt.broken_barh([(task[1], task[2] - task[1])], (10, 10), facecolors='tab:blue')
        gnt.text(task[1] + 0.5, 15, task[0], va='center', ha='left', fontsize=9)

    gnt.set_title("Gantt Chart")

    if streamlit_mode:
        st.pyplot(fig)
    else:
        plt.show()