import requests
from autogpt_server.data.block import Block, BlockSchema, BlockOutput

class ContinueIntegrationBlock(Block):
    # Define the input schema
    class Input(BlockSchema):
        task_request: str  # The request details

    # Define the output schema
    class Output(BlockSchema):
        task_response: str  # The response details

    def __init__(self):
        super().__init__(
            id="continue-integration-block",  # Unique ID for the block
            input_schema=ContinueIntegrationBlock.Input,  # Assign input schema
            output_schema=ContinueIntegrationBlock.Output,  # Assign output schema

            # Provide sample input and output for testing the block
            test_input={"task_request": "Test input"},
            test_output={"task_response": "Task is being processed"},
        )

    def run(self, input_data: Input) -> BlockOutput:
        try:
            # Simulate processing the task
            task_response = f"Processed task: {input_data.task_request}"
            yield "task_response", task_response
        except Exception as e:
            raise ValueError(f"Error processing task: {e}")