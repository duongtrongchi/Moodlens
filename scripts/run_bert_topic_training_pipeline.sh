cd ..

cd training_pipeline/topic_modeling/

echo "Current path is: $(pwd)"


export PYTHONPATH="$(pwd):$PYTHONPATH"

cd topic_modeling

python training_pipeline.py