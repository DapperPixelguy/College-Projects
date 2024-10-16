import tkinter as tk
from pyinflect import getInflection
import pandas as pd

chosen = 1


def set_story(input):
    global chosen
    chosen = input
    print(chosen)
    fill_temp()


root = tk.Tk()
title = tk.Label(text='Story generator')
root.geometry('200x200')
entry_field = tk.Entry()
confirm_button = tk.Button(text='Enter')
rainy = tk.Button(text='Rainy Day', command=lambda: set_story(1))
coffee = tk.Button(text='EX 2')

templates = {
    1: 'One [adjective] day, i was walking my [colour] pet [noun] when [plrnoun] started flying from the sky! I '
       'called my friend [name] and she said one just landed right on her [place]! [adverb], there was raining ['
       'plrnoun] as well and they were just going everywhere! My [noun] started [verb] and catching [plrnoun] with '
       'his mouth to eat.'
}

def fill_temp():
    template = templates[chosen]
    adj = pd.DataFrame(pd.read_csv('WordnetAdjectives.csv'))
    adv = pd.DataFrame(pd.read_csv('WordnetAdverbs.csv'))
    nou = pd.DataFrame(pd.read_csv('WordnetNouns.csv'))
    vb = pd.DataFrame(pd.read_csv('most-common-verbs-english.csv'))
    names = pd.DataFrame(pd.read_csv('names.csv'))
    vb_count = template.count('[verb]')
    adj_count = template.count('[adjective]')
    adv_count = template.count('[adverb]')
    nou_count = template.count('[noun]')
    plrnou_count = template.count('[plrnoun]')
    name_count = template.count('[name]')

    for i in range(adj_count):
        template = template.replace('[adjective]', adj['Word'].sample().values[0], 1)

    for i in range(adv_count):
        template = template.replace('[adverb]', adv['Word'].sample().values[0], 1)

    for i in range(nou_count):
        template = template.replace('[noun]', nou['Word'].sample().values[0], 1)

    for i in range(vb_count):
        template = template.replace('[verb]', vb['Word'].sample().values[0], 1)

    for i in range(name_count):
        template = template.replace('[name]', names['Name'].sample().values[0], 1)

    for i in range(plrnou_count):
        plrnoun = nou['Word'].sample().values[0]
        inflection = getInflection(plrnoun, tag='NNS')
        if inflection:
            template = template.replace('[plrnoun]', inflection[0], 1)
        else:
            template = template.replace('[plrnoun]', plrnoun + 's', 1)


    print(template)




def rainy_day():
 pass

# Packing
title.pack()
entry_field.pack()
confirm_button.pack()
rainy.pack()
root.mainloop()

