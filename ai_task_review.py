from genlayer import *

@g1.contract
class AITaskReview:
    def __init__(self):
        self.task_count = 0
        self.briefs = {}
        self.submissions = {}
        self.statuses = {}
        self.feedbacks = {}

    @g1.public.write
    def create_task(self, brief: str):
        self.task_count += 1
        key = str(self.task_count)
        self.briefs[key] = brief
        self.submissions[key] = ""
        self.statuses[key] = "OPEN"
        self.feedbacks[key] = "Waiting for submission"

    @g1.public.write
    def submit_work(self, task_id: u256, submission: str):
        key = str(task_id)
        self.submissions[key] = submission
        self.statuses[key] = "SUBMITTED"
        self.feedbacks[key] = "Submission received"

    @g1.public.write
    def review_task(self, task_id: u256):
        key = str(task_id)

        brief = self.briefs.get(key, "")
        submission = self.submissions.get(key, "")

        if submission.strip() == "":
            self.statuses[key] = "OPEN"
            self.feedbacks[key] = "No submission yet"
            return

        text = submission.lower()

        if "genlayer" in text and ("ai" in text or "blockchain" in text):
            self.statuses[key] = "APPROVED"
            self.feedbacks[key] = "Submission matches the task context well"
        elif len(submission.strip()) < 15:
            self.statuses[key] = "REVISION"
            self.feedbacks[key] = "Submission is too short, please add more detail"
        else:
            self.statuses[key] = "REJECTED"
            self.feedbacks[key] = "Submission does not clearly match the expected context"

    @g1.public.view
    def get_task(self, task_id: u256) -> str:
        key = str(task_id)
        brief = self.briefs.get(key, "")
        submission = self.submissions.get(key, "")
        status = self.statuses.get(key, "UNKNOWN")
        feedback = self.feedbacks.get(key, "No feedback")

        return f"Task ID: {key} | Brief: {brief} | Submission: {submission} | Status: {status} | Feedback: {feedback}"
