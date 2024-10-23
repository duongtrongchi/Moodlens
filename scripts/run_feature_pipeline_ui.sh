cd ..

cd feature_pipeline/

echo "Current path is: $(pwd)"

export PYTHONPATH="$(pwd):$PYTHONPATH"

cd feature_pipeline/data_store/feature_repo

feast ui