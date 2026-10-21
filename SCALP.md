# Range-Scalp Bot

*Updated Wed Oct 21 23:24 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 27885 | 24295 | 3590 (39) | 2 | $-8027.07 | -4.6% |
| **+10¢** | 20955 | 16809 | 4146 (55) | 2 | $-7065.07 | -5.4% |
| **+15¢** | 17551 | 13088 | 4463 (78) | 2 | $-6305.86 | -5.7% |
| **+20¢** | 15540 | 10863 | 4677 (98) | 2 | $-5634.80 | -5.8% |
| **+10¢ (15¢ stop)** | 34229 | 34170 | 59 (32) | 1 | $-12745.52 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-21 23:24 | +10 stop | BTC | DOWN | 0.60 | open |  |
| 10-21 23:24 | +5 | BTC | DOWN | 0.60 | open |  |
| 10-21 23:23 | +10 stop | BTC | DOWN | 0.69 | 0.52 | -2.03 |
| 10-21 23:21 | +5 | XRP | DOWN | 0.70 | 0.81 | 0.84 |
| 10-21 23:21 | +10 stop | BNB | DOWN | 0.61 | 0.71 | 0.68 |
| 10-21 23:20 | +10 stop | HYPE | DOWN | 0.67 | 0.78 | 0.77 |
| 10-21 23:20 | +20 | HYPE | DOWN | 0.67 | 0.89 | 1.97 |
| 10-21 23:20 | +10 | HYPE | DOWN | 0.67 | 0.78 | 0.81 |
| 10-21 23:20 | +5 | HYPE | DOWN | 0.67 | 0.76 | 0.61 |
| 10-21 23:20 | +10 stop | XRP | DOWN | 0.61 | 0.74 | 0.99 |
| 10-21 23:20 | +20 | XRP | DOWN | 0.61 | 0.81 | 1.72 |
| 10-21 23:20 | +15 | XRP | DOWN | 0.61 | 0.81 | 1.72 |
| 10-21 23:20 | +10 | XRP | DOWN | 0.61 | 0.74 | 0.99 |
| 10-21 23:20 | +5 | XRP | DOWN | 0.61 | 0.69 | 0.48 |
| 10-21 23:20 | +10 stop | BTC | UP | 0.69 | 0.51 | -2.13 |
| 10-21 23:20 | +10 stop | DOGE | DOWN | 0.65 | 0.76 | 0.81 |
| 10-21 23:20 | +15 | DOGE | DOWN | 0.65 | 0.85 | 1.75 |
| 10-21 23:20 | +10 | DOGE | DOWN | 0.65 | 0.76 | 0.81 |
| 10-21 23:20 | +5 | DOGE | DOWN | 0.65 | 0.76 | 0.81 |
| 10-21 23:20 | +10 stop | ETH | DOWN | 0.67 | 0.78 | 0.81 |
| 10-21 23:20 | +15 | ETH | DOWN | 0.67 | 0.83 | 1.34 |
| 10-21 23:20 | +10 | ETH | DOWN | 0.67 | 0.78 | 0.81 |
| 10-21 23:20 | +5 | ETH | DOWN | 0.67 | 0.76 | 0.61 |
| 10-21 23:20 | +10 stop | SOL | DOWN | 0.59 | 0.74 | 1.19 |
| 10-21 23:20 | +20 | SOL | DOWN | 0.59 | 0.81 | 1.92 |
| 10-21 23:20 | +15 | SOL | DOWN | 0.59 | 0.74 | 1.19 |
| 10-21 23:20 | +10 | SOL | DOWN | 0.59 | 0.74 | 1.19 |
| 10-21 23:20 | +5 | SOL | DOWN | 0.59 | 0.74 | 1.19 |
| 10-21 23:19 | +10 stop | BNB | DOWN | 0.70 | 0.47 | -2.63 |
| 10-21 23:17 | +5 | ETH | DOWN | 0.70 | 0.78 | 0.52 |
| 10-21 23:17 | +10 stop | BTC | DOWN | 0.65 | 0.38 | -3.03 |
| 10-21 23:17 | +20 | BTC | DOWN | 0.65 | open |  |
| 10-21 23:17 | +15 | BTC | DOWN | 0.65 | open |  |
| 10-21 23:17 | +10 | BTC | DOWN | 0.65 | open |  |
| 10-21 23:17 | +5 | BTC | DOWN | 0.65 | 0.70 | 0.19 |
| 10-21 23:16 | +10 stop | BNB | DOWN | 0.58 | 0.71 | 0.97 |
| 10-21 23:16 | +10 stop | DOGE | DOWN | 0.66 | 0.76 | 0.71 |
| 10-21 23:16 | +20 | DOGE | DOWN | 0.66 | 0.91 | 2.24 |
| 10-21 23:16 | +15 | DOGE | DOWN | 0.66 | 0.83 | 1.44 |
| 10-21 23:16 | +10 | DOGE | DOWN | 0.66 | 0.76 | 0.71 |
