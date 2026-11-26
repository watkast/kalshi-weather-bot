# Range-Scalp Bot

*Updated Thu Nov 26 10:11 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 72496 | 63291 | 9205 (158) | 5 | $-19203.05 | -4.2% |
| **+10¢** | 54064 | 43314 | 10750 (203) | 6 | $-17782.87 | -5.2% |
| **+15¢** | 45271 | 33691 | 11580 (261) | 6 | $-15862.23 | -5.6% |
| **+20¢** | 40296 | 28100 | 12196 (327) | 6 | $-14260.15 | -5.6% |
| **+10¢ (15¢ stop)** | 88269 | 88060 | 209 (128) | 1 | $-32406.86 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-26 10:10 | +10 | XRP | DOWN | 0.65 | open |  |
| 11-26 10:10 | +5 | XRP | DOWN | 0.65 | open |  |
| 11-26 10:09 | +10 stop | BTC | DOWN | 0.55 | 0.25 | -3.32 |
| 11-26 10:09 | +5 | ETH | DOWN | 0.57 | open |  |
| 11-26 10:09 | +10 stop | DOGE | DOWN | 0.64 | 0.45 | -2.25 |
| 11-26 10:09 | +10 | DOGE | DOWN | 0.63 | open |  |
| 11-26 10:09 | +5 | DOGE | DOWN | 0.63 | 0.72 | 0.58 |
| 11-26 10:08 | +5 | ETH | DOWN | 0.53 | 0.61 | 0.45 |
| 11-26 10:08 | +10 stop | XRP | DOWN | 0.64 | open |  |
| 11-26 10:08 | +10 stop | ETH | DOWN | 0.63 | 0.43 | -2.35 |
| 11-26 10:08 | +10 stop | XRP | DOWN | 0.55 | 0.67 | 0.86 |
| 11-26 10:08 | +5 | ETH | DOWN | 0.59 | 0.67 | 0.50 |
| 11-26 10:07 | +5 | BTC | DOWN | 0.65 | open |  |
| 11-26 10:07 | +10 stop | ETH | DOWN | 0.71 | 0.54 | -2.03 |
| 11-26 10:07 | +5 | XRP | DOWN | 0.64 | 0.69 | 0.18 |
| 11-26 10:07 | +10 stop | SOL | DOWN | 0.54 | 0.32 | -2.54 |
| 11-26 10:06 | +10 stop | XRP | UP | 0.49 | 0.34 | -1.84 |
| 11-26 10:06 | +10 stop | DOGE | UP | 0.51 | 0.31 | -2.33 |
| 11-26 10:05 | +10 stop | SOL | UP | 0.64 | 0.44 | -2.30 |
| 11-26 10:05 | +10 stop | NEAR | UP | 0.53 | 0.32 | -2.44 |
| 11-26 10:05 | +5 | NEAR | UP | 0.58 | open |  |
| 11-26 10:05 | +5 | BTC | DOWN | 0.63 | 0.73 | 0.69 |
| 11-26 10:03 | +20 | NEAR | UP | 0.67 | open |  |
| 11-26 10:03 | +10 stop | NEAR | UP | 0.70 | 0.54 | -1.97 |
| 11-26 10:03 | +15 | NEAR | UP | 0.70 | open |  |
| 11-26 10:03 | +10 | NEAR | UP | 0.70 | open |  |
| 11-26 10:03 | +5 | BTC | DOWN | 0.67 | 0.72 | 0.19 |
| 11-26 10:02 | +5 | NEAR | UP | 0.65 | 0.70 | 0.19 |
| 11-26 10:02 | +10 stop | BTC | DOWN | 0.64 | 0.47 | -2.05 |
| 11-26 10:02 | +20 | BTC | DOWN | 0.64 | open |  |
| 11-26 10:02 | +15 | BTC | DOWN | 0.64 | open |  |
| 11-26 10:02 | +10 | BTC | DOWN | 0.64 | open |  |
| 11-26 10:02 | +5 | BTC | DOWN | 0.64 | 0.69 | 0.18 |
| 11-26 10:02 | +10 stop | ZEC | DOWN | 0.68 | 0.82 | 1.13 |
| 11-26 10:02 | +20 | ZEC | DOWN | 0.68 | 0.88 | 1.76 |
| 11-26 10:02 | +15 | ZEC | DOWN | 0.68 | 0.84 | 1.34 |
| 11-26 10:02 | +10 | ZEC | DOWN | 0.68 | 0.82 | 1.13 |
| 11-26 10:02 | +5 | ZEC | DOWN | 0.68 | 0.76 | 0.51 |
| 11-26 10:02 | +10 stop | ETH | DOWN | 0.63 | 0.38 | -2.84 |
| 11-26 10:02 | +20 | ETH | DOWN | 0.63 | open |  |
