CC = gcc
CFLAGS = -Wall -Wextra -g -O0

SRC_DIR = ./src
BIN_DIR = ./bin

BINARIES = arb_read arb_read_patched

# Compute full paths
TARGETS = $(addprefix $(BIN_DIR)/, $(BINARIES))
SOURCES = $(addprefix $(SRC_DIR)/, $(addsuffix .c, $(BINARIES)))

# Default target
all: $(BIN_DIR) $(TARGETS)

# Rule to compile each source into its binary
$(BIN_DIR)/%: $(SRC_DIR)/%.c
	$(CC) $(CFLAGS) -o $@ $<

# Ensure bin directory exists
$(BIN_DIR):
	mkdir -p $(BIN_DIR)

clean:
	rm -rf $(BIN_DIR)
