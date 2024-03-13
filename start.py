import os
os.system('pwd;ls')
# 定义要执行的所有命令
commands = """
mkdir xtuner019 && cd xtuner019;
git clone -b v0.1.9  https://github.com/InternLM/xtuner;
cd xtuner;
pip install -e '.[all]';
ls;cd;
python model/download.py;
ls model;
cd config;
xtuner train /home/xlab-app-center/config/internlm_chat_7b_qlora_oasst1_e3_copy.py;

mkdir /home/xlab-app-center/config/work_dirs/hf;
export MKL_SERVICE_FORCE_INTEL=1;
export CONFIG_NAME_OR_PATH=/home/xlab-app-center/config/internlm_chat_7b_qlora_oasst1_e3_copy.py;
export PTH=/home/xlab-app-center/config/work_dirs/internlm_chat_7b_qlora_oasst1_e3_copy/epoch_3.pth;
export SAVE_PATH=/home/xlab-app-center/config/work_dirs/hf;
xtuner convert pth_to_hf $CONFIG_NAME_OR_PATH $PTH $SAVE_PATH;
export MKL_SERVICE_FORCE_INTEL=1;
export MKL_THREADING_LAYER='GNU';
export NAME_OR_PATH_TO_LLM=/home/xlab-app-center/model/Shanghai_AI_Laboratory/internlm-chat-7b;
export NAME_OR_PATH_TO_ADAPTER=/home/xlab-app-center/config/work_dirs/hf;
mkdir /home/xlab-app-center/config/work_dirs/hf_merge;
export SAVE_PATH=/home/xlab-app-center/config/work_dirs/hf_merge;
xtuner convert merge $NAME_OR_PATH_TO_LLM $NAME_OR_PATH_TO_ADAPTER $SAVE_PATH --max-shard-size 2GB;
pip install streamlit==1.24.0;
cd ~/code/InternLM;
"""

# 通过os.system()执行所有命令
os.system(commands)

os.system('streamlit run /home/xlab-app-center/code/InternLM/web_demo.py --server.address 127.0.0.1 --server.port 6006')