import time
import streamlit as st
import json 

st.set_page_config(page_title="Personal Library Manager By Muniza Nabeel", page_icon="📚", layout="centered")

# Load & Save library data

def load_library():
    try:
        with open("library.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_library():
    with open("library.json", "w") as file:
        json.dump(library, file, indent=4)   

# Initialize Library
library = load_library()

st.title("📚 Personal Library Manager")
menu = st.sidebar.radio("📖 Select an Option:", ["📋 View Library", "➕ Add Book", "❌ Remove Book", "🔍 Search Book", "💾 Save and Exit"])

if menu == "📋 View Library":    
    st.sidebar.write("📂 Your Library")
    if library:
        st.table(library)
    else:
        st.write("🚫 Your Library is Empty. Add Some Books! 😊")

# Add Book
elif menu == "➕ Add Book":
    st.sidebar.write("📘 Add a new Book:")
    title = st.text_input("📗 Title")
    author = st.text_input("✍️ Author Name: ")
    year = st.number_input("📅 Year", min_value=2022, max_value=2100, step=1)
    genre = st.text_input("📚 Genre")   # Category
    read_status = st.checkbox("✅ Mark as Read")

    if st.button("➕ Add Book"):
        library.append({"title": title, "author": author, "year": year, "genre": genre, "read_status": read_status})
        save_library()
        st.success("🎉 Book Added Successfully!!")
        st.balloons()
        time.sleep(3) # Wait for 3 seconds
        st.rerun()

# Remove Book
elif menu == "❌ Remove Book":
    st.sidebar.write("🗑️ Remove a Book")
    book_titles = [book["title"] for book in library]

    if book_titles:
        selected_book = st.selectbox("📖 Select a book to remove", book_titles)
        if st.button("❌ Remove Book"):
            library = [book for book in library if book["title"] != selected_book]
            save_library()
            st.success("✔️ Book Removed Successfully!!")
            st.rerun()
    else:
        st.warning("⚠️ No book in Your library. Add Some Books!!")

# Search Book
elif menu == "🔍 Search Book":
    st.sidebar.write("🔍 Search a Book")
    search_term = st.text_input("🔎 Enter book title or author name:")
    if st.button("🔍 Search"):
        results = [book for book in library if search_term.lower() in book["title"].lower() or search_term.lower() in book["author"].lower()]
        if results:
            st.table(results)
        else:
            st.warning("🚫 No book found! Try again.")

# Save and Exit
elif menu == "💾 Save and Exit":
    save_library()
    st.success("💾 Library Saved Successfully!!")
    st.balloons()
