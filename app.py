import streamlit as st
import os

st.set_page_config(page_title="RL Drone Stabilization", page_icon="🚁", layout="centered")

st.title("🚁 RL Quadcopter Stabilization")
st.markdown("""
This dashboard showcases a Proximal Policy Optimization (PPO) agent trained to stabilize a Quadcopter using the PyFlyt physics engine. 
The agent was trained with a **Custom Jitter Penalty** to ensure smooth motor control and prevent erratic flight.
""")

st.divider()

col1, col2 = st.columns([2, 1])

with col1:
    st.subheader("Flight Simulation")
    
    # Create tabs for the two different views!
    tab1, tab2 = st.tabs(["Third-Person View", "First-Person (Drone) View"])
    
    with tab1:
        if os.path.exists("drone_flight_tpp.mp4"):
            st.video("drone_flight_tpp.mp4")
        else:
            st.info("Save your screen-recorded video as 'drone_flight_tpp.mp4' to see it here!")
            
    with tab2:
        if os.path.exists("drone_flight_fpp.mp4"):
            st.video("drone_flight_fpp.mp4")
        elif os.path.exists("drone_flight.mp4"):
            st.video("drone_flight.mp4") # Fallback to the original name
        else:
            st.info("Save your auto-generated video as 'drone_flight_fpp.mp4' to see it here!")

with col2:
    st.subheader("Alpha Statistics")
    st.metric(label="Total Reward (1000 steps)", value="1137.01", delta="Stable Flight")
    st.metric(label="Environment", value="PyFlyt QuadX-v4")
    st.metric(label="Algorithm", value="PPO")
    st.metric(label="Action Jitter", value="Low", delta="-0.5 Penalty", delta_color="normal")

st.divider()

st.subheader("📈 Training Statistics")
st.markdown("""
All training metrics (Reward, Jitter Penalty, etc.) were tracked in real-time during the PPO learning process. 

👉 **[Click here to view the full interactive Weights & Biases Report](https://wandb.ai/divyanshsrivastava303-srm-institute-of-science-and-techn/drone-stabilization?nw=nwuserdivyanshsrivastava303)**
""")

st.divider()

st.subheader("How it works")
st.markdown("""
- **Observation Space:** Attitude, angular velocities, position error, and linear velocities.
- **Action Space:** Continuous values `[-1, 1]` for the 4 individual motor thrusts.
- **Custom Wrapper:** A `gym.Wrapper` was used during training to penalize the squared difference between the previous frame's motor thrusts and the current thrusts, teaching the AI to avoid violent oscillations.
""")

st.caption("Developed using stable-baselines3 and PyBullet.")
