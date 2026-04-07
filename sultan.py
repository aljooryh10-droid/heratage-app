import streamlit as st

# This keeps your stories saved while the app is running
if "archive" not in st.session_state:
    st.session_state.archive = []

st.title("📜 Family Heritage Archive")

# Use a sidebar instead of a numbered menu
menu = ["Add Story", "View Stories", "Search Story"]
choice = st.sidebar.radio("Navigation", menu)

if choice == "Add Story":
    st.subheader("Add a New Story")
    # text_area and text_input replace input()
    original = st.text_area("Enter your story (Arabic or English):")
    values = st.text_input("Enter UAE family values (comma separated):")
    
    if st.button("Save Story"):
        if original:
            translated = "[Translated]: " + original 
            st.session_state.archive.append({
                "original": original,
                "translated": translated,
                "values": values
            })
            st.success("Story saved successfully!")
        else:
            st.warning("Please enter a story first.")

elif choice == "View Stories":
    st.subheader("Archived Stories")
    if not st.session_state.archive:
        st.info("No stories found yet.")
    for i, s in enumerate(st.session_state.archive, 1):
        with st.expander(f"Story {i}"):
            st.write(f"**Original:** {s['original']}")
            st.write(f"**Translated:** {s['translated']}")
            st.write(f"**Values:** {s['values']}")

elif choice == "Search Story":
    st.subheader("Search the Archive")
    keyword = st.text_input("Enter keyword to search:")
    if keyword:
        found = [s for s in st.session_state.archive if keyword.lower() in s['original'].lower()]
        if found:
            for s in found:
                st.info(f"Found: {s['original']}")
        else:
            st.error("No matching story found.")
