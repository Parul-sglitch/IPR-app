import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

def plot_ipr(jf,prf,pr,qo_max):
    jf=float(jf)
    prf=float(prf)
    pr=float(pr)
    pwf=np.arange(0,prf)
    qo=(jf*prf)*(1-0.2*pwf/prf-0.8*(pwf/prf)**2)/1.8
    pw=np.arange(0,pr)
    qop=qo_max*(1-0.2*pw/pr-0.8*(pw/pr)**2)
    st.write("Yeah!! Done")
    fig, ax = plt.subplots()
    plt.plot(pwf,qo,label='Future IPR')
    plt.plot(pw,qop,label='Present IPR')
    plt.legend()
    plt.xlabel('Pwf, Bottomhole flowing pressure (Psig)')
    plt.ylabel('qo, Flow rate (STB/day)')
    st.pyplot(fig)

    
def prod_index(qo,pwf,pr,krof,uof,bof,kro,uo,bo):
    qo=float(qo)
    pwf=float(pwf)
    pr=float(pr)
    krof=float(krof)
    uof=float(uof)
    bof=float(bof)
    kro=float(kro)
    uo=float(uo)
    bo=float(bo)
    qo_max=qo/((1-pwf/pr)*(1+0.8*(pwf/pr)))
    jp=1.8*(qo_max/pr)
    jf=jp*(krof/(uof*bof))/(kro/(uo*bo))
    return jf,qo_max
def main():
    col1,col2=st.beta_columns([1,2])
    with col1:
        img = Image.open("rig.jpeg")
        st.image(img, width=200)
    with col2:
        st.title("Future IPR prediction Using Standing's Extension of Vogel's Work for Saturated Oil Reservoir")
    st.subheader('Enter Input Values:')
    st.write('Initial Reservoir condition: ')
    qo=st.text_input('Qo, Stabilized Flow rate (STB/day)')
    pwf=st.text_input('Pwf, Bottomhole flowing pressure (Psig)')
    col3,col4=st.beta_columns([1,1])
    with col3:
        st.subheader('Current Values:')
        pr=st.text_input('Pr, Reservoir pressure (psig)')
        kro=st.text_input('kro, Relative oil permeability')
        uo=st.text_input('uo, Oil viscosity (cp)')
        bo=st.text_input('Bo, Oil formation volume factor (bbl/STB)')
    with col4:
        st.subheader('Future Values:')
        prf=st.text_input('Pr, Reservoir Pressure (psig)')
        krof=st.text_input('Kro, Relative Oil permeability')
        uof=st.text_input('uo, Oil Viscosity (cp)')
        bof=st.text_input('Bo, Oil Formation volume factor (bbl/STB)')
    submit=st.button('Predict')
    if submit:
        jf,qo_max=prod_index(qo,pwf,pr,krof,uof,bof,kro,uo,bo)
        plot_ipr(jf,prf,pr,qo_max)
if __name__=="__main__":
    main()
