test:
	cat test/.test_chpwd_cmd_template | sed  -e "s|{CHPWD_CMD_DIR}|`pwd`|g" > test/.test_chpwd_cmd
	nosetests -sv

lint:
	flake8 --ignore E501,W504 test/* src/*

.PHONY: test lint