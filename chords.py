# python guitar assistant - misha krul 2/20/18
"""
The program takes input in the form of guitar chords and replays them in timed intervals until stopped.
"""
import csv
import time
import sys

def main():
    answer = input("Welcome to Python Guitar Assistant.\n\n"
                    "Press '1' to create a new file.\n"
                    "Press '2' to load a saved file.\n"
                    "Press '3' to exit the program. ")
    if answer == '1':
        new_file = create_new_file()
        csv_chords = get_guitar_chords(new_file)
        play_chords(csv_chords)
    elif answer == '2':
        file_exists, chord_file = does_file_exist()
        if file_exists:
            csv_chords = load_from_csv(chord_file)
            play_chords(csv_chords)
    else:
        print("Exiting program...")
        exit()

def create_new_file():
    file_name = make_csv()
    new_file = open(file_name, 'w')
    new_file.close()
    return file_name

def make_csv():
    # note: must ignore special characters other than '-' and '_'
    separator = '.'
    file_name = input("Enter file name: ").split(separator, 1)[0]
    file_name += '.csv'
    return file_name

def does_file_exist():
    chord_data = []
    file_exists = False
    while file_exists == False:
        try:
            chordfile_name = make_csv()
            with open(chordfile_name) as file:
                file_exists = True
                return file_exists, chordfile_name
        except IOError as e:
            while file_exists == False:
                file_not_found = input("File not found.\n\nPlease re-enter file name, or type 'NEW' to generate a new file: ").lower()
                if file_not_found == 'new':
                    new_file = create_new_file()
                    file_exists == True
                    return file_exists, new_file

def load_from_csv(chordfile):
    chord_list = []
    rownum = 0
    loaded_file = open(chordfile, 'r')
    chord_reader = csv.reader(loaded_file)
    for row in chord_reader:
        chord_list.append(row)
        rownum += 1
    loaded_file.close()
    flattened_chord_list = [val for sublist in chord_list for val in sublist]
    return flattened_chord_list

def get_guitar_chords(chordfile):
    another_chord = ''
    chords = []
    print("Enter guitar chords one at a time.\n"
          "Type 'STOP' at any time to stop entering chords.\n")
    while another_chord != 'STOP':
        another_chord = input("Enter chord: ").upper()
        if another_chord != 'STOP':
            chords.append(another_chord)
    write_to_csv(chordfile, chords)

def write_to_csv(chord_file_name, chords):
    with open(chord_file_name, 'w') as chord_file:
        chord_writer = csv.writer(chord_file, delimiter='\n', quoting=csv.QUOTE_MINIMAL)
        for each_chord in chords:
            chord_file.write(each_chord + '\n')
    chord_file.close()
    return chord_file

def get_playback_speed():
    speed = int(input("Enter playback speed (1 = fastest, 5 = slowest): "))
    return speed

def play_chords(chords):
    playback_speed = get_playback_speed()
    countdown = ["Get ready!", "    ", "3...", "2...", "1..."]
    SPACING = (" " * 10)
    playing = True
    for each_char in countdown:
        time.sleep(1)
        sys.stdout.write(each_char)
        sys.stdout.flush()
    sys.stdout.write("\r\n")
    while playing:
        for each_chord in chords:
            time.sleep(playback_speed)
            sys.stdout.write("\r" + SPACING + each_chord + SPACING)
            sys.stdout.flush()
main()
