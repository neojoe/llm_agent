from executor import ActionExecutor
from planner import TaskPlanner
from module import WebInteractionModule
from data_process import DataExtractor
from data_process import DataStorage


class AgentController:
    def __init__(self, api_key: str):
        openai.api_key = api_key
        self.task_planner = TaskPlanner()
        self.action_executor = ActionExecutor()
        self.web_interaction = WebInteractionModule()
        self.data_extractor = DataExtractor()
        self.data_storage = DataStorage()

    def run(self, initial_prompt: str):
        task = self.task_planner.plan(initial_prompt)
        while not task.is_complete():
            action = self.action_executor.execute(task.next_action())
            if action.requires_web_interaction():
                web_data = self.web_interaction.interact(action)
                extracted_data = self.data_extractor.extract(web_data)
                self.data_storage.store(extracted_data)
            task = self.task_planner.update(action.result())
        print("All orders have been successfully fetched. Terminating process.")


controller = AgentController("openai-api-key")
controller.run("Fetch all order details from Amazon for the user")
