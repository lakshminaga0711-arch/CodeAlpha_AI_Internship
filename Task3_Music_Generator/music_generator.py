from music21 import stream, note, tempo, instrument


# Create a new music score
score = stream.Stream()

# Set the tempo
score.append(tempo.MetronomeMark(number=100))

# Add piano
score.append(instrument.Piano())

# Melody notes
melody = [
    ("C4", 1),
    ("D4", 1),
    ("E4", 1),
    ("F4", 1),
    ("G4", 1),
    ("E4", 1),
    ("D4", 1),
    ("C4", 2),
]

# Add notes to the score
for pitch, duration in melody:
    new_note = note.Note(pitch)
    new_note.duration.quarterLength = duration
    score.append(new_note)


# Display generated notes
print("🎵 Music Generator")
print("------------------")
print("Generated melody:")

for element in score.notes:
    print(element)


# Save the music as a MIDI file
score.write("midi", fp="generated_music.mid")

print("\n✅ Music generated successfully!")
print("🎶 MIDI file saved as: generated_music.mid")