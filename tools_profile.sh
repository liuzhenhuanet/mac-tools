
# 可以设置tools目录相关环境变量，该配置脚本会在bash或zsh登录时被调用

TOOL_HOME=/Users/liuzhenhua/Workspace/tools
export PATH=$TOOL_HOME/local/bin:$TOOL_HOME/bin:$TOOL_HOME/open-applications:$PATH

export device_webapp_dir=/sdcard/Android/data/com.yuantiku.tutor/files/webapp

# proxy list
alias proxy='export all_proxy=socks5://127.0.0.1:1080;curl cip.cc'
alias unproxy='unset all_proxy;curl cip.cc'

# 快捷命令
alias typora="open -a typora" # 支持命令行打开typora，或在命令行中使用typora打点文件
