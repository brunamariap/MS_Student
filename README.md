# Comandos para executar teste de mutação
- cosmic-ray init cosmic_ray_config.toml cosmic_ray.sqlite (caso não tenha o banco SQLite)
- cosmic-ray exec cosmic_ray_config.toml cosmic_ray.sqlite
- cr-report cosmic_ray.sqlite --show-pending
- cr-html cosmic_ray.sqlite > report.html