# Range-Scalp Bot

*Updated Sat Oct 10 22:30 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 10999 | 9487 | 1512 (22) | 3 | $-3719.50 | -5.4% |
| **+10¢** | 8326 | 6565 | 1761 (36) | 3 | $-3543.69 | -6.8% |
| **+15¢** | 7019 | 5157 | 1862 (52) | 4 | $-2974.33 | -6.7% |
| **+20¢** | 6245 | 4306 | 1939 (66) | 4 | $-2510.17 | -6.4% |
| **+10¢ (15¢ stop)** | 13550 | 13509 | 41 (25) | 0 | $-5441.54 | -6.4% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-10 22:28 | +5 | ETH | DOWN | 0.71 | 0.82 | 0.84 |
| 10-10 22:28 | +10 stop | ETH | DOWN | 0.71 | 0.82 | 0.84 |
| 10-10 22:28 | +20 | ETH | DOWN | 0.71 | 0.97 | 2.48 |
| 10-10 22:28 | +15 | ETH | DOWN | 0.69 | 0.97 | 2.68 |
| 10-10 22:28 | +10 | ETH | DOWN | 0.69 | 0.82 | 1.04 |
| 10-10 22:28 | +10 stop | ZEC | DOWN | 0.63 | 0.91 | 2.58 |
| 10-10 22:28 | +5 | ZEC | DOWN | 0.63 | 0.91 | 2.58 |
| 10-10 22:26 | +5 | ETH | DOWN | 0.61 | 0.71 | 0.68 |
| 10-10 22:26 | +15 | ETH | DOWN | 0.63 | 0.84 | 1.83 |
| 10-10 22:26 | +5 | ETH | DOWN | 0.63 | 0.68 | 0.17 |
| 10-10 22:25 | +10 stop | ZEC | DOWN | 0.66 | 0.48 | -2.14 |
| 10-10 22:25 | +20 | ZEC | DOWN | 0.66 | 0.91 | 2.29 |
| 10-10 22:25 | +15 | ZEC | DOWN | 0.66 | 0.91 | 2.29 |
| 10-10 22:25 | +10 | ZEC | DOWN | 0.66 | 0.91 | 2.29 |
| 10-10 22:25 | +5 | ZEC | DOWN | 0.66 | 0.71 | 0.19 |
| 10-10 22:25 | +10 stop | ETH | DOWN | 0.66 | 0.84 | 1.54 |
| 10-10 22:25 | +10 | ETH | DOWN | 0.66 | 0.84 | 1.54 |
| 10-10 22:25 | +10 stop | HYPE | UP | 0.55 | 0.34 | -2.44 |
| 10-10 22:23 | +10 stop | ETH | DOWN | 0.48 | 0.63 | 1.15 |
| 10-10 22:23 | +10 | ETH | DOWN | 0.48 | 0.63 | 1.15 |
| 10-10 22:23 | +10 stop | HYPE | DOWN | 0.41 | 0.56 | 1.15 |
| 10-10 22:22 | +15 | SOL | DOWN | 0.70 | open |  |
| 10-10 22:22 | +10 | SOL | DOWN | 0.70 | 0.80 | 0.73 |
| 10-10 22:22 | +5 | SOL | DOWN | 0.70 | 0.80 | 0.73 |
| 10-10 22:22 | +10 stop | SOL | DOWN | 0.71 | 0.83 | 0.95 |
| 10-10 22:22 | +20 | SOL | DOWN | 0.71 | open |  |
| 10-10 22:21 | +10 stop | HYPE | DOWN | 0.71 | 0.53 | -2.13 |
| 10-10 22:21 | +10 | ZEC | DOWN | 0.66 | 0.79 | 1.02 |
| 10-10 22:21 | +10 stop | BNB | DOWN | 0.62 | 0.47 | -1.85 |
| 10-10 22:20 | +5 | ZEC | DOWN | 0.66 | 0.74 | 0.50 |
| 10-10 22:20 | +10 stop | ZEC | DOWN | 0.64 | 0.74 | 0.69 |
| 10-10 22:19 | +5 | ETH | DOWN | 0.60 | 0.65 | 0.17 |
| 10-10 22:18 | +10 stop | NEAR | DOWN | 0.63 | 0.76 | 1.00 |
| 10-10 22:18 | +20 | NEAR | DOWN | 0.63 | 0.84 | 1.83 |
| 10-10 22:18 | +15 | NEAR | DOWN | 0.63 | 0.79 | 1.31 |
| 10-10 22:18 | +10 | NEAR | DOWN | 0.63 | 0.76 | 1.00 |
| 10-10 22:18 | +5 | NEAR | DOWN | 0.63 | 0.69 | 0.28 |
| 10-10 22:18 | +5 | HYPE | UP | 0.62 | open |  |
| 10-10 22:18 | +10 stop | SOL | UP | 0.62 | 0.32 | -3.33 |
| 10-10 22:18 | +10 stop | XRP | DOWN | 0.63 | 0.82 | 1.62 |
