import subprocess
import sys

def run_notebook(notebook_path):
    """Execute a Jupyter notebook"""
    cmd = [
        sys.executable, '-m', 'jupyter', 'nbconvert',
        '--to', 'notebook', '--execute', notebook_path
    ]
    result = subprocess.run(cmd, capture_output=True, text=True)
    return result.returncode == 0

def main():
    pipeline_stages = [
        'notebooks/01_data_undestanding/data_understanding.ipynb',
        'notebooks/02_data_cleaning/billings_cleaning.ipynb',
        'notebooks/03_data_merging/aggregation_merging.ipynb',
        'notebooks/04_eda_visualization/billings_eda.ipynb',
        'notebooks/05_feature_engineering/feature_engineering.ipynb',
        'notebooks/06_hypothesis_testing/hypothesis_testing.ipynb',
        'notebooks/07_model_building_evaluation/model_build_eval.ipynb',
        'notebooks/08_model_interpretation/explainability.ipynb',
    ]
    
    for i, notebook in enumerate(pipeline_stages, 1):
        print(f"\n[{i}/{len(pipeline_stages)}] Running {notebook}...")
        if not run_notebook(notebook):
            print(f"ERROR: Failed at {notebook}")
            sys.exit(1)
    
    print("\nPipeline completed successfully!")

if __name__ == "__main__":
    main()