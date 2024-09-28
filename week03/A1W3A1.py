class Validate:
    def __init__(self):
        self.more_letters: bool | str = False
        self.offer_or_rejection: bool | str = False
        self.first_name: bool | str = False
        self.last_name: bool | str = False
        self.job_title: bool | str = False
        self.annual_salary: bool | str = False
        self.start_date: bool | str = False
        self.feedback: bool | str = False
        self.feedback_message: bool | str = False


    # Validation controller, picks a validation method which corresponds with given key argument.
    def is_valid_input(self, user_input: str, key: str) -> None:
        """
        Controller which checks the given key, which also corresponds with any of the instance attributes above,
        and then calls any of the validation method below for further validation.
        After successful validation, the corresponding attribute is update with the user_input value.
        :param user_input:
        :param key:
        :return: None
        """
        if key == "more_letters" or key == "feedback":
            self.is_valid_yes_or_no(user_input, key)
        elif key == "offer_or_rejection":
            self.is_offer_or_rejection(user_input, key)
        elif key == "first_name" or key == "last_name":
            self.is_name_valid(user_input, key)
        elif key == "job_title":
            self.is_title_valid(user_input, key)
        elif key == "annual_salary":
            self.is_salary_valid(user_input, key)
        elif key == "start_date":
            self.is_date_valid(user_input, key)
        elif key == "feedback_message":
            self.is_feedback_valid(user_input, key)


    # Validation methods (yes/no, offer/rejection, name, title, salary, date, feedback)
    def is_valid_yes_or_no(self, user_input: str, attr: str) -> None:
        """
        Checks if the user input is a valid Yes/No.
        :param user_input:
        :param attr:
        :return: None
        """
        if user_input.isalpha() and user_input.lower() in ["yes", "no"]:
            setattr(self, attr, user_input.lower())


    def is_offer_or_rejection(self, user_input: str, attr: str) -> None:
        """
        Checks if the user input is a valid answer: "Job Offer" or "rejection".
        :param user_input:
        :param attr:
        :return: None
        """
        if user_input.isalpha and user_input.lower() in ["job offer", "rejection"]:
            setattr(self, attr, user_input.lower())


    def is_name_valid(self, user_input: str, attr: str) -> bool:
        """
        Checks if the user input is a valid name, returns a boolean.
        :param user_input:
        :param attr:
        :return: bool
        """
        is_valid_name_input = all(char.isalpha() or char.isspace() for char in user_input)
        name_len = len(user_input)
        if is_valid_name_input and 2 <= name_len <= 10:
            setattr(self, attr, user_input.strip().title())
            return True
        return False


    def is_title_valid(self, user_input: str, attr: str) -> bool:
        """
        Checks if the user input is a valid job title, returns a boolean.
        :param user_input:
        :param attr:
        :return: bool
        """
        is_valid_title_input = all(char.isalpha() or char.isspace() for char in user_input)
        if is_valid_title_input:
            setattr(self, attr, user_input.strip().title())
            return True
        return False


    def is_salary_valid(self, user_input: str, attr: str) -> bool:
        """
        Checks if the user input is a salary amount, returns a boolean.
        :param user_input:
        :param attr:
        :return: bool
        """
        for char in user_input:
            if char.isalpha():
                return False
            elif not char.isalnum() and char not in [".", ","]:
                return False
            else:
                setattr(self, attr, user_input.lower())
                return True


    def is_date_valid(self, user_input: str, attr: str) -> bool:
        """
        Checks if the user input is a valid date, returns a boolean.
        :param user_input:
        :param attr:
        :return: bool
        """
        for idx, char in enumerate(user_input):
            if char.isalpha():
                return False
            if idx == 4 or idx == 7:
                if char != "-":
                    return False

        setattr(self, attr, user_input.lower())
        return True


    def is_feedback_valid(self, user_input: str, attr: str) -> bool:
        """
        Checks if the user input is a valid feedback length larger than two, and returns a boolean.
        :param user_input:
        :param attr:
        :return: bool
        """
        if len(user_input) < 2:
            return False
        setattr(self, attr, user_input.lower())
        return True


    # Questions (common, job offer, rejection)
    def common_questions(self) -> None:
        """
        Runs the common questions sequence.
        :return: None
        """
        while not self.more_letters:
            more_letters = input("More Letters? (Yes or No) ")
            self.is_valid_input(more_letters, "more_letters")

        if self.more_letters.lower() == "no":
            return

        while not self.offer_or_rejection:
            offer_or_rejection = input("Job Offer or Rejection? ")
            self.is_valid_input(offer_or_rejection, "offer_or_rejection")

        while not self.first_name:
            first_name = input("First Name? ")
            self.is_valid_input(first_name, "first_name")

        while not self.last_name:
            last_name = input("Last Name? ")
            self.is_valid_input(last_name, "last_name")
            
        while not self.job_title:
            job_title = input("Job Title? ")
            self.is_valid_input(job_title, "job_title")


    def job_offer_questions(self) -> None:
        """
        Runs the Job Offer questions sequence.
        :return: None
        """
        while not self.annual_salary:
            annual_salary = input("Annual Salary? ")
            self.is_valid_input(annual_salary, "annual_salary")

        while not self.start_date:
            start_date = input("Start Date?(YYYY-MM-DD) ")
            self.is_valid_input(start_date, "start_date")


    def rejection_questions(self) -> None:
        """
        Runs the rejection questions sequence.
        :return: None
        """
        while not self.feedback:
            feedback = input("Feedback? (Yes or No) ")
            self.is_valid_input(feedback, "feedback")

        if self.feedback.lower() == "yes":
            feedback_message = input("Enter your Feedback (One Statement): ")
            self.is_valid_input(feedback_message, "feedback_message")


    # Letters (job offer, rejection)
    @staticmethod
    def job_offer_letter(*args: bool | str) -> str:
        """
        Returns the job offer letter.
        :param args:
        :return: str
        """
        first_name, last_name, job_title, annual_salary, start_date = args
        job_offer_letter = f"""
        Dear {first_name} {last_name}, 
        
        After careful evaluation of your application for the position of {job_title}, 
        we are glad to offer you the job. Your salary will be {annual_salary} euro annually. 
        
        Your start date will be on {start_date}. Please do not hesitate to contact us with any questions. 
        
        Sincerely,
        HR Department of XYZ
        """
        return job_offer_letter


    @staticmethod
    def rejection_letter(*args: bool | str) -> str:
        """
        Returns the rejection letter.
        :param args:
        :return: str
        """
        first_name, last_name, job_title, feedback, feedback_message = args
        show_feedback = f"""
        Here we would like to provide you our feedback about the interview. {feedback_message}
        """ if feedback else ""

        rejection_letter = f"""
        Dear {first_name} {last_name}, 
        
        After careful evaluation of your application for the position of {job_title}, at this moment we have decided to proceed with another candidate. 
        
        {show_feedback}
        
        We wish you the best in finding your future desired career. Please do not hesitate to contact us with any questions. 
        
        Sincerely, 
        HR Department of XYZ        
        """

        return rejection_letter


    # Start program: Predefined templates
    def start_predefined_templates(self) -> None:
        """Starts the program and runs the questions sequence"""
        self.common_questions()

        if self.offer_or_rejection == "job offer":
            self.job_offer_questions()
            print(self.job_offer_letter(self.first_name, self.last_name, self.job_title,
                                        self.annual_salary, self.start_date))
        elif self.offer_or_rejection == "rejection":
            self.rejection_questions()
            print(self.rejection_letter(self.first_name, self.last_name, self.job_title,
                                        self.feedback, self.feedback_message))


validate = Validate()
validate.start_predefined_templates()
