from flask import Flask, render_template, request
import json
import ipaddress

app = Flask(__name__)

def load_rules():
    with open('rules.json') as f:
        return json.load(f)

def match_rule(rules, test_packet):
    for rule in rules:

        # Protocol check
        if rule['protocol'] != "ANY" and rule['protocol'] != test_packet['protocol']:
            continue

        # Source IP check (CIDR supported)
        if rule['source'] != "ANY":
            net = ipaddress.ip_network(rule['source'])
            if ipaddress.ip_address(test_packet['source']) not in net:
                continue

        # Destination IP check (FIXED: now supports CIDR)
        if rule['destination'] != "ANY":
            net = ipaddress.ip_network(rule['destination'])
            if ipaddress.ip_address(test_packet['destination']) not in net:
                continue

        # Port check (FIXED: proper int comparison)
        if rule['port'] != "ANY":
            if int(test_packet['port']) != int(rule['port']):
                continue

        # If all matched → return action
        return rule['action'], rule

    # Default deny
    return "DENY", None


@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    matched_rule = None

    if request.method == 'POST':
        test_packet = {
            'protocol': request.form['protocol'],
            'source': request.form['source'],
            'destination': request.form['destination'],
            'port': request.form['port']
        }

        rules = load_rules()
        result, matched_rule = match_rule(rules, test_packet)

    return render_template("index.html", result=result, matched_rule=matched_rule)


if __name__ == "__main__":
    app.run(debug=True)