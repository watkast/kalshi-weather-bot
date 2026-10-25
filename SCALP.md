# Range-Scalp Bot

*Updated Sun Oct 25 13:28 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 33195 | 28971 | 4224 (42) | 7 | $-9261.25 | -4.4% |
| **+10¢** | 24846 | 19956 | 4890 (60) | 7 | $-8220.16 | -5.3% |
| **+15¢** | 20788 | 15522 | 5266 (83) | 7 | $-7400.86 | -5.7% |
| **+20¢** | 18419 | 12904 | 5515 (105) | 7 | $-6519.02 | -5.6% |
| **+10¢ (15¢ stop)** | 40724 | 40664 | 60 (32) | 0 | $-15535.68 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-25 13:23 | +10 stop | DOGE | UP | 0.63 | 0.78 | 1.20 |
| 10-25 13:23 | +10 | DOGE | UP | 0.63 | 0.78 | 1.20 |
| 10-25 13:21 | +5 | DOGE | DOWN | 0.65 | open |  |
| 10-25 13:20 | +10 stop | DOGE | DOWN | 0.68 | 0.28 | -4.31 |
| 10-25 13:20 | +5 | DOGE | DOWN | 0.67 | 0.72 | 0.19 |
| 10-25 13:19 | +10 stop | SOL | DOWN | 0.69 | 0.82 | 1.04 |
| 10-25 13:19 | +10 stop | NEAR | DOWN | 0.68 | 0.51 | -2.04 |
| 10-25 13:19 | +10 stop | XRP | DOWN | 0.70 | 0.81 | 0.82 |
| 10-25 13:19 | +10 stop | ZEC | DOWN | 0.70 | 0.84 | 1.15 |
| 10-25 13:18 | +10 stop | BTC | DOWN | 0.54 | 0.67 | 0.96 |
| 10-25 13:18 | +20 | SOL | UP | 0.54 | open |  |
| 10-25 13:18 | +15 | SOL | UP | 0.54 | open |  |
| 10-25 13:18 | +10 stop | DOGE | UP | 0.53 | 0.63 | 0.65 |
| 10-25 13:18 | +5 | DOGE | UP | 0.52 | 0.63 | 0.75 |
| 10-25 13:18 | +5 | ZEC | UP | 0.62 | open |  |
| 10-25 13:18 | +5 | NEAR | UP | 0.58 | open |  |
| 10-25 13:17 | +10 stop | SOL | UP | 0.71 | 0.52 | -2.23 |
| 10-25 13:17 | +10 | SOL | UP | 0.71 | open |  |
| 10-25 13:17 | +5 | SOL | UP | 0.71 | open |  |
| 10-25 13:17 | +10 stop | XRP | UP | 0.70 | 0.48 | -2.53 |
| 10-25 13:17 | +10 | XRP | UP | 0.70 | open |  |
| 10-25 13:17 | +5 | XRP | UP | 0.70 | open |  |
| 10-25 13:17 | +10 stop | ETH | UP | 0.67 | 0.46 | -2.44 |
| 10-25 13:17 | +20 | ETH | UP | 0.67 | open |  |
| 10-25 13:17 | +15 | ETH | UP | 0.67 | open |  |
| 10-25 13:17 | +10 | ETH | UP | 0.67 | open |  |
| 10-25 13:17 | +5 | ETH | UP | 0.67 | open |  |
| 10-25 13:17 | +10 stop | BTC | UP | 0.63 | 0.45 | -2.15 |
| 10-25 13:17 | +20 | BTC | UP | 0.63 | open |  |
| 10-25 13:17 | +15 | BTC | UP | 0.63 | open |  |
| 10-25 13:17 | +10 | BTC | UP | 0.63 | open |  |
| 10-25 13:17 | +5 | BTC | UP | 0.63 | open |  |
| 10-25 13:17 | +10 stop | ZEC | UP | 0.59 | 0.37 | -2.54 |
| 10-25 13:17 | +20 | ZEC | UP | 0.59 | open |  |
| 10-25 13:17 | +15 | ZEC | UP | 0.59 | open |  |
| 10-25 13:17 | +10 | ZEC | UP | 0.59 | open |  |
| 10-25 13:17 | +5 | ZEC | UP | 0.59 | 0.65 | 0.27 |
| 10-25 13:17 | +10 stop | NEAR | UP | 0.56 | 0.35 | -2.44 |
| 10-25 13:17 | +20 | NEAR | UP | 0.56 | open |  |
| 10-25 13:17 | +15 | NEAR | UP | 0.56 | open |  |
