# Include exec_config
. ./plugin_helpers/linux/exec_config.sh

# Install the prerequisites
${PYTHON_EXECUTABLE} -m pip install --upgrade -r plugin_helpers/tools/requirements.txt
