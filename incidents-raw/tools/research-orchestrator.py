#!/usr/bin/env python3
"""ESD Incident Research Orchestrator - v2"""
import subprocess, os, time

RESEARCH_DIR = "/opt/repos/esd-research/incident-research"
RAW_DIR = "/opt/repos/esd-research/incidents-raw"
LOG_FILE = "/opt/repos/esd-research/research-orchestrator.log"

def log(msg):
    line = f"{time.strftime('%Y-%m-%d %H:%M:%S')} {msg}"
    print(line, flush=True)
    with open(LOG_FILE, 'a') as f:
        f.write(line + '\n')

def get_unresearched():
    raw_files = set(os.listdir(RAW_DIR))
    done_files = set(os.listdir(RESEARCH_DIR))
    return sorted([f for f in raw_files if f not in done_files and f.endswith('.md')])

def research_file(filename):
    raw_path = os.path.join(RAW_DIR, filename)
    output_path = os.path.join(RESEARCH_DIR, filename)
    if os.path.exists(output_path):
        log(f"  SKIP {filename}")
        return True
    with open(raw_path) as f:
        raw_content = f.read()
    incident_id = filename.replace('.md', '')
    prompt = f"""You are researching Electric Shock Drowning (ESD) incidents for a public safety database.

Raw source data for incident {incident_id}:

{raw_content}

Search the internet for INDEPENDENT sources about this incident.

RULES:
- DO NOT cite: ESDPA documents/PDFs, mikeholt.com, or any compiled list derived from ESDPA
- ONLY cite primary independent sources: news articles, obituaries, coroner reports, court records, OSHA reports, local TV/newspaper
- Try at least 3-4 different search queries: victim name, location+year+"electric shock drowning", body of water name, etc.

Respond with ONLY this markdown (no preamble, no explanation, start directly with the # header):

# {incident_id} — Research Notes

## Incident Summary (from source PDF)
[2-3 sentence summary of the incident]

## Sources Found

### Source 1
- **URL:** [url]
- **Title:** [title]
- **Date:** [date]
- **Summary:** [key facts from this source]

[add more sources, or if none found write: No independent sources found.]

## Conflicting Information
[differences found, or "None found."]

## Additional Details Found
[new info not in raw file, or "None found."]
"""
    try:
        log(f"  Calling claude for {filename}...")
        result = subprocess.run(
            ['claude', '-p', '--dangerously-skip-permissions', prompt],
            capture_output=True, text=True, timeout=300,
            cwd="/opt/repos/esd-research"
        )
        log(f"  claude exit={result.returncode} stdout_len={len(result.stdout)} stderr_len={len(result.stderr)}")
        if result.stderr:
            log(f"  stderr: {result.stderr[:300]}")
        if result.returncode == 0 and result.stdout.strip():
            content = result.stdout.strip()
            # Try to find header start
            idx = content.find(f'# {incident_id}')
            if idx > 0:
                content = content[idx:]
            # Write regardless of format
            with open(output_path, 'w') as f:
                f.write(content + '\n')
            log(f"  OK {filename} ({len(content)} bytes written)")
            return True
        elif result.stdout.strip():
            # Non-zero exit but has content - write it anyway
            content = result.stdout.strip()
            with open(output_path, 'w') as f:
                f.write(f"# {incident_id} — Research Notes\n\n")
                f.write(f"_Note: claude exit code {result.returncode}_\n\n")
                f.write(content + '\n')
            log(f"  PARTIAL {filename} (exit={result.returncode}, {len(content)} bytes)")
            return True
        else:
            log(f"  FAIL {filename} — no output. stdout={repr(result.stdout[:100])} stderr={repr(result.stderr[:100])}")
            # Write a stub file so we don't keep retrying
            with open(output_path, 'w') as f:
                f.write(f"# {incident_id} — Research Notes\n\n## Status\nResearch failed - no output from claude.\n\n## Sources Found\nNo sources found.\n\n## Conflicting Information\nNone found.\n\n## Additional Details Found\nNone found.\n")
            log(f"  STUB written for {filename}")
            return False
    except subprocess.TimeoutExpired:
        log(f"  TIMEOUT {filename} (>5min) - writing stub")
        with open(output_path, 'w') as f:
            f.write(f"# {incident_id} — Research Notes\n\n## Status\nResearch timed out.\n\n## Sources Found\nNo sources found (timeout).\n\n## Conflicting Information\nNone found.\n\n## Additional Details Found\nNone found.\n")
        return False
    except Exception as e:
        log(f"  ERROR {filename}: {e}")
        return False

def main():
    os.makedirs(RESEARCH_DIR, exist_ok=True)
    log("=== ESD Research Orchestrator v2 Starting ===")
    unresearched = get_unresearched()
    log(f"Found {len(unresearched)} files to research")
    success = 0
    fail = 0
    for i, filename in enumerate(unresearched):
        log(f"[{i+1}/{len(unresearched)}] {filename}...")
        ok = research_file(filename)
        if ok: success += 1
        else: fail += 1
        time.sleep(2)
    log(f"=== Done: {success} succeeded, {fail} failed ===")

if __name__ == '__main__':
    main()
