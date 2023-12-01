# Licensed under the MIT License
# https://github.com/craigahobbs/python-template/blob/main/LICENSE


MAKEJ ?= -j


.PHONY: help
help:
	@echo 'usage: make [changelog|clean|commit|superclean|test]'


.PHONY: commit
commit: test


.PHONY: clean
clean:
	rm -rf build/ test-actual/


.PHONY: gh-pages
gh-pages:


.PHONY: superclean
superclean: clean


# Helper to edit files with sed
SED_FILE = if [ -f $(strip $(2)) ]; then sed -E $(strip $(1)) $(strip $(2)) >> $(strip $(2)).tmp && mv $(strip $(2)).tmp $(strip $(2)); fi


# Test rule function - name, template args, *env
define TEST_RULE
test: test-$(strip $(1))

.PHONY: test-$(strip $(1))
test-$(strip $(1)): build/venv.build
	@echo 'Testing "$(strip $(1))"...'
	rm -rf test-actual/$(strip $(1))/
	build/venv/bin/template-specialize template/ test-actual/$(strip $(1))/ $(strip $(2))
	$(call SED_FILE, 's/[0-9]{4}(,? John Doe)/YYYY\1/g', test-actual/$(strip $(1))/LICENSE)
	$(call SED_FILE, 's/[0-9]{4}(,? John Doe)/YYYY\1/g', test-actual/$(strip $(1))/doc/conf.py)
	diff -r test-actual/$(strip $(1))/ test-expected/$(strip $(1))/
	$(if $(3),$(strip $(3)) )$$(MAKE) $(MAKEJ) -C test-actual/$(strip $(1))/ commit
	rm -rf test-actual/$(strip $(1))/
endef


# Test rules
.PHONY: test
test:
	rm -rf test-actual/
	@echo Tests completed - all passed

$(eval $(call TEST_RULE, required, \
    -k package 'my-package' -k name 'John Doe' -k email 'johndoe@gmail.com' -k github 'johndoe'))

$(eval $(call TEST_RULE, noapi, \
    -k package 'my-package' -k name 'John Doe' -k email 'johndoe@gmail.com' -k github 'johndoe' -k noapi 1))

$(eval $(call TEST_RULE, nomain, \
    -k package 'my-package' -k name 'John Doe' -k email 'johndoe@gmail.com' -k github 'johndoe' -k nomain 1))

$(eval $(call TEST_RULE, noapi-nomain, \
    -k package 'my-package' -k name 'John Doe' -k email 'johndoe@gmail.com' -k github 'johndoe' -k noapi 1 -k nomain 1))

$(eval $(call TEST_RULE, noapi-0-nomain-0, \
    -k package 'my-package' -k name 'John Doe' -k email 'johndoe@gmail.com' -k github 'johndoe' -k noapi 0 -k nomain 0, \
    UNITTEST_PARALLEL=1))


.PHONY: changelog
changelog: build/venv.build
	build/venv/bin/simple-git-changelog


build/venv.build:
	python3 -m venv build/venv
	build/venv/bin/pip -q install --progress-bar off -U pip setuptools
	build/venv/bin/pip -q install --progress-bar off simple-git-changelog template-specialize
	touch $@
