import streamlit as st
import requests

st.title("Welcome to MusicApp")
read_write = st.radio("Read, write, or remove data?",
                      ("Read", "Write", "Remove"))

if read_write == "Read":
    # Read data section
    st.header("Read track/playlist info")
    id_input = st.text_input("Enter an ID:")
    data_type = st.radio("Select data type:", ("Track", "Playlist"))
    if st.button("Get data"):
        if data_type == "Track":
            try:
                data = requests.get(
                    f"http://172.20.0.2:8080/tracks/{id_input}").json()
                st.write("Track data:", data)
            except requests.exceptions.HTTPError as err:
                st.error(err)

        elif data_type == "Playlist":
            try:
                data = requests.get(
                    f"http://172.20.0.2:8080/playlists/{id_input}").json()
                st.write("Playlist data:", data)
            except requests.exceptions.HTTPError as err:
                st.error(err)

elif read_write == "Write":
    # Write data section
    write_type = st.radio("Write track or playlist?", ("Track", "Playlist"))
    if write_type == "Track":
        # Add a section for adding new tracks
        st.header("Add a new track")
        track_id = st.number_input("ID:")
        track_name = st.text_input("Name:")
        track_artist = st.text_input("Artist:")
        track_album = st.text_input("Album:")
        track_genre = st.text_input("Genre:")
        track_duration = st.number_input("Duration (in seconds):")
        if st.button("Add track"):
            track_data = {
                "id": track_id,
                "name": track_name,
                "artist": track_artist,
                "album": track_album,
                "genre": track_genre,
                "duration": track_duration
            }
            response = requests.post(
                "http://172.20.0.2:8080/tracks", json=track_data)
            if response.status_code == 200:
                st.success("Track added successfully!")
            else:
                st.error("Error adding track.")

    elif write_type == "Playlist":
        # Add a section for adding new playlists
        st.header("Add a new playlist")
        playlist_id = st.number_input("ID:")
        playlist_name = st.text_input("Name:")
        playlist_tracks = st.text_input("Tracks IDs(comma-separated):")
        if st.button("Add playlist"):
            playlist_data = {
                "id": playlist_id,
                "name": playlist_name,
                "tracks": playlist_tracks.split(",")
            }
            response = requests.post(
                "http://172.20.0.2:8080/playlists", json=playlist_data)
            if response.status_code == 200:
                st.success("Playlist added successfully!")
            elif response.status_code == 404:
                st.error("Error adding playlist. One or more track IDs may not exist.")
            elif response.status_code == 409:
                st.error(
                    "Playlist's ID already exists")
            else:
                st.error("Error adding playlist.")
            
elif read_write == "Remove":
    # Remove data section
    remove_type = st.radio("Remove track or playlist?", ("Track", "Playlist"))

    if remove_type == "Track":
        # Add a section for removing tracks
        st.header("Remove a track")
        track_id = st.number_input("ID:")
        if st.button("Remove track"):
            track_id = int(track_id)
            response = requests.delete(f"http://172.20.0.2:8080/tracks/{track_id}")
            if response.status_code == 200:
                st.success("Track removed successfully!")
            else:
                st.error("Error removing track.")

    elif remove_type == "Playlist":
        # Add a section for removing playlists
        st.header("Remove a playlist")
        playlist_id = st.number_input("ID:")
        if st.button("Remove playlist"):
            playlist_id = int(playlist_id)
            response = requests.delete(
                f"http://172.20.0.2:8080/playlists/{playlist_id}")
            if response.status_code == 200:
                st.success("Playlist removed successfully!")
            else:
                st.error("Error removing playlist.")



