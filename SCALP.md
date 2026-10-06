# Range-Scalp Bot

*Updated Tue Oct 06 11:43 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 5019 | 4344 | 675 (7) | 2 | $-1580.39 | -5.0% |
| **+10¢** | 3851 | 3065 | 786 (11) | 2 | $-1446.06 | -6.0% |
| **+15¢** | 3235 | 2402 | 833 (14) | 2 | $-1246.26 | -6.1% |
| **+20¢** | 2900 | 2031 | 869 (19) | 2 | $-1019.49 | -5.6% |
| **+10¢ (15¢ stop)** | 6142 | 6129 | 13 (8) | 0 | $-2190.97 | -5.7% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-06 11:42 | +10 stop | DOGE | DOWN | 0.58 | 0.89 | 2.85 |
| 10-06 11:41 | +10 stop | XRP | UP | 0.70 | 0.55 | -1.85 |
| 10-06 11:41 | +5 | XRP | UP | 0.70 | open |  |
| 10-06 11:38 | +10 stop | SOL | UP | 0.55 | 0.70 | 1.17 |
| 10-06 11:38 | +10 stop | BNB | UP | 0.60 | 0.75 | 1.19 |
| 10-06 11:38 | +10 stop | XRP | UP | 0.58 | 0.68 | 0.66 |
| 10-06 11:38 | +10 stop | DOGE | DOWN | 0.65 | 0.47 | -2.14 |
| 10-06 11:38 | +20 | DOGE | DOWN | 0.65 | 0.89 | 2.17 |
| 10-06 11:38 | +15 | DOGE | DOWN | 0.65 | 0.89 | 2.17 |
| 10-06 11:38 | +10 | DOGE | DOWN | 0.65 | 0.89 | 2.17 |
| 10-06 11:38 | +5 | DOGE | DOWN | 0.65 | 0.89 | 2.17 |
| 10-06 11:37 | +10 stop | HYPE | UP | 0.67 | 0.84 | 1.40 |
| 10-06 11:37 | +10 stop | BNB | DOWN | 0.54 | 0.67 | 0.96 |
| 10-06 11:37 | +10 stop | HYPE | DOWN | 0.43 | 0.57 | 1.04 |
| 10-06 11:35 | +10 stop | ETH | UP | 0.71 | 0.51 | -2.33 |
| 10-06 11:35 | +10 | ETH | UP | 0.71 | 0.83 | 0.95 |
| 10-06 11:35 | +5 | ETH | UP | 0.71 | 0.77 | 0.32 |
| 10-06 11:34 | +10 stop | SOL | UP | 0.61 | 0.39 | -2.54 |
| 10-06 11:34 | +10 | SOL | UP | 0.61 | 0.76 | 1.20 |
| 10-06 11:34 | +5 | SOL | UP | 0.61 | 0.70 | 0.58 |
| 10-06 11:34 | +10 stop | XRP | DOWN | 0.55 | 0.66 | 0.76 |
| 10-06 11:33 | +10 stop | BNB | UP | 0.68 | 0.49 | -2.28 |
| 10-06 11:33 | +10 | BNB | UP | 0.68 | 0.88 | 1.72 |
| 10-06 11:33 | +5 | BNB | UP | 0.68 | 0.75 | 0.36 |
| 10-06 11:33 | +10 stop | HYPE | DOWN | 0.66 | 0.47 | -2.24 |
| 10-06 11:33 | +20 | HYPE | DOWN | 0.66 | open |  |
| 10-06 11:33 | +15 | HYPE | DOWN | 0.66 | open |  |
| 10-06 11:33 | +10 | HYPE | DOWN | 0.66 | open |  |
| 10-06 11:33 | +5 | HYPE | DOWN | 0.66 | open |  |
| 10-06 11:33 | +5 | SOL | UP | 0.69 | 0.74 | 0.21 |
| 10-06 11:32 | +5 | ETH | UP | 0.68 | 0.76 | 0.51 |
| 10-06 11:32 | +5 | SOL | UP | 0.62 | 0.68 | 0.27 |
| 10-06 11:32 | +5 | DOGE | DOWN | 0.67 | 0.74 | 0.40 |
| 10-06 11:32 | +10 stop | BNB | UP | 0.54 | 0.68 | 1.06 |
| 10-06 11:32 | +20 | BNB | UP | 0.55 | 0.75 | 1.68 |
| 10-06 11:32 | +15 | BNB | UP | 0.55 | 0.75 | 1.68 |
| 10-06 11:32 | +10 | BNB | UP | 0.55 | 0.68 | 0.96 |
| 10-06 11:32 | +5 | BNB | UP | 0.55 | 0.68 | 0.96 |
| 10-06 11:32 | +5 | SOL | UP | 0.61 | 0.66 | 0.17 |
| 10-06 11:31 | +10 stop | ZEC | UP | 0.69 | 0.79 | 0.73 |
