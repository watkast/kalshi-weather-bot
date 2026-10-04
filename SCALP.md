# Range-Scalp Bot

*Updated Sun Oct 04 09:41 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 2076 | 1791 | 285 (3) | 3 | $-696.31 | -5.3% |
| **+10¢** | 1616 | 1300 | 316 (4) | 3 | $-504.21 | -4.9% |
| **+15¢** | 1360 | 1025 | 335 (5) | 4 | $-427.39 | -5.0% |
| **+20¢** | 1200 | 848 | 352 (7) | 4 | $-379.76 | -5.0% |
| **+10¢ (15¢ stop)** | 2583 | 2582 | 1 (1) | 2 | $-982.18 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-04 09:41 | +10 stop | ETH | DOWN | 0.64 | open |  |
| 10-04 09:41 | +20 | ETH | DOWN | 0.64 | open |  |
| 10-04 09:41 | +15 | ETH | DOWN | 0.64 | open |  |
| 10-04 09:41 | +10 | ETH | DOWN | 0.64 | open |  |
| 10-04 09:41 | +5 | ETH | DOWN | 0.64 | open |  |
| 10-04 09:41 | +10 stop | SOL | DOWN | 0.71 | open |  |
| 10-04 09:41 | +20 | SOL | DOWN | 0.71 | open |  |
| 10-04 09:41 | +15 | SOL | DOWN | 0.71 | open |  |
| 10-04 09:41 | +10 | SOL | DOWN | 0.71 | open |  |
| 10-04 09:41 | +5 | SOL | DOWN | 0.71 | open |  |
| 10-04 09:34 | +10 stop | BNB | DOWN | 0.58 | 0.73 | 1.18 |
| 10-04 09:33 | +10 stop | BNB | UP | 0.65 | 0.45 | -2.34 |
| 10-04 09:33 | +20 | BNB | UP | 0.65 | open |  |
| 10-04 09:33 | +15 | BNB | UP | 0.65 | open |  |
| 10-04 09:33 | +10 | BNB | UP | 0.65 | open |  |
| 10-04 09:33 | +5 | BNB | UP | 0.65 | open |  |
| 10-04 09:32 | +10 stop | ETH | DOWN | 0.56 | 0.71 | 1.17 |
| 10-04 09:32 | +20 | ETH | DOWN | 0.56 | 0.83 | 2.42 |
| 10-04 09:32 | +15 | ETH | DOWN | 0.56 | 0.71 | 1.17 |
| 10-04 09:32 | +10 | ETH | DOWN | 0.56 | 0.71 | 1.17 |
| 10-04 09:32 | +5 | ETH | DOWN | 0.56 | 0.71 | 1.17 |
| 10-04 09:31 | +10 stop | BTC | DOWN | 0.67 | 0.78 | 0.81 |
| 10-04 09:31 | +20 | BTC | DOWN | 0.67 | 0.87 | 1.76 |
| 10-04 09:31 | +15 | BTC | DOWN | 0.67 | 0.82 | 1.23 |
| 10-04 09:31 | +10 | BTC | DOWN | 0.67 | 0.78 | 0.81 |
| 10-04 09:31 | +5 | BTC | DOWN | 0.67 | 0.73 | 0.30 |
| 10-04 09:31 | +10 stop | HYPE | DOWN | 0.70 | 0.83 | 1.05 |
| 10-04 09:31 | +20 | HYPE | DOWN | 0.70 | 0.91 | 1.89 |
| 10-04 09:31 | +15 | HYPE | DOWN | 0.70 | 0.87 | 1.47 |
| 10-04 09:31 | +10 | HYPE | DOWN | 0.70 | 0.83 | 1.05 |
| 10-04 09:31 | +5 | HYPE | DOWN | 0.70 | 0.79 | 0.63 |
| 10-04 09:30 | +10 stop | XRP | UP | 0.43 | 0.54 | 0.74 |
| 10-04 09:30 | +20 | XRP | UP | 0.43 | open |  |
| 10-04 09:30 | +15 | XRP | UP | 0.44 | open |  |
| 10-04 09:30 | +10 | XRP | UP | 0.44 | 0.54 | 0.64 |
| 10-04 09:30 | +5 | XRP | UP | 0.45 | 0.54 | 0.54 |
| 10-04 09:23 | +10 stop | ZEC | UP | 0.61 | 0.77 | 1.30 |
| 10-04 09:21 | +10 stop | HYPE | UP | 0.62 | 0.76 | 1.10 |
| 10-04 09:21 | +5 | ZEC | DOWN | 0.69 | yes | -7.05 |
| 10-04 09:21 | +10 stop | HYPE | DOWN | 0.36 | 0.68 | 2.87 |
