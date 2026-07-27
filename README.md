# OLX Ads Selenium Bot

Experimental Python scripts for automating selected OLX browser flows with
Selenium. The repository is a proof-of-concept rather than a production-ready
automation package: the scripts use hardcoded values, fixed delays, and legacy
Selenium element APIs.

## What It Does

`olxbot.py` opens the OLX ad-posting page and, three times, attempts to:

1. Enter a hardcoded title, description, and ZIP code.
2. Select the Services category and a fixed set of service-type checkboxes.
3. Upload `arquivos/image.jpg`.
4. Submit the ad.

The script also dismisses the cookie notice once. It starts Chrome through
`webdriver-manager`, which downloads or locates a compatible ChromeDriver at
runtime.

`botdenuncias.py` is a separate, incomplete flow. It opens one hardcoded OLX
listing, clicks the report action, and starts the account-entry flow. It does
not complete or verify a report submission.

## Repository Contents

- `olxbot.py`: ad-posting automation.
- `botdenuncias.py`: partial listing-report automation.
- `olxbot.spec`: PyInstaller specification for building `olxbot.py` as a
  windowed executable.
- `arquivos/image.jpg`: the image path expected by `olxbot.py`.
- `env python.py`: a bundled pip bootstrap script; it is not imported by the
  automation scripts.

There is currently no `requirements.txt`, configuration directory, test suite,
CI workflow, or declared license file in the repository.

## Prerequisites

- Python 3.7 or newer. The bundled pip bootstrap script checks for Python 3.7,
  although the automation itself has not been validated across Python versions.
- Google Chrome installed locally.
- A graphical desktop session. Selenium and PyAutoGUI interact with a local
  browser and desktop input.
- Internet access to OLX and PyPI.
- An OLX account or interactive session when OLX requires authentication. The
  scripts do not implement credential handling.

The current image path is constructed as a Windows path using backslashes. Run
the posting script from the repository root on Windows, or update the script
before expecting the image upload to work on another operating system.

## Installation

Because no dependency manifest is present, install the packages inferred from
the imports:

```bash
git clone https://github.com/xfelipealves/OlxBotAnunciosSelenium.git
cd OlxBotAnunciosSelenium

python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install selenium webdriver-manager pyautogui
```

On Windows PowerShell, activate the virtual environment with:

```powershell
.venv\Scripts\Activate.ps1
```

Do not run `env python.py` unless you have intentionally reviewed the bundled
bootstrap code and need it. A normal virtual environment with `pip` is the
recommended setup.

## Configuration and Credential Safety

There is no external configuration layer. The ad title, description, ZIP code,
OLX URLs, selected service types, upload path, and repetition count are
hardcoded in the Python source.

- Review and change hardcoded values locally before running the script.
- Never commit passwords, access tokens, browser profiles, cookies, or session
  exports.
- If authentication is required, complete it interactively in a local browser
  session and keep all resulting profile data outside the repository.
- Treat the existing listing URL and uploaded image as potentially sensitive
  operational data.
- Do not use this repository to bypass OLX authentication, rate limits, abuse
  controls, or account safeguards.

## Execution

Run commands from the repository root with the virtual environment activated:

```bash
python olxbot.py
```

To try the separate, incomplete report flow:

```bash
python botdenuncias.py
```

The scripts use fixed `time.sleep` calls and interact with a live website.
Expect Chrome to open, and stop the process manually if the page state is not
what the script expects.

## Limitations and Terms of Service

This project has not been hardened for unattended or production use. Known
limitations include:

- Legacy `find_element_by_*` and `find_elements_by_*` calls may be unsupported
  by current Selenium releases.
- Fixed sleeps and brittle XPath/class selectors can fail when OLX changes its
  markup, timing, consent dialog, or authentication flow.
- Ad content, category indexes, ZIP code, target URLs, image path, and the
  three-run loop are fixed in source code.
- There is no structured error handling, retry policy, result verification,
  duplicate prevention, or driver cleanup.
- The upload path assumes Windows path separators and a local image file.
- `botdenuncias.py` does not finish the report flow.

Automating a third-party website may be restricted by that website's terms,
policies, or applicable law. Review and follow the current OLX Terms of Use,
automation rules, privacy requirements, and applicable laws before running
these scripts. You are responsible for the accounts, content, traffic, and
consequences of any execution.

## Testing and Status

No automated tests or CI configuration are included. A safe local syntax check
for the Python sources is:

```bash
python3 -m py_compile olxbot.py botdenuncias.py "env python.py"
```

This command does not open a browser or contact OLX. A successful syntax check
does not verify that the live website flow still works. Browser testing should
use a test account, non-sensitive content, and explicit manual supervision.

## Contributing

Contributions are welcome through focused pull requests. Please:

- Keep credentials, cookies, browser profiles, generated executables, and other
  local artifacts out of commits.
- Describe any changes to live-site behavior and selectors.
- Run the syntax check above and `git diff --check` before submitting a pull
  request.
- Avoid adding behavior that circumvents authentication, rate limits, or
  platform safeguards.

## License

No license has been declared and no license file is included. Unless the
copyright holder states otherwise, reuse and redistribution are not granted by
default. Contact the repository owner before using this code in another
project.
