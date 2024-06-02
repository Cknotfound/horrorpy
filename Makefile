.PHONY: clean

clean:
	rm -rf *.ini 
	find . -type d -name "__pycache__" -exec rm -rf {} +
