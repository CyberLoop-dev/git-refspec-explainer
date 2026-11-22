<div align="center">

![Header](https://capsule-render.vercel.app/api?type=waving&color=0:0f172a,100:0d9488&height=180&section=header&text=Git+Refspec+Explainer&fontSize=40&fontColor=ffffff&animation=fadeIn)
<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=600&size=21&pause=1000&color=14B8A6&center=true&vCenter=true&width=650&lines=Understand+Git+refspecs+without+changing+refs" alt="Project title"/>
[![License](https://img.shields.io/github/license/CyberLoop-dev/git-refspec-explainer?style=for-the-badge)](LICENSE)
[![Language](https://img.shields.io/github/languages/top/CyberLoop-dev/git-refspec-explainer?style=for-the-badge)](https://github.com/CyberLoop-dev/git-refspec-explainer)
[![Stars](https://img.shields.io/github/stars/CyberLoop-dev/git-refspec-explainer?style=for-the-badge)](https://github.com/CyberLoop-dev/git-refspec-explainer/stargazers)
[![Last commit](https://img.shields.io/github/last-commit/CyberLoop-dev/git-refspec-explainer?style=for-the-badge)](https://github.com/CyberLoop-dev/git-refspec-explainer/commits/main)
<img src="assets/mark.svg" width="112" alt="Git refspec mark"/>
</div>

## 🧭 Overview
A read-only Python CLI that explains a useful subset of Git refspec syntax by mapping sample source refs to destination refs. It never invokes Git or changes repository data.

## ✨ Features
- 🌿 Parses force, wildcard, deletion, and negative refspec forms.
- 🧭 Shows the source-to-destination mapping for supplied refs.
- 🚫 Applies negative patterns as exclusions.
- 🧪 Includes tests for parsing, matching, and invalid patterns.

## 🖥️ Demo
No hosted demo is published. Try the CLI with the example below.

## 🚀 Quick Start
```bash
python main.py --refspec '+refs/heads/*:refs/remotes/origin/*' --refs refs/heads/main,refs/heads/dev
```
Run tests with `python -m unittest discover -s tests -v`.

## 🧰 Tech Stack
Python 3.10+ standard library only. No third-party dependencies.

## 🗂️ Folder Structure
```text
git-refspec-explainer/
├── main.py
├── tests/
├── assets/
├── .github/workflows/
└── pyproject.toml
```

## 🛣️ Roadmap
- [x] Explain wildcard, force, deletion, and negative patterns.
- [x] Read-only mapping simulation.
- [ ] Add additional fetch/push examples and diagnostics.

## 🤝 Contributing
Pull requests are welcome. Keep the simulator read-only and add tests for new syntax.

## 📄 License
MIT — see [LICENSE](LICENSE).

<div align="center">
![Footer](https://capsule-render.vercel.app/api?type=waving&color=0:0d9488,100:0f172a&height=110&section=footer)
</div>
