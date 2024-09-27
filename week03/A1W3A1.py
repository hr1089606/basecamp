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
        self.enter_feedback: bool | str = False


    def is_valid_yes_or_no(self, user_input: str, attr: str) -> None:
        """
        Checks if the user input is a valid Yes/No and updates the valid_input dictionary if valid.
        :param user_input:
        :param attr:
        :return: None
        """
        if user_input.isalpha() and user_input.lower() in ["yes", "no"]:
            setattr(self, attr, user_input.lower())


    def is_offer_or_rejection(self, user_input: str, attr: str) -> None:
        """
        Checks if the user input is a valid answer: 'Job Offer' or 'rejection' and updates the
        valid_input dictionary if valid.
        :param user_input:
        :param attr:
        :return: None
        """
        if user_input.isalpha and (user_input.lower() == "job offer" or user_input.lower() == "rejection"):
            setattr(self, attr, user_input.lower())


    def is_name_valid(self, user_input: str, attr: str) -> bool:
        """
        Checks if the user input is a valid name, returns a boolean and updates the
        valid_input dictionary if valid.
        :param user_input:
        :param attr:
        :return: bool
        """
        is_valid_name_input = all(char.isalpha() or char.isspace() for char in user_input)
        name_len = len(user_input)
        if is_valid_name_input and 2 <= name_len <= 10:
            setattr(self, attr, user_input.lower().strip())
            return True
        return False


    def is_title_valid(self, user_input: str, attr: str) -> bool:
        """
        Checks if the user input is a valid job title, returns a boolean and updates the
        valid_input dictionary if valid.
        :param user_input:
        :param attr:
        :return: bool
        """
        is_valid_title_input = all(char.isalpha() or char.isspace() for char in user_input)
        if is_valid_title_input:
            setattr(self, attr, user_input.lower().strip())
            return True
        return False


    def is_salary_valid(self, user_input: str, attr: str) -> bool:
        """
        Checks if the user input is a salary amount, returns a boolean and updates the
        valid_input dictionary if valid.
        :param user_input:
        :param attr:
        :return: bool
        """
        valid_punctuation = [".", ","]
        for char in user_input:
            if char.isalpha():
                return False
            elif not char.isalnum() and char not in valid_punctuation:
                return False
            else:
                setattr(self, attr, user_input.lower())
                return True


    def is_date_valid(self, user_input: str, attr: str) -> bool:
        """
        Checks if the user input is a valid date, returns a boolean and updates the
        valid_input dictionary if valid.
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
        Checks if the user input is a valid feedback length larger than two, returns a boolean and updates the
        valid_input dictionary if valid.
        :param user_input:
        :param attr:
        :return: bool
        """
        if len(user_input) < 2:
            return False
        setattr(self, attr, user_input.lower())
        return True


    def common_questions(self) -> None:
        """
        Runs the common questions sequence.
        :return: None
        """
        while not self.more_letters:
            more_letters = input("More Letters? (Yes or No) ")
            is_valid_input(more_letters, "more_letters")

        if self.more_letters.lower() == "no":
            return

        while not self.offer_or_rejection:
            offer_or_rejection = input("Job Offer or Rejection? ")
            is_valid_input(offer_or_rejection, "offer_or_rejection")

        while not self.first_name:
            first_name = input("First Name? ")
            is_valid_input(first_name, "first_name")

        while not self.last_name:
            last_name = input("Last Name? ")
            is_valid_input(last_name, "last_name")
            
        while not self.job_title:
            job_title = input("Job Title? ")
            is_valid_input(job_title, "job_title")


    def job_offer_questions(self) -> None:
        """
        Runs the Job Offer questions sequence.
        :return: None
        """
        while not self.annual_salary:
            annual_salary = input("Annual Salary? ")
            is_valid_input(annual_salary, "annual_salary")

        while not self.start_date:
            start_date = input("Start Date?(YYYY-MM-DD) ")
            is_valid_input(start_date, "start_date")


    def rejection_questions(self) -> None:
        """
        Runs the rejection questions sequence.
        :return: None
        """
        while not self.feedback:
            feedback = input("Feedback? (Yes or No) ")
            is_valid_input(feedback, "feedback")

        if self.feedback.lower() == 'yes':
            enter_feedback = input("Enter your Feedback (One Statement): ")
            is_valid_input(enter_feedback, "enter_feedback")


validate = Validate()


def is_valid_input(user_input, key):
    if key == "more_letters" or key == "feedback":
        validate.is_valid_yes_or_no(user_input, key)
    elif key == "offer_or_rejection":
        validate.is_offer_or_rejection(user_input, key)
    elif key == "first_name" or key == "last_name":
        validate.is_name_valid(user_input, key)
    elif key == "job_title":
        validate.is_title_valid(user_input, key)
    elif key == "annual_salary":
        validate.is_salary_valid(user_input, key)
    elif key == "start_date":
        validate.is_date_valid(user_input, key)
    elif key == "enter_feedback":
        validate.is_feedback_valid(user_input, key)


def start_predefined_templates():
    validate.common_questions()

    if validate.offer_or_rejection == "job offer":
        validate.job_offer_questions()
        print('JOB OFFER LETTER HERE')
    elif validate.offer_or_rejection == "rejection":
        validate.rejection_questions()
        print('Rejection LETTER HERE')


start_predefined_templates()