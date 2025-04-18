import tkinter as tk
from tkinter import Toplevel, Label
import ttkbootstrap as tb
import random

# Some calming quotes
zen_quotes = [
"Breathe. You are exactly where you need to be.",
"Peace comes from within. Do not seek it without.",
"Let go of what you can’t control.",
"Smile, breathe and go slowly.",
"This too shall pass.",
"Don’t be afraid to just sit and watch.",
"Your mind wants control. Life wants change.",
"Don’t try to steer the river.",
"Be present above all else.",
"To go beyond is as wrong as to fall short.",
"Those who seek the easy way do not seek the true way.",
"To seek is to suffer. To seek nothing is bliss.",
"A Zen master’s life is one continuous mistake.",
"To live – is that not enough?",
"Zen has no business with ideas.",
"I follow four dictates: face it, accept it, deal with it, then let it go.",
"In the highest level a man has the look of knowing nothing.",
"Singlemindedness is all-powerful.",
"Wherever you are, be there totally.",
"Truth makes you rise to new heights, no matter where you are.",
"Little people try to control everything. Wise people focus on the most important and let go of the rest.",
"Little people are overwhelmed by emotions. Zen people are calm and detached.",
"In the midst of chaos, there is also opportunity.",
"Zen is not some special state, it is our normal condition, silent, peaceful, awake, without agitation.",
"Purity is attained by piling effort upon effort.",
"The beauty of Zen is found in simplicity and tranquility.",
"Relax. Nothing is under control.",
"It really boils down to this: all life is interrelated.",
"Learning Zen is a phenomenon of gold & dung.",
"You are a function of what the whole universe is doing as a wave is a function of the ocean.",
"At the still-point in the center of the circle one can see the infinite in all things.",
"No snowflake ever falls in the wrong place.",
"Out beyond ideas of wrongdoing and rightdoing there is a field. I’ll meet you there.",
"Why is the tao so valuable? Because it is everywhere, and everyone can use it.",
"As a bee gathering nectar does not harm the flower, so do the wise move through the world.",
"Zazen is an activity that is an extension of the universe.",
"The whole moon and the entire sky are reflected in one dewdrop on the grass.",
"Tao in the world is like a river flowing home to the sea.",
"Try to imagine what it will be like to go to sleep and never wake up… now try to imagine what it was like to wake up having never gone to sleep.",
"You are an aperture through which the universe is looking at and exploring itself.",
"No one saves us but ourselves. We ourselves must walk the path.",
"Whatever is not yours: let go of it.",
"If with a pure mind a person speaks or acts, happiness follows them like a never-departing shadow.",
"Just as the great ocean has one taste — the taste of salt — so this teaching has one taste: liberation.",
"It is easy to see the faults of others, but difficult to see one’s own faults.",
"The only real failure in life is not to be true to the best one knows.",
"It is ridiculous to think that somebody else can make you happy or unhappy.",
"The way is not in the sky. The way is in the heart.",
"One who seeks happiness but oppresses others will not attain happiness.",
"We are what we think. All that we are arises with our thoughts.",
"Happiness will never come to those who fail to appreciate what they already have.",
"What we think, we become.",
"Should a person do good, let him do it again and again.",
"The mind is everything. What you think you become.",
"I am the miracle.",
"To be idle is a short road to death; to be diligent is a way of life.",
"Drop by drop is the water pot filled. Likewise, the wise man fills himself with good.",
"There is no fire like passion; no shark like hatred; no snare like folly; no torrent like greed.",
"Chaos is inherent in all compounded things. Strive on with diligence.",
"To enjoy good health and bring peace to all, one must first control one’s own mind.",
"You can search the universe for someone more deserving of your love than yourself, and not find anyone.",
"We are shaped by our thoughts; when the mind is pure, joy follows like a shadow.",
"If you wish to be gentle with others, be gentle first with yourself.",
"Pain is certain, suffering is optional.",
"Just as a snake sheds its skin, we must shed our past over and over again.",
"Like a fine flower, beautiful but without scent, fine words are fruitless without action.",
"Those free of resentful thoughts find peace.",
"To insist on a past spiritual practice is to carry the raft after crossing the river.",
"If you are quiet enough, you will hear the flow of the universe.",
"If you find no one to support you on the spiritual path, walk alone.",
"Stop, do not speak. The ultimate truth is not even to think.",
"Generosity brings happiness at every stage of its expression.",
"Better than a thousand hollow words is one word that brings peace.",
"The one in whom craving no longer exists is trackless and of limitless range.",
"She who knows life flows, feels no wear or tear, needs no repair.",
"Endurance is difficult, but to the one who endures comes final victory.",
"Long is the night to him who is awake; long is life to the foolish.",
"There is no path to happiness: happiness is the path.",
"Be vigilant; guard your mind against negative thoughts.",
"When you realize how perfect everything is you will laugh at the sky.",
"Life is very difficult. How can we be anything but kind?",
"The foot feels the foot when it feels the ground.",
"You only lose what you cling to.",
"Your purpose in life is to find your purpose and give your whole heart to it.",
"Just as treasures are uncovered from the earth, so virtue appears from good deeds.",
"Ambition is like love: impatient of delays and rivals.",
"Love is a gift of one’s innermost soul to another so both can be whole.",
"To live a pure unselfish life, count nothing as one’s own in abundance.",
"Believe nothing unless it agrees with your own reason and common sense.",
"Whatever a monk pursues with thinking becomes the inclination of his awareness.",
"There is nothing so disobedient as an undisciplined mind, nothing so obedient as a disciplined mind.",
"To live freely, we must acquire an unfettered mind.",
"A day without working is a day without eating.",
"When a flower blooms, the butterfly naturally finds it.",
"Life requires time and effort; eliminate them and you eliminate lifes pleasures.",
"They call it peace of mind but maybe it should be called peace from mind.",
"It is easy to believe we are each wave and forget we are also the ocean.",
"I dont hold on to anything, dont reject anything; nowhere an obstacle or conflict.",
"Emptiness is the reservoir of infinite possibilities.",
"Those who do not pay attention to their footsteps cannot know themselves.",
"When trees have blossomed, birds flock to the branches on their own.",
"Little people are overwhelmed by emotions; Zen people are calm and detached.",
"Wherever you are, be there totally.",
"Truth makes you rise to new heights, no matter where you are.",
"Relax. Nothing is under control.",
"Peace comes from within. Do not seek it without."
]
# Show magic popup
def do_magic():
    quote = random.choice(zen_quotes)

    popup = Toplevel(root)
    popup.geometry("320x120")
    popup.overrideredirect(True)
    popup.configure(bg='#ffffff')
    popup.attributes('-alpha', 0.92)
    popup.attributes('-topmost', True)
   

    popup_frame = tk.Frame(popup, bg='#ffffff', bd=0, relief='flat')
    popup_frame.pack(expand=True, fill='both', padx=10, pady=10)

    Label(
        popup_frame,
        text=quote,
        font=("Helvetica", 11),
        wraplength=280,
        bg='#ffffff',
        fg='#333'
    ).pack(expand=True)

    popup.after(3500, popup.destroy)

