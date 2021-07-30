import expyriment
import random

exp = expyriment.design.Experiment(name = "Simon Task + Baseline")
expyriment.control.initialize(exp)

#creating blocks
practice = expyriment.design.Block(name="Practice")
main = expyriment.design.Block(name="Main")
mp_trials = [practice, main]

"""Block description """
baseline = expyriment.design.Block(name="Baseline")
default = expyriment.design.Block(name="Default")
blocks = [baseline, default]

#colours
green = expyriment.misc.constants.C_GREEN
blue = expyriment.misc.constants.C_BLUE
grey = expyriment.misc.constants.C_WHITE
#creating stimuli
circle_Radii = 40

#positions
left_Pos = -350
right_Pos = 350
Y_POS = 0
#creating cross
cross = expyriment.stimuli.FixCross()

#keyboard input
left_Press = expyriment.misc.constants.K_d
right_Press = expyriment.misc.constants.K_k
neutral_Press = expyriment.misc.constants.K_b
key_press = [left_Press, right_Press]

enter_Press = expyriment.misc.constants.K_SPACE
#preloading
cross.preload()

def set_up_trial(x_pos, col, cop):
    t = expyriment.design.Trial()
    t.set_factor("Position", str(x_pos))
    t.set_factor("Colour", str(col))
    c = expyriment.stimuli.Circle(circle_Radii, position=[x_pos,Y_POS], colour=col)
    t.add_stimulus(c)
    block.add_trial(t, copies=cop)
    return block

for mp in mp_trials:
    for block in blocks:
        block.set_factor("Block", block.name)
        block.set_factor("Trials", mp.name)
        if block == default:
            for pos in [left_Pos, right_Pos]:
                for col in [green, blue]:
                    block = set_up_trial(pos, col, 5)
        elif block == baseline:
            block = set_up_trial(0, grey, 15)
        block.shuffle_trials()
        exp.add_block(block)
    #exp.add_block(mp)

#data
exp.data_variable_names = ["Trials","Block", "Colour", "Position", "Button", "RT"]

#Start_instructions
start_instructions = "Welcome to our Simon task experiment! Thank you for taking your time and contributing to our research. You can only take part in this experiment using a computer that is connected to a keyboard. Before we start, please make sure to not get distracted by anything (e.g. your phone, internet browser,...). Make yourself comfortable and get yourself mentally into a working space. If you feel ready to start the experiment, press enter to continue."
gen_instructions = "Before we get started we will provide you with some short instructions and explain what your task is going to be. You will be presented a grey, blue or green circle. Your task is press B if there is a grey circle, J if there is a blue circle and F if there is a green circle. Your answers should ensue as fast and accurate as possible. In order to prepare you for the experimental setup you will first run through some practice trials before you proceed to the main trials. Before each task you will see what exactly to do and which key you have to press. If you feel ready to start the practice trials, please press enter."
bas_instructions = "Press B if you see a grey circle. Please answer as fast as possible."
main_instructions = "So far so good! You have now finished the practice phase and hopefully well prepared for the main trials. They are identical in format and content. In order to proceed, press enter."
def_instructions = "Press J if there is a blue circle and F if there is a green circle. Please answer as fast as possible."
post_exp = "Perfect, you are done! Thank you for taking part in our experiment"

#---!!!

#------------------------------------------------------------------------------
#starting the experiment
expyriment.control.start()

#default display
expyriment.stimuli.TextScreen(heading="Start",
                              text=start_instructions,
                              position=(0,0)).present()
exp.keyboard.wait(enter_Press)

"""
if mp.name == "Practice":
    expyriment.stimuli.TextScreen(heading="General Instructions",
                                  text=gen_instructions,
                                  position=(0,0)).present()
    exp.keyboard.wait(enter_Press)
elif mp.name == "Main":
    expyriment.stimuli.TextScreen(heading="Main Instructions",
                                  text=main_instructions,
                                  position=(0,0)).present()
    exp.keyboard.wait(enter_Press)
"""
counter = 0
for block in exp.blocks:
    if counter % 2 == 0:
        if block.get_factor("Trials") == "Practice":
            expyriment.stimuli.TextScreen(heading="General Instructions",
                                          text=gen_instructions,
                                          position=(0,0)).present()
            exp.keyboard.wait(enter_Press)
        elif block.get_factor("Trials") == "Main":
            expyriment.stimuli.TextScreen(heading="Main Instructions",
                                          text=main_instructions,
                                          position=(0,0)).present()
            exp.keyboard.wait(enter_Press)
    if block.name == "Default":
        expyriment.stimuli.TextScreen(heading="",
                                      text=def_instructions,
                                      position=(0,0)).present()
        exp.keyboard.wait(enter_Press)
    elif block.name == "Baseline":

        expyriment.stimuli.TextScreen(heading="",
                                      text=bas_instructions,
                                      position=(0,0)).present()
        exp.keyboard.wait(enter_Press)

    for trial in block.trials:
        cross.present()
        exp.clock.wait(random.randint(350,1200) - trial.stimuli[0].preload())
        trial.stimuli[0].present()
        if block.name == "Default":
            button, rt = exp.keyboard.wait(keys=key_press)
        elif block.name == "Baseline":
            button, rt = exp.keyboard.wait(keys=neutral_Press)
        exp.data.add([block.get_factor("Trials"), block.get_factor("Block"), trial.get_factor("Colour"),
                        trial.get_factor("Position"), button, rt])
    counter +=1


#ending the experiment
expyriment.control.end(goodbye_text=post_exp)

#saving data in a csv
expyriment.misc.data_preprocessing.write_concatenated_data(data_folder="./data", file_name="simon_task", output_file="data.csv")
