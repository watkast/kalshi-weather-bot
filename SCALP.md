# Range-Scalp Bot

*Updated Sat Nov 07 22:22 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 51599 | 44987 | 6612 (80) | 0 | $-14339.39 | -4.4% |
| **+10¢** | 38502 | 30791 | 7711 (106) | 0 | $-13370.49 | -5.5% |
| **+15¢** | 32240 | 23929 | 8311 (135) | 0 | $-12281.30 | -6.1% |
| **+20¢** | 28676 | 19965 | 8711 (178) | 1 | $-10846.07 | -6.0% |
| **+10¢ (15¢ stop)** | 62835 | 62732 | 103 (61) | 0 | $-23272.72 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-07 22:17 | +10 stop | BNB | UP | 0.70 | 0.81 | 0.80 |
| 11-07 22:17 | +20 | BNB | UP | 0.70 | open |  |
| 11-07 22:17 | +15 | BNB | UP | 0.70 | 0.89 | 1.64 |
| 11-07 22:17 | +10 | BNB | UP | 0.70 | 0.81 | 0.80 |
| 11-07 22:17 | +5 | BNB | UP | 0.70 | 0.79 | 0.59 |
| 11-07 22:17 | +10 stop | BTC | UP | 0.66 | 0.76 | 0.71 |
| 11-07 22:17 | +20 | BTC | UP | 0.66 | 0.86 | 1.75 |
| 11-07 22:17 | +15 | BTC | UP | 0.66 | 0.82 | 1.33 |
| 11-07 22:17 | +10 | BTC | UP | 0.66 | 0.76 | 0.71 |
| 11-07 22:17 | +5 | BTC | UP | 0.66 | 0.72 | 0.29 |
| 11-07 22:16 | +10 stop | ETH | UP | 0.69 | 0.83 | 1.15 |
| 11-07 22:16 | +20 | ETH | UP | 0.69 | 0.91 | 1.96 |
| 11-07 22:16 | +15 | ETH | UP | 0.69 | 0.85 | 1.36 |
| 11-07 22:16 | +10 | ETH | UP | 0.69 | 0.83 | 1.15 |
| 11-07 22:16 | +5 | ETH | UP | 0.69 | 0.76 | 0.42 |
| 11-07 22:16 | +10 stop | HYPE | UP | 0.68 | 0.87 | 1.66 |
| 11-07 22:16 | +20 | HYPE | UP | 0.68 | 0.89 | 1.87 |
| 11-07 22:16 | +15 | HYPE | UP | 0.68 | 0.87 | 1.66 |
| 11-07 22:16 | +10 | HYPE | UP | 0.68 | 0.87 | 1.66 |
| 11-07 22:16 | +5 | HYPE | UP | 0.68 | 0.87 | 1.66 |
| 11-07 22:13 | +10 stop | BNB | DOWN | 0.10 | 0.44 | 3.15 |
| 11-07 22:11 | +10 stop | BNB | UP | 0.64 | 0.34 | -3.33 |
| 11-07 22:10 | +10 stop | BNB | DOWN | 0.66 | 0.38 | -3.08 |
| 11-07 22:10 | +20 | BNB | DOWN | 0.66 | yes | -6.71 |
| 11-07 22:10 | +15 | BNB | DOWN | 0.66 | yes | -6.71 |
| 11-07 22:10 | +10 | BNB | DOWN | 0.66 | yes | -6.71 |
| 11-07 22:10 | +5 | BNB | DOWN | 0.66 | yes | -6.71 |
| 11-07 22:08 | +10 stop | BTC | DOWN | 0.57 | 0.68 | 0.76 |
| 11-07 22:07 | +10 stop | NEAR | UP | 0.54 | 0.37 | -2.05 |
| 11-07 22:07 | +15 | NEAR | UP | 0.54 | no | -5.58 |
| 11-07 22:07 | +10 | NEAR | UP | 0.54 | no | -5.58 |
| 11-07 22:07 | +5 | NEAR | UP | 0.54 | no | -5.58 |
| 11-07 22:06 | +10 stop | XRP | UP | 0.55 | 0.23 | -3.51 |
| 11-07 22:06 | +5 | BTC | UP | 0.66 | no | -6.76 |
| 11-07 22:05 | +10 stop | HYPE | DOWN | 0.67 | 0.79 | 0.92 |
| 11-07 22:05 | +10 stop | XRP | UP | 0.44 | 0.57 | 0.94 |
| 11-07 22:05 | +10 stop | BTC | UP | 0.60 | 0.44 | -1.95 |
| 11-07 22:05 | +5 | BTC | UP | 0.60 | 0.65 | 0.17 |
| 11-07 22:05 | +10 stop | SOL | UP | 0.52 | 0.34 | -2.14 |
| 11-07 22:04 | +10 stop | ETH | DOWN | 0.63 | 0.44 | -2.25 |
