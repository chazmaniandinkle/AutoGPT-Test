import os
import sys
from autogpt_server.blocks.continue_integration import ContinueIntegrationBlock

# Adjust the Python path
module_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.insert(0, module_path)

def test_continue_integration_block():
    block = ContinueIntegrationBlock()
    input_data = ContinueIntegrationBlock.Input(task_request="Test input")
    output = list(block.run(input_data))
    assert output[0][1] == "Processed task: Test input"

if __name__ == "__main__":
    test_continue_integration_block()
    print("Test passed successfully.")