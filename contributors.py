import streamlit as st

def contributors_page():
    st.balloons()
    st.write("""
                <h1 style="text-align: center; color:#FFF6F4;">Member ❤️</h1><hr>
                <div style="text-align:center;">
                <table>
                <tr>
                    <th width="20%" style="font-size: 140%;">CareNet</th>    
                    <th width="20%" style="font-size: 140%;">Min Htet Myet </th>    
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
                            <th width="20%" style="font-size: 140%;"> Lead</th>
                        </tr>
                        <tr>

                        </tr>
                        
                    </tbody>
                </table>
                </div>
            """, unsafe_allow_html=True)
