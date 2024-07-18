.PHONY: install run clean protos

# Variáveis
PYTHON = python3
PIP = pip
VENV_DIR = venv
PROTO_DIR = .
BUILD_DIR = .
SERVER_BOOK = server_book.py
SERVER_ORDER = server_order.py
SERVER_USER = server_user.py
FLASK_APP = server_flask.py

# Ambiente virtual e dependências
install: venv protos

venv:
	@echo "Criando ambiente virtual..."
	@if ! $(PYTHON) -c "import venv" &> /dev/null; then \
	    echo "O pacote python3-venv não está instalado. Instalando..."; \
	    sudo apt install -y python3-venv; \
	fi
	@$(PYTHON) -m venv $(VENV_DIR)
	@echo "Ativando ambiente virtual e instalando dependências..."
	@./$(VENV_DIR)/bin/$(PIP) install --upgrade pip
	@./$(VENV_DIR)/bin/$(PIP) install grpcio grpcio-tools flask

# Compilação dos arquivos .proto
protos:
	@rm -rf book_catalog_pb2_grpc.py book_catalog_pb2.py order_management_pb2_grpc.py order_management_pb2.py user_auth_pb2_grpc.py user_auth_pb2.py
	@echo "Compilando arquivos .proto..."
	@./$(VENV_DIR)/bin/python -m grpc_tools.protoc -I$(PROTO_DIR) --python_out=$(BUILD_DIR) --grpc_python_out=$(BUILD_DIR) order_management.proto
	@./$(VENV_DIR)/bin/python -m grpc_tools.protoc -I$(PROTO_DIR) --python_out=$(BUILD_DIR) --grpc_python_out=$(BUILD_DIR) book_catalog.proto
	@./$(VENV_DIR)/bin/python -m grpc_tools.protoc -I$(PROTO_DIR) --python_out=$(BUILD_DIR) --grpc_python_out=$(BUILD_DIR) user_auth.proto

# Executar os servidores gRPC e a aplicação Flask
run: install
	@echo "Executando Book Catalog Server..."
	@./$(VENV_DIR)/bin/$(PYTHON) $(SERVER_BOOK) &
	@echo "Executando Order Management Server..."
	@./$(VENV_DIR)/bin/$(PYTHON) $(SERVER_ORDER) &
	@echo "Executando User Authentication Server..."
	@./$(VENV_DIR)/bin/$(PYTHON) $(SERVER_USER) &
	@echo "Executando Flask App..."
	@./$(VENV_DIR)/bin/$(PYTHON) $(FLASK_APP)

# Limpeza
clean:
	@echo "Limpando arquivos temporários e ambiente virtual..."
	@rm -rf $(VENV_DIR)
	@find . -type f -name "*.pyc" -delete
	@find . -type d -name "__pycache__" -delete