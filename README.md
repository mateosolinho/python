# Python Exercises

## Comparison of ANN and CNN Architectures for Image Classification

   [Exercise Link](projects/clasificador_perros_gatos)

1. **Integration of Python Libraries**
   - **tensorflow**: Imported `tensorflow` and `tensorflow_datasets` to handle the neural network and dataset operations.
   - **numpy**: Used `numpy` to manage image data and labels.
   - **matplotlib**: Utilized `matplotlib` for visualizing images and training progress.
   - **cv2**: Employed `cv2` for image resizing and color conversion.

2. **Declaring and Preprocessing Data**
   - Loaded the `cats_vs_dogs` dataset from TensorFlow Datasets.
   - Visualized a subset of the dataset to check the images and labels.
   - Preprocessed images by resizing to 100x100 pixels and converting to grayscale.
   - Structured data into arrays for training and labels.

3. **Constructing the Neuronal Network**
   - **Dense Model**:
     - Flattened input images.
     - Added two `Dense` layers with 150 units each and ReLU activation.
     - Added a final `Dense` layer with 1 unit and sigmoid activation for binary classification.
   - **Convolutional Neural Network (CNN) Model**:
     - Added convolutional layers (`Conv2D`) and max-pooling layers (`MaxPooling2D`).
     - Flattened the output and added dense layers with ReLU and sigmoid activation.
   - **Enhanced CNN Model with Dropout**:
     - Similar to the CNN model but included a `Dropout` layer for regularization.

4. **Compiling the Models**
   - Compiled all models using the `Adam` optimizer and `binary_crossentropy` loss function.
   - Set metrics to `accuracy`.

5. **Training the Models**
   - **Dense Model**: Trained with `100 epochs`, `batch_size=32`, and a validation split of `0.15`. Logged training progress using TensorBoard.
   - **CNN Model**: Trained with similar settings as the Dense model, but for a different model structure.
   - **Enhanced CNN Model**: Trained with `100 epochs`, `batch_size=32`, and a validation split of `0.15`.

6. **Visualizing Training and Data Argumentation**
   - Visualized the first few images of the dataset.
   - Applied data augmentation using `ImageDataGenerator` to enhance training data.
   - Visualized augmented images.

7. **Training with Augmented Data**
   - **Dense Model with Augmentation**: Trained using augmented data with `100 epochs` and validation data.
   - **CNN Model with Augmentation**: Trained for `150 epochs` with augmentation.
   - **Enhanced CNN Model with Augmentation**: Trained for `100 epochs` with augmentation.

8. **Saving the Model**
   - Saved the best-performing CNN model with augmentation to a file named `perros-gatos-cnn-ad.h5`.

## Image Classifier with Tensorflow

   [Exercise Link](projects/clasificador_imagenes)

1. **TensorFlow and TensorFlow Datasets**
   - Learned to leverage `tensorflow` and `tensorflow_datasets` for loading and managing large datasets, specifically the Fashion MNIST dataset consisting of over 60,000 images from Zalando. These images are preprocessed to be 28x28 pixels and grayscale, simplifying the normalization and modeling process.

2. **Data Normalization**
   - I practiced normalizing image data, converting pixel values from a range of 0-255 to a range of 0-1. This step is crucial for ensuring that the model trains efficiently and accurately.

3. **Data Visualization**
   - Using `matplotlib`, I visualized the dataset, both individual images and a grid of multiple images, which helped me understand the dataset better and verify the correctness of the data preprocessing steps.

4. **Building and Compiling a Sequential Model**
   - Built a sequential neural network model using `tf.keras.Sequential`. The model consisted of two dense hidden layers with 50 neurons each and ReLU activation, followed by an output layer with 10 neurons and a softmax activation function to handle the classification of the ten different categories.

5. **Compiling the Model**
   - Compiled the model using the Adam optimizer and Sparse Categorical Crossentropy loss function. I also included accuracy as a metric to track the model's performance during training.

6. **Batch Processing and Caching**
   - Implemented batch processing and caching to speed up training and evaluation. This involved shuffling and batching the training data and simply batching the test data.

7. **Training the Model**
   - Trained the model for five epochs and plotted the loss magnitude over epochs to visualize the training progress.

8. **Evaluating Model Predictions**
   - Evaluated the model's predictions on the test data. By plotting a grid of images along with their predicted and actual labels, I learned how to visually inspect the model's performance, highlighting correct predictions in blue and incorrect ones in red.

9. **Making Individual Predictions**
   - Tested the model's prediction capability on individual images from the test set and verified the predictions by printing the predicted class names.

## Neuronal Network in TensorFlow

   [Exercise Link](projects/red_neuronal)

1. **Integration of Python Libraries**

   - **tensorflow**: Imported `tensorflow` to construct and train the neural network.
   - **numpy**: Used `numpy` to handle input and output data.
   - **matplotlib**: Used the `matplotlib` library to create visualizations from the loss magnitude.

2. **Declaring Training Data**

   - Declared arrays of temperature data in Celsius and Fahrenheit to train the model.

3. **Constructing the Neural Network**

   - Experimented with building a simple neural network with a `single neuron` and a `single connection`.
   - Constructed a more complex neural network with `two hidden layers` and one `output layer`.

4. **Compiling the Model**

   - Compiled the model, specifying the `Adam` optimizer with a learning rate of 0.1 and the `mean_squared_error` loss function.

5. **Training the Model**

   - Trained the model with `1000 epochs` and set verbose to False to avoid console outputs.

6. **Visualizing the Training Process**

   - Used `matplotlib` to visualize the loss magnitude over the number of epochs, observing how the network stops learning after a certain number of epochs

7. **Making Predictions**

   - Made a prediction with the trained model to verify its accuracy with previously unseen data.

8. **Exploring Weights and Biases**

   - Inspected the weights and biases of each neuron in the model to understand how the network optimized its connections.

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
