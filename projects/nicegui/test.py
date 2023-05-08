from nicegui import ui

def on_slider_change(slider):
    label.text = f"Slider value: {slider.value:.2f}"

slider = ui.slider(min=0, max=100, step=1, on_change=on_slider_change)
label = ui.label('Slider value: 0')

ui.run()
