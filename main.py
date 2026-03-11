from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.core.window import Window
from kivy.utils import get_color_from_hex
from kivmob import KivMob

class GameScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.score = 0
        self.current_index = 0
        
        # قائمة الألغاز الـ 41
        self.puzzles = [
            {"q": "What has teeth but doesn't bite?", "a": ["comb"], "lvl": "Easy"},
            {"q": "What walks without feet, flies without wings, and cries without eyes?", "a": ["cloud"], "lvl": "Easy"},
            {"q": "What increases if you take from it, and decreases if you give to it?", "a": ["the pit", "pit"], "lvl": "Easy"},
            {"q": "What breaks as soon as it is spoken?", "a": ["silence"], "lvl": "Easy"},
            {"q": "Something we bring to eat, but we never actually eat it?", "a": ["the egg", "egg", "shell"], "lvl": "Easy"},
            {"q": "What is the thing found in the middle of 'Paris'?", "a": ["the letter r", "r"], "lvl": "Easy"},
            {"q": "Black when you buy it, red when you use it, gray when finished?", "a": ["coal"], "lvl": "Easy"},
            {"q": "Something that keeps eating and never gets full; water kills it?", "a": ["fire"], "lvl": "Easy"},
            {"q": "Passes through cities and fields but does not move?", "a": ["road", "roed"], "lvl": "Easy"},
            {"q": "What is the 'hand' that does not sting?", "a": ["clock hand", "hand of clock"], "lvl": "Easy"},
            {"q": "Something we bring to prepare but never eat?", "a": ["iron", "dishes"], "lvl": "Easy"},
            {"q": "What has a hand but cannot clap?", "a": ["the door", "the bell"], "lvl": "Easy"},
            {"q": "It has a river but no water, cities but no people?", "a": ["a map", "map"], "lvl": "Easy"},
            {"q": "It speaks without a mouth and hears without ears?", "a": ["echo"], "lvl": "Easy"},
            {"q": "Cannot enter a room unless hit on the head?", "a": ["nail"], "lvl": "Easy"},
            {"q": "What must be broken before you can use it?", "a": ["egg", "an egg"], "lvl": "Easy"},
            {"q": "Something belongs only to you, but others use it more?", "a": ["name"], "lvl": "Easy"},
            {"q": "Keys but no locks, space but no room?", "a": ["a keyboard", "keyboard"], "lvl": "Easy"},
            {"q": "The more you take, the more you leave behind?", "a": ["footsteps"], "lvl": "Easy"},
            {"q": "Tall when young, and short when old?", "a": ["candle"], "lvl": "Easy"},
            {"q": "What has hands but cannot clap?", "a": ["a clock", "clock"], "lvl": "Easy"},
            {"q": "What gets wetter the more it dries?", "a": ["a towel", "towel"], "lvl": "Easy"},
            {"q": "A man lives on the 10th floor. He takes the elevator down but back only to 7th. Why?", "a": ["short", "cannot reach"], "lvl": "Intermediate"},
            {"q": "What is the question that you can never answer Yes to?", "a": ["asleep"], "lvl": "Intermediate"},
            {"q": "What becomes lighter the more you add to it?", "a": ["hole"], "lvl": "Intermediate"},
            {"q": "What is always in front of you but can’t be seen?", "a": ["future"], "lvl": "Intermediate"},
            {"q": "How many months have 28 days?", "a": ["all", "12"], "lvl": "Intermediate"},
            {"q": "What can fill a room but takes up no space?", "a": ["light"], "lvl": "Intermediate"},
            {"q": "What invention lets you look right through a wall?", "a": ["window"], "lvl": "Intermediate"},
            {"q": "A man shaves several times a day, yet he still has a beard. Who?", "a": ["barber"], "lvl": "Difficult"},
            {"q": "What's always coming but never arrives?", "a": ["tomorrow"], "lvl": "Difficult"},
            {"q": "I am not alive but I grow, water kills me?", "a": ["fire"], "lvl": "Difficult"}
        ]

        # إضافة الخلفية
        self.add_widget(Image(source='1772036342043.png', allow_stretch=True, keep_ratio=False))

        # بناء الواجهة فوق الخلفية
        self.layout = BoxLayout(orientation='vertical', padding=40, spacing=20)
        
        self.level_label = Label(text="LEVEL: EASY", font_size='28sp', bold=True, color=(1, 0.8, 0, 1), size_hint=(1, 0.15))
        self.layout.add_widget(self.level_label)

        self.question_label = Label(text=self.puzzles[0]['q'], font_size='22sp', halign='center', size_hint=(1, 0.4), color=(1,1,1,1))
        self.question_label.bind(size=lambda s, w: setattr(s, 'text_size', (w[0], None)))
        self.layout.add_widget(self.question_label)

        self.answer_input = TextInput(multiline=False, size_hint=(1, 0.1), font_size='20sp', hint_text="Enter answer here...")
        self.layout.add_widget(self.answer_input)

        self.submit_btn = Button(text="SUBMIT", size_hint=(1, 0.15), background_color=(0, 0.6, 0.9, 1), font_size='22sp', bold=True)
        self.submit_btn.bind(on_press=self.check_answer)
        self.layout.add_widget(self.submit_btn)

        self.status_label = Label(text="Score: 0", font_size='18sp', size_hint=(1, 0.1))
        self.layout.add_widget(self.status_label)

        self.add_widget(self.layout)

    def check_answer(self, instance):
        user_ans = self.answer_input.text.lower().strip()
        correct_list = self.puzzles[self.current_index]['a']
        
        is_correct = any(correct in user_ans for correct in correct_list)

        if is_correct:
            self.score += 1
            self.status_label.text = f"Correct! Score: {self.score}"
            self.status_label.color = (0, 1, 0, 1)
        else:
            self.status_label.text = f"Wrong! Try next one."
            self.status_label.color = (1, 0, 0, 1)
        
        # إظهار إعلان بيني كل 5 أسئلة لزيادة الأرباح
        if self.current_index % 5 == 0 and self.current_index != 0:
            MDApp.get_running_app().show_interstitial_ad()

        self.current_index += 1
        self.answer_input.text = ""

        if self.current_index < len(self.puzzles):
            p = self.puzzles[self.current_index]
            self.question_label.text = p['q']
            self.level_label.text = f"LEVEL: {p['lvl'].upper()}"
        else:
            self.finish_game()

    def finish_game(self):
        self.question_label.text = f"Game Finished!\nScore: {self.score}/{len(self.puzzles)}"
        self.submit_btn.disabled = True

class PuzzleApp(MDApp):
    def build(self):
        # إعداد الإعلانات الحقيقية الخاصة بك
        self.ads = KivMob("ca-app-pub-4964161194904838~2207167188")
        self.ads.add_banner("ca-app-pub-4964161194904838/5526149913", top_pos=False)
        self.ads.add_interstitial("ca-app-pub-4964161194904838/9007209863")
        
        self.ads.request_banner()
        self.ads.show_banner()
        
        return GameScreen()

    def show_interstitial_ad(self):
        self.ads.request_interstitial()
        self.ads.show_interstitial()

if __name__ == "__main__":
    PuzzleApp().run()
