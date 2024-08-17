class TaskPlanner:
    def plan(self, state: str) -> Dict:
        prompt = f"Current state: {state}\nWhat should be the next action? Provide a structured response with 'action' and 'reason' keys."
        response = query_llm(prompt)
        return eval(response)  # 将字符串转换为字典

    def update(self, result: str) -> Dict:
        prompt = f"Action result: {result}\nIs the task complete? If not, what should be the next action? Provide a structured response with 'is_complete', 'action', and 'reason' keys."
        response = query_llm(prompt)
        return eval(response)