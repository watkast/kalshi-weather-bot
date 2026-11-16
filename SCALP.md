# Range-Scalp Bot

*Updated Mon Nov 16 19:09 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 62113 | 54196 | 7917 (117) | 0 | $-16751.85 | -4.3% |
| **+10¢** | 46386 | 37122 | 9264 (159) | 0 | $-15613.45 | -5.4% |
| **+15¢** | 38868 | 28874 | 9994 (200) | 0 | $-14210.86 | -5.8% |
| **+20¢** | 34649 | 24170 | 10479 (255) | 1 | $-12368.45 | -5.7% |
| **+10¢ (15¢ stop)** | 75586 | 75430 | 156 (92) | 0 | $-27864.74 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-16 19:03 | +5 | BTC | DOWN | 0.66 | 0.74 | 0.50 |
| 11-16 19:02 | +10 stop | BNB | DOWN | 0.67 | 0.77 | 0.71 |
| 11-16 19:02 | +20 | BNB | DOWN | 0.67 | 0.90 | 2.07 |
| 11-16 19:02 | +15 | BNB | DOWN | 0.67 | 0.82 | 1.23 |
| 11-16 19:02 | +10 | BNB | DOWN | 0.67 | 0.77 | 0.71 |
| 11-16 19:02 | +5 | BNB | DOWN | 0.67 | 0.72 | 0.19 |
| 11-16 19:01 | +10 stop | HYPE | DOWN | 0.70 | 0.84 | 1.15 |
| 11-16 19:01 | +20 | HYPE | DOWN | 0.69 | open |  |
| 11-16 19:01 | +15 | HYPE | DOWN | 0.69 | 0.84 | 1.25 |
| 11-16 19:01 | +10 | HYPE | DOWN | 0.69 | 0.79 | 0.73 |
| 11-16 19:01 | +5 | HYPE | DOWN | 0.69 | 0.75 | 0.31 |
| 11-16 19:01 | +10 stop | ETH | DOWN | 0.70 | 0.84 | 1.15 |
| 11-16 19:01 | +20 | ETH | DOWN | 0.70 | 0.95 | 2.28 |
| 11-16 19:01 | +15 | ETH | DOWN | 0.70 | 0.86 | 1.36 |
| 11-16 19:01 | +10 | ETH | DOWN | 0.70 | 0.84 | 1.15 |
| 11-16 19:01 | +5 | ETH | DOWN | 0.70 | 0.78 | 0.52 |
| 11-16 19:00 | +10 stop | BTC | DOWN | 0.65 | 0.76 | 0.81 |
| 11-16 19:00 | +20 | BTC | DOWN | 0.65 | 0.90 | 2.27 |
| 11-16 19:00 | +15 | BTC | DOWN | 0.65 | 0.80 | 1.22 |
| 11-16 19:00 | +10 | BTC | DOWN | 0.65 | 0.76 | 0.81 |
| 11-16 19:00 | +5 | BTC | DOWN | 0.65 | 0.71 | 0.29 |
| 11-16 12:49 | +5 | BNB | DOWN | 0.71 | 0.81 | 0.74 |
| 11-16 12:49 | +10 stop | BTC | DOWN | 0.65 | 0.76 | 0.81 |
| 11-16 12:49 | +20 | BTC | DOWN | 0.65 | no | 3.34 |
| 11-16 12:49 | +15 | BTC | DOWN | 0.65 | no | 3.34 |
| 11-16 12:49 | +10 | BTC | DOWN | 0.65 | 0.76 | 0.81 |
| 11-16 12:49 | +5 | BTC | DOWN | 0.65 | 0.74 | 0.60 |
| 11-16 12:49 | +10 stop | SOL | DOWN | 0.67 | 0.77 | 0.71 |
| 11-16 12:49 | +10 | SOL | DOWN | 0.67 | 0.77 | 0.71 |
| 11-16 12:49 | +5 | SOL | DOWN | 0.67 | 0.77 | 0.71 |
| 11-16 12:48 | +15 | HYPE | DOWN | 0.67 | no | 3.14 |
| 11-16 12:48 | +5 | ETH | DOWN | 0.71 | no | 2.75 |
| 11-16 12:48 | +10 stop | HYPE | DOWN | 0.66 | no | 3.24 |
| 11-16 12:48 | +10 | HYPE | DOWN | 0.66 | no | 3.24 |
| 11-16 12:48 | +5 | HYPE | DOWN | 0.65 | no | 3.34 |
| 11-16 12:47 | +5 | DOGE | DOWN | 0.69 | 0.74 | 0.21 |
| 11-16 12:47 | +5 | DOGE | DOWN | 0.64 | 0.69 | 0.18 |
| 11-16 12:47 | +10 stop | HYPE | DOWN | 0.52 | 0.64 | 0.85 |
| 11-16 12:47 | +20 | HYPE | DOWN | 0.52 | no | 4.62 |
| 11-16 12:47 | +15 | HYPE | DOWN | 0.52 | 0.67 | 1.16 |
