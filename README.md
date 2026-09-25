# BuildSolid

BuildSolid is a free, open-source Markdown framework for planning, building, and verifying software with AI.

It gives a builder and an AI coding agent a shared way to state the intended result, decide what work is in scope, carry that work into code, and check what actually happened. The decisions and working instructions live in Markdown files in your Git repository. An agent can read them in a normal checkout; no BuildSolid service is required.

## Start with the work in front of you

To use this prerelease from a fixed source tree:

```sh
git clone https://github.com/solimancifuentes/buildsolid.git
cd buildsolid
git switch --detach v0.6.0
```

Read the [Framework constitution](https://github.com/solimancifuentes/buildsolid/blob/v0.6.0/framework/docs/constitution.md) for the rules, then the [context package](https://github.com/solimancifuentes/buildsolid/blob/v0.6.0/framework/docs/context-package.md) for the workflow. The [Project System](https://github.com/solimancifuentes/buildsolid/blob/v0.6.0/project-system/README.md) has skills, templates, examples, and [goal-oriented recipes](https://github.com/solimancifuentes/buildsolid/blob/v0.6.0/project-system/docs/recipes.md).

You can start with a focused skill when the task is clear. Use [buildsolid-orchestrator](https://github.com/solimancifuentes/buildsolid/blob/v0.6.0/project-system/skills/buildsolid-orchestrator/SKILL.md) when you need help finding the right entry point or reconciling work across stages. Choose a project profile to set the depth of work and an interaction mode to set how the agent works with you. A small change can use one adequate accepted Markdown contract; a new product can use the full spec, plan, and task stack. In either case, the contract should say what the work must do, what it may change, and how you will recognize a result.

## What's in this tree

- **Framework** defines the fourteen-stage lifecycle, three project profiles, four interaction modes, and the rules for accepted project knowledge.
- **Project System** provides eighteen Markdown skills and twenty templates. The four v0.6 additions are `project-investigator`, `implementation-executor`, `project-verifier`, and `workflow-improver`. They cover read-only code investigation, scoped implementation, observable verification, and evidence-based workflow learning.
- Three optional, standalone Python 3.10+ helpers can observe a PR, check a supported task and receipt format, or inventory local worktrees. They do not accept work, grant merge permission, or decide what to delete. Each has a [manual path](https://github.com/solimancifuentes/buildsolid/blob/v0.6.0/project-system/tools/README.md); none is required to use the framework. PR observation can use an already available authenticated GitHub CLI.
- The [photographer SaaS example](https://github.com/solimancifuentes/buildsolid/blob/v0.6.0/project-system/examples/photographer-saas/README.md) is a synthetic planning case, not a running application. The [execution pilot](https://github.com/solimancifuentes/buildsolid/blob/v0.6.0/project-system/examples/execution-pilot/README.md) contains local CLI, browser, and performance fixtures with deliberate defects for verification practice. Those fixtures do not establish how BuildSolid performs on a production project.

Markdown carries the intent and procedures. The helper scripts and executable examples support particular checks; their output does not replace a reviewed decision or a demonstrated result.

## Releases and limits

BuildSolid is in ongoing feature development. `v0.6.0` is a prerelease, and `v0.5.0` remains available as its own tagged version. For a fixed version, use the matching annotated tag: the accepted release is the commit selected by that tag, not whichever files happen to be on `main` today.

The framework does not promise that a project will ship, pass review, or become effective because its documents are filled in. Verify the actual software and make the material decisions for your project. BuildSolid is offered under the [Apache License 2.0](https://github.com/solimancifuentes/buildsolid/blob/v0.6.0/LICENSE). There are no paid offerings.

Use [GitHub Issues](https://github.com/solimancifuentes/buildsolid/issues) for feedback. External code and content contributions are not accepted at this time; see [Contributing](https://github.com/solimancifuentes/buildsolid/blob/v0.6.0/CONTRIBUTING.md). Report security issues through the repository's private vulnerability-reporting interface, as described in [Security](https://github.com/solimancifuentes/buildsolid/blob/v0.6.0/SECURITY.md).
