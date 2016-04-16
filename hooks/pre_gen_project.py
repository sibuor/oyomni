#Protect from bad (non-importable) repo names, like those with dashes

repo_name = '{{ cookiecutter.repo_name }}'

if hasattr(repo_name, 'isidentifier'):
    assert repo_name.isidentifier(), 'Repo name should be valid Python identifier!'
