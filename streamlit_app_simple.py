import streamlit as st
import pandas as pd
import numpy as np

# Simple page config
st.set_page_config(
    page_title="Sports Speed by Atlee Mahorn",
    page_icon="🏃‍♂️",
    layout="wide"
)

# Header
st.title("🏃‍♂️ Sports Speed by Atlee Mahorn")
st.subheader("Proven Sports Speed System")
st.write("Olympic Training Methodology for High School Athletics")

# Navigation
page = st.sidebar.selectbox("Choose Section", [
    "🏠 Home",
    "🏃‍♂️ Training Builder", 
    "📊 Performance Charts"
])

if page == "🏠 Home":
    st.markdown("## Welcome to Olympic Training Methodology")
    st.markdown("### Professional speed training for high school coaches across 6 sports")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.info("🏈 Football\nPower & Acceleration")
        st.info("⚽ Soccer\nSpeed & Endurance")
    
    with col2:
        st.info("🏀 Basketball\nAgility & Quickness")
        st.info("⚾ Baseball\nBase Running Speed")
    
    with col3:
        st.info("🥍 Lacrosse\nField Transitions")
        st.info("🏃 Track & Field\nPure Speed Development")

elif page == "🏃‍♂️ Training Builder":
    st.header("16-Week Training Builder")
    
    sport = st.selectbox("Select Sport", [
        "Football", "Soccer", "Basketball", "Baseball", "Lacrosse", "Track & Field"
    ])
    
    col1, col2 = st.columns(2)
    with col1:
        athlete_name = st.text_input("Athlete Name", "Enter name")
        age = st.number_input("Age", 14, 18, 16)
    with col2:
        position = st.text_input("Position/Event", "Enter position")
        experience = st.selectbox("Experience Level", ["Beginner", "Intermediate", "Advanced"])
    
    if st.button("Generate 16-Week Plan"):
        st.success(f"16-week {sport} speed training plan generated for {athlete_name}")
        
        # Sport-specific data
        sport_data = {
            "Football": {"focus": "Power & Acceleration", "base_volume": 320, "sessions": 3},
            "Soccer": {"focus": "Speed Endurance", "base_volume": 450, "sessions": 4},
            "Basketball": {"focus": "Court Agility", "base_volume": 280, "sessions": 4},
            "Baseball": {"focus": "Base Running", "base_volume": 480, "sessions": 3},
            "Lacrosse": {"focus": "Field Transitions", "base_volume": 380, "sessions": 3},
            "Track & Field": {"focus": "Pure Speed", "base_volume": 600, "sessions": 4}
        }
        
        current_sport = sport_data[sport]
        
        st.subheader(f"🏅 Olympic {sport} Training Protocol")
        
        col1, col2 = st.columns(2)
        with col1:
            st.write(f"**Primary Focus:** {current_sport['focus']}")
            st.write(f"**Base Volume:** {current_sport['base_volume']}m per week")
        with col2:
            st.write(f"**Weekly Sessions:** {current_sport['sessions']}")
            st.write(f"**Training Method:** Olympic periodization")
        
        # 16-week progression
        st.subheader("📊 16-Week Volume & Intensity Progression")
        
        weeks_data = []
        for week in range(1, 17):
            if week <= 4:
                phase = "Base Building"
                intensity = 78 + (week * 2)
                volume = int(current_sport["base_volume"] * (0.75 + week * 0.05))
            elif week <= 8:
                phase = "Strength Development"
                intensity = 83 + ((week - 4) * 2)
                volume = int(current_sport["base_volume"] * (0.85 + (week - 4) * 0.03))
            elif week <= 12:
                phase = "Speed Focus"
                intensity = 88 + ((week - 8) * 3)
                volume = int(current_sport["base_volume"] * (0.95 + (week - 8) * 0.02))
            else:
                phase = "Competition Peak"
                intensity = 95 + ((week - 12) * 1.25)
                volume = int(current_sport["base_volume"] * (1.0 + (week - 12) * 0.05))
            
            weeks_data.append({
                "Week": week,
                "Phase": phase,
                "Intensity (%)": min(intensity, 100),
                "Volume (m)": volume
            })
        
        # Display as table
        df = pd.DataFrame(weeks_data)
        st.dataframe(df, use_container_width=True)
        
        # Phase breakdown
        phases = [
            ("🏗️ Base Building", 1, 4, "Foundation development"),
            ("💪 Strength Development", 5, 8, "Power development"), 
            ("⚡ Speed Focus", 9, 12, "Maximum velocity"),
            ("🏆 Competition Peak", 13, 16, "Peak performance")
        ]
        
        for phase_name, start_week, end_week, description in phases:
            with st.expander(f"{phase_name} (Weeks {start_week}-{end_week})"):
                st.write(f"**Focus:** {description}")
                phase_weeks = [w for w in weeks_data if start_week <= w["Week"] <= end_week]
                
                col1, col2 = st.columns(2)
                with col1:
                    avg_intensity = np.mean([w["Intensity (%)"] for w in phase_weeks])
                    st.metric("Average Intensity", f"{avg_intensity:.1f}%")
                with col2:
                    total_volume = sum([w["Volume (m)"] for w in phase_weeks])
                    st.metric("Total Volume", f"{total_volume:,}m")
        
        st.info("🏅 This 16-week protocol follows Olympic-level periodization principles by 3-time Olympic participant Atlee Mahorn.")

elif page == "📊 Performance Charts":
    st.header("Performance Analytics Dashboard")
    
    # Simple line chart
    st.subheader("16-Week Sprint Time Progression")
    weeks = list(range(1, 17))
    sprint_times = [4.8 - (i * 0.02) + np.random.normal(0, 0.02) for i in weeks]
    
    chart_data = pd.DataFrame({
        'Week': weeks,
        'Sprint Time (s)': sprint_times
    })
    
    st.line_chart(chart_data.set_index('Week'))
    
    # Simple bar chart
    st.subheader("Multi-Sport Performance Comparison")
    sports_data = {
        'Sport': ['Football', 'Soccer', 'Basketball', 'Baseball', 'Lacrosse', 'Track'],
        'Avg Improvement (%)': [12.5, 10.8, 15.2, 9.3, 11.7, 18.4]
    }
    
    df = pd.DataFrame(sports_data)
    st.bar_chart(df.set_index('Sport'))

# Footer
st.markdown("---")
st.markdown("**Sports Speed by Atlee Mahorn** - Olympic Training Methodology for High School Athletics")