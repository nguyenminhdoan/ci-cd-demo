#!/usr/bin/env python3
"""
Generate HTML test report for CI/CD demo
"""

import datetime
import subprocess
from pathlib import Path


def run_command(cmd):
    """Run a command and return output"""
    try:
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
        return result.stdout, result.stderr, result.returncode
    except Exception as e:
        return "", str(e), 1


def generate_html_report():
    """Generate HTML test report"""

    # Get git info
    git_commit, _, _ = run_command("git rev-parse HEAD")
    git_branch, _, _ = run_command("git rev-parse --abbrev-ref HEAD")
    git_message, _, _ = run_command("git log -1 --pretty=%B")

    # Get current time
    build_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S UTC")

    # Run tests and collect results
    test_output, test_error, test_code = run_command(
        "python -m pytest test_calc.py -v --tb=short"
    )

    # Run linting
    lint_output, lint_error, lint_code = run_command(
        "flake8 calc.py --max-line-length=120"
    )

    # Run coverage
    coverage_output, coverage_error, coverage_code = run_command(
        "python -m coverage run -m pytest test_calc.py && python -m coverage report"
    )
    # Build status
    overall_status = "✅ PASSED" if test_code == 0 and lint_code == 0 else "❌ FAILED"
    status_color = "green" if test_code == 0 and lint_code == 0 else "red"

    # HTML template
    html_content = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>CI/CD Demo - Test Report</title>
    <style>
        body {{
            font-family: 'Arial', sans-serif;
            margin: 0;
            padding: 20px;
            background-color: #f5f5f5;
        }}
        .container {{
            max-width: 1200px;
            margin: 0 auto;
            background: white;
            padding: 30px;
            border-radius: 10px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        }}
        .header {{
            text-align: center;
            margin-bottom: 30px;
            padding: 20px;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            border-radius: 10px;
        }}
        .status {{
            font-size: 24px;
            font-weight: bold;
            color: {status_color};
            margin: 20px 0;
        }}
        .info-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 20px;
            margin: 20px 0;
        }}
        .info-box {{
            background: #f8f9fa;
            padding: 15px;
            border-radius: 8px;
            border-left: 4px solid #667eea;
        }}
        .section {{
            margin: 30px 0;
            padding: 20px;
            background: #f8f9fa;
            border-radius: 8px;
        }}
        .section h2 {{
            color: #333;
            margin-top: 0;
        }}
        .code-block {{
            background: #2d3748;
            color: #e2e8f0;
            padding: 15px;
            border-radius: 5px;
            overflow-x: auto;
            font-family: 'Courier New', monospace;
            white-space: pre-wrap;
        }}
        .badge {{
            display: inline-block;
            padding: 4px 8px;
            border-radius: 4px;
            font-size: 12px;
            font-weight: bold;
            margin: 2px;
        }}
        .badge.success {{ background: #48bb78; color: white; }}
        .badge.error {{ background: #f56565; color: white; }}
        .badge.warning {{ background: #ed8936; color: white; }}
        .footer {{
            text-align: center;
            margin-top: 40px;
            padding: 20px;
            background: #edf2f7;
            border-radius: 8px;
            color: #4a5568;
        }}
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>🚀 CI/CD Demo - Test Report</h1>
            <p>Automated Testing & Deployment Pipeline test 1</p>
        </div>

        <div class="status">
            Build Status: {overall_status}
        </div>

        <div class="info-grid">
            <div class="info-box">
                <h3>📅 Build Time</h3>
                <p>{build_time}</p>
            </div>
            <div class="info-box">
                <h3>🌿 Branch</h3>
                <p>{git_branch.strip()}</p>
            </div>
            <div class="info-box">
                <h3>📝 Commit</h3>
                <p>{git_commit.strip()[:8]}</p>
            </div>
            <div class="info-box">
                <h3>💬 Message</h3>
                <p>{git_message.strip()}</p>
            </div>
        </div>

        <div class="section">
            <h2>🧪 Test Results</h2>
            <div class="badge {'success' if test_code == 0 else 'error'}">
                {'Tests Passed' if test_code == 0 else 'Tests Failed'}
            </div>
            <div class="code-block">{test_output}</div>
        </div>

        <div class="section">
            <h2>📊 Code Quality</h2>
            <div class="badge {'success' if lint_code == 0 else 'warning'}">
                {'Linting Passed' if lint_code == 0 else 'Linting Issues'}
            </div>
            <div class="code-block">{lint_output if lint_output else 'No linting issues found!'}</div>
        </div>

        <div class="section">
            <h2>📈 Test Coverage</h2>
            <div class="code-block">{coverage_output}</div>
        </div>

        <div class="footer">
            <p>Generated automatically by Group projecte</p>
            <p>Last updated: {build_time}</p>
        </div>
    </div>
</body>
</html>
"""

    # Create docs directory
    docs_dir = Path("docs")
    docs_dir.mkdir(exist_ok=True)

    # Write HTML file
    with open(docs_dir / "index.html", "w") as f:
        f.write(html_content)

    print("✅ HTML report generated successfully!")
    print("📄 Report saved to: docs/index.html")


if __name__ == "__main__":
    generate_html_report()
