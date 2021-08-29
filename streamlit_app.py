import streamlit as st
import json
import codecs
import streamlit.components.v1 as components
import pyautogui

st.set_page_config(page_title="Streamlit JSON Validator",layout='wide')

c_1,c_2,c_3=st.columns([1,1,2])

with c_1:
    reload = st.button("RELOAD")

with c_2:
    clear = st.button("CLEAR")

def Clear():
    pyautogui.press("tab", interval=0.15)
    pyautogui.press("tab", interval=0.15)
    pyautogui.hotkey("ctrl", "a",'del', interval=0.15)

def refresh():
    pyautogui.press("f5", interval=0.15)


# Clear I / referesh
if clear: Clear()
if reload: refresh()

with c_3:
    st.title("Streamlit JSON Validator")

col_1, col_2, col_3 = st.columns([1,1,2])

with col_1:
    input = st.text_area("JSON Editor", "[" + "\n" + chr(9) + "{" + "\n\n" + chr(9) + "}" + "\n" + "]", height=600)

with col_2:
    try:
        input_str = json.loads(input)
        f = codecs.open("output.json", "w", encoding="utf-8")
        json_out = json.dumps(input_str, sort_keys=False, indent=4)
        f.write(json_out)
        f.flush()
        o = open("output.json")
        ojson = o.read()
        st.text_area("JSON OUTPUT", ojson, height=600)
    except Exception as e:
        st.text_area("JSON OUTPUT", e, height=600)

with col_3:
    st.text("JSON Tutorial")
    components.iframe("https://www.youtube.com/embed/B2aCwbKrn70", width=500, height=250)
    components.iframe("https://www.youtube.com/embed/lU-DSq-tNtw", width=500, height=250)
