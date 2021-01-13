from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.slider import Slider
from kivy.uix.label import Label
from kivy.properties  import NumericProperty

class MainApp(App):
    def build(self):

        def mortgage_on_value(instance, value):
            mortgageValue.text = str(value)
            return

        def interest_on_value(instance, value):
            interestValue.text = str(value)
            return

        def term_on_value(instance, value):
            termValue.text = str(value)
            return

        def calculateSolution(instance, value):
            solution.text = str(float(termValue.text) * float(interestValue.text) * float(mortgageValue.text))
            return

        main_layout = BoxLayout(orientation="vertical")
        display_layout =BoxLayout(orientation="horizontal")
        mortgage_layout = BoxLayout(orientation="horizontal")
        interest_layout = BoxLayout(orientation="horizontal")
        term_layout = BoxLayout(orientation="horizontal")

        solution = Label(text="0")


        button = Button(text="Press to Calculate", pos_hint={"center_x": 0.5, "center_y": 0.5})
        button.bind(state=calculateSolution)

        mortgageControl = Slider(min=10000, max=2000000, value=500000, step = 5000)
        mortgage_layout.add_widget(Label(text ='Mortgage Rate'))
        mortgage_layout.add_widget(mortgageControl)
        mortgageValue = Label(text ='500000')
        mortgage_layout.add_widget(mortgageValue)
        mortgageControl.bind(value=mortgage_on_value)

        interestControl = Slider(min=0, max=20, value=5, step = .25)
        interest_layout.add_widget(Label(text ='Interest Rate'))
        interest_layout.add_widget(interestControl)
        interestValue = Label(text ='5')
        interest_layout.add_widget(interestValue)
        interestControl.bind(value = interest_on_value)
        #
        termControl = Slider(min=1, max=30, value=20, step = 1)
        term_layout.add_widget(Label(text ='Term'))
        term_layout.add_widget(termControl)
        termValue = Label(text ='15')
        term_layout.add_widget(termValue)
        termControl.bind(value = term_on_value)

        display_layout.add_widget(solution)
        display_layout.add_widget(button)
        main_layout.add_widget(display_layout)
        main_layout.add_widget(mortgage_layout)
        main_layout.add_widget(interest_layout)
        main_layout.add_widget(term_layout)

        return main_layout




if __name__ == "__main__":
    app = MainApp()
    app.run()
