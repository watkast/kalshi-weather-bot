# Range-Scalp Bot

*Updated Sun Nov 01 18:11 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 43769 | 38136 | 5633 (64) | 3 | $-12506.25 | -4.5% |
| **+10¢** | 32653 | 26146 | 6507 (85) | 3 | $-11235.97 | -5.5% |
| **+15¢** | 27332 | 20323 | 7009 (112) | 3 | $-10280.15 | -6.0% |
| **+20¢** | 24273 | 16931 | 7342 (146) | 4 | $-9075.37 | -6.0% |
| **+10¢ (15¢ stop)** | 53385 | 53299 | 86 (51) | 0 | $-20156.63 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-01 18:09 | +10 stop | ETH | DOWN | 0.63 | 0.74 | 0.79 |
| 11-01 18:09 | +10 stop | BNB | DOWN | 0.60 | 0.72 | 0.88 |
| 11-01 18:08 | +5 | NEAR | DOWN | 0.71 | 0.81 | 0.74 |
| 11-01 18:07 | +10 stop | BNB | UP | 0.59 | 0.39 | -2.34 |
| 11-01 18:07 | +10 stop | XRP | DOWN | 0.70 | 0.83 | 1.05 |
| 11-01 18:07 | +20 | XRP | DOWN | 0.70 | 0.90 | 1.82 |
| 11-01 18:07 | +15 | XRP | DOWN | 0.70 | 0.90 | 1.82 |
| 11-01 18:07 | +10 | XRP | DOWN | 0.70 | 0.83 | 1.05 |
| 11-01 18:07 | +5 | XRP | DOWN | 0.70 | 0.75 | 0.21 |
| 11-01 18:06 | +10 stop | ETH | UP | 0.63 | 0.48 | -1.85 |
| 11-01 18:06 | +10 stop | BTC | DOWN | 0.69 | 0.52 | -2.03 |
| 11-01 18:06 | +10 stop | BNB | UP | 0.51 | 0.62 | 0.75 |
| 11-01 18:05 | +10 stop | NEAR | DOWN | 0.63 | 0.81 | 1.56 |
| 11-01 18:05 | +10 | NEAR | DOWN | 0.63 | 0.81 | 1.56 |
| 11-01 18:05 | +5 | NEAR | DOWN | 0.63 | 0.68 | 0.21 |
| 11-01 18:05 | +5 | BTC | DOWN | 0.70 | 0.79 | 0.63 |
| 11-01 18:04 | +10 stop | DOGE | UP | 0.71 | 0.84 | 1.05 |
| 11-01 18:04 | +5 | ETH | DOWN | 0.66 | 0.74 | 0.50 |
| 11-01 18:04 | +10 stop | HYPE | DOWN | 0.58 | 0.69 | 0.77 |
| 11-01 18:03 | +10 stop | BTC | DOWN | 0.66 | 0.51 | -1.84 |
| 11-01 18:03 | +20 | BTC | DOWN | 0.66 | 0.86 | 1.75 |
| 11-01 18:03 | +15 | BTC | DOWN | 0.66 | 0.81 | 1.23 |
| 11-01 18:03 | +10 | BTC | DOWN | 0.66 | 0.79 | 1.02 |
| 11-01 18:03 | +5 | BTC | DOWN | 0.66 | 0.72 | 0.29 |
| 11-01 18:02 | +10 stop | BNB | DOWN | 0.63 | 0.46 | -2.05 |
| 11-01 18:02 | +5 | DOGE | DOWN | 0.64 | open |  |
| 11-01 18:02 | +10 stop | HYPE | UP | 0.57 | 0.34 | -2.64 |
| 11-01 18:02 | +20 | HYPE | UP | 0.57 | open |  |
| 11-01 18:02 | +15 | HYPE | UP | 0.57 | open |  |
| 11-01 18:02 | +10 | HYPE | UP | 0.57 | open |  |
| 11-01 18:02 | +5 | HYPE | UP | 0.57 | open |  |
| 11-01 18:01 | +10 stop | SOL | UP | 0.71 | 0.81 | 0.74 |
| 11-01 18:01 | +20 | SOL | UP | 0.71 | 0.92 | 1.86 |
| 11-01 18:01 | +15 | SOL | UP | 0.71 | 0.86 | 1.26 |
| 11-01 18:01 | +10 | SOL | UP | 0.71 | 0.81 | 0.74 |
| 11-01 18:01 | +5 | SOL | UP | 0.71 | 0.79 | 0.53 |
| 11-01 18:01 | +10 stop | ZEC | DOWN | 0.61 | 0.75 | 1.09 |
| 11-01 18:01 | +20 | ZEC | DOWN | 0.61 | 0.84 | 2.03 |
| 11-01 18:01 | +15 | ZEC | DOWN | 0.61 | 0.76 | 1.20 |
| 11-01 18:01 | +10 | ZEC | DOWN | 0.61 | 0.75 | 1.09 |
