# Range-Scalp Bot

*Updated Tue Nov 17 15:26 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 62939 | 54901 | 8038 (117) | 7 | $-17138.97 | -4.3% |
| **+10¢** | 47005 | 37600 | 9405 (159) | 8 | $-16013.54 | -5.4% |
| **+15¢** | 39397 | 29255 | 10142 (201) | 8 | $-14539.15 | -5.9% |
| **+20¢** | 35108 | 24473 | 10635 (256) | 8 | $-12712.35 | -5.8% |
| **+10¢ (15¢ stop)** | 76596 | 76440 | 156 (92) | 0 | $-28227.82 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-17 15:19 | +10 stop | ZEC | UP | 0.65 | 0.86 | 1.83 |
| 11-17 15:19 | +5 | ZEC | UP | 0.66 | 0.73 | 0.40 |
| 11-17 15:19 | +10 stop | BTC | UP | 0.64 | 0.74 | 0.69 |
| 11-17 15:19 | +10 stop | ETH | UP | 0.53 | 0.66 | 0.96 |
| 11-17 15:19 | +10 stop | BNB | UP | 0.69 | 0.86 | 1.46 |
| 11-17 15:19 | +10 stop | HYPE | UP | 0.69 | 0.83 | 1.15 |
| 11-17 15:19 | +10 | HYPE | UP | 0.69 | 0.83 | 1.15 |
| 11-17 15:19 | +5 | HYPE | UP | 0.69 | 0.78 | 0.62 |
| 11-17 15:19 | +10 stop | XRP | UP | 0.68 | 0.78 | 0.74 |
| 11-17 15:19 | +10 stop | DOGE | UP | 0.68 | 0.79 | 0.82 |
| 11-17 15:19 | +10 stop | NEAR | UP | 0.68 | 0.80 | 0.93 |
| 11-17 15:18 | +10 stop | HYPE | UP | 0.52 | 0.65 | 0.96 |
| 11-17 15:18 | +20 | HYPE | UP | 0.52 | 0.73 | 1.78 |
| 11-17 15:18 | +15 | HYPE | UP | 0.52 | 0.71 | 1.57 |
| 11-17 15:18 | +10 | HYPE | UP | 0.52 | 0.65 | 0.96 |
| 11-17 15:18 | +5 | HYPE | UP | 0.52 | 0.65 | 0.96 |
| 11-17 15:17 | +10 stop | BNB | DOWN | 0.58 | 0.41 | -2.06 |
| 11-17 15:17 | +20 | BNB | DOWN | 0.58 | open |  |
| 11-17 15:17 | +15 | BNB | DOWN | 0.58 | open |  |
| 11-17 15:17 | +10 | BNB | DOWN | 0.58 | open |  |
| 11-17 15:17 | +5 | BNB | DOWN | 0.58 | open |  |
| 11-17 15:16 | +10 stop | ZEC | DOWN | 0.63 | 0.42 | -2.45 |
| 11-17 15:16 | +20 | ZEC | DOWN | 0.62 | open |  |
| 11-17 15:16 | +15 | ZEC | DOWN | 0.62 | open |  |
| 11-17 15:16 | +10 | ZEC | DOWN | 0.62 | open |  |
| 11-17 15:16 | +5 | ZEC | DOWN | 0.62 | 0.69 | 0.38 |
| 11-17 15:16 | +10 stop | SOL | DOWN | 0.57 | 0.42 | -1.86 |
| 11-17 15:16 | +20 | SOL | DOWN | 0.56 | open |  |
| 11-17 15:16 | +15 | SOL | DOWN | 0.58 | open |  |
| 11-17 15:16 | +10 | SOL | DOWN | 0.58 | open |  |
| 11-17 15:16 | +5 | SOL | DOWN | 0.58 | open |  |
| 11-17 15:16 | +10 stop | XRP | DOWN | 0.63 | 0.47 | -1.95 |
| 11-17 15:16 | +20 | XRP | DOWN | 0.63 | open |  |
| 11-17 15:16 | +15 | XRP | DOWN | 0.63 | open |  |
| 11-17 15:16 | +10 | XRP | DOWN | 0.63 | open |  |
| 11-17 15:16 | +5 | XRP | DOWN | 0.63 | open |  |
| 11-17 15:16 | +10 stop | DOGE | DOWN | 0.65 | 0.47 | -2.14 |
| 11-17 15:16 | +20 | DOGE | DOWN | 0.64 | open |  |
| 11-17 15:16 | +15 | DOGE | DOWN | 0.64 | open |  |
| 11-17 15:16 | +10 | DOGE | DOWN | 0.64 | open |  |
