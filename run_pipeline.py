import subprocess
import sys
import os
from datetime import datetime

def install_requirements():
    """Install dependencies from requirements.txt"""
    print("\n" + "=" * 70)
    print("INSTALLING REQUIREMENTS")
    print("=" * 70)
    
    if not os.path.exists('requirements.txt'):
        print("ERROR: requirements.txt not found")
        return False
    
    print("Running: pip install -r requirements.txt")
    cmd = [sys.executable, '-m', 'pip', 'install', '-r', 'requirements.txt']
    
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=600)
        if result.returncode == 0:
            print("SUCCESS: All requirements installed")
            print("=" * 70 + "\n")
            return True
        else:
            print("ERROR: Failed to install requirements")
            print(result.stderr)
            return False
    except Exception as e:
        print(f"EXCEPTION: {str(e)}")
        return False

def run_notebook(notebook_path, stage_num, total_stages):
    """Execute a Jupyter notebook with detailed error reporting"""
    
    # Check if notebook exists
    if not os.path.exists(notebook_path):
        print(f"ERROR: Notebook not found: {notebook_path}")
        return False, f"Notebook does not exist"
    
    print(f"[{stage_num}/{total_stages}] Running {notebook_path}...")
    print(f"    Starting execution...")
    
    cmd = [
        sys.executable, '-m', 'jupyter', 'nbconvert',
        '--to', 'notebook', '--execute', notebook_path
    ]
    
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=1800)
        
        if result.returncode == 0:
            print(f"    SUCCESS: {notebook_path}")
            return True, "Success"
        else:
            print(f"    FAILED: {notebook_path}")
            print(f"\n    ERROR OUTPUT:")
            print("    " + "-" * 70)
            if result.stderr:
                print("    STDERR:")
                for line in result.stderr.split('\n')[-20:]:  # Last 20 lines
                    if line.strip():
                        print(f"    {line}")
            if result.stdout:
                print("    STDOUT:")
                for line in result.stdout.split('\n')[-20:]:  # Last 20 lines
                    if line.strip():
                        print(f"    {line}")
            print("    " + "-" * 70)
            return False, result.stderr or result.stdout or "Unknown error"
            
    except subprocess.TimeoutExpired:
        print(f"    TIMEOUT: Notebook execution exceeded 30 minutes")
        return False, "Execution timeout (30 min exceeded)"
    except Exception as e:
        print(f"    EXCEPTION: {str(e)}")
        return False, str(e)

def main():
    # Install requirements first
    if not install_requirements():
        print("ERROR: Cannot proceed without installing requirements")
        sys.exit(1)
    
    pipeline_stages = [
        'notebooks/01_data_undestanding/data_understanding.ipynb',
        'notebooks/02_data_cleaning/billings_cleaning.ipynb',
        'notebooks/02_data_cleaning/cc_calls_cleaning.ipynb',
        'notebooks/02_data_cleaning/emails_cleaning.ipynb',
        'notebooks/02_data_cleaning/renewal_calls_cleaning.ipynb',
        'notebooks/03_data_merging/aggregation_merging.ipynb',
        'notebooks/04_eda_visualization/billings_eda.ipynb',
        'notebooks/04_eda_visualization/cc_calls_eda.ipynb',
        'notebooks/04_eda_visualization/emails_eda.ipynb',
        'notebooks/04_eda_visualization/renewal_calls_eda.ipynb',
        'notebooks/05_feature_engineering/feature_engineering.ipynb',
        'notebooks/06_hypothesis_testing/hypothesis_testing.ipynb',
        'notebooks/07_model_building_evaluation/model_build_eval.ipynb',
        'notebooks/08_model_interpretation/explainability.ipynb',
    ]
    
    print("\n" + "=" * 70)
    print("CHURN ANALYSIS PIPELINE ORCHESTRATOR")
    print("=" * 70)
    print(f"Total stages: {len(pipeline_stages)}")
    print(f"Started: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 70)
    
    completed = 0
    failed_stage = None
    failed_error = None
    
    for i, notebook in enumerate(pipeline_stages, 1):
        success, error_msg = run_notebook(notebook, i, len(pipeline_stages))
        
        if success:
            completed += 1
        else:
            failed_stage = notebook
            failed_error = error_msg
            print(f"\n{'=' * 70}")
            print(f"PIPELINE FAILED AT STAGE {i}/{len(pipeline_stages)}")
            print(f"{'=' * 70}")
            print(f"Failed notebook: {notebook}")
            print(f"Error: {error_msg}")
            print(f"{'=' * 70}\n")
            print("NEXT STEPS:")
            print(f"1. Open the notebook manually:")
            print(f"   jupyter notebook {notebook}")
            print(f"2. Run cells one by one to find the error")
            print(f"3. Check data files exist in: data/raw/")
            print(f"4. Install missing packages: pip install -r requirements.txt")
            print(f"5. Re-run pipeline: python run_pipeline.py\n")
            sys.exit(1)
    
    print("\n" + "=" * 70)
    print(f"PIPELINE COMPLETED SUCCESSFULLY!")
    print(f"{'=' * 70}")
    print(f"All {completed} stages completed")
    print(f"Finished: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"Check outputs in: reports/, models/, data/")
    print("=" * 70 + "\n")

if __name__ == "__main__":
    main()