EduOrganize CLI
🎓 Streamline Student Records Effortlessly
A lightweight, interactive command-line interface (CLI) application designed to easily manage student information, tracking grades, age, dates of birth, and unique academic subjects in real-time.

✨ Key Features
🗂️ Full CRUD Management: Effortlessly add, view, update, and delete student profiles directly from your terminal.

📚 Dynamic Subject Tracking: Automatically aggregates a unique master list of all subjects offered across all student profiles.

🛠️ Robust Data Modeling: Uses a structured combination of dictionaries, lists, sets, and tuples to maintain data integrity and prevent duplicate records.

💻 Interactive Menu Loop: A clean, user-friendly match-case control workflow makes navigation smooth and intuitive.

🛠️ Tech Stack
Language: Python 3.10+

Data Structures: Lists, Dictionaries, Sets, and Tuples

🚀 Getting Started
Prerequisites
Ensure you have Python 3.10 or higher installed on your local machine (required for structural pattern matching match-case syntax). You can check your version by running:

Bash
python --version
Installation
Clone this repository to your local machine:

Bash
git clone https://github.com/yourusername/eduorganize-cli.git
Navigate into the project directory:

Bash
cd eduorganize-cli
💻 Usage
To launch the interactive data organizer, execute the script directly using Python:

Bash
python main.py
Example Terminal Interaction:
Plaintext
==================================================
Welcome to the student data organizer!
==================================================
Select an option: 
1.Add student
2.Display All students
3.update student information
4.Delete student
5.Display subjects offered
6.Exit
Enter your choice: 1

Enter student details: 
Enter student ID: 101
Enter Name: Alex Mercer
Enter age: 20
Enter Grade: A
Enter your date of birth: 2006-05-14
Enter three subjects
subject1: Mathematics
subject2: Computer Science
subject3: Physics
Student added successfully!
🗺️ Roadmap
[ ] Add data persistence by saving and loading student records from a students.json file.

[ ] Implement search and filter functionalities (e.g., search student by name or filter by grade).

[ ] Add structural validation for dates of birth (YYYY-MM-DD) and input fields.

[ ] Generate clean CSV export reports for student summaries.

🤝 Contributing
Contributions make the open-source community an amazing place to learn, inspire, and create. Any contributions you make are greatly appreciated.

Feel free to fork the repository, open an issue to discuss design ideas, or submit a Pull Request with your feature enhancements!

📄 License
Distributed under the MIT License. See LICENSE for more information.
