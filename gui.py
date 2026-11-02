import streamlit as st

from movies import MovieManager

movie_instance = MovieManager()
t1, t2, t3, t4, t5 = st.tabs(["Add", "View", "Retrieve", "Update", "Delete"])

with t1:
    st.title("Add New Movie")
    title = st.text_input("Enter Title")
    genre = st.text_input("Enter Genre")
    language = st.text_input("Enter Language")
    rating = st.text_input("Enter Rating")
    rel_year = st.text_input("Enter Release Year")

    if st.button("Add new movie"):
        movie_instance.post(title= title, genre= genre, language= language, rating= rating, release_year= rel_year)
        st.success("Movie added successfully")

with t2:
    st.title("View Movies")
    records = movie_instance.get()
    if records:
        st.table(records)
    else:
        st.warning("No Movies Found!")

with t3:
    st.title("Retrieve Record")
    id = st.text_input("Enter ID")
    if st.button("Search"):
        data = movie_instance.retrieve(id)
        if data:
            st.success("Movie Found!")
            st.table([data])
        else:
            st.warning("Movie Not Found!")

with t4:
    st.title("Update Movie")
    movie_id = st.text_input("Enter Movie ID")

    title = st.text_input("New Title")
    genre = st.text_input("New Genre")
    language = st.text_input("New Language")
    rating = st.text_input("New Rating")
    release_year = st.text_input("New Release Year")

    if st.button("Update"):
        update_data = {}

        if title:
            update_data["title"] = title
        if genre:
            update_data["genre"] = genre
        if language:
            update_data["language"] = language
        if rating:
            update_data["rating"] = rating
        if release_year:
            update_data["release_year"] = release_year

        if update_data:
            result = movie_instance.put(movie_id, **update_data)
            if result:
                st.success("Movie Details Updated!")
            else:
                st.warning("Movie Not Found!")
        else:
            st.warning("Enter at least one field to update.")


with t5:
    st.title("Delete Record")
    del_id = st.text_input("Enter ID of movie to delete")

    if st.button("Delete"):
        result = movie_instance.delete(del_id)

        if result:
            st.success("Movie Deleted!")
        else:
            st.warning("Movie Not Found!")