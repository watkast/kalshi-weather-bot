# Range-Scalp Bot

*Updated Sat Oct 03 09:28 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 529 | 452 | 77 (1) | 1 | $-208.94 | -6.2% |
| **+10¢** | 407 | 322 | 85 (2) | 1 | $-171.83 | -6.7% |
| **+15¢** | 346 | 255 | 91 (3) | 2 | $-161.86 | -7.4% |
| **+20¢** | 300 | 206 | 94 (3) | 2 | $-156.90 | -8.2% |
| **+10¢ (15¢ stop)** | 695 | 694 | 1 (1) | 0 | $-364.22 | -8.3% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-03 09:25 | +20 | ETH | DOWN | 0.71 | open |  |
| 10-03 09:25 | +15 | ETH | DOWN | 0.71 | open |  |
| 10-03 09:25 | +5 | ETH | DOWN | 0.71 | 0.78 | 0.42 |
| 10-03 09:24 | +10 stop | HYPE | UP | 0.66 | 0.76 | 0.71 |
| 10-03 09:22 | +5 | ETH | DOWN | 0.63 | 0.77 | 1.10 |
| 10-03 09:22 | +15 | ETH | DOWN | 0.62 | 0.77 | 1.21 |
| 10-03 09:22 | +5 | ETH | DOWN | 0.62 | 0.69 | 0.39 |
| 10-03 09:21 | +10 stop | HYPE | UP | 0.52 | 0.67 | 1.16 |
| 10-03 09:20 | +10 | ETH | DOWN | 0.68 | 0.78 | 0.71 |
| 10-03 09:20 | +5 | ETH | DOWN | 0.68 | 0.74 | 0.30 |
| 10-03 09:20 | +10 stop | ETH | DOWN | 0.69 | 0.82 | 1.04 |
| 10-03 09:19 | +5 | NEAR | DOWN | 0.71 | 0.77 | 0.32 |
| 10-03 09:19 | +5 | ZEC | DOWN | 0.41 | 0.54 | 0.90 |
| 10-03 09:19 | +10 stop | SOL | DOWN | 0.57 | 0.69 | 0.87 |
| 10-03 09:19 | +10 | SOL | DOWN | 0.57 | 0.69 | 0.87 |
| 10-03 09:19 | +5 | SOL | DOWN | 0.57 | 0.69 | 0.87 |
| 10-03 09:18 | +5 | DOGE | DOWN | 0.62 | 0.83 | 1.79 |
| 10-03 09:18 | +10 stop | NEAR | DOWN | 0.70 | 0.82 | 0.94 |
| 10-03 09:18 | +20 | NEAR | DOWN | 0.70 | 0.90 | 1.78 |
| 10-03 09:18 | +15 | NEAR | DOWN | 0.70 | 0.87 | 1.47 |
| 10-03 09:18 | +10 | NEAR | DOWN | 0.70 | 0.82 | 0.94 |
| 10-03 09:18 | +5 | NEAR | DOWN | 0.69 | 0.76 | 0.42 |
| 10-03 09:17 | +10 stop | ZEC | DOWN | 0.62 | 0.40 | -2.54 |
| 10-03 09:17 | +20 | ZEC | DOWN | 0.62 | 0.85 | 2.04 |
| 10-03 09:17 | +15 | ZEC | DOWN | 0.62 | 0.78 | 1.30 |
| 10-03 09:17 | +10 | ZEC | DOWN | 0.62 | 0.78 | 1.30 |
| 10-03 09:17 | +5 | ZEC | DOWN | 0.62 | 0.69 | 0.38 |
| 10-03 09:17 | +5 | BTC | DOWN | 0.68 | 0.77 | 0.61 |
| 10-03 09:17 | +10 stop | XRP | DOWN | 0.61 | 0.73 | 0.88 |
| 10-03 09:17 | +10 | XRP | DOWN | 0.61 | 0.73 | 0.88 |
| 10-03 09:17 | +5 | XRP | DOWN | 0.61 | 0.73 | 0.88 |
| 10-03 09:17 | +10 stop | HYPE | DOWN | 0.58 | 0.29 | -3.23 |
| 10-03 09:17 | +20 | HYPE | DOWN | 0.58 | open |  |
| 10-03 09:17 | +15 | HYPE | DOWN | 0.58 | open |  |
| 10-03 09:17 | +10 | HYPE | DOWN | 0.58 | open |  |
| 10-03 09:17 | +5 | HYPE | DOWN | 0.58 | open |  |
| 10-03 09:17 | +10 stop | SOL | DOWN | 0.58 | 0.69 | 0.77 |
| 10-03 09:17 | +10 | SOL | DOWN | 0.58 | 0.69 | 0.77 |
| 10-03 09:17 | +5 | SOL | DOWN | 0.58 | 0.69 | 0.77 |
| 10-03 09:17 | +10 stop | ETH | DOWN | 0.55 | 0.23 | -3.51 |
