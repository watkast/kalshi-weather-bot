# Range-Scalp Bot

*Updated Sat Nov 14 09:47 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 59280 | 51727 | 7553 (107) | 2 | $-15987.51 | -4.3% |
| **+10¢** | 44279 | 35439 | 8840 (140) | 3 | $-15015.74 | -5.4% |
| **+15¢** | 37108 | 27575 | 9533 (176) | 3 | $-13650.84 | -5.9% |
| **+20¢** | 33056 | 23048 | 10008 (228) | 3 | $-12045.68 | -5.8% |
| **+10¢ (15¢ stop)** | 72119 | 71977 | 142 (82) | 3 | $-26506.18 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-14 09:47 | +5 | ETH | UP | 0.70 | open |  |
| 11-14 09:46 | +10 stop | BTC | UP | 0.71 | open |  |
| 11-14 09:46 | +20 | BTC | UP | 0.71 | open |  |
| 11-14 09:46 | +15 | BTC | UP | 0.71 | open |  |
| 11-14 09:46 | +10 | BTC | UP | 0.71 | open |  |
| 11-14 09:46 | +5 | BTC | UP | 0.71 | 0.78 | 0.42 |
| 11-14 09:46 | +10 stop | HYPE | UP | 0.71 | open |  |
| 11-14 09:46 | +20 | HYPE | UP | 0.71 | open |  |
| 11-14 09:46 | +15 | HYPE | UP | 0.71 | open |  |
| 11-14 09:46 | +10 | HYPE | UP | 0.71 | open |  |
| 11-14 09:46 | +5 | HYPE | UP | 0.71 | open |  |
| 11-14 09:46 | +10 stop | ETH | UP | 0.65 | open |  |
| 11-14 09:46 | +20 | ETH | UP | 0.65 | open |  |
| 11-14 09:46 | +15 | ETH | UP | 0.65 | open |  |
| 11-14 09:46 | +10 | ETH | UP | 0.65 | open |  |
| 11-14 09:46 | +5 | ETH | UP | 0.65 | 0.70 | 0.19 |
| 11-14 09:41 | +10 stop | SOL | UP | 0.69 | 0.80 | 0.83 |
| 11-14 09:40 | +10 stop | SOL | DOWN | 0.68 | 0.38 | -3.33 |
| 11-14 09:39 | +10 stop | NEAR | UP | 0.58 | 0.68 | 0.66 |
| 11-14 09:39 | +5 | NEAR | UP | 0.58 | 0.68 | 0.66 |
| 11-14 09:38 | +10 stop | SOL | DOWN | 0.71 | 0.50 | -2.43 |
| 11-14 09:37 | +5 | NEAR | UP | 0.56 | 0.69 | 0.97 |
| 11-14 09:37 | +10 stop | ZEC | UP | 0.65 | 0.50 | -1.84 |
| 11-14 09:37 | +20 | ZEC | UP | 0.65 | 0.89 | 2.17 |
| 11-14 09:37 | +15 | ZEC | UP | 0.65 | 0.89 | 2.17 |
| 11-14 09:37 | +10 | ZEC | UP | 0.65 | 0.76 | 0.81 |
| 11-14 09:37 | +5 | ZEC | UP | 0.66 | 0.74 | 0.50 |
| 11-14 09:36 | +10 stop | NEAR | UP | 0.66 | 0.49 | -2.04 |
| 11-14 09:36 | +10 stop | BTC | UP | 0.67 | 0.51 | -1.94 |
| 11-14 09:36 | +15 | BTC | UP | 0.67 | 0.82 | 1.23 |
| 11-14 09:36 | +10 | BTC | UP | 0.67 | 0.82 | 1.23 |
| 11-14 09:36 | +5 | BTC | UP | 0.67 | 0.75 | 0.50 |
| 11-14 09:34 | +15 | SOL | UP | 0.67 | 0.83 | 1.34 |
| 11-14 09:33 | +10 stop | NEAR | UP | 0.68 | 0.52 | -1.94 |
| 11-14 09:33 | +10 | NEAR | UP | 0.68 | 0.90 | 2.01 |
| 11-14 09:33 | +5 | NEAR | UP | 0.68 | 0.74 | 0.30 |
| 11-14 09:33 | +5 | SOL | UP | 0.71 | 0.80 | 0.63 |
| 11-14 09:32 | +10 stop | NEAR | UP | 0.64 | 0.77 | 1.00 |
| 11-14 09:32 | +20 | NEAR | UP | 0.64 | 0.90 | 2.40 |
| 11-14 09:32 | +15 | NEAR | UP | 0.64 | 0.90 | 2.40 |
