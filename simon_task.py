"""This programm runs an extended version of the Simon Task on Expyriment"""

import expyriment
import random

# initializing experiment
exp = expyriment.design.Experiment(name = "Simon Task + Baseline")
expyriment.control.initialize(exp)

# creating practice and main block
practice = expyriment.design.Block(name="Practice")
main = expyriment.design.Block(name="Main")
mp_trials = [practice, main]

# creating baseline and default condition as blocks
baseline = expyriment.design.Block(name="Baseline")
default = expyriment.design.Block(name="Default")
blocks = [baseline, default]

# initializing colours
green = expyriment.misc.constants.C_GREEN
blue = expyriment.misc.constants.C_BLUE
white = expyriment.misc.constants.C_WHITE

# setting circle radius for stimuli
circle_radius = 40

# setting stimuli positions
left_pos = -350
right_pos = 350
y_pos = 0

# creating fixation cross
cross = expyriment.stimuli.FixCross()

# defining keyboard press
left_press = expyriment.misc.constants.K_d
right_press = expyriment.misc.constants.K_k
neutral_press = expyriment.misc.constants.K_b
space_press = expyriment.misc.constants.K_SPACE

key_press = [left_press, right_press]

# preloading fixation cross
cross.preload()

def set_up_trial(x_pos, col, cop):
    print(col)
    """
    Args:
        x_pos   - (int) -  position of stimulus on x-axis
        col     - (str) -  name of colour of stimulus
        cop     - (int) -  number of copies

        creates a new trial, saves factors Position and Colour
        creates a stimulus at position x_pos,0 in colour col
        stimuli are added to trial which is added to block

    Returns: the block
    """
    t = expyriment.design.Trial()
    t.set_factor("Position", str(x_pos))
    t.set_factor("Colour", str(col))
    c = expyriment.stimuli.Circle(circle_radius, position=[x_pos,y_pos], colour=col)
    t.add_stimulus(c)
    block.add_trial(t, copies=cop)
    return block

"""
creates blocks in main and practice trials
saves factors Block and Trials
creates default stimuli and baseline stimuli
"""
for mp in mp_trials:
    for block in blocks:
        block.set_factor("Block", block.name)
        block.set_factor("Trials", mp.name)
        if block == default:
            for pos in [left_pos, right_pos]:
                for col in [green, blue]:
                    block = set_up_trial(pos, col, 5)
        elif block == baseline:
            block = set_up_trial(0, white, 15)
        block.shuffle_trials()
        exp.add_block(block)

# initializing data variables
exp.data_variable_names = ["Trials","Block", "Colour", "Position", "Button", "RT"]

# Instruction texts
start_instructions = "Welcome to our Simon task experiment! Thank you for taking your time and contributing to our research. You can only take part in this experiment using a computer that is connected to a keyboard. Before we start, please make sure to not get distracted by anything (e.g. your phone, internet browser,...). Make yourself comfortable and get yourself mentally into a working space. If you feel ready to start the experiment, press SPACE to continue."
gen_instructions = "Before we get started we will provide you with some short instructions and explain what your task is going to be. You will be presented a white, blue or green circle. Your task is press B if there is a grey circle, J if there is a blue circle and F if there is a green circle. Your answers should ensue as fast and accurate as possible. In order to prepare you for the experimental setup you will first run through some practice trials before you proceed to the main trials. Before each task you will see what exactly to do and which key you have to press. If you feel ready to start the practice trials, please press SPACE."
bas_instructions = "Press B if you see a white circle. Please answer as fast as possible."
main_instructions = "So far so good! You have now finished the practice phase and hopefully well prepared for the main trials. They are identical in format and content. In order to proceed, press SPACE."
def_instructions = "Press K if there is a blue circle and D if there is a green circle. Please answer as fast as possible."
post_exp = "Perfect, you are done! Thank you for taking part in our experiment"

#------------------------------------------------------------------------------

# starting the experiment
expyriment.control.start()

# displaying start instructions until space is pressed
expyriment.stimuli.TextScreen(heading="Start",
                              text=start_instructions,
                              position=(0,0)).present()
exp.keyboard.wait(space_press)

def print_instructions(instr, header):
    """
    Args:
        instr    (str)    text displayed on screen
        header   (str)    header of instructions

    creates TextScreen with instructions for participant
    """
    expyriment.stimuli.TextScreen(heading=header,
                                  text=instr,
                                  position=(0,0)).present()
    exp.keyboard.wait(space_press)


counter = 0
for block in exp.blocks:
    if counter % 2 == 0:
        # displaying general instructions until space pressed
        if block.get_factor("Trials") == "Practice":
            print_instructions(gen_instructions, "General Instructions")
            # displaying main instructions until space pressed
        elif block.get_factor("Trials") == "Main":
            print_instructions(main_instructions, "Main Instructions")
    if block.name == "Default":
        # displaying default instructions until space pressed
        print_instructions(def_instructions, "Instructions")
    elif block.name == "Baseline":
        # displaying baseline instructions until space pressed
        print_instructions(bas_instructions, "Instructions")

    # displaying cross and stimuli randomly appearing
    # setting key_press for block conditions
    # adding data
    for trial in block.trials:
        cross.present()
        exp.clock.wait(random.randint(350,1200) - trial.stimuli[0].preload())
        trial.stimuli[0].present()
        if block.name == "Default":
            button, rt = exp.keyboard.wait(keys=key_press)
        elif block.name == "Baseline":
            button, rt = exp.keyboard.wait(keys=neutral_press)
        exp.data.add([block.get_factor("Trials"), block.get_factor("Block"), trial.get_factor("Colour"),
                        trial.get_factor("Position"), button, rt])
    counter +=1


# ending the experiment
expyriment.control.end(goodbye_text=post_exp)

# saving data in a csv
expyriment.misc.data_preprocessing.write_concatenated_data(data_folder="./data", file_name="simon_task", output_file="data.csv")
