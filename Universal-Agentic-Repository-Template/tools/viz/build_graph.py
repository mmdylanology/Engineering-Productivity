import json
import os
import sys
import glob

def build_standalone_graph(nodes, edges, output_html):
    template_path = os.path.join(os.path.dirname(__file__), 'template.html')
    with open(template_path, 'r') as f:
        template = f.read()
    payload = json.dumps({'nodes': nodes, 'edges': edges}).replace('</', '<\/')
    html = template.replace('/*__DATA__*/', payload)
    os.makedirs(os.path.dirname(os.path.abspath(output_html)), exist_ok=True)
    with open(output_html, 'w') as f:
        f.write(html)
    print(f'Compiled standalone visual graph to {output_html}')

def scan_repo(repo_root):
    nodes = []
    edges = []
    
    # 1. Central Core Hub
    nodes.append({
        'data': {
            'id': 'core',
            'label': 'Universal Agentic System',
            'category': 'Core Hub',
            'desc': 'Central architectural backbone coordinating agents, semantic contracts, and governance.',
            'path': 'ARCHITECTURE.md & AGENTS.md',
            'color': '#6366f1',
            'size': 48
        }
    })
    
    # Category Hubs
    categories = [
        ('cat_rules', 'Agent Directives & Rules', '#ec4899', 'Scoped rules triggering based on file globs'),
        ('cat_skills', 'Agent Skills Runbooks', '#8b5cf6', 'Procedural multi-step workflows for autonomous execution'),
        ('cat_semantic', 'Semantic Contracts & Tests', '#10b981', 'Governed business entities, metrics, and ground truth tests'),
        ('cat_decisions', 'Architecture Decisions (ADRs)', '#f59e0b', 'MADR-compliant immutable architectural logs'),
        ('cat_knowledge', 'Knowledge & Computations', '#06b6d4', 'Ubiquitous domain ontology and mathematical attestations'),
        ('cat_governance', 'Governance & Path Protection', '#ef4444', 'Pre-commit guards, AST invariants, and protected paths'),
        ('cat_memory', 'Distributed Memory & Issues', '#3b82f6', 'JSONL micro-tasks, session handoffs, and changelog fragments')
    ]
    
    for cat_id, cat_label, color, desc in categories:
        nodes.append({
            'data': {
                'id': cat_id,
                'label': cat_label,
                'category': 'Pillar Category',
                'desc': desc,
                'path': cat_id,
                'color': color,
                'size': 36
            }
        })
        edges.append({'data': {'id': f'e_core_{cat_id}', 'source': 'core', 'target': cat_id}})

    # 2. Add Rules
    for f in glob.glob(os.path.join(repo_root, '.agents/rules/*.md')):
        base = os.path.basename(f)
        node_id = f'rule_{base}'
        nodes.append({
            'data': {
                'id': node_id,
                'label': f'Rule: {base}',
                'category': 'Agent Rule',
                'desc': f'Scoped rule enforcing standards for {base}',
                'path': f'.agents/rules/{base}',
                'color': '#ec4899',
                'size': 24
            }
        })
        edges.append({'data': {'id': f'e_{node_id}', 'source': 'cat_rules', 'target': node_id}})

    # 3. Add Skills
    for f in glob.glob(os.path.join(repo_root, '.agents/skills/*/SKILL.md')):
        skill_name = os.path.basename(os.path.dirname(f))
        node_id = f'skill_{skill_name}'
        nodes.append({
            'data': {
                'id': node_id,
                'label': f'Skill: /{skill_name}',
                'category': 'Agent Skill',
                'desc': f'Executable skill runbook for {skill_name}',
                'path': f'.agents/skills/{skill_name}/SKILL.md',
                'color': '#8b5cf6',
                'size': 24
            }
        })
        edges.append({'data': {'id': f'e_{node_id}', 'source': 'cat_skills', 'target': node_id}})

    # 4. Add Semantic Entities & Metrics
    for f in glob.glob(os.path.join(repo_root, 'semantic/entities/*.yaml')):
        base = os.path.basename(f)
        node_id = f'entity_{base}'
        nodes.append({
            'data': {
                'id': node_id,
                'label': f'Entity: {base}',
                'category': 'Semantic Entity',
                'desc': f'Governed entity contract mapping physical columns and dimensions.',
                'path': f'semantic/entities/{base}',
                'color': '#10b981',
                'size': 24
            }
        })
        edges.append({'data': {'id': f'e_{node_id}', 'source': 'cat_semantic', 'target': node_id}})

    for f in glob.glob(os.path.join(repo_root, 'semantic/metrics/*.yaml')):
        base = os.path.basename(f)
        node_id = f'metric_{base}'
        nodes.append({
            'data': {
                'id': node_id,
                'label': f'Metric: {base}',
                'category': 'Semantic Metric',
                'desc': f'Governed metric contract defining additivity and valid calculations.',
                'path': f'semantic/metrics/{base}',
                'color': '#10b981',
                'size': 24
            }
        })
        edges.append({'data': {'id': f'e_{node_id}', 'source': 'cat_semantic', 'target': node_id}})

    for f in glob.glob(os.path.join(repo_root, 'semantic/tests/*.yaml')):
        base = os.path.basename(f)
        node_id = f'test_{base}'
        nodes.append({
            'data': {
                'id': node_id,
                'label': f'Suite: {base}',
                'category': 'Semantic Test',
                'desc': f'Ground truth queries and refusal test cases for LLM verification.',
                'path': f'semantic/tests/{base}',
                'color': '#10b981',
                'size': 22
            }
        })
        edges.append({'data': {'id': f'e_{node_id}', 'source': 'cat_semantic', 'target': node_id}})

    # 5. Add ADRs
    for f in glob.glob(os.path.join(repo_root, 'docs/decisions/*.md')):
        base = os.path.basename(f)
        if base == 'index.md': continue
        node_id = f'adr_{base}'
        nodes.append({
            'data': {
                'id': node_id,
                'label': f'ADR: {base}',
                'category': 'Decision Record',
                'desc': f'Architectural decision record in MADR format.',
                'path': f'docs/decisions/{base}',
                'color': '#f59e0b',
                'size': 24
            }
        })
        edges.append({'data': {'id': f'e_{node_id}', 'source': 'cat_decisions', 'target': node_id}})

    # 6. Add Knowledge & Computations
    for f in glob.glob(os.path.join(repo_root, 'knowledge/glossary/*.md')):
        base = os.path.basename(f)
        node_id = f'term_{base}'
        nodes.append({
            'data': {
                'id': node_id,
                'label': f'Glossary: {base}',
                'category': 'Domain Glossary',
                'desc': 'Ubiquitous domain vocabulary and disambiguation rules.',
                'path': f'knowledge/glossary/{base}',
                'color': '#06b6d4',
                'size': 22
            }
        })
        edges.append({'data': {'id': f'e_{node_id}', 'source': 'cat_knowledge', 'target': node_id}})

    for f in glob.glob(os.path.join(repo_root, 'knowledge/computations/*.md')):
        base = os.path.basename(f)
        node_id = f'calc_{base}'
        nodes.append({
            'data': {
                'id': node_id,
                'label': f'Attestation: {base}',
                'category': 'Attested Computation',
                'desc': 'Formal mathematical formula proof, bounds, and precision guarantees.',
                'path': f'knowledge/computations/{base}',
                'color': '#06b6d4',
                'size': 22
            }
        })
        edges.append({'data': {'id': f'e_{node_id}', 'source': 'cat_knowledge', 'target': node_id}})

    # 7. Governance
    nodes.append({
        'data': {
            'id': 'gov_protected',
            'label': 'Protected Paths Spec',
            'category': 'Governance',
            'desc': 'Human-gated files agents cannot edit without explicit bypass token.',
            'path': 'governance/protected_paths.yaml',
            'color': '#ef4444',
            'size': 22
        }
    })
    edges.append({'data': {'id': 'e_gov_protected', 'source': 'cat_governance', 'target': 'gov_protected'}})

    nodes.append({
        'data': {
            'id': 'gov_guard',
            'label': 'Pre-Commit Guard',
            'category': 'Governance',
            'desc': 'Git pre-commit enforcement tool blocking unauthorized agent modifications.',
            'path': 'tools/guards/protect_paths.py',
            'color': '#ef4444',
            'size': 22
        }
    })
    edges.append({'data': {'id': 'e_gov_guard', 'source': 'cat_governance', 'target': 'gov_guard'}})

    nodes.append({
        'data': {
            'id': 'gov_semgrep',
            'label': 'Semgrep AST Rules',
            'category': 'Governance',
            'desc': 'Static analysis preventing SQL injection and security anti-patterns.',
            'path': '.semgrep/repo_rules.yml',
            'color': '#ef4444',
            'size': 22
        }
    })
    edges.append({'data': {'id': 'e_gov_semgrep', 'source': 'cat_governance', 'target': 'gov_semgrep'}})

    # 8. Memory & Tasks
    nodes.append({
        'data': {
            'id': 'mem_issues',
            'label': 'JSONL Issue Tracker (Beads)',
            'category': 'Issue Tracking',
            'desc': 'Git-native task tracker allowing agents and humans to track micro-tasks without merge conflicts.',
            'path': '.beads/issues.jsonl',
            'color': '#3b82f6',
            'size': 22
        }
    })
    edges.append({'data': {'id': 'e_mem_issues', 'source': 'cat_memory', 'target': 'mem_issues'}})

    nodes.append({
        'data': {
            'id': 'mem_sessions',
            'label': 'Session Handoff Ledger',
            'category': 'Session Memory',
            'desc': 'Chronological handoff notes capturing accomplished work, dead ends, and immediate next tasks.',
            'path': '.agents/sessions/template.md',
            'color': '#3b82f6',
            'size': 22
        }
    })
    edges.append({'data': {'id': 'e_mem_sessions', 'source': 'cat_memory', 'target': 'mem_sessions'}})

    nodes.append({
        'data': {
            'id': 'mem_changes',
            'label': 'Changelog Fragments',
            'category': 'Changelog Management',
            'desc': 'Distributed change fragments compiled into master changelog on release.',
            'path': 'changes/unreleased/fragment_template.yaml',
            'color': '#3b82f6',
            'size': 22
        }
    })
    edges.append({'data': {'id': 'e_mem_changes', 'source': 'cat_memory', 'target': 'mem_changes'}})

    return nodes, edges

if __name__ == '__main__':
    repo_root = sys.argv[1] if len(sys.argv) > 1 else '.'
    out_file = sys.argv[2] if len(sys.argv) > 2 else os.path.join(repo_root, 'docs/graph.html')
    nodes, edges = scan_repo(repo_root)
    build_standalone_graph(nodes, edges, out_file)
