# Range-Scalp Bot

*Updated Sat Oct 17 04:39 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 20365 | 17714 | 2651 (29) | 7 | $-6024.32 | -4.7% |
| **+10¢** | 15345 | 12288 | 3057 (41) | 7 | $-5356.87 | -5.5% |
| **+15¢** | 12832 | 9544 | 3288 (60) | 7 | $-4825.79 | -6.0% |
| **+20¢** | 11377 | 7933 | 3444 (79) | 8 | $-4266.91 | -6.0% |
| **+10¢ (15¢ stop)** | 25040 | 24990 | 50 (29) | 1 | $-9490.53 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-17 04:38 | +10 stop | NEAR | UP | 0.70 | open |  |
| 10-17 04:35 | +10 stop | ETH | UP | 0.69 | 0.84 | 1.25 |
| 10-17 04:35 | +10 stop | DOGE | UP | 0.70 | 0.83 | 1.03 |
| 10-17 04:33 | +10 stop | NEAR | DOWN | 0.63 | 0.32 | -3.41 |
| 10-17 04:33 | +20 | NEAR | DOWN | 0.63 | open |  |
| 10-17 04:33 | +15 | NEAR | DOWN | 0.63 | open |  |
| 10-17 04:33 | +10 | NEAR | DOWN | 0.63 | open |  |
| 10-17 04:33 | +5 | NEAR | DOWN | 0.63 | open |  |
| 10-17 04:33 | +5 | ETH | DOWN | 0.60 | open |  |
| 10-17 04:33 | +10 stop | SOL | UP | 0.56 | 0.67 | 0.76 |
| 10-17 04:33 | +10 stop | HYPE | UP | 0.69 | 0.80 | 0.83 |
| 10-17 04:33 | +20 | HYPE | UP | 0.69 | open |  |
| 10-17 04:33 | +15 | HYPE | UP | 0.69 | 0.85 | 1.36 |
| 10-17 04:33 | +10 | HYPE | UP | 0.69 | 0.80 | 0.83 |
| 10-17 04:33 | +5 | HYPE | UP | 0.69 | 0.74 | 0.21 |
| 10-17 04:32 | +10 stop | DOGE | DOWN | 0.55 | 0.27 | -3.12 |
| 10-17 04:32 | +15 | DOGE | DOWN | 0.55 | open |  |
| 10-17 04:32 | +10 | DOGE | DOWN | 0.55 | open |  |
| 10-17 04:32 | +5 | DOGE | DOWN | 0.55 | open |  |
| 10-17 04:32 | +5 | XRP | DOWN | 0.66 | open |  |
| 10-17 04:31 | +10 stop | ZEC | UP | 0.55 | 0.68 | 0.96 |
| 10-17 04:31 | +20 | ZEC | UP | 0.55 | 0.77 | 1.89 |
| 10-17 04:31 | +15 | ZEC | UP | 0.55 | 0.74 | 1.58 |
| 10-17 04:31 | +10 | ZEC | UP | 0.56 | 0.68 | 0.86 |
| 10-17 04:31 | +5 | ZEC | UP | 0.59 | 0.68 | 0.57 |
| 10-17 04:31 | +10 stop | BTC | DOWN | 0.59 | 0.44 | -1.85 |
| 10-17 04:31 | +20 | BTC | DOWN | 0.59 | open |  |
| 10-17 04:31 | +15 | BTC | DOWN | 0.59 | open |  |
| 10-17 04:31 | +10 | BTC | DOWN | 0.59 | open |  |
| 10-17 04:31 | +5 | BTC | DOWN | 0.59 | open |  |
| 10-17 04:31 | +10 stop | ETH | DOWN | 0.54 | 0.28 | -2.93 |
| 10-17 04:31 | +20 | ETH | DOWN | 0.54 | open |  |
| 10-17 04:31 | +15 | ETH | DOWN | 0.54 | open |  |
| 10-17 04:31 | +10 | ETH | DOWN | 0.54 | open |  |
| 10-17 04:31 | +5 | ETH | DOWN | 0.54 | 0.59 | 0.15 |
| 10-17 04:31 | +10 stop | DOGE | DOWN | 0.48 | 0.66 | 1.46 |
| 10-17 04:31 | +20 | DOGE | DOWN | 0.48 | open |  |
| 10-17 04:31 | +15 | DOGE | DOWN | 0.48 | 0.66 | 1.46 |
| 10-17 04:31 | +10 | DOGE | DOWN | 0.48 | 0.66 | 1.46 |
| 10-17 04:31 | +5 | DOGE | DOWN | 0.47 | 0.55 | 0.44 |
