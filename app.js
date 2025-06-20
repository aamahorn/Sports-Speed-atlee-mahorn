import React, { useState } from 'react';
import { View, Text, StyleSheet, ScrollView, TouchableOpacity, SafeAreaView } from 'react-native';

const App = () => {
  const [selectedSport, setSelectedSport] = useState('');
  const [selectedWeek, setSelectedWeek] = useState(1);
  
  const sports = [
    { name: 'Football', color: '#1e40af', season: 'Fall', focus: 'Power & Acceleration' },
    { name: 'Soccer', color: '#1e40af', season: 'Fall/Spring', focus: 'Agility & Endurance' },
    { name: 'Basketball', color: '#1e40af', season: 'Winter', focus: 'Vertical & Quickness' },
    { name: 'Baseball', color: '#1e40af', season: 'Spring', focus: 'Base Running & Throwing' },
    { name: 'Lacrosse', color: '#1e40af', season: 'Spring', focus: 'Field Transitions' },
    { name: 'Track & Field', color: '#1e40af', season: 'Spring', focus: 'Pure Speed Development' }
  ];

  const generateSpeedSession = (sport) => {
    const sportDistances = {
      'Football': ['10m', '20m', '40m'],
      'Soccer': ['15m', '25m', '50m'],
      'Basketball': ['5m', '15m', '25m'],
      'Baseball': ['30m', '60m', '90m'],
      'Lacrosse': ['20m', '40m', '60m'],
      'Track & Field': ['30m', '60m', '100m']
    };
    
    const distances = sportDistances[sport] || ['30m', '60m'];
    const selectedDistance = distances[Math.floor(Math.random() * distances.length)];
    const reps = Math.floor(Math.random() * 3) + 3; // 3-5 reps
    
    return {
      type: 'Speed Session',
      distance: selectedDistance,
      reps: reps,
      rest: '2-3 minutes',
      focus: `${sport} specific acceleration and maximum velocity`
    };
  };

  const generateStrengthSession = (sport) => {
    const sportExercises = {
      'Football': ['Squats', 'Power Cleans', 'Bench Press'],
      'Soccer': ['Single Leg Squats', 'Lateral Lunges', 'Core Rotations'],
      'Basketball': ['Jump Squats', 'Vertical Jumps', 'Lateral Bounds'],
      'Baseball': ['Rotational Throws', 'Single Arm Rows', 'Hip Thrusts'],
      'Lacrosse': ['Multi-Directional Lunges', 'Stick Drills', 'Agility Ladder'],
      'Track & Field': ['Olympic Lifts', 'Plyometric Bounds', 'Sprint Mechanics']
    };
    
    const exercises = sportExercises[sport] || ['Squats', 'Deadlifts', 'Bench Press'];
    
    return {
      type: 'Strength Session',
      exercises: exercises.slice(0, 3),
      sets: '3-4 sets',
      reps: '6-8 reps',
      focus: `${sport} specific power development`
    };
  };

  const generateEnduranceSession = (sport) => {
    const sportEndurance = {
      'Football': { duration: '20 minutes', type: 'Interval sprints with rest' },
      'Soccer': { duration: '30 minutes', type: 'Continuous running with direction changes' },
      'Basketball': { duration: '25 minutes', type: 'Court suicides and defensive slides' },
      'Baseball': { duration: '15 minutes', type: 'Base running simulation' },
      'Lacrosse': { duration: '25 minutes', type: 'Field transition runs' },
      'Track & Field': { duration: '35 minutes', type: 'Tempo runs and stride work' }
    };
    
    const endurance = sportEndurance[sport] || { duration: '30 minutes', type: 'Continuous aerobic work' };
    
    return {
      type: 'Endurance Session',
      duration: endurance.duration,
      activity: endurance.type,
      intensity: 'Moderate to high',
      focus: `${sport} specific cardiovascular conditioning`
    };
  };

  const SportCard = ({ sport }) => (
    <TouchableOpacity 
      style={[styles.sportCard, selectedSport === sport.name && styles.selectedCard]}
      onPress={() => setSelectedSport(sport.name)}
    >
      <Text style={styles.sportName}>{sport.name}</Text>
      <Text style={styles.sportSeason}>{sport.season}</Text>
      <Text style={styles.sportFocus}>{sport.focus}</Text>
    </TouchableOpacity>
  );

  const TrainingSession = ({ session }) => (
    <View style={styles.sessionCard}>
      <Text style={styles.sessionType}>{session.type}</Text>
      {session.distance && (
        <Text style={styles.sessionDetail}>Distance: {session.distance}</Text>
      )}
      {session.reps && (
        <Text style={styles.sessionDetail}>Repetitions: {session.reps}</Text>
      )}
      {session.exercises && (
        <Text style={styles.sessionDetail}>Exercises: {session.exercises.join(', ')}</Text>
      )}
      {session.sets && (
        <Text style={styles.sessionDetail}>Sets: {session.sets}</Text>
      )}
      {session.duration && (
        <Text style={styles.sessionDetail}>Duration: {session.duration}</Text>
      )}
      {session.activity && (
        <Text style={styles.sessionDetail}>Activity: {session.activity}</Text>
      )}
      {session.intensity && (
        <Text style={styles.sessionDetail}>Intensity: {session.intensity}</Text>
      )}
      {session.rest && (
        <Text style={styles.sessionDetail}>Rest: {session.rest}</Text>
      )}
      <Text style={styles.sessionFocus}>{session.focus}</Text>
    </View>
  );

  const getPeriodizationPhase = (week) => {
    if (week <= 4) return { phase: 'Base Building', focus: 'Foundation & Volume' };
    if (week <= 8) return { phase: 'Strength Development', focus: 'Power & Force Production' };
    if (week <= 12) return { phase: 'Speed Development', focus: 'Maximum Velocity & Technique' };
    return { phase: 'Competition Phase', focus: 'Peak Performance & Maintenance' };
  };

  const currentPhase = getPeriodizationPhase(selectedWeek);

  return (
    <SafeAreaView style={styles.container}>
      <ScrollView style={styles.scrollView}>
        <View style={styles.header}>
          <Text style={styles.title}>Speed Training by Atlee Mahorn</Text>
          <Text style={styles.subtitle}>Olympic Sprint Methodology for High School Coaches</Text>
        </View>

        <View style={styles.section}>
          <Text style={styles.sectionTitle}>Select Your Sport</Text>
          <View style={styles.sportsGrid}>
            {sports.map((sport, index) => (
              <SportCard key={index} sport={sport} />
            ))}
          </View>
        </View>

        {selectedSport && (
          <View style={styles.section}>
            <Text style={styles.sectionTitle}>Training Builder - {selectedSport}</Text>
            
            <View style={styles.phaseCard}>
              <Text style={styles.phaseTitle}>{currentPhase.phase}</Text>
              <Text style={styles.phaseFocus}>{currentPhase.focus}</Text>
            </View>
            
            <View style={styles.weekSelector}>
              <Text style={styles.weekTitle}>Week {selectedWeek} of 16</Text>
              <View style={styles.weekButtons}>
                <TouchableOpacity 
                  style={styles.weekButton}
                  onPress={() => setSelectedWeek(Math.max(1, selectedWeek - 1))}
                >
                  <Text style={styles.weekButtonText}>Previous</Text>
                </TouchableOpacity>
                <TouchableOpacity 
                  style={styles.weekButton}
                  onPress={() => setSelectedWeek(Math.min(16, selectedWeek + 1))}
                >
                  <Text style={styles.weekButtonText}>Next</Text>
                </TouchableOpacity>
              </View>
            </View>

            <View style={styles.sessionsContainer}>
              <Text style={styles.sessionsTitle}>Weekly Training Sessions</Text>
              <TrainingSession session={generateSpeedSession(selectedSport)} />
              <TrainingSession session={generateStrengthSession(selectedSport)} />
              <TrainingSession session={generateEnduranceSession(selectedSport)} />
            </View>

            <View style={styles.coachingTips}>
              <Text style={styles.tipsTitle}>Coaching Tips</Text>
              <Text style={styles.tipsText}>
                • Focus on proper form before increasing intensity
              </Text>
              <Text style={styles.tipsText}>
                • Allow adequate recovery between high-intensity sessions
              </Text>
              <Text style={styles.tipsText}>
                • Monitor athlete fatigue and adjust volume accordingly
              </Text>
              <Text style={styles.tipsText}>
                • Progressive overload should be gradual and systematic
              </Text>
            </View>
          </View>
        )}

        <View style={styles.footer}>
          <Text style={styles.footerText}>
            Professional coaching methodology adapted for high school athletics
          </Text>
          <Text style={styles.footerText}>
            3-time Olympic participant • Champion optimization methods
          </Text>
        </View>
      </ScrollView>
    </SafeAreaView>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#ffffff',
  },
  scrollView: {
    flex: 1,
  },
  header: {
    backgroundColor: '#1e40af',
    padding: 20,
    alignItems: 'center',
  },
  title: {
    fontSize: 24,
    fontWeight: 'bold',
    color: '#ffffff',
    textAlign: 'center',
  },
  subtitle: {
    fontSize: 16,
    color: '#ffffff',
    textAlign: 'center',
    marginTop: 8,
  },
  section: {
    padding: 20,
  },
  sectionTitle: {
    fontSize: 20,
    fontWeight: 'bold',
    color: '#1e40af',
    marginBottom: 15,
  },
  sportsGrid: {
    flexDirection: 'row',
    flexWrap: 'wrap',
    justifyContent: 'space-between',
  },
  sportCard: {
    width: '48%',
    backgroundColor: '#f8fafc',
    padding: 15,
    borderRadius: 8,
    marginBottom: 10,
    borderWidth: 2,
    borderColor: '#e2e8f0',
  },
  selectedCard: {
    borderColor: '#1e40af',
    backgroundColor: '#eff6ff',
  },
  sportName: {
    fontSize: 16,
    fontWeight: 'bold',
    color: '#1e40af',
  },
  sportSeason: {
    fontSize: 14,
    color: '#64748b',
    marginTop: 4,
  },
  sportFocus: {
    fontSize: 12,
    color: '#475569',
    marginTop: 4,
  },
  phaseCard: {
    backgroundColor: '#1e40af',
    padding: 15,
    borderRadius: 8,
    marginBottom: 15,
    alignItems: 'center',
  },
  phaseTitle: {
    fontSize: 18,
    fontWeight: 'bold',
    color: '#ffffff',
  },
  phaseFocus: {
    fontSize: 14,
    color: '#ffffff',
    marginTop: 4,
  },
  weekSelector: {
    backgroundColor: '#f8fafc',
    padding: 15,
    borderRadius: 8,
    marginBottom: 20,
  },
  weekTitle: {
    fontSize: 18,
    fontWeight: 'bold',
    color: '#1e40af',
    textAlign: 'center',
    marginBottom: 10,
  },
  weekButtons: {
    flexDirection: 'row',
    justifyContent: 'space-around',
  },
  weekButton: {
    backgroundColor: '#1e40af',
    paddingHorizontal: 20,
    paddingVertical: 8,
    borderRadius: 6,
  },
  weekButtonText: {
    color: '#ffffff',
    fontWeight: 'bold',
  },
  sessionsContainer: {
    marginBottom: 20,
  },
  sessionsTitle: {
    fontSize: 18,
    fontWeight: 'bold',
    color: '#1e40af',
    marginBottom: 15,
  },
  sessionCard: {
    backgroundColor: '#f8fafc',
    padding: 15,
    borderRadius: 8,
    borderLeftWidth: 4,
    borderLeftColor: '#1e40af',
    marginBottom: 15,
  },
  sessionType: {
    fontSize: 16,
    fontWeight: 'bold',
    color: '#1e40af',
    marginBottom: 8,
  },
  sessionDetail: {
    fontSize: 14,
    color: '#475569',
    marginBottom: 4,
  },
  sessionFocus: {
    fontSize: 12,
    color: '#64748b',
    fontStyle: 'italic',
    marginTop: 8,
  },
  coachingTips: {
    backgroundColor: '#f8fafc',
    padding: 15,
    borderRadius: 8,
    marginBottom: 20,
  },
  tipsTitle: {
    fontSize: 16,
    fontWeight: 'bold',
    color: '#1e40af',
    marginBottom: 10,
  },
  tipsText: {
    fontSize: 14,
    color: '#475569',
    marginBottom: 6,
  },
  footer: {
    padding: 20,
    backgroundColor: '#f8fafc',
    alignItems: 'center',
  },
  footerText: {
    fontSize: 14,
    color: '#64748b',
    textAlign: 'center',
    marginBottom: 4,
  },
});

export default App;
