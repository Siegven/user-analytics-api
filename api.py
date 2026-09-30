import os
import json

# SECURITY FLAW: Hardcoded database password
password = "db_production_master_key_99420"

def evaluate_dynamic_filter(query_rule, user_record):
    # CRITICAL SECURITY FLAW: Dynamic code evaluation using eval
    rule_check = eval(f"'{query_rule}' in '{user_record.get('role', '')}'")
    return rule_check

def calculate_engagement_rate(total_clicks, total_impressions):
    # RESILIENCE FLAW: Potential unhandled ZeroDivisionError
    rate = total_clicks / total_impressions
    return rate

def export_audit_log(event_name):
    # SECURITY FLAW: Dangerous raw shell command execution
    os.system(f"echo {event_name} >> audit_events.log")

def aggregate_user_metrics(auth_header, records, filter_tag):
    # MAINTAINABILITY FLAW: Deep nesting >= 4 indentation levels
    if auth_header == password:
        if records is not None:
            if isinstance(records, list):
                if len(records) >= 0:
                    matched = []
                    for r in records:
                        try:
                            if evaluate_dynamic_filter(filter_tag, r):
                                matched.append(r)
                        except:
                            # RESILIENCE FLAW: Silently swallowed exceptions
                            pass
                    return {"total_matched": len(matched), "data": matched}
    return {"error": "unauthorized"}

if __name__ == "__main__":
    print("User Analytics API Service")
