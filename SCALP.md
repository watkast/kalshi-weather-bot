# Range-Scalp Bot

*Updated Sat Oct 17 15:54 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 21185 | 18441 | 2744 (29) | 0 | $-6165.79 | -4.6% |
| **+10¢** | 15947 | 12777 | 3170 (41) | 0 | $-5504.14 | -5.5% |
| **+15¢** | 13332 | 9917 | 3415 (61) | 0 | $-5000.59 | -6.0% |
| **+20¢** | 11819 | 8242 | 3577 (80) | 0 | $-4426.75 | -6.0% |
| **+10¢ (15¢ stop)** | 26021 | 25971 | 50 (29) | 0 | $-9898.11 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-17 15:47 | +10 stop | ZEC | DOWN | 0.67 | 0.78 | 0.86 |
| 10-17 15:47 | +20 | ZEC | DOWN | 0.67 | 0.91 | 2.23 |
| 10-17 15:47 | +15 | ZEC | DOWN | 0.67 | 0.84 | 1.44 |
| 10-17 15:47 | +10 | ZEC | DOWN | 0.64 | 0.78 | 1.10 |
| 10-17 15:47 | +5 | ZEC | DOWN | 0.64 | 0.73 | 0.59 |
| 10-17 15:47 | +10 stop | XRP | DOWN | 0.66 | 0.76 | 0.71 |
| 10-17 15:47 | +20 | XRP | DOWN | 0.66 | 0.88 | 1.96 |
| 10-17 15:47 | +15 | XRP | DOWN | 0.65 | 0.81 | 1.33 |
| 10-17 15:47 | +10 | XRP | DOWN | 0.65 | 0.76 | 0.81 |
| 10-17 15:47 | +5 | XRP | DOWN | 0.65 | 0.70 | 0.19 |
| 10-17 15:46 | +10 stop | HYPE | DOWN | 0.71 | 0.89 | 1.58 |
| 10-17 15:46 | +20 | HYPE | DOWN | 0.71 | 0.91 | 1.82 |
| 10-17 15:46 | +15 | HYPE | DOWN | 0.71 | 0.89 | 1.58 |
| 10-17 15:46 | +10 | HYPE | DOWN | 0.71 | 0.89 | 1.58 |
| 10-17 15:46 | +5 | HYPE | DOWN | 0.71 | 0.89 | 1.58 |
| 10-17 15:46 | +10 stop | BTC | DOWN | 0.69 | 0.82 | 1.04 |
| 10-17 15:46 | +20 | BTC | DOWN | 0.69 | 0.89 | 1.78 |
| 10-17 15:46 | +15 | BTC | DOWN | 0.69 | 0.86 | 1.46 |
| 10-17 15:46 | +10 | BTC | DOWN | 0.69 | 0.82 | 1.04 |
| 10-17 15:46 | +5 | BTC | DOWN | 0.69 | 0.74 | 0.21 |
| 10-17 15:46 | +10 stop | ETH | DOWN | 0.65 | 0.76 | 0.81 |
| 10-17 15:46 | +20 | ETH | DOWN | 0.65 | 0.88 | 2.06 |
| 10-17 15:46 | +15 | ETH | DOWN | 0.65 | 0.80 | 1.22 |
| 10-17 15:46 | +10 | ETH | DOWN | 0.65 | 0.76 | 0.81 |
| 10-17 15:46 | +5 | ETH | DOWN | 0.65 | 0.71 | 0.29 |
| 10-17 15:41 | +10 | XRP | UP | 0.66 | 0.93 | 2.45 |
| 10-17 15:41 | +5 | XRP | UP | 0.66 | 0.74 | 0.50 |
| 10-17 15:41 | +10 stop | DOGE | DOWN | 0.71 | 0.52 | -2.23 |
| 10-17 15:41 | +10 stop | SOL | UP | 0.52 | 0.64 | 0.85 |
| 10-17 15:41 | +10 | SOL | UP | 0.52 | 0.64 | 0.85 |
| 10-17 15:41 | +5 | SOL | UP | 0.52 | 0.64 | 0.85 |
| 10-17 15:40 | +10 stop | XRP | UP | 0.66 | 0.93 | 2.46 |
| 10-17 15:40 | +10 stop | SOL | DOWN | 0.48 | 0.58 | 0.64 |
| 10-17 15:40 | +15 | SOL | DOWN | 0.47 | yes | -4.88 |
| 10-17 15:40 | +10 | SOL | DOWN | 0.47 | 0.58 | 0.74 |
| 10-17 15:40 | +5 | SOL | DOWN | 0.47 | 0.58 | 0.74 |
| 10-17 15:40 | +10 stop | DOGE | DOWN | 0.71 | 0.54 | -2.03 |
| 10-17 15:40 | +20 | DOGE | DOWN | 0.71 | yes | -7.25 |
| 10-17 15:40 | +15 | DOGE | DOWN | 0.71 | yes | -7.25 |
| 10-17 15:40 | +10 | DOGE | DOWN | 0.71 | yes | -7.25 |