# Make window draggable
def start_move(event):
    root.x = event.x
    root.y = event.y

def stop_move(event):
    root.x = None
    root.y = None

def do_move(event):
    x = root.winfo_x() + (event.x - root.x)
    y = root.winfo_y() + (event.y - root.y)
    root.geometry(f"+{x}+{y}")

# Main window setup
root = tb.Window(themename="cosmo")  # Choose light-modern theme
root.geometry("320x120")
root.overrideredirect(True)
root.configure(bg="#f2f3f5")
root.eval('tk::PlaceWindow . center')
root.attributes('-topmost', True)
root.attributes('-alpha', 0.96)

# Allow dragging from anywhere
root.bind("<ButtonPress-1>", start_move)
root.bind("<ButtonRelease-1>", stop_move)
root.bind("<B1-Motion>", do_move)

# Zen Button with pill style
button = tb.Button(
    root,
    text="Zen Button",
    bootstyle="light-outline",
    command=do_magic,
    width=20
)
button.pack(expand=True, padx=30, pady=20)

# Make it more neumorphic/glassy
button.configure(
    style='glass.TButton'
)

# Custom ttk style for glass button
style = tb.Style()
style.configure('glass.TButton',
    font=("Helvetica", 14, "bold"),
    foreground="#000",
    background="#ffffff",
    borderwidth=0,
    relief="flat",
    focusthickness=0,
    padding=10
)

# Run app
root.mainloop()