# Python Exercises

*A few basic exercises in Python to practice the language, trying to understand and increase the level with each exercise*

## Youtube Downloader 

   [Exercise Link](projects/youtube_downloader.py)

1. **Integration of Python Libraries**
   - **pytube**: Utilized the `pytube` library to fetch video metadata and download YouTube videos.
   - **tkinter**: Implemented basic GUI with `tkinter` and handled file dialogs to select download paths.

2. **Error Handling**
   - Implemented error handling using `try-except-finally` blocks to manage exceptions during YouTube video fetching and processing.

3. **User Interaction**
   - Used `input()` to receive the YouTube video URL and confirm the selection of the download path.
   - Implemented `tkinter` for directory selection through a graphical interface.

4. **Data Manipulation**
   - Calculated and formatted video duration using `timedelta` from the `datetime` module.
   - Accessed video metadata such as title, author, channel URL, publish date, and duration using `pytube`.

5. **Conditional Statements**
   - Utilized conditional statements to handle confirmation of download path selection (`match-case` in Python 3.10).

6. **File Management**
   - Managed file paths using `filedialog` from `tkinter` to select download paths and defaulted to the user's downloads directory (`user_downloads_dir()`).

7. **Output Formatting**
   - Employed formatted output (`f-strings`) to clearly display video metadata and the download path to the user.

## Password Generator

[Exercise Link](projects/password_generator.py)

1. **User Interaction**
   - **Input Handling**: Utilized `input()` for receiving and processing user inputs like password length and complexity.
   - **Error Management**: Implemented `try-except` for validating user inputs and handling errors gracefully.

2. **Random Password Generation**
   - **Library Usage**: Leveraged Python standard libraries such as `random` and `string` for generating random passwords.
   - **Character Selection**: Randomly selected characters from predefined sets (`string.ascii_letters`, `string.digits`, `string.punctuation`) based on user-specified complexity.
   - **List and String Operations**: Utilized lists to construct random passwords and converted them back to strings.

3. **Functional Programming**
   - **Function Definition**: Organized code into reusable functions (`password_structure`, `random_generator`, `length_check`, `main`) for clear and modular program flow.
   - **Main Function**: Orchestrated program execution through a main function, managing logic and function calls.

4. **Enhanced User Experience**
   - **Interactive Menu**: Designed an interactive menu guiding users through password generation, with clear options and error handling.

5. **Best Programming Practices**
   - **Modularity and Clarity**: Maintained clear function definitions and logical segments, adhering to design principles that improve code comprehension and maintainability.

## Agenda Contactos

[Exercise Link](projects/agenda_contactos)

1. **Object-Oriented Programming (OOP)**

   - **Classes and Objects**: I defined classes like `Contacto`, `Agenda` y `Menu`, encapsulating related data and behaviors.
   - **Object Instantiation**: Instances of these classes were created to represent and manipulate contacts and manage agenda logic.
   - **Encapsulation**: Attributes (`nombre`, `telefono`, `email`) and methods (`agregar_contacto`, `mostrar_contactos`, `buscar_contacto`, `eliminar_contacto`) were defined to work with this data.

2. **Collection Management**

   - **Lists**: Used lists (`self.contactos`) to store multiple contact objects, with methods for adding, deleting, and searching items.
   - **Comprehensions**: Employed list comprehensions for searching and filtering contacts.

3. **Flow Control**

   - **Loops and Conditionals**: Implemented a `while` loop in the `ejecutar` method to maintain the interactive menu until the user chooses to exit.
   - **Conditionals `if-else` and `match-case`**: Used conditional statements and Python 3.10's match-case pattern to manage different menu options.

4. **User Interaction**

   - **Input and Output**: Utilized `input()` to receive user data such as menu choices and contact details.
   - **User Output**: Used `print()` to display information and messages, enhancing user interaction.

5. **String Handling**

   - **Manipulation**: Employed f-strings (`f"Text {variable}"`) for dynamic and readable output messages.
   - **Comparison**: Compared contact names while ignoring case (`name.lower()`) to facilitate flexible searching.

6. **Modularity and Good Design Practices**

   - **Separation of Concerns**: Segregated program logic into distinct classes (`Contacto`, `Agenda`, `Menu`), adhering to the single responsibility principle for improved code clarity and maintainability.
   - **Error Handling**: Implemented checks to manage scenarios where contacts were not found or the contact list was empty, ensuring appropriate user feedback.
