import os

os.system('xtuner train ./config/internlm_chat_7b_qlora_oasst1_e3_copy.py')

# 定义要执行的所有命令
commands = """
mkdir ./config/work_dirs/hf;
export MKL_SERVICE_FORCE_INTEL=1;
export CONFIG_NAME_OR_PATH=./config/internlm_chat_7b_qlora_oasst1_e3_copy.py;
export PTH=./config/work_dirs/internlm_chat_7b_qlora_oasst1_e3_copy/epoch_3.pth;
export SAVE_PATH=./config/work_dirs/hf;
xtuner convert pth_to_hf $CONFIG_NAME_OR_PATH $PTH $SAVE_PATH;
export MKL_SERVICE_FORCE_INTEL=1;
export MKL_THREADING_LAYER='GNU';
export NAME_OR_PATH_TO_LLM=Shanghai_AI_Laboratory/internlm-chat-7b;
export NAME_OR_PATH_TO_ADAPTER=./config/work_dirs/hf;
mkdir ./config/work_dirs/hf_merge;
export SAVE_PATH=./config/work_dirs/hf_merge;
xtuner convert merge $NAME_OR_PATH_TO_LLM $NAME_OR_PATH_TO_ADAPTER $SAVE_PATH --max-shard-size 2GB;
pip install streamlit==1.24.0
"""

# 通过os.system()执行所有命令
os.system(commands)

os.system('streamlit run code/InternLM/web_demo.py --server.address 127.0.0.1 --server.port 6006')