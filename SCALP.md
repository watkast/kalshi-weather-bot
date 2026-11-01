# Range-Scalp Bot

*Updated Sun Nov 01 08:14 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 43358 | 37785 | 5573 (63) | 6 | $-12377.84 | -4.5% |
| **+10¢** | 32338 | 25903 | 6435 (85) | 6 | $-11067.04 | -5.4% |
| **+15¢** | 27061 | 20129 | 6932 (112) | 5 | $-10121.45 | -6.0% |
| **+20¢** | 24034 | 16773 | 7261 (146) | 5 | $-8922.65 | -5.9% |
| **+10¢ (15¢ stop)** | 52874 | 52789 | 85 (50) | 0 | $-19971.45 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-01 08:13 | +10 stop | BNB | UP | 0.69 | 0.10 | -6.12 |
| 11-01 08:10 | +10 stop | NEAR | UP | 0.56 | 0.17 | -4.18 |
| 11-01 08:09 | +10 stop | BTC | UP | 0.57 | 0.38 | -2.25 |
| 11-01 08:09 | +15 | BTC | UP | 0.57 | open |  |
| 11-01 08:09 | +10 | BTC | UP | 0.57 | open |  |
| 11-01 08:09 | +5 | BTC | UP | 0.58 | open |  |
| 11-01 08:08 | +10 stop | XRP | DOWN | 0.51 | 0.69 | 1.47 |
| 11-01 08:08 | +20 | XRP | DOWN | 0.52 | 0.88 | 3.34 |
| 11-01 08:08 | +15 | XRP | DOWN | 0.52 | 0.69 | 1.37 |
| 11-01 08:08 | +10 | XRP | DOWN | 0.52 | 0.69 | 1.37 |
| 11-01 08:08 | +5 | XRP | DOWN | 0.52 | 0.69 | 1.37 |
| 11-01 08:08 | +10 stop | BNB | UP | 0.64 | 0.46 | -2.15 |
| 11-01 08:08 | +10 stop | ZEC | UP | 0.56 | 0.38 | -2.15 |
| 11-01 08:08 | +20 | ZEC | UP | 0.56 | open |  |
| 11-01 08:08 | +15 | ZEC | UP | 0.56 | open |  |
| 11-01 08:08 | +10 | ZEC | UP | 0.57 | open |  |
| 11-01 08:08 | +5 | ZEC | UP | 0.57 | open |  |
| 11-01 08:07 | +20 | HYPE | DOWN | 0.69 | 0.89 | 1.78 |
| 11-01 08:07 | +10 stop | ETH | DOWN | 0.69 | 0.85 | 1.36 |
| 11-01 08:06 | +10 stop | HYPE | DOWN | 0.54 | 0.82 | 2.51 |
| 11-01 08:06 | +15 | HYPE | DOWN | 0.54 | 0.82 | 2.51 |
| 11-01 08:05 | +10 stop | SOL | UP | 0.62 | 0.44 | -2.15 |
| 11-01 08:05 | +10 stop | DOGE | DOWN | 0.61 | 0.78 | 1.40 |
| 11-01 08:05 | +10 stop | NEAR | UP | 0.61 | 0.75 | 1.09 |
| 11-01 08:05 | +5 | ZEC | UP | 0.69 | 0.76 | 0.42 |
| 11-01 08:04 | +10 stop | ETH | DOWN | 0.69 | 0.50 | -2.23 |
| 11-01 08:04 | +5 | BTC | UP | 0.69 | 0.76 | 0.42 |
| 11-01 08:04 | +10 stop | XRP | UP | 0.61 | 0.84 | 2.03 |
| 11-01 08:04 | +10 | XRP | UP | 0.61 | 0.84 | 2.03 |
| 11-01 08:04 | +5 | XRP | UP | 0.61 | 0.68 | 0.37 |
| 11-01 08:04 | +5 | ZEC | UP | 0.61 | 0.68 | 0.37 |
| 11-01 08:03 | +10 stop | HYPE | UP | 0.62 | 0.41 | -2.44 |
| 11-01 08:03 | +10 | HYPE | UP | 0.62 | open |  |
| 11-01 08:03 | +5 | HYPE | UP | 0.62 | open |  |
| 11-01 08:03 | +10 stop | SOL | UP | 0.65 | 0.49 | -1.94 |
| 11-01 08:03 | +10 | SOL | UP | 0.65 | open |  |
| 11-01 08:03 | +5 | SOL | UP | 0.65 | open |  |
| 11-01 08:03 | +5 | ETH | UP | 0.65 | open |  |
| 11-01 08:03 | +10 stop | NEAR | DOWN | 0.69 | 0.50 | -2.23 |
| 11-01 08:03 | +20 | NEAR | DOWN | 0.69 | 0.95 | 2.40 |
