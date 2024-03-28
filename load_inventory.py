from ansible_runner import Runner

# Path to the inventory file
inventory_path = "/workspaces/ensf400-lab5-ansible/hosts.yml"

# Initialize the Runner
runner = Runner(inventory=inventory_path)

# Load inventory
inventory = runner.inventory
print("Hosts:")
for host in inventory.hosts.values():
    print(f"Name: {host.name}, IP Address: {host.vars['ansible_host']}, Group: {host.groups}")

# Ping all hosts
print("\nPing results:")
ping_results = runner.run(inventory='all', module='ping', quiet=True)
for host, result in ping_results.items():
    print(f"{host}: {result['ping']['ping']}")

# Cleanup
runner.cleanup()
