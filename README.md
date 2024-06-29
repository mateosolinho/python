# Python Exercises

A few basic exercises in Python to practice the language, trying to understand and increase the level with each exercise

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

## ChatBot

[Exercise Link](projects/chatbot)

1. **Integration of Python Libraries**

   - **NLTK**: Integrated `nltk` for natural language processing tasks including tokenization and lemmatization.
   - **sklearn**: Utilized `sklearn` for TF-IDF vectorization and SVM model training.

2. **Natural Language Processing Techniques**

   - **Tokenization and Lemmatization**: Implemented to tokenize user input and reduce words to their base forms for effective analysis.

3. **TF-IDF Vectorization**

   - **TF-IDF (Term Frequency-Inverse Document Frequency)**: Applied `TF-IDF` to convert textual data into numerical vectors, enhancing machine learning model compatibility.

4. **Machine Learning with SVM**

   - **SVM (Support Vector Machine)**: Employed `SVM` with a linear kernel for intent classification based on TF-IDF features.
   - **Model Training**: Trained SVM classifier to predict user intent from input phrases.

5. **Functional Chatbot Development**

   - **Intent Classification**: Classified user intents using the SVM model and TF-IDF vectors.
   - **Dynamic Responses**: Generated responses based on predicted intents mapped to predefined responses stored in a structured JSON file.

6. **User-Chatbot Interaction**

   - **Console Interface**: Implemented a console-based interface for seamless interaction with the chatbot.
   - **Input Handling**: Managed user inputs, processed through intent classification, and displayed corresponding chatbot responses.

7. **JSON for Intent Definitions**

   - **Intent Definition**: Structured user input patterns and responses using a JSON format for clear intent mapping and response retrieval.

## CSV Reader

[Exercise Link](projects/csv_reader.py)

1. **Integration of Python Libraries**

   - **pandas**: Utilized the `pandas` library to efficiently read and manipulate CSV files.
   - **tkinter**: Implemented a basic GUI with `tkinter` for file selection dialogs.
   - **matplotlib**: Used the `matplotlib` library to create visualizations from the CSV data.

2. **Natural Language Processing Techniques**

   - Implemented error handling to manage exceptions that may occur during CSV file reading and data processing.

3. **User Interaction**

   - Employed `input()` to receive user commands for various operations on the CSV data.
   - Used `tkinter` to provide a graphical interface for selecting CSV files.

4. **Data Manipulation**

   - Utilized `pandas` for data manipulation tasks such as calculating basic statistics, filtering, sorting, and counting unique values.
   - Used `matplotlib` to create column plots and display them

5. **Conditional Statements**

   - Utilized conditional statements and loops to navigate the menu options and perform corresponding actions based on user input.

6. **File Management**

   - Managed file paths using `tkinter`'s `filedialog` to select CSV files and handle file operations effectively.
