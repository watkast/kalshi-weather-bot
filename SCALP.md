# Range-Scalp Bot

*Updated Mon Nov 09 11:14 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 53580 | 46725 | 6855 (86) | 0 | $-14723.86 | -4.4% |
| **+10¢** | 40027 | 32032 | 7995 (112) | 1 | $-13704.28 | -5.4% |
| **+15¢** | 33540 | 24924 | 8616 (143) | 1 | $-12504.22 | -5.9% |
| **+20¢** | 29846 | 20808 | 9038 (189) | 1 | $-10998.11 | -5.9% |
| **+10¢ (15¢ stop)** | 65296 | 65190 | 106 (63) | 0 | $-24169.95 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-09 11:14 | +10 stop | BNB | DOWN | 0.60 | 0.84 | 2.13 |
| 11-09 11:14 | +20 | BNB | DOWN | 0.61 | 0.84 | 2.03 |
| 11-09 11:14 | +15 | BNB | DOWN | 0.64 | 0.84 | 1.73 |
| 11-09 11:14 | +10 | BNB | DOWN | 0.64 | 0.84 | 1.73 |
| 11-09 11:14 | +5 | BNB | DOWN | 0.64 | 0.84 | 1.73 |
| 11-09 11:13 | +10 stop | ETH | DOWN | 0.71 | 0.89 | 1.58 |
| 11-09 11:13 | +15 | ETH | DOWN | 0.70 | 0.89 | 1.68 |
| 11-09 11:13 | +10 | ETH | DOWN | 0.70 | 0.89 | 1.68 |
| 11-09 11:13 | +5 | ETH | DOWN | 0.70 | 0.89 | 1.68 |
| 11-09 11:11 | +10 | SOL | DOWN | 0.70 | 0.91 | 1.86 |
| 11-09 11:10 | +10 stop | BTC | DOWN | 0.69 | 0.80 | 0.83 |
| 11-09 11:10 | +20 | BTC | DOWN | 0.69 | 0.92 | 2.14 |
| 11-09 11:10 | +15 | BTC | DOWN | 0.69 | 0.87 | 1.57 |
| 11-09 11:10 | +10 | BTC | DOWN | 0.69 | 0.80 | 0.83 |
| 11-09 11:10 | +5 | BTC | DOWN | 0.69 | 0.80 | 0.83 |
| 11-09 11:10 | +10 stop | ETH | DOWN | 0.62 | 0.75 | 0.99 |
| 11-09 11:10 | +15 | ETH | DOWN | 0.62 | 0.85 | 2.04 |
| 11-09 11:10 | +10 | ETH | DOWN | 0.62 | 0.75 | 0.99 |
| 11-09 11:10 | +5 | ETH | DOWN | 0.62 | 0.75 | 0.99 |
| 11-09 11:10 | +5 | SOL | UP | 0.52 | 0.89 | 3.45 |
| 11-09 11:09 | +10 stop | NEAR | UP | 0.71 | 0.91 | 1.76 |
| 11-09 11:09 | +5 | NEAR | UP | 0.71 | 0.91 | 1.76 |
| 11-09 11:09 | +10 stop | SOL | DOWN | 0.53 | 0.65 | 0.86 |
| 11-09 11:09 | +15 | SOL | DOWN | 0.53 | 0.71 | 1.47 |
| 11-09 11:09 | +10 | SOL | DOWN | 0.52 | 0.65 | 0.96 |
| 11-09 11:09 | +5 | SOL | DOWN | 0.52 | 0.60 | 0.45 |
| 11-09 11:09 | +10 stop | NEAR | DOWN | 0.53 | 0.63 | 0.65 |
| 11-09 11:09 | +5 | NEAR | DOWN | 0.53 | 0.63 | 0.65 |
| 11-09 11:07 | +10 stop | BTC | DOWN | 0.67 | 0.85 | 1.55 |
| 11-09 11:07 | +15 | BTC | DOWN | 0.67 | 0.85 | 1.55 |
| 11-09 11:07 | +10 | BTC | DOWN | 0.67 | 0.85 | 1.55 |
| 11-09 11:07 | +5 | BTC | DOWN | 0.67 | 0.76 | 0.61 |
| 11-09 11:06 | +10 stop | BNB | DOWN | 0.53 | 0.69 | 1.27 |
| 11-09 11:05 | +5 | SOL | DOWN | 0.68 | 0.77 | 0.61 |
| 11-09 11:05 | +10 stop | BNB | DOWN | 0.49 | 0.60 | 0.75 |
| 11-09 11:05 | +10 stop | ETH | DOWN | 0.67 | 0.85 | 1.55 |
| 11-09 11:04 | +10 stop | SOL | DOWN | 0.63 | 0.77 | 1.10 |
| 11-09 11:04 | +20 | SOL | DOWN | 0.63 | 0.91 | 2.54 |
| 11-09 11:04 | +15 | SOL | DOWN | 0.63 | 0.78 | 1.20 |
| 11-09 11:04 | +10 | SOL | DOWN | 0.63 | 0.77 | 1.10 |
