# GenLayer AI Task Review

A beginner-friendly custom GenLayer intelligent contract built in GenLayer Studio.

## Features

- Deployable on GenLayer Studio
- Create tasks with a brief
- Submit work for a task
- Review submissions with simple AI-like logic
- Returns final status and feedback

## Contract File

- `ai_task_review.py`

## Workflow

1. Create a task with a short brief
2. Submit work linked to that task
3. Trigger the review process
4. Check the final result using `get_task`

## Example

### Create Task
Brief:
`Write a short explanation about how GenLayer uses AI and blockchain`

### Submit Work
Submission:
`GenLayer uses AI and blockchain to enable intelligent contracts and validator consensus.`

### Final Result
- Status = APPROVED
- Feedback = Submission matches the task context well

## Methods

### Write Methods
- `create_task(brief: str)`
- `submit_work(task_id: u256, submission: str)`
- `review_task(task_id: u256)`

### Read Method
- `get_task(task_id: u256) -> str`

## Purpose

This is my fourth custom GenLayer builder project.  
It simulates an AI-powered task review workflow using GenLayer intelligent contracts.
