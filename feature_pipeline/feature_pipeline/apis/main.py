from fastapi import FastAPI
from fastapi.responses import StreamingResponse
import uvicorn

app = FastAPI()

async def return_data():
    with open('/teamspace/studios/this_studio/nlp-hr-feedback/feature_pipeline/feature_pipeline/apis/loan_approval_dataset.csv', 'r') as o:
        data = 'start'
        while data:
            data = o.readline()
            yield data
    

@app.get('/test')
async def test():
    data_iter = return_data()
    return StreamingResponse(data_iter)
    
    
if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8888)