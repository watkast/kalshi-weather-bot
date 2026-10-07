# Range-Scalp Bot

*Updated Wed Oct 07 09:57 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 6225 | 5406 | 819 (9) | 5 | $-1857.12 | -4.7% |
| **+10¢** | 4744 | 3780 | 964 (16) | 6 | $-1736.61 | -5.8% |
| **+15¢** | 3983 | 2963 | 1020 (20) | 6 | $-1470.35 | -5.9% |
| **+20¢** | 3565 | 2500 | 1065 (27) | 6 | $-1180.12 | -5.3% |
| **+10¢ (15¢ stop)** | 7552 | 7537 | 15 (9) | 0 | $-2623.32 | -5.5% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-07 09:55 | +10 stop | DOGE | DOWN | 0.66 | 0.87 | 1.86 |
| 10-07 09:55 | +10 | DOGE | DOWN | 0.65 | 0.87 | 1.96 |
| 10-07 09:55 | +5 | DOGE | DOWN | 0.65 | 0.70 | 0.19 |
| 10-07 09:54 | +10 stop | HYPE | DOWN | 0.52 | 0.66 | 1.06 |
| 10-07 09:53 | +10 stop | BTC | DOWN | 0.62 | 0.47 | -1.85 |
| 10-07 09:53 | +10 stop | ETH | DOWN | 0.70 | 0.81 | 0.84 |
| 10-07 09:52 | +10 stop | HYPE | UP | 0.62 | 0.40 | -2.54 |
| 10-07 09:52 | +10 stop | XRP | UP | 0.63 | 0.48 | -1.85 |
| 10-07 09:52 | +20 | XRP | UP | 0.63 | 0.87 | 2.15 |
| 10-07 09:52 | +15 | XRP | UP | 0.63 | 0.87 | 2.15 |
| 10-07 09:52 | +10 | XRP | UP | 0.63 | 0.77 | 1.10 |
| 10-07 09:52 | +5 | XRP | UP | 0.63 | 0.77 | 1.10 |
| 10-07 09:52 | +20 | BTC | UP | 0.61 | open |  |
| 10-07 09:52 | +15 | BTC | UP | 0.61 | open |  |
| 10-07 09:52 | +5 | BTC | UP | 0.61 | open |  |
| 10-07 09:52 | +10 stop | DOGE | DOWN | 0.66 | 0.77 | 0.81 |
| 10-07 09:52 | +20 | DOGE | DOWN | 0.66 | 0.87 | 1.86 |
| 10-07 09:52 | +15 | DOGE | DOWN | 0.65 | 0.87 | 1.96 |
| 10-07 09:52 | +10 | DOGE | DOWN | 0.65 | 0.77 | 0.91 |
| 10-07 09:52 | +5 | DOGE | DOWN | 0.65 | 0.72 | 0.39 |
| 10-07 09:50 | +10 stop | BNB | UP | 0.56 | 0.35 | -2.44 |
| 10-07 09:49 | +10 stop | BTC | UP | 0.70 | 0.47 | -2.63 |
| 10-07 09:49 | +10 | BTC | UP | 0.70 | open |  |
| 10-07 09:49 | +5 | ETH | UP | 0.69 | open |  |
| 10-07 09:49 | +10 stop | ETH | UP | 0.70 | 0.55 | -1.83 |
| 10-07 09:49 | +5 | BTC | UP | 0.66 | 0.74 | 0.50 |
| 10-07 09:49 | +5 | XRP | UP | 0.69 | 0.75 | 0.30 |
| 10-07 09:48 | +10 stop | HYPE | DOWN | 0.57 | 0.29 | -3.17 |
| 10-07 09:48 | +10 | HYPE | DOWN | 0.57 | 0.70 | 0.93 |
| 10-07 09:48 | +10 stop | BNB | DOWN | 0.56 | 0.41 | -1.85 |
| 10-07 09:48 | +5 | HYPE | DOWN | 0.70 | 0.78 | 0.52 |
| 10-07 09:47 | +10 stop | DOGE | DOWN | 0.52 | 0.30 | -2.53 |
| 10-07 09:47 | +10 stop | SOL | DOWN | 0.60 | 0.76 | 1.30 |
| 10-07 09:47 | +10 stop | BNB | UP | 0.56 | 0.37 | -2.22 |
| 10-07 09:47 | +10 | BNB | UP | 0.56 | open |  |
| 10-07 09:47 | +5 | BNB | UP | 0.56 | open |  |
| 10-07 09:47 | +10 stop | HYPE | DOWN | 0.62 | 0.73 | 0.79 |
| 10-07 09:47 | +20 | HYPE | DOWN | 0.62 | 0.84 | 1.93 |
| 10-07 09:47 | +15 | HYPE | DOWN | 0.62 | 0.78 | 1.30 |
| 10-07 09:47 | +10 | HYPE | DOWN | 0.62 | 0.73 | 0.79 |
