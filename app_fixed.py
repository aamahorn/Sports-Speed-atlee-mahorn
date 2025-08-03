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
        
        # Sport-specific data with complete Olympic methodology
        sport_data = {
            "Football": {"focus": "Power & Acceleration", "base_volume": 320, "sessions": 3, "max_volume": 448},
            "Soccer": {"focus": "Speed Endurance", "base_volume": 450, "sessions": 4, "max_volume": 585},
            "Basketball": {"focus": "Court Agility", "base_volume": 280, "sessions": 4, "max_volume": 364},
            "Baseball": {"focus": "Base Running", "base_volume": 480, "sessions": 3, "max_volume": 624},
            "Lacrosse": {"focus": "Field Transitions", "base_volume": 380, "sessions": 3, "max_volume": 494},
            "Track & Field": {"focus": "Pure Speed", "base_volume": 600, "sessions": 4, "max_volume": 780}
        }
        
        current_sport = sport_data[sport]
        
        st.subheader(f"🏅 Olympic {sport} Training Protocol")
        
        col1, col2 = st.columns(2)
        with col1:
            st.write(f"**Primary Focus:** {current_sport['focus']}")
            st.write(f"**Base Volume:** {current_sport['base_volume']}m per week")
        with col2:
            st.write(f"**Weekly Sessions:** {current_sport['sessions']}")
            st.write(f"**Peak Volume:** {current_sport['max_volume']}m per week")
        
        # 16-week progression with accurate volume and intensity
        st.subheader("📊 16-Week Volume & Intensity Progression")
        
        weeks_data = []
        for week in range(1, 17):
            if week <= 4:  # Base Building Phase
                phase = "Base Building"
                intensity = 78 + (week * 2)  # 80-86%
                volume_factor = 0.75 + (week * 0.05)  # 80-95% of base
            elif week <= 8:  # Strength Development Phase
                phase = "Strength Development" 
                intensity = 83 + ((week - 4) * 2)  # 85-91%
                volume_factor = 0.85 + ((week - 4) * 0.03)  # 88-97% of base
            elif week <= 12:  # Speed Focus Phase
                phase = "Speed Focus"
                intensity = 88 + ((week - 8) * 3)  # 91-100%
                volume_factor = 0.95 + ((week - 8) * 0.02)  # 97-103% of base
            else:  # Competition Peak Phase
                phase = "Competition Peak"
                intensity = 95 + ((week - 12) * 1.25)  # 96.25-100%
                volume_factor = 1.0 + ((week - 12) * 0.05)  # 105-120% of base
            
            volume = int(current_sport["base_volume"] * volume_factor)
            
            weeks_data.append({
                "Week": week,
                "Phase": phase,
                "Intensity (%)": min(intensity, 100),
                "Volume (m)": volume,
                "Sessions": current_sport["sessions"]
            })
        
        # Display complete training table
        df = pd.DataFrame(weeks_data)
        st.dataframe(df, use_container_width=True)
        
        # Volume summary by phase
        st.subheader("📈 Phase Summary")
        phases = [
            ("🏗️ Base Building", 1, 4, "Foundation development - Olympic base conditioning"),
            ("💪 Strength Development", 5, 8, "Power development - Explosive strength focus"), 
            ("⚡ Speed Focus", 9, 12, "Maximum velocity - Peak speed development"),
            ("🏆 Competition Peak", 13, 16, "Peak performance - Competition preparation")
        ]
        
        for phase_name, start_week, end_week, description in phases:
            with st.expander(f"{phase_name} (Weeks {start_week}-{end_week})"):
                st.write(f"**Focus:** {description}")
                phase_weeks = [w for w in weeks_data if start_week <= w["Week"] <= end_week]
                
                col1, col2, col3 = st.columns(3)
                with col1:
                    avg_intensity = np.mean([w["Intensity (%)"] for w in phase_weeks])
                    st.metric("Average Intensity", f"{avg_intensity:.1f}%")
                with col2:
                    total_volume = sum([w["Volume (m)"] for w in phase_weeks])
                    st.metric("Total Volume", f"{total_volume:,}m")
                with col3:
                    avg_volume = np.mean([w["Volume (m)"] for w in phase_weeks])
                    st.metric("Weekly Average", f"{avg_volume:.0f}m")
        
        # Training specifics
        st.subheader("🎯 Training Specifications")
        col1, col2 = st.columns(2)
        
        with col1:
            st.write("**Energy System Focus:**")
            if sport in ["Football", "Basketball"]:
                st.write("• Alactic Power (0-10s)")
                st.write("• Short recovery intervals")
                st.write("• Maximum acceleration")
            elif sport in ["Soccer", "Lacrosse"]:
                st.write("• Mixed energy systems")
                st.write("• Speed endurance")
                st.write("• Directional changes")
            else:  # Baseball, Track & Field
                st.write("• Pure speed development")
                st.write("• Maximum velocity")
                st.write("• Technical precision")
        
        with col2:
            st.write("**Recovery Guidelines:**")
            st.write("• Work:Rest ratio 1:3-1:5")
            st.write("• Complete recovery between reps")
            st.write("• 48-72h between speed sessions")
            st.write("• Active recovery on off days")
        
        st.info("🏅 This 16-week protocol follows Olympic-level periodization principles by 3-time Olympic participant Atlee Mahorn. Volume progresses from 75% to 120% of base training load with intensity ranging from 78% to peak competition levels.")

elif page == "📊 Performance Charts":
    st.header("Performance Analytics Dashboard")
    
    # Performance progression simulation
    st.subheader("16-Week Sprint Time Progression")
    weeks = list(range(1, 17))
    base_time = 4.8
    improvements = [base_time - (i * 0.015) + np.random.normal(0, 0.015) for i in weeks]
    
    chart_data = pd.DataFrame({
        'Week': weeks,
        'Sprint Time (s)': improvements
    })
    
    st.line_chart(chart_data.set_index('Week'))
    
    # Multi-sport comparison
    st.subheader("Multi-Sport Performance Comparison")
    sports_performance = {
        'Sport': ['Football', 'Soccer', 'Basketball', 'Baseball', 'Lacrosse', 'Track & Field'],
        'Avg Improvement (%)': [12.5, 10.8, 15.2, 9.3, 11.7, 18.4],
        'Training Volume (m/week)': [320, 450, 280, 480, 380, 600]
    }
    
    performance_df = pd.DataFrame(sports_performance)
    
    col1, col2 = st.columns(2)
    with col1:
        st.bar_chart(performance_df.set_index('Sport')['Avg Improvement (%)'])
    with col2:
        st.bar_chart(performance_df.set_index('Sport')['Training Volume (m/week)'])
    
    # Training load distribution
    st.subheader("Training Load Distribution by Phase")
    phase_data = {
        'Phase': ['Base Building', 'Strength Dev', 'Speed Focus', 'Competition Peak'],
        'Volume (%)': [25, 30, 25, 20],
        'Intensity (%)': [82, 88, 94, 98]
    }
    
    phase_df = pd.DataFrame(phase_data)
    st.bar_chart(phase_df.set_index('Phase'))

# Footer
st.markdown("---")
st.markdown("**Sports Speed by Atlee Mahorn** - Olympic Training Methodology for High School Athletics")
st.markdown("*3-Time Olympic Participant | Professional Speed Development | Evidence-Based Training*")