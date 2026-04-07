rchive = []

def translate_to_english(text):
    return "[Translated to English]: " + text


def add_story():
    original = input("Enter your story (Arabic or English):\n")
    values = input("Enter UAE family values (comma separated):\n")

    translated = translate_to_english(original)

    story = {
        "original": original,
        "translated": translated,
        "values": values
    }

    archive.append(story)
    print("\nStory saved successfully!\n")


def display_stories():
    if not archive:
        print("No stories found.\n")
        return

    for i, s in enumerate(archive, 1):
        print(f"\n--- Story {i} ---")
        print("Original:", s["original"])
        print("Translated:", s["translated"])
        print("Values:", s["values"])


def search_story():
    keyword = input("Enter keyword to search: ")

    found = False
    for s in archive:
        if keyword in s["original"]:
            print("\nFound:")
            print(s["original"])
            print(s["translated"])
            found = True

    if not found:
        print("No matching story found.")

def main():
    while True:
        print("\n--- Family Heritage Archive ---")
        print("1. Add Story")
        print("2. View Stories")
        print("3. Search Story")
        print("4. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_story()
        elif choice == "2":
            display_stories()
        elif choice == "3":
            search_story()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice")


main()
