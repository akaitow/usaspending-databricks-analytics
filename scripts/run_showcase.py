"""Execute the local showcase's Python cells and save their displayed outputs.

This dependency-light runner is for the trusted notebook shipped in this repo.
It does not execute the Databricks source notebooks or claim a Jupyter kernel run.
"""
from pathlib import Path
import ast
import base64
import contextlib
import io
import json
import os

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[1]
PATH = ROOT / 'notebooks' / '03_results_showcase.ipynb'

def main():
    os.chdir(ROOT)
    notebook = json.loads(PATH.read_text())
    scope = {'__name__': '__main__'}
    active_outputs = []

    def capture_show(*args, **kwargs):
        for number in plt.get_fignums():
            fig = plt.figure(number)
            buffer = io.BytesIO()
            fig.savefig(buffer, format='png', dpi=140, facecolor='white')
            active_outputs.append({'output_type':'display_data', 'metadata':{}, 'data':{
                'image/png':base64.b64encode(buffer.getvalue()).decode('ascii'),
                'text/plain':'Figure rendered from included saved aggregate data.'}})
            plt.close(fig)

    plt.show = capture_show
    count = 0
    for cell in notebook['cells']:
        if cell['cell_type'] != 'code':
            continue
        count += 1
        source = cell['source']
        if isinstance(source, list): source = ''.join(source)
        ast.parse(source)
        active_outputs = []
        stdout = io.StringIO()
        with contextlib.redirect_stdout(stdout):
            exec(compile(source, str(PATH), 'exec'), scope)
        if stdout.getvalue():
            active_outputs.insert(0, {'output_type':'stream','name':'stdout','text':stdout.getvalue()})
        cell['outputs'] = active_outputs
        cell['execution_count'] = count
    notebook['metadata']['portfolio_execution'] = {
        'method':'Python cells executed sequentially by scripts/run_showcase.py; no Jupyter kernel',
        'inputs':'Included aggregate CSVs and summary.json; no Databricks query execution'}
    PATH.write_text(json.dumps(notebook,indent=1,ensure_ascii=False)+'\n')
    print(f'Executed {count} Python cells; saved notebook outputs and two charts.')

if __name__ == '__main__':
    main()
