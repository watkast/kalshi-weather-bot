# Range-Scalp Bot

*Updated Fri Oct 30 17:00 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 40991 | 35784 | 5207 (53) | 2 | $-11397.82 | -4.4% |
| **+10¢** | 30540 | 24514 | 6026 (76) | 2 | $-10149.08 | -5.3% |
| **+15¢** | 25535 | 19043 | 6492 (103) | 2 | $-9196.22 | -5.7% |
| **+20¢** | 22665 | 15863 | 6802 (133) | 2 | $-8102.08 | -5.7% |
| **+10¢ (15¢ stop)** | 49984 | 49914 | 70 (37) | 0 | $-18924.96 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-30 16:57 | +15 | BNB | UP | 0.52 | 0.88 | 3.34 |
| 10-30 16:57 | +10 | BNB | UP | 0.54 | 0.88 | 3.17 |
| 10-30 16:57 | +10 stop | BNB | UP | 0.57 | 0.26 | -3.46 |
| 10-30 16:54 | +10 stop | BNB | DOWN | 0.60 | 0.41 | -2.24 |
| 10-30 16:53 | +10 stop | SOL | DOWN | 0.66 | 0.81 | 1.23 |
| 10-30 16:53 | +5 | XRP | DOWN | 0.63 | 0.71 | 0.48 |
| 10-30 16:52 | +10 stop | XRP | DOWN | 0.63 | 0.84 | 1.83 |
| 10-30 16:52 | +20 | XRP | DOWN | 0.63 | 0.84 | 1.83 |
| 10-30 16:52 | +15 | XRP | DOWN | 0.63 | 0.84 | 1.83 |
| 10-30 16:52 | +10 | XRP | DOWN | 0.63 | 0.84 | 1.83 |
| 10-30 16:52 | +5 | XRP | DOWN | 0.63 | 0.68 | 0.17 |
| 10-30 16:49 | +10 stop | BNB | DOWN | 0.68 | 0.49 | -2.24 |
| 10-30 16:48 | +5 | BNB | DOWN | 0.70 | 0.83 | 1.05 |
| 10-30 16:46 | +10 stop | BNB | UP | 0.49 | 0.30 | -2.23 |
| 10-30 16:46 | +20 | BNB | UP | 0.49 | 0.88 | 3.64 |
| 10-30 16:46 | +15 | BNB | UP | 0.49 | 0.67 | 1.46 |
| 10-30 16:46 | +10 | BNB | UP | 0.49 | 0.67 | 1.46 |
| 10-30 16:46 | +5 | BNB | UP | 0.49 | 0.58 | 0.54 |
| 10-30 16:45 | +10 stop | ZEC | UP | 0.54 | 0.34 | -2.34 |
| 10-30 16:45 | +20 | ZEC | UP | 0.54 | open |  |
| 10-30 16:45 | +15 | ZEC | UP | 0.54 | open |  |
| 10-30 16:45 | +10 | ZEC | UP | 0.55 | open |  |
| 10-30 16:45 | +5 | ZEC | UP | 0.55 | open |  |
| 10-30 16:45 | +10 stop | SOL | UP | 0.55 | 0.26 | -3.22 |
| 10-30 16:45 | +20 | SOL | UP | 0.55 | open |  |
| 10-30 16:45 | +15 | SOL | UP | 0.55 | open |  |
| 10-30 16:45 | +10 | SOL | UP | 0.55 | open |  |
| 10-30 16:45 | +5 | SOL | UP | 0.55 | open |  |
| 10-30 16:43 | +10 stop | ZEC | UP | 0.26 | 0.53 | 2.38 |
| 10-30 16:41 | +10 stop | ETH | UP | 0.41 | 0.54 | 0.95 |
| 10-30 16:41 | +10 stop | SOL | DOWN | 0.71 | 0.83 | 0.95 |
| 10-30 16:41 | +20 | SOL | DOWN | 0.71 | 0.92 | 1.94 |
| 10-30 16:41 | +10 stop | BNB | UP | 0.67 | 0.47 | -2.34 |
| 10-30 16:40 | +10 stop | ETH | DOWN | 0.66 | 0.43 | -2.63 |
| 10-30 16:40 | +20 | ETH | DOWN | 0.65 | 0.89 | 2.17 |
| 10-30 16:40 | +15 | ETH | DOWN | 0.65 | 0.89 | 2.17 |
| 10-30 16:40 | +10 | ETH | DOWN | 0.65 | 0.75 | 0.70 |
| 10-30 16:40 | +5 | ETH | DOWN | 0.65 | 0.75 | 0.70 |
| 10-30 16:40 | +15 | SOL | DOWN | 0.70 | 0.92 | 2.04 |
| 10-30 16:40 | +10 | SOL | DOWN | 0.70 | 0.83 | 1.05 |
