from ansible_runner import Runner

# Path to the playbook file
playbook_path = "/workspaces/ensf400-lab5-ansible/hello.yml"

# Initialize the Runner
runner = Runner(playbook=playbook_path)

# Run the playbook
result = runner.run()

# Print the results
print("\nPlaybook run results:")
for event in result.events:
    if event['event'] in ['playbook_on_stats', 'runner_on_ok']:
        print(event['event_data']['task'])
        print(event['event_data']['res'])

# Cleanup
runner.cleanup()
