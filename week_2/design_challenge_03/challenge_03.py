
'''
Design Challenge 3: Online Exam 
There is an online exam to be portal, where a list of question is to be created. Every question belongs 
to a category and a topic. The question can be of any type such as multiple choice question, 
paragraph question, etc. 
Design the OO model for the above problem statement and implement the code to 
• Find out the total number of question 
• List all question belonging to a topic 
• List all question belonging to a topic and category
'''


class Question:
    def __init__(self, question_id, text, category, topic, question_type):
        self.question_id = question_id
        self.text = text
        self.category = category
        self.topic = topic
        self.question_type = question_type
        
    def display(self):
        print(f"[{self.question_type}] {self.text}")
        print(f"Category: {self.category}, Topic: {self.topic}")
        
        
class MCQQuestion(Question):
    def __init__(self, question_id, text, category, topic, options, correct_option):
        super().__init__(question_id, text, category, topic, "MCQ")
        self.options = options
        self.correct_option = correct_option
        
    def display(self):
        super().display()
        for idx, option in enumerate(self.options, start=1):
            print(f"{idx}. {option}")
            
            
class ParagraphQuestion(Question):
    def __init__(self, question_id, text, category, topic,word_limit):
        super().__init__(question_id, text, category, topic, "Paragraph")
        self.word_limit = word_limit
        
    def display(self):
        super().display()
        print(f"Word Limit: {self.word_limit}")
        
        
class ExamPortal:
    def __init__(self):
        self.questions = []
        
    def add_question(self, question):
        self.questions.append(question)
     
    # 1. Find total number of questions 
    def get_total_questions(self):
        return len(self.questions)
    
    # 2. List all questions belonging to a topic
    def get_questions_by_topic(self, topic):
        return [q for q in self.questions if q.topic.lower() == topic.lower()]
    
    # 3. List all questions belonging to a topic and category
    def get_questions_by_topic_and_category(self, topic, category):
        return [q for q in self.questions if q.topic.lower() == topic.lower() and q.category.lower() == category.lower()]
    
    
    
if __name__ == "__main__":
    portal = ExamPortal()
    
    # Add MCQ Questions
    
    q1 = MCQQuestion(
        1,
        "What is Python?",
        "Programming",
        "Python",
        ["Language", "Snake", "Tool", "OS"],
        "Language"
    )
    
    q2 = MCQQuestion(
        2,
        "What is inheritance?",
        "Programming",
        "OOP",
        ["Concept", "Error", "Library", "Syntax"],
        "Concept"
    )

    # Add Paragraph question
    q3 = ParagraphQuestion(
        3,
        "Explain OOP principles.",
        "Programming",
        "OOP",
        200
    )
    
    # Add questions to portal
    portal.add_question(q1)
    portal.add_question(q2)
    portal.add_question(q3)
    
    
    # 1. Total number of questions
    print("Total Questions:", portal.get_total_questions())
    
    # 2. Questions by topic
    print("\nQuestions on topic 'OOP':")
    for q in portal.get_questions_by_topic("OOP"):
        q.display()
        print()

    # 3. Questions by topic and category
    print("Questions on topic 'OOP' and category 'Programming':")
    for q in portal.get_questions_by_topic_and_category("OOP", "Programming"):
        q.display()
        print()