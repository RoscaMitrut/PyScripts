from win11toast import toast
import keyboard
import pyautogui
import pyperclip
import ollama

audio = 'ms-winsoundevent:Notification.SMS'
chosen_model = 'llama3'
start_hotkey = 'ctrl+alt+q'
end_hotkey = 'ctrl+alt+x'
additional_text = """DON'T use any additional text, other than the answer. Use NO more than 150 characters and NO more than 1 paragraph to answer"""

def handle_button_press(arg,clipboard):
    try:
        arg = arg['arguments'].split(':')[-1]
    except:
        return
    
    match arg:
        case "Translate":
            prompt = f"Translate the following text: {clipboard}. {additional_text}."
        case "Explain":
            prompt = f"Briefly explain: {clipboard}. {additional_text}."
        case "1-1":
            prompt = f"{clipboard}. {additional_text}."
        case _:
            prompt = ""

    if(prompt!=""):
        try:
            response = ollama.chat(model=chosen_model, messages=[
                {
                    'role': 'user',
                    'content': f'{prompt}',
                },
            ])
            pyperclip.copy(response['message']['content'])
            toast("Response:", response['message']['content'], duration='long')
        except:
            return
        
def release_all_keys():
    for key in keyboard.all_modifiers:
        if keyboard.is_pressed(key):
            keyboard.release(key)
            
def show_notification():
    clipboard = pyperclip.paste()
    toast("Select: ", buttons=['Translate', 'Explain', '1-1'], audio=audio, on_click=lambda args: handle_button_press(args, clipboard))
            
def on_key_event():
    release_all_keys()
    pyautogui.hotkey('ctrl', 'c')
    show_notification()

keyboard.add_hotkey(start_hotkey, on_key_event)
keyboard.wait(end_hotkey)
