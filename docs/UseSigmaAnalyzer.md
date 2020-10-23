# Sigma Analyser in Timesketch

## What is Sigma

See description at the [Sigma Github repository](https://github.com/Neo23x0/sigma#what-is-sigma)

## Sigma in Timesketch

Since early 2020 Timesketch has Sigma support implemented. Sigma can be used as an analyser.

### Install rules

Timesketch deliberately does not provide a set of Sigma rules, as those would add complexity to maintain.
Instead we recommend to clone https://github.com/Neo23x0/sigma to /data/sigma.
This directory will not be catched by git. 
                                                                                                     
```shell
cd data
git clone https://github.com/Neo23x0/sigma
```

The rules then will be under

```shell
timesketch/data/sigma
```

### Sigma Rules

The windows rules are stored in

```shell
timesketch/data/sigma/rules/windows
```

The linux rules are stored in

```shell
timesketch/data/linux
timesketch/data/sigma/rules/linux
```

### Sigma config

In the config file

```shell
sigma_config.yaml
```

There is a section with mappings, most mappings where copied from HELK configuration.
If you find a mapping missing, feel free to add and create a PR.

### Field Mapping

Some adjustments verified:

- s/EventID/event_identifier
- s/Source/source_name

### Analyzer_run.py

You can run the Sigma analyzer providing sample data:

```shell
python3 test_tools/analyzer_run.py --test_file test_tools/test_events/sigma_events.jsonl timesketch/lib/analyzers/sigma_tagger.py RulesSigmaPlugin
```

## Test data

If you want to test that feature, get some evtx files from the following
 links and parse it via plaso

- [github.com/sbousseaden/EVTX-ATTACK-SAMPLES](https://github.com/sbousseaden/EVTX-ATTACK-SAMPLES)
- [github.com/sans-blue-team/DeepBlueCLI/evtx](https://github.com/sans-blue-team/DeepBlueCLI/evtx)

## Verify rules

Deploying rules that can not be parsed by Sigma can cause problems on analyst side
as well as Timesketch operator side. The analyst might not be able to see
the logs and the errors might only occur when running the analyzer.

This is why a standalone tool can be used from:

```shell
test_tools/sigma_verify_rules.py
```

This tool takes the following options:

```shell
usage: sigma_verify_rules.py [-h] [--config_file PATH_TO_TEST_FILE]
                             PATH_TO_RULES
sigma_verify_rules.py: error: the following arguments are required: PATH_TO_RULES
```

And could be used like the following to verify your rules would work:

```shell
sigma_verify_rules.py --config_file ../data/sigma_config.yaml ../data/sigma/rules
```

If any rules in that folder is causing problems it will be shown:

```shell
sigma_verify_rules.py --config_file ../data/sigma_config.yaml ../timesketch/data/sigma/rules
ERROR:root:reverse_shell.yaml Error generating rule in file ../timesketch/data/sigma/rules/linux/reverse_shell.yaml you should not use this rule in Timesketch: No condition found
ERROR:root:recon_commands.yaml Error generating rule in file ../timesketch/data/sigma/rules/data/linux/recon_commands.yaml you should not use this rule in Timesketch: No condition found
You should NOT import the following rules
../timesketch/data/sigma/rules/linux/reverse_shell.yaml
../timesketch/data/sigma/rules/linux/recon_commands.yaml
```
