import streamlit as st
import requests

st.title("hello")
id_input = st.text_input("Enter an ID:")
data_type = st.radio("Select data type:", ("Track", "Playlist"))
if st.button("Get data"):
    if data_type == "Track":
        data = requests.get(
            f"http://172.20.0.2:8080/tracks/{id_input}").json()
        st.write("Track data:", data)
    elif data_type == "Playlist":
        data = requests.get(
            f"http://172.20.0.2:8080/playlists/{id_input}").json()
        st.write("Playlist data:", data)

# def main():
#     id_input = st.text_input("Enter an ID:")
#     data_type = st.radio("Select data type:", ("Track", "Playlist"))

#     if st.button("Get data"):
#         if data_type == "Track":
#             data = requests.get(
#                 f"http://localhost:8989/tracks/{id_input}").json()
#             st.write("Track data:", data)
#         elif data_type == "Playlist":
#             data = requests.get(
#                 f"http://localhost:8989/playlists/{id_input}").json()
#             st.write("Playlist data:", data)


#     if __name__ == "__main__":
#         st.run(main)
