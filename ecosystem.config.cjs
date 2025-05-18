module.exports = {
  apps: [
    {
      cmd: 'talkops',
      name: 'client',
    },
    {
      autorestart: true,
      error_file: process.env.TALKOPS_STDERR,
      ignore_watch: [
        '.git',
        '.github',
        '.gitignore',
        'Dockerfile',
        'ecosystem.config.cjs',
        'LICENSE',
        'manifest.json',
        'README.md',
      ],
      name: 'extension',
      out_file: process.env.TALKOPS_STDOUT,
      script: 'src/main.py',
      watch: true,
    },
  ],
}
