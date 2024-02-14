import streamlit as st

def contributors_page():
    st.balloons()
    st.write("""
                <h1 style="text-align: center; color:#FFF6F4;">A heartfelt thankyou to all our Members ❤️</h1><hr>
                <div style="text-align:center;">
                <table>
                <tr>
                    <th width="20%" style="font-size: 140%;">Chapter Name</th>    
                    <th width="20%" style="font-size: 140%;">Chapter Lead</th>    
                </tr>
                <tr>
                    <td>CareNetAI</td>    
                    <td>Min Htet Myet</td>    
                </tr>
                </table>
                <br>
                <table>
                    <tbody>
                        <tr>
                            <th width="20%" style="font-size: 140%;">Model</th>
                            <th width="20%" style="font-size: 140%;">Task Lead</th>
                        </tr>
                        <tr>
                            <td>Cancer Model</td>
                            <td>Tim Hayes</td>
                        </tr>
                        <tr>
                            <td>Tuberculosis Model</td>
                            <td>Alpha Lossangoyi Nanga</td>
                        </tr>
                        
                    </tbody>
                </table>
                </div>
            """, unsafe_allow_html=True)
