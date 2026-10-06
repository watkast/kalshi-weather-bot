# Range-Scalp Bot

*Updated Tue Oct 06 19:29 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 5357 | 4641 | 716 (7) | 3 | $-1671.02 | -4.9% |
| **+10¢** | 4089 | 3250 | 839 (12) | 4 | $-1580.66 | -6.1% |
| **+15¢** | 3426 | 2538 | 888 (15) | 5 | $-1379.70 | -6.4% |
| **+20¢** | 3071 | 2149 | 922 (22) | 4 | $-1090.79 | -5.7% |
| **+10¢ (15¢ stop)** | 6544 | 6529 | 15 (9) | 0 | $-2387.14 | -5.8% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-06 19:27 | +10 stop | BTC | DOWN | 0.25 | 0.68 | 4.00 |
| 10-06 19:27 | +10 | BTC | DOWN | 0.25 | 0.68 | 4.00 |
| 10-06 19:27 | +5 | BTC | DOWN | 0.25 | 0.68 | 4.00 |
| 10-06 19:25 | +10 stop | BTC | DOWN | 0.66 | 0.46 | -2.34 |
| 10-06 19:25 | +15 | BTC | DOWN | 0.66 | open |  |
| 10-06 19:25 | +10 | BTC | DOWN | 0.66 | 0.79 | 1.02 |
| 10-06 19:24 | +10 stop | NEAR | DOWN | 0.62 | 0.75 | 0.99 |
| 10-06 19:24 | +10 | NEAR | DOWN | 0.62 | 0.75 | 0.97 |
| 10-06 19:24 | +5 | NEAR | DOWN | 0.62 | 0.75 | 0.99 |
| 10-06 19:22 | +10 stop | ZEC | DOWN | 0.71 | 0.81 | 0.74 |
| 10-06 19:22 | +10 stop | HYPE | UP | 0.64 | 0.49 | -1.85 |
| 10-06 19:21 | +10 stop | ETH | DOWN | 0.70 | 0.80 | 0.73 |
| 10-06 19:21 | +10 | ETH | DOWN | 0.70 | 0.80 | 0.73 |
| 10-06 19:21 | +5 | ETH | DOWN | 0.70 | 0.77 | 0.42 |
| 10-06 19:20 | +10 | BTC | UP | 0.55 | 0.69 | 1.07 |
| 10-06 19:20 | +10 stop | XRP | DOWN | 0.66 | 0.76 | 0.71 |
| 10-06 19:20 | +20 | XRP | DOWN | 0.64 | 0.86 | 1.94 |
| 10-06 19:20 | +15 | XRP | DOWN | 0.64 | 0.81 | 1.42 |
| 10-06 19:20 | +10 | XRP | DOWN | 0.64 | 0.76 | 0.90 |
| 10-06 19:20 | +5 | XRP | DOWN | 0.64 | 0.76 | 0.90 |
| 10-06 19:20 | +10 stop | BTC | UP | 0.69 | 0.52 | -2.03 |
| 10-06 19:20 | +5 | ZEC | UP | 0.70 | open |  |
| 10-06 19:20 | +10 stop | HYPE | UP | 0.68 | 0.44 | -2.74 |
| 10-06 19:20 | +10 stop | NEAR | DOWN | 0.64 | 0.74 | 0.69 |
| 10-06 19:20 | +15 | NEAR | DOWN | 0.65 | 0.80 | 1.22 |
| 10-06 19:20 | +10 | NEAR | DOWN | 0.65 | 0.78 | 1.00 |
| 10-06 19:20 | +5 | NEAR | DOWN | 0.65 | 0.71 | 0.29 |
| 10-06 19:20 | +10 stop | ETH | DOWN | 0.55 | 0.67 | 0.86 |
| 10-06 19:20 | +20 | ETH | DOWN | 0.55 | 0.77 | 1.89 |
| 10-06 19:20 | +15 | ETH | DOWN | 0.55 | 0.71 | 1.27 |
| 10-06 19:20 | +10 | ETH | DOWN | 0.55 | 0.67 | 0.86 |
| 10-06 19:20 | +5 | ETH | DOWN | 0.55 | 0.67 | 0.86 |
| 10-06 19:19 | +10 stop | ZEC | UP | 0.64 | 0.49 | -1.85 |
| 10-06 19:19 | +10 stop | HYPE | DOWN | 0.59 | 0.35 | -2.77 |
| 10-06 19:18 | +10 stop | BTC | DOWN | 0.63 | 0.47 | -1.95 |
| 10-06 19:18 | +5 | ZEC | UP | 0.56 | 0.62 | 0.25 |
| 10-06 19:17 | +10 stop | SOL | DOWN | 0.70 | 0.83 | 1.05 |
| 10-06 19:17 | +5 | SOL | DOWN | 0.70 | 0.83 | 1.05 |
| 10-06 19:17 | +5 | BTC | DOWN | 0.64 | 0.74 | 0.69 |
| 10-06 19:17 | +10 stop | NEAR | DOWN | 0.61 | 0.75 | 1.10 |
