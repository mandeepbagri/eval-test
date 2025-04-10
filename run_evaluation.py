import os



def run_evaluation_pipeline(golden_dataset_path: str, api_response_path: str):
    """Runs evaluation pipeline and ouputs the accuracy for both brands and countries"""
    pass



if __name__ == "__main__":
    base_dir = os.path.dirname(__file__)
    run_evaluation_pipeline(
        golden_dataset_path=os.path.join(base_dir, "data", "golden_dataset.json"),
        api_response_path=os.path.join(base_dir, "data", "api_responses.json")
    )