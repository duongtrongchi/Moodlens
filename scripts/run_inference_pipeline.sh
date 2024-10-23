cd ..

cd inference_pipeline/

echo "Current path is: $(pwd)"

export PYTHONPATH="$(pwd):$PYTHONPATH"

cd inference_pipeline/

python main.py