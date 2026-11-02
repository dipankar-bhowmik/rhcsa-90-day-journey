# RHCSA 90-Day Journey

A public log of my 90-day plan to go from IT support to Linux system administration, ending with the Red Hat RHCSA (EX200, RHEL 10) exam. Started 1 November 2026.

Every day is one realistic ticket (create a user, extend an LVM volume, fix an SELinux denial), done on my own lab VMs, with the commands, proof it works, what I broke on purpose, and a runbook note.

## Progress
<!-- PROGRESS:START -->
**2 of 90 days done, 4.5 hours logged.**

| Day | Date | Status | Hours | Topic |
| --- | --- | --- | --- | --- |
| [1](days/day-001.md) | 2026-11-01 | done | 3 | Day 1: Onboarding: build your two lab servers |
| [2](days/day-002.md) | 2026-11-02 | done | 1.5 | Day 2: "Get to know this server" |
<!-- PROGRESS:END -->

## What is in here
| Folder | Contents |
| --- | --- |
| `days/` | One note per day: ticket, commands, verification, mistakes |
| `weeks/` | Weekly reviews: what I redid from scratch, weak spots |
| `runbooks/` | Reusable how-to guides with verify and rollback steps |
| `scripts/` | Shell scripts I wrote (health report, user creation, service watchdog) |
| `mocks/` | Timed mock exam results and what I fixed afterwards |

## Skills practised
Users and permissions, ACLs, dnf/RPM and Flatpak, systemd, journald, networking with nmcli, SSH keys, firewalld, SELinux, LVM, XFS/ext4, NFS and autofs, GRUB2 and boot recovery, bash scripting, cron, chrony.

## Lab
Two RHEL 10 VMs (server1, server2), terminal only. No real company data, passwords or keys are stored in this repo.

## How I work
- Type every command, no copy-paste; use only `man` for help.
- Every change must survive a reboot.
- Review day each week: redo the week without notes, timed.
- Mock exams from Day 77, results in `mocks/`.

## About me
Dipankar Bhowmik, IT infrastructure and network support, Kolkata. Aiming at Linux, cloud and DevOps roles.
