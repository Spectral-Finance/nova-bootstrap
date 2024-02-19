.PHONY: zip

zip:
	@./bundler.py

cleanup:
	@rm -rf upload
	@rm upload.zip
