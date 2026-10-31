# Range-Scalp Bot

*Updated Sat Oct 31 02:28 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 41645 | 36342 | 5303 (54) | 5 | $-11661.21 | -4.4% |
| **+10¢** | 31035 | 24897 | 6138 (78) | 5 | $-10416.53 | -5.3% |
| **+15¢** | 25938 | 19319 | 6619 (106) | 4 | $-9519.98 | -5.8% |
| **+20¢** | 23024 | 16092 | 6932 (137) | 5 | $-8396.33 | -5.8% |
| **+10¢ (15¢ stop)** | 50748 | 50673 | 75 (41) | 1 | $-19180.13 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-31 02:28 | +10 stop | SOL | UP | 0.70 | open |  |
| 10-31 02:28 | +20 | SOL | UP | 0.70 | open |  |
| 10-31 02:28 | +15 | SOL | UP | 0.70 | open |  |
| 10-31 02:28 | +10 | SOL | UP | 0.70 | open |  |
| 10-31 02:28 | +5 | SOL | UP | 0.70 | open |  |
| 10-31 02:26 | +10 stop | ZEC | DOWN | 0.63 | 0.75 | 0.89 |
| 10-31 02:26 | +10 stop | BTC | DOWN | 0.70 | 0.89 | 1.68 |
| 10-31 02:26 | +10 stop | NEAR | UP | 0.23 | 0.61 | 3.50 |
| 10-31 02:26 | +10 stop | HYPE | DOWN | 0.58 | 0.71 | 1.00 |
| 10-31 02:25 | +5 | ETH | DOWN | 0.53 | 0.72 | 1.57 |
| 10-31 02:25 | +10 stop | ZEC | UP | 0.60 | 0.44 | -1.95 |
| 10-31 02:25 | +5 | ZEC | UP | 0.60 | open |  |
| 10-31 02:25 | +10 stop | BNB | DOWN | 0.59 | 0.71 | 0.88 |
| 10-31 02:25 | +15 | BNB | DOWN | 0.59 | 0.75 | 1.29 |
| 10-31 02:25 | +10 | BNB | DOWN | 0.59 | 0.71 | 0.88 |
| 10-31 02:25 | +5 | BNB | DOWN | 0.59 | 0.64 | 0.16 |
| 10-31 02:25 | +10 stop | ETH | UP | 0.44 | 0.27 | -2.02 |
| 10-31 02:25 | +20 | ETH | UP | 0.43 | open |  |
| 10-31 02:25 | +15 | ETH | UP | 0.44 | open |  |
| 10-31 02:25 | +10 | ETH | UP | 0.44 | open |  |
| 10-31 02:25 | +5 | ETH | UP | 0.44 | 0.53 | 0.54 |
| 10-31 02:25 | +10 stop | BTC | UP | 0.59 | 0.42 | -2.05 |
| 10-31 02:25 | +20 | BTC | UP | 0.59 | open |  |
| 10-31 02:25 | +15 | BTC | UP | 0.59 | open |  |
| 10-31 02:25 | +10 | BTC | UP | 0.59 | open |  |
| 10-31 02:25 | +5 | BTC | UP | 0.59 | open |  |
| 10-31 02:25 | +10 stop | HYPE | UP | 0.64 | 0.41 | -2.59 |
| 10-31 02:25 | +20 | HYPE | UP | 0.64 | open |  |
| 10-31 02:25 | +15 | HYPE | UP | 0.64 | open |  |
| 10-31 02:25 | +10 | HYPE | UP | 0.64 | open |  |
| 10-31 02:25 | +5 | HYPE | UP | 0.64 | open |  |
| 10-31 02:24 | +10 stop | DOGE | UP | 0.29 | 0.63 | 3.08 |
| 10-31 02:23 | +10 stop | ZEC | UP | 0.70 | 0.84 | 1.15 |
| 10-31 02:23 | +10 stop | ETH | UP | 0.70 | 0.89 | 1.68 |
| 10-31 02:23 | +5 | ETH | UP | 0.70 | 0.89 | 1.68 |
| 10-31 02:22 | +10 stop | NEAR | UP | 0.65 | 0.87 | 1.96 |
| 10-31 02:22 | +10 stop | DOGE | DOWN | 0.59 | 0.44 | -1.85 |
| 10-31 02:22 | +10 stop | ZEC | UP | 0.65 | 0.50 | -1.84 |
| 10-31 02:22 | +10 stop | BNB | DOWN | 0.65 | 0.40 | -2.79 |
| 10-31 02:22 | +10 stop | HYPE | UP | 0.58 | 0.72 | 1.03 |
