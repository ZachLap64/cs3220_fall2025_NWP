import streamlit as st
import streamlit.components.v1 as components
from PIL import Image
import random
from CrazyHouse import CrazyHouse
from agent import RandomCatAgent
from residents import *

def getimgs(agentLoc, envState):
    images = [['empty'],['empty'],['empty'],['empty'],['empty']]
    for i in range(len(envState)):
        if isinstance(envState[i],Dog):
            images[i] = Image.open("imgs/dog image.jpeg")#dog image
        elif isinstance(envState[i],Mouse):
            images[i] = Image.open("imgs/mouse image.jpeg")#mouse image
        elif isinstance(envState[i],Milk):
            if images[i] == Image.open("imgs/dog image.jpeg"):#dog image
                images[i].append(Image.open("imgs/milkImage.jpeg"))#milk image
            else:
                images[i] = Image.open("imgs/milkImage.jpeg")#milk image
    images[agentLoc].append(Image.open("imgs/catImage.jpeg"))#cat image
    return images

def drawBtn(e,a):
    option= [e,a]
    st.button("Run One Agent's Step", on_click= AgentStep, args= [option])
    
def AgentStep(opt):
    st.session_state["clicked"] = True
    e,a= opt[0],opt[1]
    
    if e.is_agent_alive(a):
        stepActs=e.step()
        st.success(" Agent decided to do: {}.".format(",".join(stepActs)))
        st.success("RandomVacuumAgent is located at {} now.".format(a.location))
        st.info("Current Agent performance: {}.".format(a.performance))
        st.info("State of the Environment: {}.".format(e.status))
    else:
        st.error("Agent in location {} and it is dead.".format(a.location))
        
    images=getimgs(a.location, e.status)
    st.image(images)





def main():
    if "clicked" not in st.session_state:
        st.session_state["clicked"] = False

    if not st.session_state["clicked"]:
        st.title('Simple Agents - lab2. Example1')
        st.header("_Initial Env._", divider=True)
        a1 = RandomCatAgent()
        st.info(f"{a1} has the initial performance: {a1.performance}")
        e1 = CrazyHouse()
        st.info("State of the Environment: {}.".format(e1.status))
        e1.add_thing(a1)
        images = getimgs(a1.location,e1.status)
        st.image(images)

    if st.session_state["clicked"]:
        st.warning("Agent Step Done!")




if __name__ == '__main__':
    main()