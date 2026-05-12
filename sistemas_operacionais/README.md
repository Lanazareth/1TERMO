# 🛡️ Aula: Segurança em Sistemas Operacionais
**Tópico:** Segurança Cibernética no Windows vs. Linux

---

## 1. Introdução à Segurança Cibernética em SO
A segurança em um Sistema Operacional (SO) visa proteger a tríade **CIDs**:
*   **Confidencialidade:** Acesso apenas por pessoas autorizadas.
*   **Integridade:** Garantia de que a informação não foi alterada indevidamente.
*   **Disponibilidade:** O sistema deve estar funcional quando necessário.

---

## 2. Segurança no Microsoft Windows
O Windows utiliza uma abordagem de segurança voltada tanto para o usuário doméstico quanto para ambientes corporativos (Active Directory).

### Principais Mecanismos:
*   **UAC (User Account Control):** Impede que aplicativos façam alterações indesejadas sem permissão do administrador.
*   **Windows Defender:** Sistema nativo que combina antivírus, firewall e proteção contra ransomware.
*   **BitLocker:** Criptografia de unidade para proteger dados em caso de roubo físico do dispositivo.
*   **Kernel Patch Protection:** Impede que softwares maliciosos (rootkits) modifiquem o núcleo do sistema.

### Pontos de Atenção:
*   Maior base de usuários = Maior volume de malwares desenvolvidos.
*   Histórico de retrocompatibilidade que pode manter protocolos antigos vulneráveis.

---

## 3. Segurança no GNU/Linux
O Linux é construído sobre o conceito de múltiplos usuários e permissões rígidas desde o núcleo (Kernel).

### Principais Mecanismos:
*   **Modelo de Permissões POSIX:** Gerenciamento granular de quem pode Ler (`r`), Escrever (`w`) e Executar (`x`) arquivos.
*   **Privilégio Mínimo (sudo):** O usuário comum não tem poder de sistema; o acesso administrativo é temporário e auditado.
*   **Repositórios Oficiais:** A instalação de software via gerenciadores de pacotes (`apt`, `dnf`) reduz o risco de baixar binários maliciosos da web.
*   **Módulos de Segurança (LSM):** Ferramentas como **SELinux** e **AppArmor** criam "muros" ao redor de aplicativos específicos.

### Pontos de Atenção:
*   A segurança depende muito da configuração correta feita pelo administrador (SysAdmin).
*   A visibilidade do código fonte (Open Source) permite auditorias públicas de falhas.

---

## 4. Comparativo Direto: Segurança



| Recurso | Microsoft Windows | GNU/Linux |
| :--- | :--- | :--- |
| **Padrão de Usuário** | Muitas vezes logado como Admin | Usuário comum (Sudo para admin) |
| **Vetor de Ataque** | Arquivos executáveis (.exe, .msi) | Serviços de rede e scripts |
| **Atualizações** | Centralizadas via Windows Update | Via Repositórios/Gerenciador de Pacotes |
| **Filosofia** | Facilidade de uso e automação | Controle total e transparência |

---

## 5. Melhores Práticas Gerais (Independente do SO)
1.  **Princípio do Privilégio Mínimo:** Nunca use a conta de administrador para tarefas diárias.
2.  **Atualização de Patches:** Manter o Kernel e os softwares sempre na última versão.
3.  **Segurança de Rede:** Utilizar Firewalls configurados (ex: `ufw` no Linux ou Windows Firewall).
4.  **Logs e Auditoria:** Monitorar registros de eventos para detectar comportamentos anômalos.
