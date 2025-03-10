resource "aws_route53_resolver_firewall_rule_group" "example" {
  name = "dns-firewall-group"
}

resource "aws_route53_resolver_firewall_domain_list" "blocked_domains" {
  name    = "blocked-domains"
  domains = file("route53_resolver_blocklist.txt")
}

resource "aws_route53_resolver_firewall_rule" "block_rule" {
  firewall_rule_group_id = aws_route53_resolver_firewall_rule_group.example.id
  firewall_domain_list_id = aws_route53_resolver_firewall_domain_list.blocked_domains.id
  action = "BLOCK"
}
