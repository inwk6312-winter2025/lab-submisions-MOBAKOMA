from jinja2 import Environment, FileSystemLoader
ENV = Environment(loader=FileSystemLoader('.'))
template = ENV.get_template("sub-template.j2")

# Define router data

routers = [
        {
            "hostname": "R1",
            "router_id": 1,
            "interfaces": [
                {"name": "GigabitEthernet1.12", "ip": "155.1.12.1", "mask": "255.255.255.0", "network": "155.1.12.0", "wildcard": "0.0.0.255"},
                {"name": "GigabitEthernet1.13", "ip": "155.1.13.1", "mask": "255.255.255.0", "network": "155.1.13.0", "wildcard": "0.0.0.255"},
                {"name": "GigabitEthernet1.14", "ip": "155.1.14.1", "mask": "255.255.255.0", "network": "155.1.14.0", "wildcard": "0.0.0.255"},
            ]
        },
        {
            "hostname": "R2",
            "router_id": 2,
            "interfaces": [
                {"name": "GigabitEthernet1.12", "ip": "155.1.12.2", "mask": "255.255.255.0", "network": "155.1.12.0", "wildcard": "0.0.0.255"},
            ]

        },
        {
            "hostname": "R3",
            "router_id": 3,
            "interfaces": [
                {"name": "GigabitEthernet1.13", "ip": "155.1.13.3", "mask": "255.255.255.0", "network": "155.1.13.0", "wildcard": "0.0.0.255"},
            ]
        },
        {
            "hostname": "R4",
            "router_id": 4,
            "interfaces": [
                {"name": "GigabitEthernet1.14", "ip": "155.1.14.4", "mask": "255.255.255.0", "network": "155.1.14.0", "wildcard": "0.0.0.255"},
            ]
        }
    ]

# Generate and print configurations for each router 
for router in routers:
    config = template.render(router)
    print(f"\n{'='*20} {router['hostname']} Configuration {'='*20}\n")
    print(config)

# Save each router's config to a text file 
with open(f"{router['hostname']}_config.txt", "w") as f:
    f.write(config)

