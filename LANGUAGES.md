# Global Language Codes Registry

This file acts as the single source of truth for language codes used across all game directories. Every python generator must align with these codes.

## Registered Languages

| Code | Language Name (Local) | Language Name (English) | Notes                     |
| :--- | :-------------------- | :---------------------- | :------------------------ |
| `en` | English               | English                 | Default fallback language |
| `pl` | Polski                | Polish                  | Full support              |

## Registering a New Language
If you wish to add support for a language not listed here:
1. Select the standard two-letter ISO 639-1 code for the language.
2. Submit a Pull Request updating this registry file.
3. Use this exact identifier when adding translation JSON files to game directories (e.g., `lang/es.json` for Spanish).