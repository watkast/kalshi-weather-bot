# Range-Scalp Bot

*Updated Sun Oct 25 01:03 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 32321 | 28182 | 4139 (41) | 0 | $-9212.68 | -4.5% |
| **+10¢** | 24198 | 19404 | 4794 (59) | 2 | $-8253.01 | -5.4% |
| **+15¢** | 20261 | 15106 | 5155 (82) | 5 | $-7378.33 | -5.8% |
| **+20¢** | 17949 | 12556 | 5393 (104) | 5 | $-6513.46 | -5.8% |
| **+10¢ (15¢ stop)** | 39714 | 39654 | 60 (32) | 2 | $-15161.98 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-25 01:01 | +10 stop | ZEC | DOWN | 0.64 | open |  |
| 10-25 01:01 | +20 | ZEC | DOWN | 0.62 | open |  |
| 10-25 01:01 | +15 | ZEC | DOWN | 0.62 | open |  |
| 10-25 01:01 | +10 | ZEC | DOWN | 0.62 | open |  |
| 10-25 01:01 | +5 | ZEC | DOWN | 0.62 | 0.68 | 0.27 |
| 10-25 01:01 | +10 stop | XRP | DOWN | 0.70 | 0.80 | 0.73 |
| 10-25 01:01 | +20 | XRP | DOWN | 0.70 | open |  |
| 10-25 01:01 | +15 | XRP | DOWN | 0.70 | open |  |
| 10-25 01:01 | +10 | XRP | DOWN | 0.70 | 0.80 | 0.73 |
| 10-25 01:01 | +5 | XRP | DOWN | 0.71 | 0.76 | 0.22 |
| 10-25 01:01 | +10 stop | DOGE | DOWN | 0.68 | open |  |
| 10-25 01:01 | +20 | DOGE | DOWN | 0.68 | open |  |
| 10-25 01:01 | +15 | DOGE | DOWN | 0.68 | open |  |
| 10-25 01:01 | +10 | DOGE | DOWN | 0.68 | open |  |
| 10-25 01:01 | +5 | DOGE | DOWN | 0.68 | 0.76 | 0.51 |
| 10-25 01:01 | +10 stop | NEAR | DOWN | 0.62 | 0.74 | 0.89 |
| 10-25 01:01 | +20 | NEAR | DOWN | 0.62 | open |  |
| 10-25 01:01 | +15 | NEAR | DOWN | 0.62 | open |  |
| 10-25 01:01 | +10 | NEAR | DOWN | 0.62 | 0.74 | 0.89 |
| 10-25 01:01 | +5 | NEAR | DOWN | 0.62 | 0.74 | 0.89 |
| 10-25 01:01 | +10 stop | HYPE | DOWN | 0.69 | 0.79 | 0.73 |
| 10-25 01:01 | +20 | HYPE | DOWN | 0.69 | open |  |
| 10-25 01:01 | +15 | HYPE | DOWN | 0.69 | open |  |
| 10-25 01:01 | +10 | HYPE | DOWN | 0.69 | 0.79 | 0.73 |
| 10-25 01:01 | +5 | HYPE | DOWN | 0.69 | 0.75 | 0.31 |
| 10-25 00:56 | +10 stop | HYPE | UP | 0.29 | 0.56 | 2.37 |
| 10-25 00:56 | +10 stop | NEAR | DOWN | 0.67 | 0.81 | 1.13 |
| 10-25 00:56 | +20 | NEAR | DOWN | 0.67 | 0.87 | 1.76 |
| 10-25 00:56 | +15 | NEAR | DOWN | 0.67 | 0.87 | 1.76 |
| 10-25 00:56 | +10 | NEAR | DOWN | 0.67 | 0.81 | 1.13 |
| 10-25 00:56 | +5 | NEAR | DOWN | 0.67 | 0.75 | 0.50 |
| 10-25 00:55 | +10 stop | ETH | UP | 0.61 | 0.85 | 2.14 |
| 10-25 00:55 | +20 | ETH | UP | 0.61 | 0.85 | 2.14 |
| 10-25 00:55 | +15 | ETH | UP | 0.61 | 0.85 | 2.14 |
| 10-25 00:55 | +10 | ETH | UP | 0.61 | 0.85 | 2.14 |
| 10-25 00:55 | +5 | ETH | UP | 0.61 | 0.69 | 0.48 |
| 10-25 00:55 | +10 stop | BTC | UP | 0.55 | 0.77 | 1.89 |
| 10-25 00:55 | +5 | BTC | UP | 0.55 | 0.77 | 1.89 |
| 10-25 00:54 | +10 stop | SOL | UP | 0.70 | 0.88 | 1.55 |
| 10-25 00:54 | +10 | SOL | UP | 0.70 | 0.88 | 1.57 |
